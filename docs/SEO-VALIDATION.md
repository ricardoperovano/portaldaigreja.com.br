# Validação de SEO — como conferir que está tudo certo

## 1. Verificação automática

```bash
python3 tools/seo_check.py          # confere os arquivos do repositório (use antes de publicar)
python3 tools/seo_check.py --live   # confere a produção (use depois de publicar)
```

Sem dependências além do Python 3. Sai com código 1 em caso de falha, então serve para CI.

O que ele verifica, para cada URL do sitemap:

- a página existe (no modo `--live`, responde 200);
- `title` único e com até 60 caracteres;
- `meta description` única, entre 50 e 160 caracteres;
- exatamente um `<h1>`;
- canonical presente, absoluto e apontando para a própria URL;
- Open Graph (title, description, image, url) e `twitter:card`;
- JSON-LD válido e **sem** nota/avaliação (`AggregateRating`/`Review`) enquanto não houver
  avaliações reais;
- nenhum `href="#"` (link morto) e nenhum link interno quebrado;
- nenhuma imagem sem `alt`;
- nenhuma das afirmações proibidas (ver lista em `BANNED_PATTERNS`, espelhando `SEO-AUDIT.md`):
  "+500 igrejas", "R$ 2,5 mi", "centenas de igrejas", "30 dias de garantia",
  `AW-CONVERSION_ID`, "não conseguirá lê-las", estrelas de avaliação.

E no sitemap: nenhuma âncora (`#`), nenhuma URL repetida, todas no domínio.

Resultado da última execução local (13/10/2026): **896 verificações, 0 falhas**.

Nas páginas em inglês ele verifica ainda:

- `hreflang` nos dois sentidos entre a página e a sua equivalente em português, com `x-default`;
- `<html lang>` correto;
- a presença do aviso de que o sistema é em português e a cobrança é em reais.

## 2. Ao criar uma página nova

1. Acrescente o conteúdo em `tools/content_pt.py` e, se for publicar nos dois idiomas, em
   `tools/content_en.py` (só o que o produto faz — confira em
   `docs/CATALOGO-FUNCIONALIDADES-IGREJAS.md`).
2. Ligue as duas versões em `EQUIVALENT`, em `tools/build_pages.py` e em `tools/seo_check.py`.
3. `python3 tools/build_pages.py`
4. Acrescente as URLs em `sitemap.xml`.
5. `python3 tools/seo_check.py`
6. Publique e rode `python3 tools/seo_check.py --live`.

**Ao mexer na home em português**, rode `python3 tools/build_en_home.py` em seguida: ele traduz a
home para `/en/` e ERRA se encontrar uma frase nova sem tradução, em vez de publicar português na
página em inglês.

## 3. Conferência manual (uma vez, após publicar)

| O que | Como | Esperado |
|---|---|---|
| Páginas no ar | abrir as 5 URLs | 200, layout igual ao da home |
| Sitemap | `curl -s https://portaldaigreja.com.br/sitemap.xml` | 15 URLs (8 em português, 7 em inglês), nenhuma com `#` |
| 404 | abrir `/pagina-que-nao-existe` | página com a marca e links |
| Prévia de compartilhamento | colar a URL no WhatsApp | imagem e título corretos |
| Dados estruturados | [Rich Results Test](https://search.google.com/test/rich-results) | Organization, SoftwareApplication, FAQPage e BreadcrumbList sem erro |
| Mobile | abrir no celular | sem rolagem lateral, botões alcançáveis |
| Velocidade | [PageSpeed Insights](https://pagespeed.web.dev/) no celular | LCP até 2,5 s; comparar campo e laboratório |
| HTTPS | abrir `http://portaldaigreja.com.br` | deve redirecionar para https (hoje **não** redireciona — pendência B) |

## 4. Search Console (depois da publicação)

1. Enviar `https://portaldaigreja.com.br/sitemap.xml`.
2. Inspecionar e pedir indexação das 5 URLs novas.
3. Em 7 dias, conferir a cobertura: "Descoberta, não indexada" é normal no começo; "Página com
   redirecionamento" ou "Duplicada" exige correção de canonical.
4. Em 30 dias, olhar as consultas: separar marca ("portal da igreja") do resto. Só o resto mede
   o efeito deste trabalho.

## 5. Medição de conversão — o que ainda não é confiável

O site mede **cliques** no CTA (`cta_cadastro_click`), não cadastros: o cadastro acontece em
`app.portaldaigreja.com.br`, que é outro domínio e não tem medição ligada a este site. Não
configure esse evento como conversão de cadastro no GA4 ou nos relatórios — ele mede intenção.

Para medir de verdade: marcar o cadastro concluído dentro do app e ligar os dois domínios no
GA4. Até lá, o número real de cadastros está no console do super-admin.
