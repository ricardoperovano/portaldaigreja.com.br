# Estratégia de SEO — Portal da Igreja

Objetivo comercial: trazer igrejas que já estão procurando um sistema de gestão e levá-las ao
cadastro gratuito. Este documento diz quais páginas existem, para qual busca cada uma responde e
o que vem depois. Nenhuma estimativa de volume ou dificuldade é inventada aqui: onde não houve
dado verificado, está escrito "a verificar no Search Console / Keyword Planner".

## 1. Arquitetura atual

```
/                               marca + visão geral + planos (página de conversão)
├── /sistema-gestao-igrejas/    página-pilar: a solução completa
├── /cadastro-membros-igreja/   secretaria: ficha, famílias, grupos, importação
├── /controle-dizimos-ofertas/  tesouraria: dízimo, oferta, Pix, informe anual
├── /financeiro-para-igrejas/   tesouraria: receitas, despesas, relatórios
├── /site-para-igrejas/         presença digital: construtor de site incluso
└── /whatsapp/                  página de contato (fina, mantida por já existir)
```

Todas as páginas novas linkam entre si ("Veja também"), a home linka para as cinco, e as cinco
voltam para a home e para `/#planos`. Sem página órfã e sem link morto — verificado por
`tools/seo_check.py`.

## 2. Mapa de palavras-chave

Volume e concorrência **não foram medidos** (sem acesso a ferramenta de dados no momento da
execução). A prioridade abaixo vem da intenção comercial, não de volume estimado.

| Palavra-chave | Intenção | Página destino | Prioridade |
|---|---|---|---|
| sistema de gestão para igrejas | compra | `/sistema-gestao-igrejas/` | 1 |
| software para igrejas | compra | `/sistema-gestao-igrejas/` | 1 |
| programa para administrar igreja | compra | `/sistema-gestao-igrejas/` | 2 |
| sistema de gestão eclesiástica | compra | `/sistema-gestao-igrejas/` | 2 |
| controle de dízimos e ofertas | compra/problema | `/controle-dizimos-ofertas/` | 1 |
| dízimo por Pix / QR Code para igreja | funcionalidade | `/controle-dizimos-ofertas/` | 1 |
| sistema de dízimo online | compra | `/controle-dizimos-ofertas/` | 2 |
| cadastro de membros de igreja | compra/problema | `/cadastro-membros-igreja/` | 1 |
| controle de membros de igreja | compra | `/cadastro-membros-igreja/` | 2 |
| importar planilha de membros | problema | `/cadastro-membros-igreja/` | 3 |
| sistema financeiro para igrejas | compra | `/financeiro-para-igrejas/` | 1 |
| tesouraria de igreja online | compra | `/financeiro-para-igrejas/` | 2 |
| prestação de contas de igreja | problema | `/financeiro-para-igrejas/` | 2 |
| relatório financeiro de igreja | problema | `/financeiro-para-igrejas/` | 3 |
| criar site para igreja | compra | `/site-para-igrejas/` | 1 |
| site para igreja evangélica | compra | `/site-para-igrejas/` | 2 |
| portal do membro | funcionalidade | `/sistema-gestao-igrejas/` (seção) | 3 |
| gestão de células / ministérios | funcionalidade | `/cadastro-membros-igreja/` (seção) | 3 |

**Canibalização:** "sistema de gestão" e "software para igrejas" respondem à mesma intenção e
ficam na mesma página, de propósito. A home disputa a marca ("Portal da Igreja"), por isso o
title dela é diferente do da página-pilar.

## 3. Páginas que NÃO devem ser criadas agora

| URL candidata | Por quê não |
|---|---|
| `/secretaria-de-igreja/` | o produto não tem carteirinha, declaração, carta de transferência nem atas. A página prometeria o que não existe |
| `/gestao-celulas-ministerios/` | existe cadastro de grupos, mas não presença nem multiplicação: conteúdo fino demais para sustentar uma página própria. Fica como seção |
| `/gestao-eventos-igreja/` | a agenda não tem inscrição nem presença; hoje é um bloco do site da igreja |
| `/relatorios-financeiros-igreja/` | canibalizaria `/financeiro-para-igrejas/`, que já cobre relatórios |
| `/portal-do-membro/` | pode valer no futuro; hoje repetiria trechos das outras duas páginas |

Reavalie cada uma quando o módulo correspondente existir (ver oportunidades no catálogo).

## 4. Conteúdo editorial (`/blog/`) — ainda não criado

Recomendo começar com três artigos, e só depois decidir se o blog continua. Cada um responde a
uma dúvida real de quem administra igreja e leva para a página comercial correspondente:

1. "Como organizar a tesouraria da igreja em 5 passos" → `/financeiro-para-igrejas/`
2. "Como fazer a prestação de contas da igreja sem expor quem contribuiu" → `/controle-dizimos-ofertas/`
3. "Como migrar a lista de membros da planilha para um sistema" → `/cadastro-membros-igreja/`

Regras: nada de orientação jurídica, contábil ou fiscal apresentada como consultoria; nada de
texto gerado em massa; cada artigo precisa de um ponto de vista próprio e de exemplos reais do
produto.

## 5. Medição

Hoje o site mede cliques (`cta_cadastro_click`, `whatsapp_click`, `login_click`, `scroll_depth`),
não cadastros. **Clique no CTA não é cadastro.** Para medir resultado de verdade é preciso
marcar o cadastro concluído dentro do app e ligar os dois domínios no GA4 (pendência D da
auditoria). Enquanto isso não existir, use estes indicadores:

- Impressões e cliques por página no Search Console (separando marca de não marca).
- Posição média das consultas das cinco páginas.
- Cliques no CTA por página (proporção em relação às sessões).
- Cadastros, contados no próprio app (console do super-admin).

## 6. Acompanhamento de 90 dias

**Dias 1–7** — enviar o sitemap no Search Console, inspecionar as 5 URLs novas, conferir se as
páginas foram descobertas, validar os eventos no GA4 em tempo real.

**Dias 8–30** — acompanhar indexação e corrigir exclusões ("Descoberta, não indexada" é comum em
site novo); conferir se a home e a página-pilar não estão competindo pela mesma consulta.

**Dias 31–60** — ler as consultas sem marca que já aparecem; ajustar title e description das
páginas com impressão alta e CTR baixo; reforçar links internos a partir da home para a página
com melhor desempenho.

**Dias 61–90** — comparar cliques orgânicos com cadastros no app; decidir se cria o blog, se cria
`/secretaria-de-igreja/` (caso o módulo exista até lá) e quais temas têm demanda real.

Não há meta de posição: ranking não se promete. A meta é cadastro de igreja, medido no app.
