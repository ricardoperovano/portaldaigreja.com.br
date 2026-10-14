#!/usr/bin/env python3
"""Validação de SEO do site — roda offline (arquivos) ou contra a produção.

    python3 tools/seo_check.py            # valida os arquivos do repositório
    python3 tools/seo_check.py --live     # valida https://portaldaigreja.com.br

Sem dependências: só a biblioteca padrão do Python 3. Sai com código 1 se algum
teste falhar, então serve para CI.

O que é verificado, por página do sitemap:
  * o arquivo existe (ou a URL responde 200, no modo --live);
  * title único, com no máximo 60 caracteres;
  * meta description única, entre 50 e 160 caracteres;
  * exatamente um <h1>;
  * canonical presente, absoluto e apontando para a própria URL;
  * Open Graph (title, description, image, url) e twitter:card;
  * JSON-LD sintaticamente válido e sem nota/avaliação inventada
    (AggregateRating/Review são proibidos enquanto não houver avaliações reais);
  * nenhum link href="#" (link morto);
  * links internos apontando para páginas que existem;
  * nenhuma imagem sem alt.
E, no sitemap: nenhuma âncora (#), nenhuma URL duplicada, todas listadas.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://portaldaigreja.com.br"
# Afirmações que não podem voltar sem lastro comprovável (ver docs/SEO-AUDIT.md).
BANNED_PATTERNS = [
    (r"\+?\s*500\s+igrejas", "número de igrejas sem comprovação"),
    (r"R\$\s*2,5\s*mi", "valor gerenciado sem comprovação"),
    (r"centenas de igrejas", "quantidade de clientes sem comprovação"),
    (r"30 dias de garantia", "garantia de reembolso que não existe"),
    (r"AW-CONVERSION_ID", "placeholder de conversão do Google Ads"),
    (r"não conseguirá lê-las", "garantia absoluta de segurança"),
    (r"★★★★★", "avaliação em estrelas sem avaliações reais"),
    # versão em inglês: as mesmas regras, além do que não existe fora do Brasil
    (r"money[- ]back guarantee", "garantia de reembolso que não existe"),
    (r"\b500\+? churches", "número de clientes sem comprovação"),
    (r"(?<!no )automatic(ally)? reconcil", "baixa automática de Pix, que não existe"),
]
# O contrário de uma proibição: a página em inglês PRECISA avisar que o sistema é
# em português e cobrado em reais, para ninguém assinar achando o contrário.
REQUIRED_EN = [
    (r"Portuguese", "o aviso de que o sistema/suporte é em português"),
    (r"Brazilian reais|BRL", "o aviso de que a cobrança é em reais"),
]
# Pares de páginas equivalentes: toda página precisa apontar para a sua versão no
# outro idioma (hreflang), nos dois sentidos.
EQUIVALENT = {
    "/": "/en/",
    "/sistema-gestao-igrejas/": "/en/church-management-software/",
    "/cadastro-membros-igreja/": "/en/church-member-database/",
    "/controle-dizimos-ofertas/": "/en/church-tithes-offerings/",
    "/financeiro-para-igrejas/": "/en/church-accounting-software/",
    "/prestacao-de-contas-igreja/": "/en/church-financial-reports/",
    "/site-para-igrejas/": "/en/church-website-builder/",
}
FAILURES: list[str] = []
CHECKS = 0


def check(ok: bool, msg: str) -> None:
    global CHECKS
    CHECKS += 1
    if not ok:
        FAILURES.append(msg)


def fetch(url_path: str, live: bool) -> str | None:
    if live:
        try:
            with urllib.request.urlopen(SITE + url_path, timeout=20) as r:
                if r.status != 200:
                    return None
                return r.read().decode("utf-8", "replace")
        except Exception:
            return None
    rel = url_path.strip("/")
    path = ROOT / (rel + "/index.html" if rel else "index.html")
    return path.read_text(encoding="utf-8") if path.exists() else None


def meta(html: str, attr: str, value: str) -> str | None:
    m = re.search(rf'<meta[^>]*{attr}=["\']{re.escape(value)}["\'][^>]*>', html, re.I)
    if not m:
        return None
    c = re.search(r'content=["\'](.*?)["\']', m.group(0), re.S)
    return c.group(1).strip() if c else None


def sitemap_urls(live: bool) -> list[str]:
    raw = fetch("/sitemap.xml", live) if live else (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    root = ET.fromstring(raw)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [el.text.strip() for el in root.findall(".//s:loc", ns)]


def main() -> int:
    global CHECKS
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="validar a produção em vez dos arquivos")
    args = ap.parse_args()

    urls = sitemap_urls(args.live)
    check(bool(urls), "sitemap.xml não tem URLs")
    check(len(urls) == len(set(urls)), "sitemap.xml tem URL repetida")
    for u in urls:
        check("#" not in u, f"sitemap.xml: âncora não pode entrar no sitemap: {u}")
        check(u.startswith(SITE), f"sitemap.xml: URL fora do domínio: {u}")

    titles: dict[str, str] = {}
    descriptions: dict[str, str] = {}
    paths = [u[len(SITE):] or "/" for u in urls]

    for path in paths:
        html = fetch(path, args.live)
        if html is None:
            FAILURES.append(f"{path}: página do sitemap não existe/não respondeu 200")
            continue
        where = f"{path}"

        title = (re.search(r"<title>(.*?)</title>", html, re.S) or [None, ""])[1].strip()
        check(bool(title), f"{where}: sem <title>")
        check(len(title) <= 60, f"{where}: title com {len(title)} caracteres (máx. 60): {title!r}")
        check(title not in titles, f"{where}: title repetido de {titles.get(title)}")
        titles[title] = where

        desc = meta(html, "name", "description") or ""
        check(bool(desc), f"{where}: sem meta description")
        check(50 <= len(desc) <= 160,
              f"{where}: description com {len(desc)} caracteres (ideal 50–160)")
        check(desc not in descriptions, f"{where}: description repetida de {descriptions.get(desc)}")
        descriptions[desc] = where

        h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S)
        check(len(h1s) == 1, f"{where}: {len(h1s)} <h1> (precisa ser exatamente 1)")

        canon = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\'](.*?)["\']', html, re.I)
        check(bool(canon), f"{where}: sem canonical")
        if canon:
            check(canon.group(1) == SITE + path,
                  f"{where}: canonical aponta para {canon.group(1)}, esperado {SITE + path}")

        for prop in ("og:title", "og:description", "og:image", "og:url"):
            check(bool(meta(html, "property", prop)), f"{where}: sem {prop}")
        check(bool(meta(html, "name", "twitter:card")), f"{where}: sem twitter:card")

        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                data = json.loads(block)
            except json.JSONDecodeError as exc:
                FAILURES.append(f"{where}: JSON-LD inválido ({exc})")
                continue
            flat = json.dumps(data, ensure_ascii=False)
            check("aggregateRating" not in flat and '"Review"' not in flat,
                  f"{where}: JSON-LD declara avaliação/nota sem avaliações reais")

        dead = re.findall(r'<a[^>]*href=["\']#["\']', html)
        check(not dead, f"{where}: {len(dead)} link(s) href=\"#\" (link morto)")

        for img in re.findall(r"<img[^>]*>", html):
            check("alt=" in img, f"{where}: imagem sem alt: {img[:70]}")

        for href in re.findall(r'<a[^>]*href=["\'](/[^"\'#?]*)["\']', html):
            if href.endswith((".png", ".jpg", ".webp", ".css", ".js", ".xml", ".webmanifest")):
                continue
            if not args.live:
                target = ROOT / (href.strip("/") + "/index.html" if href.strip("/") else "index.html")
                check(target.exists(), f"{where}: link interno quebrado: {href}")

        # hreflang: a página aponta para a sua equivalente no outro idioma?
        pair = EQUIVALENT.get(path) or {v: k for k, v in EQUIVALENT.items()}.get(path)
        if pair:
            langs = dict(re.findall(
                r'<link[^>]*rel=["\']alternate["\'][^>]*hreflang=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)["\']',
                html, re.I))
            check("pt-BR" in langs and "en" in langs, f"{where}: sem hreflang para os dois idiomas")
            check(langs.get("x-default", "").startswith(SITE),
                  f"{where}: sem hreflang x-default")
            expected = SITE + (pair if path in EQUIVALENT else path)
            other = SITE + (pair if path not in EQUIVALENT else pair)
            check(other in langs.values(),
                  f"{where}: hreflang não aponta para {other}")
            lang_attr = re.search(r'<html[^>]*lang=["\']([^"\']+)["\']', html)
            want = "en" if path.startswith("/en/") else "pt-BR"
            check(bool(lang_attr) and lang_attr.group(1) == want,
                  f"{where}: <html lang> deveria ser {want}")

        for pattern, why in BANNED_PATTERNS:
            check(not re.search(pattern, html, re.I), f"{where}: afirmação proibida ({why})")

        if path.startswith("/en/"):
            for pattern, what in REQUIRED_EN:
                check(bool(re.search(pattern, html)), f"{where}: falta {what}")

    # arquivos auxiliares
    if not args.live:
        for required in ("robots.txt", "404.html", "sitemap.xml", "index.html"):
            check((ROOT / required).exists(), f"falta o arquivo {required}")
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        check("Sitemap:" in robots, "robots.txt não aponta para o sitemap")
        for js in ("script.js",):
            src = (ROOT / js).read_text(encoding="utf-8")
            check("AW-CONVERSION_ID" not in src, f"{js}: placeholder de conversão do Google Ads")

    print(f"{CHECKS} verificações, {len(FAILURES)} falha(s)")
    for f in FAILURES:
        print("  ✗", f)
    if not FAILURES:
        print("  ✓ tudo certo")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
