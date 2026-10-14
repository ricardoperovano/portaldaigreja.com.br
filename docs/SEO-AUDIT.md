# Auditoria de SEO — portaldaigreja.com.br

Auditoria de 13/10/2026 sobre o site publicado (GitHub Pages, HTML estático) e sobre o código do
produto. Cada item traz a evidência, o que foi feito e o que ficou pendente.

Rode `python3 tools/seo_check.py` depois de qualquer alteração: ele falha se um dos problemas
críticos voltar.

## 1. Resolvido nesta rodada

| # | Problema | Evidência (antes) | Correção |
|---|---|---|---|
| 1 | Sitemap com 6 âncoras (`/#recursos`, `/#planos`, `/#depoimentos`…) tratadas como páginas | `sitemap.xml:12-52` | Sitemap reescrito só com URLs reais (home, as 5 páginas novas e `/whatsapp/`), sem `changefreq`/`priority` e com `lastmod` atualizado |
| 2 | "+500 igrejas" e "+R$ 2,5 mi gerenciados" sem lastro, contradizendo "centenas de igrejas" em outro trecho | `index.html:266,268,323,666` | Removidos. A faixa de confiança passou a citar fatos verificáveis (feito no Brasil, suporte em português, plano gratuito, LGPD) |
| 3 | Três depoimentos com nome, cargo e igreja, com estrelas 5/5, sem autorização | `index.html:277-325` | Seção inteira removida, junto com as estrelas e o contador "mais de 500 igrejas" |
| 4 | Garantia absoluta de segurança: "Mesmo que alguém tente roubá-las, não conseguirá lê-las" | `index.html:463,478` | Reescrito para o que o código faz: CPF/telefone/endereço criptografados, senhas nunca em texto, 2FA opcional, separação por igreja em duas camadas, consentimento e auditoria |
| 5 | "30 dias de garantia ou seu dinheiro de volta" — política inexistente | `index.html:140,587,636` | Removida (também do JSON-LD e do FAQ). No lugar: plano gratuito para sempre, cancelamento quando quiser, sem fidelidade |
| 6 | Evento de conversão com placeholder `AW-CONVERSION_ID/CONVERSION_LABEL` disparando em todo clique | `script.js:131-133` | Removido. O evento `conversion_cadastro` virou `cta_cadastro_click`, com comentário explicando que é clique, não cadastro |
| 7 | Links legais mortos (`href="#"`) em Privacidade, Termos e Sobre | `index.html:695,703,704`; `whatsapp/index.html:245` | Apontam para as páginas em vigor (`app.portaldaigreja.com.br/privacidade` e `/termos`). "Sobre" (sem página) foi retirado |
| 8 | Planos anunciavam recursos exclusivos que não existem ("Auditoria avançada", "Exportações avançadas", "Suporte prioritário", "Múltiplos usuários") | `index.html:490-527` | Cartões reescritos: todos os planos pagos têm os mesmos recursos; o que muda é o limite de membros. O selo "Mais popular" saiu (não é comprovável) |
| 9 | Mockup do painel com números fictícios e "Junho 2026" sem rótulo | `index.html:226-239` | Marcado como "Exemplo", e a descrição para leitores de tela diz que os números são fictícios |
| 10 | Title da home com 98 caracteres e `meta keywords` inútil | `index.html:16,19` | Title encurtado e distinto do da página-pilar; `keywords` removida |
| 11 | Sem página 404 própria (404 genérico do GitHub) | — | `404.html` com a marca, links para as páginas principais e `noindex` |
| 12 | `/whatsapp` com canonical sem barra (redireciona 301) e sem Twitter Card | `whatsapp/index.html:22` | Canonical corrigido para `/whatsapp/`, Twitter Card e dimensões de OG adicionados |
| 13 | Proporção declarada do logo errada (180×40 para uma imagem 1135×455) | `index.html:160` | Atributos corrigidos para 100×40 (proporção real), reduzindo deslocamento de layout |
| 14 | `favicon.ico` inexistente (404 em todo acesso) | — | Declarado `favicon-48.png` como ícone padrão |
| 15 | Nenhuma página além da home: tudo competia numa URL só | — | Cinco páginas comerciais criadas (ver `docs/SEO-STRATEGY.md`), com links internos entre elas e a partir da home |
| 16 | **Sem consentimento de cookies**: GA4 e o chat Monitchat carregavam antes de qualquer aviso | `index.html:5-12,732` | Google Consent Mode entra **negado** no `<head>` de todas as páginas; o banner (em português e em inglês) pergunta antes, e só depois do aceite o GA4 é liberado e o chat é carregado. A escolha fica no navegador da pessoa; recusar não carrega nada |

## 2. Pendente — depende de você

| # | Pendência | Por que importa | Como resolver |
|---|---|---|---|
| B | **"Enforce HTTPS" do GitHub Pages aparentemente desligado**: `http://portaldaigreja.com.br` responde 200 sem redirecionar | Conteúdo duplicado e aviso de site não seguro | Ligar em Settings → Pages → Enforce HTTPS |
| C | **`www` não resolve** | Quem digita www não chega ao site | Criar o CNAME de `www` apontando para o apex |
| D | **Conversão real não é medida.** O cadastro acontece em `app.portaldaigreja.com.br`, domínio diferente, sem medição ligada | Hoje não dá para saber quantos cadastros o site gerou | Medir o evento de cadastro concluído no app e ligar os dois domínios no GA4 |
| E | **~2,5 MB de imagens não usadas** versionadas (`assets/images/*.jpg`, `logo-mark.*`, `favicon.jpg`) | Peso do repositório e confusão de arquivos | Apagar as não referenciadas (não fiz: são seus arquivos de marca) |
| F | **Google Fonts bloqueia a renderização** | Atraso no primeiro desenho da página | Hospedar as fontes no próprio site ou carregá-las de forma assíncrona |
| G | **Search Console** não auditado | Sem dados de impressão, clique e cobertura | Enviar o sitemap novo e inspecionar as 5 páginas após a publicação |

## 3. Afirmações que ficaram no site e a base de cada uma

| Afirmação | Base |
|---|---|
| "Site da igreja incluso em todos os planos pagos" | `require_site_builder = require_plan(essencial)` |
| "Dízimo por Pix sem intermediário" | QR estático com a chave da própria igreja, sem PSP |
| "A tesouraria confirma cada Pix conferindo o extrato" | confirmação manual no código |
| Limites de 50/150/500/1.000 membros e preços | `PLAN_MEMBER_LIMITS` e `PLAN_PRICE_CENTS` |
| "Usuários da equipe sem limite" | não há limite de usuários por plano no código |
| "Importa planilha do Excel e CSV" | assistente de importação em 4 passos |
| "Não deixa cadastrar a mesma pessoa duas vezes" | regra de duplicados por CPF, e-mail e nome |
| Segurança (criptografia de campos sensíveis, 2FA, separação por igreja, auditoria, LGPD) | ver `docs/CATALOGO-FUNCIONALIDADES-IGREJAS.md` |

## 4. O que continua proibido escrever

- Qualquer número de clientes, valores administrados ou avaliação em estrelas sem documento.
- Depoimento sem autorização por escrito da pessoa e da igreja.
- "Pix com baixa automática" ou "conciliação automática".
- "Site da igreja otimizado para o Google" / "sua igreja aparece nas buscas" — o site das igrejas
  é renderizado por JavaScript, sem meta tags nem sitemap próprios.
- "Domínio próprio" como recurso autosserviço.
- Recursos inexistentes: presença, escalas, patrimônio, secretaria (carteirinha/atas/cartas),
  EBD, ministério infantil, conciliação bancária, contas a pagar, multi-congregação,
  WhatsApp automatizado, API pública, IA.
- Garantia de reembolso, SLA ou onboarding assistido enquanto não forem política escrita.
