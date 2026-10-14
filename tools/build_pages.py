#!/usr/bin/env python3
"""Gera as páginas comerciais estáticas (uma pasta por URL) a partir do conteúdo abaixo.

Por que um gerador e não HTML solto: o cabeçalho, o rodapé, os metadados e os
links internos têm de ser idênticos em todas as páginas. Edite o conteúdo aqui e
rode:

    python3 tools/build_pages.py

Cada página vira `<slug>/index.html`, servida pelo GitHub Pages como
`https://portaldaigreja.com.br/<slug>/`. A home (`index.html`) é escrita à mão e
NÃO é tocada por este script.

REGRA: só entra aqui o que o produto realmente faz. Antes de incluir uma frase
nova, confirme no código do app (repo gestaoigreja). Veja docs/CATALOGO-FUNCIONALIDADES-IGREJAS.md.
"""
from __future__ import annotations

import html
import json
import pathlib
import sys

SITE = "https://portaldaigreja.com.br"
APP = "https://app.portaldaigreja.com.br"
SIGNUP = f"{APP}/register-church"
LOGIN = f"{APP}/login"
WA = ("https://wa.me/5527998553591?text=Ol%C3%A1!%20Vim%20pelo%20site%20do%20Portal%20"
      "da%20Igreja%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.")
ROOT = pathlib.Path(__file__).resolve().parent.parent

# --------------------------------------------------------------- conteúdo
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from content_pt import PAGES as PAGES_PT          # noqa: E402
from content_en import PAGES as PAGES_EN          # noqa: E402

# Rótulo curto para o menu; o longo vai no rodapé e nos cartões "Veja também".
NAV_LABELS = {
    "sistema-gestao-igrejas": "Sistema",
    "cadastro-membros-igreja": "Membros",
    "controle-dizimos-ofertas": "Dízimos",
    "financeiro-para-igrejas": "Financeiro",
    "prestacao-de-contas-igreja": "Transparência",
    "site-para-igrejas": "Site",
}
RELATED_SUB = {
    "sistema-gestao-igrejas": "A visão geral de tudo o que o sistema faz, do cadastro ao relatório.",
    "controle-dizimos-ofertas": "Dízimo, oferta, Pix com QR Code e o informe anual do membro.",
    "cadastro-membros-igreja": "Ficha, famílias, grupos e a importação da planilha que a igreja já tem.",
    "financeiro-para-igrejas": "Receitas, despesas, contas fixas e o fechamento do mês em PDF.",
    "site-para-igrejas": "Site público com agenda, horários de culto e Pix, incluso nos planos pagos.",
    "prestacao-de-contas-igreja": "O relatório da reunião, a transparência para a igreja e o informe anual.",
}
RELATED_LABELS = {
    "sistema-gestao-igrejas": "Sistema de gestão para igrejas",
    "controle-dizimos-ofertas": "Controle de dízimos e ofertas",
    "cadastro-membros-igreja": "Cadastro de membros",
    "financeiro-para-igrejas": "Financeiro para igrejas",
    "site-para-igrejas": "Site para igrejas",
    "prestacao-de-contas-igreja": "Prestação de contas",
}


# --------------------------------------------------------------- idiomas
# O site tem duas versões: português (raiz) e inglês (/en/), esta voltada a
# igrejas BRASILEIRAS no exterior. O sistema em si é em português e cobrado em
# reais — por isso toda página em inglês carrega o aviso NOTICE.
NAV_LABELS_EN = {
    "church-management-software": "System",
    "church-member-database": "Members",
    "church-tithes-offerings": "Giving",
    "church-accounting-software": "Finances",
    "church-financial-reports": "Reports",
    "church-website-builder": "Website",
}
RELATED_LABELS_EN = {
    "church-management-software": "Church management software",
    "church-member-database": "Church member database",
    "church-tithes-offerings": "Tithes and offerings",
    "church-accounting-software": "Church accounting",
    "church-financial-reports": "Financial reports",
    "church-website-builder": "Church website builder",
}
RELATED_SUB_EN = {
    "church-management-software": "The whole picture, from member records to the monthly report.",
    "church-member-database": "Records, families, groups and importing the spreadsheet you keep.",
    "church-tithes-offerings": "Tithe, offering, Pix with a QR code and the annual statement.",
    "church-accounting-software": "Income, expenses, fixed bills and the monthly closing as a PDF.",
    "church-financial-reports": "The board report, transparency with no names, and the audit trail.",
    "church-website-builder": "A public site with the calendar, service times and Pix, included in paid plans.",
}
# Páginas equivalentes entre os idiomas, para o hreflang. A home é o par "".
EQUIVALENT = {
    "": "",
    "sistema-gestao-igrejas": "church-management-software",
    "cadastro-membros-igreja": "church-member-database",
    "controle-dizimos-ofertas": "church-tithes-offerings",
    "financeiro-para-igrejas": "church-accounting-software",
    "prestacao-de-contas-igreja": "church-financial-reports",
    "site-para-igrejas": "church-website-builder",
}
EN_OF_PT = EQUIVALENT
PT_OF_EN = {v: k for k, v in EQUIVALENT.items()}

NOTICE_EN = ("""    <section class="section">
      <div class="container container-narrow">
        <p class="pricing-note" style="font-size:.95rem;">
          <strong>Before you sign up:</strong> the software interface and support are in
          Portuguese, and subscriptions are charged in Brazilian reais (BRL). Portal da Igreja is
          built for Brazilian churches, including Brazilian congregations abroad. Giving through
          Pix requires a Brazilian bank account for the church.
          <a href="https://wa.me/5527998553591">Talk to us on WhatsApp</a> if you are unsure
          whether it fits your church.
        </p>
      </div>
    </section>
""")

CHROME = {
    "pt": {
        "lang": "pt-BR", "prefix": "", "pages": None,
        "nav": None, "related": None, "related_sub": None,
        "login": "Entrar", "signup": "Criar conta grátis",
        "plans": "Ver planos e preços", "plans_href": "/#planos",
        "badge": "✅ Plano gratuito até 50 membros · Sem cartão de crédito",
        "faq_kicker": "Dúvidas frequentes", "faq_h2": "Perguntas de quem está avaliando",
        "related_kicker": "Veja também", "related_h2": "Outras partes do sistema",
        "cta_h2": "Comece hoje, no plano gratuito",
        "cta_p": "Crie a conta da sua igreja em poucos minutos e traga a sua lista de membros da planilha.",
        "brand_p": "Gestão completa, segura e transparente para a sua igreja — na nuvem.",
        "f_product": "Produto", "f_company": "Empresa", "f_legal": "Legal",
        "f_plans": "Planos e preços", "privacy": "Política de Privacidade", "terms": "Termos de Uso",
        "wa_label": "Fale conosco no WhatsApp", "wa_footer": "💬 WhatsApp: (27) 99855-3591",
        "notice": "", "switch": "English", "switch_label": "Read this page in English",
        "rights": "© 2026 Portal da Igreja. Todos os direitos reservados.",
    },
    "en": {
        "lang": "en", "prefix": "/en", "pages": None,
        "nav": None, "related": None, "related_sub": None,
        "login": "Sign in", "signup": "Create free account",
        "plans": "See plans and prices", "plans_href": "/en/#plans",
        "badge": "✅ Free plan for up to 50 members · No credit card",
        "faq_kicker": "Frequently asked", "faq_h2": "Questions from churches considering us",
        "related_kicker": "See also", "related_h2": "Other parts of the system",
        "cta_h2": "Start today, on the free plan",
        "cta_p": "Create your church account in a few minutes and bring your member list from the spreadsheet.",
        "brand_p": "Church management, giving and website in one system — in the cloud.",
        "f_product": "Product", "f_company": "Company", "f_legal": "Legal",
        "f_plans": "Plans and prices", "privacy": "Privacy Policy", "terms": "Terms of Use",
        "wa_label": "Talk to us on WhatsApp", "wa_footer": "💬 WhatsApp: +55 27 99855-3591",
        "notice": NOTICE_EN, "switch": "Português", "switch_label": "Leia esta página em português",
        "rights": "© 2026 Portal da Igreja. All rights reserved.",
    },
}
CHROME["pt"].update(pages=PAGES_PT, nav=NAV_LABELS, related=RELATED_LABELS, related_sub=RELATED_SUB)
CHROME["en"].update(pages=PAGES_EN, nav=NAV_LABELS_EN, related=RELATED_LABELS_EN,
                    related_sub=RELATED_SUB_EN)

# --------------------------------------------------------------- template
def esc(text: str) -> str:
    """Escapa para HTML, preservando as poucas tags que o conteúdo usa."""
    out = html.escape(text, quote=False)
    return out.replace("&lt;code&gt;", "<code>").replace("&lt;/code&gt;", "</code>")


def nav(active: str, c: dict) -> str:
    return "".join(
        f'        <a href="{c["prefix"]}/{slug}/"'
        f'{" aria-current=\"page\"" if slug == active else ""}>{label}</a>\n'
        for slug, label in c["nav"].items())


def render_blocks(blocks: list[dict]) -> str:
    out = []
    alt = False
    for b in blocks:
        alt = not alt
        cls = "section section-alt" if alt else "section"
        if b["type"] == "prose":
            out.append(f'''    <section class="{cls}">
      <div class="container container-narrow">
        <div class="section-head">
          <span class="kicker">{esc(b["kicker"])}</span>
          <h2>{esc(b["h2"])}</h2>
        </div>
        {"".join(f"<p class='lead'>{esc(p)}</p>" for p in b["paras"])}
      </div>
    </section>
''')
        elif b["type"] == "features":
            cards = []
            for item in b["items"]:
                icon, tone, name = item[0], item[1], item[2]
                desc = item[3] if len(item) > 3 and item[3] else b.get("plain", {}).get(name, "")
                link = item[4] if len(item) > 4 else None
                more = (f'\n            <p><a href="{link}">{esc(name)} →</a></p>'
                        if link else "")
                cards.append(f'''          <article class="feature">
            <span class="feat-icon {tone}">{icon}</span>
            <h3>{esc(name)}</h3>
            <p>{esc(desc)}</p>{more}
          </article>''')
            sub = f'          <p>{esc(b["sub"])}</p>\n' if b.get("sub") else ""
            out.append(f'''    <section class="{cls}">
      <div class="container">
        <div class="section-head">
          <span class="kicker">{esc(b["kicker"])}</span>
          <h2>{esc(b["h2"])}</h2>
{sub}        </div>
        <div class="features-grid">
{chr(10).join(cards)}
        </div>
      </div>
    </section>
''')
        elif b["type"] == "steps":
            steps = "".join(f'''          <article class="step">
            <span class="step-num">{i}</span>
            <h3>{esc(t)}</h3>
            <p>{esc(d)}</p>
          </article>
''' for i, (t, d) in enumerate(b["items"], 1))
            out.append(f'''    <section class="{cls}">
      <div class="container">
        <div class="section-head">
          <span class="kicker">{esc(b["kicker"])}</span>
          <h2>{esc(b["h2"])}</h2>
        </div>
        <div class="steps-grid">
{steps}        </div>
      </div>
    </section>
''')
    return "".join(out)


def render_faq(items: list[tuple[str, str]], c: dict) -> str:
    rows = "".join(f'''          <details class="faq-item">
            <summary>{esc(q)}</summary>
            <div class="faq-answer"><p>{esc(a)}</p></div>
          </details>
''' for q, a in items)
    return f'''    <section class="section faq" id="faq">
      <div class="container container-narrow">
        <div class="section-head">
          <span class="kicker">{esc(c["faq_kicker"])}</span>
          <h2>{esc(c["faq_h2"])}</h2>
        </div>
        <div class="faq-list">
{rows}        </div>
      </div>
    </section>
'''


def render_related(slug: str, c: dict) -> str:
    links = "".join(
        f'          <a class="feature" href="{c["prefix"]}/{s}/"><h3>{esc(label)}</h3>'
        f'<p>{esc(c["related_sub"][s])}</p></a>\n'
        for s, label in c["related"].items() if s != slug)
    return f'''    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="kicker">{esc(c["related_kicker"])}</span>
          <h2>{esc(c["related_h2"])}</h2>
        </div>
        <div class="features-grid">
{links}        </div>
      </div>
    </section>
'''


def jsonld(page: dict, c: dict) -> str:
    url = f"{SITE}{c['prefix']}/{page['slug']}/"
    home_name = "Início" if c["lang"].startswith("pt") else "Home"
    blocks = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": home_name,
             "item": f"{SITE}{c['prefix']}/"},
            {"@type": "ListItem", "position": 2, "name": page["kicker"], "item": url},
        ]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page["faq"]]},
    ]
    return "\n".join(
        '  <script type="application/ld+json">\n  '
        + json.dumps(b, ensure_ascii=False, indent=2).replace("\n", "\n  ")
        + "\n  </script>" for b in blocks)


TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}">

<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-F49Y1WNQ4H"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    // LGPD: nada de medição antes do aceite. O Consent Mode segura o GA4 até o
    // visitante decidir no banner (ver script.js).
    gtag('consent', 'default', {{
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
      analytics_storage: 'denied',
      wait_for_update: 500
    }});
    gtag('config', 'G-F49Y1WNQ4H');
  </script>

  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#0b1f3a" />
  <link rel="canonical" href="{url}" />
{hreflang}

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Portal da Igreja" />
  <meta property="og:locale" content="pt_BR" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{site}/assets/images/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Portal da Igreja — sistema de gestão para igrejas" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="{site}/assets/images/og-image.jpg" />

  <link rel="icon" href="/favicon-48.png" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700&display=swap"
    rel="stylesheet" />
  <link rel="stylesheet" href="/styles.css" />

{jsonld}
</head>

<body>
  <header class="navbar" id="navbar">
    <div class="container nav-inner">
      <a href="/" class="nav-logo" aria-label="Portal da Igreja - início">
        <picture>
          <source srcset="/assets/images/logo-horizontal.webp" type="image/webp" />
          <img src="/assets/images/logo-horizontal.png" alt="Portal da Igreja — sistema de gestão para igrejas" width="100" height="40" decoding="async" />
        </picture>
      </a>

      <nav class="nav-links" id="navLinks" aria-label="Navegação principal">
{navlinks}      </nav>

      <div class="nav-actions">
        <a class="btn btn-ghost" href="{login}">{c_login}</a>
        <a class="btn btn-primary" href="{signup}">{c_signup}</a>
      </div>

      <button class="nav-toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false"
        aria-controls="mobileMenu">
        <span></span><span></span><span></span>
      </button>
    </div>

    <div class="mobile-menu" id="mobileMenu" hidden>
{navlinks}      <a href="{plans_href}">{c_plans}</a>
      <a href="{switch_href}" hreflang="{switch_lang}" lang="{switch_lang}">{c_switch}</a>
      <div class="mobile-actions">
        <a class="btn btn-ghost" href="{login}">{c_login}</a>
        <a class="btn btn-primary" href="{signup}">{c_signup}</a>
      </div>
    </div>
  </header>

  <main>
    <section class="hero" id="hero">
      <div class="container container-narrow">
        <div class="hero-copy">
          <span class="eyebrow">{kicker}</span>
          <h1>{h1}</h1>
          <p class="lead">{lead}</p>
          <div class="hero-ctas">
            <a class="btn btn-primary btn-lg" href="{signup}">{c_signup}</a>
            <a class="btn btn-outline btn-lg" href="{plans_href}">{c_plans}</a>
          </div>
          <p class="hero-badge">{c_badge}</p>
        </div>
      </div>
    </section>

{notice}{blocks}{faq}{related}
    <section class="cta-band">
      <div class="container cta-inner">
        <h2>{c_cta_h2}</h2>
        <p>{c_cta_p}</p>
        <a class="btn btn-white btn-lg" href="{signup}">{c_signup}</a>
      </div>
    </section>
  </main>

  <footer class="footer" id="contato">
    <div class="container footer-grid">
      <div class="footer-brand">
        <span class="footer-logo-badge">
          <picture>
            <source srcset="/assets/images/logo-horizontal.webp" type="image/webp" />
            <img src="/assets/images/logo-horizontal.png" alt="Portal da Igreja — sistema de gestão para igrejas" width="100" height="40" loading="lazy" decoding="async" />
          </picture>
        </span>
        <p>{c_brand_p}</p>
      </div>

      <div class="footer-col">
        <h4>{c_f_product}</h4>
{footerlinks}      </div>

      <div class="footer-col">
        <h4>{c_f_company}</h4>
        <a href="{plans_href}">{c_f_plans}</a>
        <a href="mailto:suporte@portaldaigreja.com.br">suporte@portaldaigreja.com.br</a>
        <a href="https://wa.me/5527998553591" target="_blank" rel="noopener">{c_wa_footer}</a>
        <a href="{switch_href}" hreflang="{switch_lang}" lang="{switch_lang}">{c_switch}</a>
      </div>

      <div class="footer-col">
        <h4>{c_f_legal}</h4>
        <a href="{app}/privacidade">{c_privacy}</a>
        <a href="{app}/termos">{c_terms}</a>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container">
        <p>{c_rights}</p>
      </div>
    </div>
  </footer>

  <a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="{c_wa_label}">
    <span class="wa-tooltip">{c_wa_label}</span>
    <svg class="wa-icon" viewBox="0 0 32 32" width="30" height="30" aria-hidden="true" focusable="false">
      <path fill="#fff" d="M16.001 3.2c-7.06 0-12.8 5.74-12.8 12.8 0 2.26.6 4.46 1.73 6.4L3.2 28.8l6.57-1.72a12.73 12.73 0 0 0 6.23 1.6h.01c7.06 0 12.8-5.74 12.8-12.8s-5.75-12.68-12.81-12.68zm0 23.02h-.01a10.6 10.6 0 0 1-5.4-1.48l-.39-.23-3.9 1.02 1.04-3.8-.25-.4a10.57 10.57 0 0 1-1.62-5.65c0-5.86 4.77-10.62 10.63-10.62 2.84 0 5.5 1.11 7.51 3.12a10.55 10.55 0 0 1 3.11 7.51c0 5.86-4.77 10.63-10.62 10.63zm5.83-7.96c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.71.16-.21.32-.82 1.04-1 1.25-.18.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.58-.95-.85-1.59-1.9-1.78-2.22-.18-.32-.02-.49.14-.65.14-.14.32-.37.48-.55.16-.18.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.71-1.72-.98-2.35-.26-.62-.52-.54-.71-.55l-.61-.01c-.21 0-.55.08-.84.4-.29.32-1.1 1.08-1.1 2.63 0 1.55 1.13 3.05 1.29 3.26.16.21 2.22 3.39 5.38 4.76.75.32 1.34.51 1.79.66.75.24 1.44.21 1.98.13.6-.09 1.89-.77 2.16-1.52.27-.75.27-1.39.19-1.52-.08-.13-.29-.21-.61-.37z"/>
    </svg>
  </a>

  <div class="sticky-cta" id="stickyCta" aria-hidden="true">
    <a class="btn btn-primary btn-block" href="{signup}">{c_signup} →</a>
  </div>

  <script src="/script.js"></script>
</body>

</html>
"""


def hreflang_block(pt_slug: str, en_slug: str) -> str:
    pt_url = f"{SITE}/{pt_slug}/" if pt_slug else f"{SITE}/"
    en_url = f"{SITE}/en/{en_slug}/" if en_slug else f"{SITE}/en/"
    return (f'  <link rel="alternate" hreflang="pt-BR" href="{pt_url}" />\n'
            f'  <link rel="alternate" hreflang="en" href="{en_url}" />\n'
            f'  <link rel="alternate" hreflang="x-default" href="{pt_url}" />')


def build() -> list[str]:
    written = []
    for lang, c in CHROME.items():
        other = CHROME["en" if lang == "pt" else "pt"]
        for page in c["pages"]:
            slug = page["slug"]
            pt_slug = slug if lang == "pt" else PT_OF_EN[slug]
            en_slug = EN_OF_PT[pt_slug]
            other_slug = en_slug if lang == "pt" else pt_slug
            url = f"{SITE}{c['prefix']}/{slug}/"
            html_out = TEMPLATE.format(
                lang=c["lang"], title=esc(page["title"]), description=esc(page["description"]),
                url=url, site=SITE, hreflang=hreflang_block(pt_slug, en_slug),
                jsonld=jsonld(page, c), navlinks=nav(slug, c),
                footerlinks="".join(f'        <a href="{c["prefix"]}/{sl}/">{label}</a>\n'
                                    for sl, label in c["related"].items()),
                kicker=esc(page["kicker"]), h1=esc(page["h1"]), lead=esc(page["lead"]),
                notice=c["notice"], blocks=render_blocks(page["blocks"]),
                faq=render_faq(page["faq"], c), related=render_related(slug, c),
                signup=SIGNUP, login=LOGIN, app=APP, wa=WA,
                plans_href=c["plans_href"], switch_href=f"{other['prefix']}/{other_slug}/",
                switch_lang=other["lang"], c_switch=c["switch"],
                c_login=c["login"], c_signup=c["signup"], c_plans=c["plans"], c_badge=c["badge"],
                c_cta_h2=c["cta_h2"], c_cta_p=c["cta_p"], c_brand_p=c["brand_p"],
                c_f_product=c["f_product"], c_f_company=c["f_company"], c_f_legal=c["f_legal"],
                c_f_plans=c["f_plans"], c_privacy=c["privacy"], c_terms=c["terms"],
                c_wa_label=c["wa_label"], c_wa_footer=c["wa_footer"], c_rights=c["rights"])
            out = ROOT / c["prefix"].strip("/") / slug / "index.html" if c["prefix"] else \
                ROOT / slug / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(html_out, encoding="utf-8")
            written.append(str(out.relative_to(ROOT)))
    return written


if __name__ == "__main__":
    for path in build():
        print("escrito:", path)
