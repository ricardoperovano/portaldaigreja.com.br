# Catálogo de funcionalidades — o que o Portal da Igreja faz hoje

**Para que serve este documento:** separar o que o produto REALMENTE faz do que um sistema de
gestão eclesiástica poderia fazer. Nenhuma frase do site pode prometer algo marcado aqui como
C ou D. Quando um módulo novo entrar no produto, atualize esta tabela ANTES de escrever
qualquer página comercial.

- **Levantamento:** 13/10/2026, por leitura do código do repositório `gestaoigreja`
  (backend FastAPI + SPA React). Caminhos: `BE = backend/app/`, `FE = frontend/src/`.
- **Status:** **A** = implementado e validado · **B** = existe com limitação relevante ·
  **C** = há rastro/planejado, não anunciável · **D** = não existe.

## Resumo para quem escreve o marketing

1. **Os planos pagos não diferem em recursos.** No código só existem dois controles por plano:
   o limite de membros (`BE models/church.py`) e o editor do site, liberado a partir do
   Essencial (`BE api/deps.py`, `require_site_builder`). Não anuncie "relatório X só no plano Y".
2. **O Pix não tem baixa automática.** QR estático com a chave da própria igreja; a tesouraria
   confirma conferindo o extrato (`BE services/engagement.py`).
3. **O site da igreja não é otimizado para buscadores.** É renderizado por JavaScript, sem
   meta tags, sitemap ou dados estruturados por igreja. Não prometa "apareça no Google".
4. **Domínio próprio depende de configuração manual** de DNS/certificado junto ao time.
5. **Não existe:** presença/check-in, escalas de voluntários, patrimônio, secretaria
   (carteirinha, atas, cartas de transferência), anexos de comprovantes, contas a pagar com
   baixa, conciliação bancária, EBD, ministério infantil, multi-congregação, envio em massa
   de e-mail/WhatsApp, API pública e IA.

## Planos (fonte: `BE models/church.py`, `BE services/billing.py`)

| Plano | Limite de membros | Preço mensal | Site da igreja | Demais recursos |
|---|---|---|---|---|
| Gratuito | 50 | R$ 0 | não | todos |
| Essencial | 150 | R$ 79,90 | sim | todos |
| Crescimento | 500 | R$ 149,90 | sim | todos |
| Avançado | 1.000 | R$ 299,90 | sim | todos |
| Enterprise | sem limite | sob consulta | sim | todos |

Anual = 20% de desconto, cobrado de uma vez. A contagem de membros inclui visitantes,
inativos e transferidos (qualquer cadastro não excluído).

## Módulos

| # | Módulo | Status | O que existe | Evidência | Página comercial |
|---|---|---|---|---|---|
| 1 | Gestão de membros | **A** | Ficha completa (contato, endereço estruturado com ViaCEP, nascimento, batismo, estado civil/casamento, função eclesiástica, profissão, notas), status (ativo/inativo/visitante/transferido), importação de planilha com assistente, bloqueio de duplicados, exportação CSV, auditoria, consentimento LGPD, exclusão em massa | `BE models/member.py`, `services/member_import.py`, `services/member_dedupe.py` | `/cadastro-membros-igreja/` |
| 1b | Foto do membro | **D** | não há campo de foto | — | — |
| 1c | Anonimização (direito ao esquecimento) | **B** | apaga nome, e-mail, CPF, telefone, nascimento e notas; **não** limpa os campos estruturados de endereço | `BE services/member.py:134` | não citar |
| 2 | Secretaria eclesiástica | **D** | só as datas de batismo e casamento na ficha. Sem carteirinha, declaração, carta de transferência, ata ou documento | — | — |
| 3 | Financeiro | **A** (com limites) | receitas/despesas, categorias por tipo (renomear funde histórico), lançamentos recorrentes automáticos, exportação CSV, previsão de 30 dias | `BE services/finance.py`, `tasks/finance.py` | `/financeiro-para-igrejas/` |
| 3b | Anexos, contas a pagar, conciliação, orçamento, centro de custo | **D** | nada disso existe | — | declarado como limite na página |
| 4 | Dízimos, ofertas e doações | **A** | dízimo, oferta, oferta avulsa (anônima), campanha, doação; histórico; exportação CSV | `BE models/finance.py`, `services/finance.py` | `/controle-dizimos-ofertas/` |
| 4b | Pix | **B** | QR estático + copia e cola com a chave da igreja, sem PSP; intenção do membro com identificador; **confirmação manual** da tesouraria | `BE utils/pix.py`, `services/engagement.py:170` | idem, com a limitação explicitada |
| 4c | Informe anual do membro (PDF) | **B** | existe no portal; o PDF traz o nome da plataforma, não o da igreja (defeito a corrigir) | `BE services/portal.py:137` | citado sem detalhar o PDF |
| 4d | Doação por cartão/boleto | **D** | Stripe só cobra a assinatura da plataforma | `BE services/billing.py` | — |
| 5 | Campanhas | **A** | meta, período, status, progresso, relatório e visão do membro | `BE models/finance.py`, `services/report.py:184` | citada nas páginas |
| 6 | Grupos e células | **B** | cadastro, líder, informações de reunião, papel do participante. **Sem** presença, frequência ou multiplicação | `BE services/group.py` | citado |
| 7 | Ministérios/departamentos | **B** | mesmo modelo de grupos | `BE models/member.py:151` | citado |
| 8 | Escalas de voluntários | **D** | não existe | — | — |
| 9 | Cultos e eventos | **B** | agenda com local, período e visibilidade pública; alimenta o site. **Sem** inscrição, presença, recorrência ou iCal | `BE models/engagement.py:77` | `/site-para-igrejas/` |
| 10 | Frequência/check-in | **D** | não existe | — | — |
| 11 | Acompanhamento pastoral | **B** | pedidos de oração com fila e resposta; aniversariantes e aniversários de casamento por e-mail; lista de quem parou de contribuir. **Sem** registro de visitas | `BE services/engagement.py`, `tasks/notifications.py` | citado |
| 12 | Visitantes | **B** | só o status "visitante" na ficha. Sem formulário público nem funil | `BE models/member.py:17` | não destacar |
| 13 | Escola bíblica/ensino | **D** | não existe | — | — |
| 14 | Ministério infantil | **D** | não existe | — | — |
| 15 | Patrimônio | **D** | não existe | — | — |
| 16 | Comunicação | **B** | mural de avisos no portal; e-mails do sistema (convite, redefinição, aniversariantes, reativação). **Sem** envio em massa, segmentação, WhatsApp oficial, SMS ou push | `BE models/engagement.py:94`, `tasks/email.py` | citado com cuidado |
| 17 | Portal do membro | **A** | perfil, contribuições, informe anual, campanhas, Pix, orações, agenda, avisos, consentimentos, sessões, exportação dos próprios dados | `BE api/v1/me.py` | citado em todas |
| 17b | Transparência para o membro | **D** | o relatório de transparência é acessível só pela equipe | `BE api/v1/reports.py:77` | **não** prometer ao membro |
| 18 | Site público da igreja | **A** (editor) | páginas, 13 tipos de bloco, tema/cores/logo, redes sociais, upload de imagens, galeria, agenda ao vivo, Pix, mapa, horários de culto | `BE services/site.py`, `FE portal/PortalView.tsx` | `/site-para-igrejas/` |
| 18b | SEO do site da igreja | **D** | SPA sem SSR; sem meta/OG/sitemap/robots por igreja; página inexistente responde 200 (soft-404); link compartilhado não mostra prévia da igreja | `FE pages/PublicPortal.tsx`, `frontend/nginx.conf` | **proibido prometer** |
| 18c | Domínio próprio | **B** | o sistema resolve o domínio, mas DNS e certificado são manuais | `BE models/site.py:44` | "caso a caso, com o time" |
| 19 | Relatórios | **A** | painel com pulso, financeiro por período, fechamento do mês em PDF, transparência (PDF/Excel), doadores, por categoria (PDF/Excel), aniversariantes, exportações CSV | `BE services/report.py`, `services/category_report.py` | `/prestacao-de-contas-igreja/` |
| 20 | Multi-igreja/congregações | **D** | cada igreja é um ambiente isolado; não há consolidação entre unidades | `BE models/church.py` | **não** prometer |
| 21 | Usuários e permissões | **A** | 5 papéis, 2FA opcional (TOTP), sessões por dispositivo com revogação, bloqueio por tentativas, auditoria imutável, primeiro acesso por link | `BE api/deps.py`, `services/twofa.py`, migração 0018 | citado |
| 21b | Permissões granulares | **D** | o acesso é por papel fixo, não por módulo ou ministério | — | — |
| 22 | Documentos e arquivos | **D** | só imagens do site; não há repositório de documentos | — | — |
| 23 | Ações sociais e missões | **C** | dá para usar campanhas e o tipo "doação", mas não é um módulo | — | — |
| 24 | Integrações | **B** | Stripe (assinatura), Pix sem PSP, e-mail (SMTP/SES/Cloudflare), ViaCEP, armazenamento em nuvem, exportações CSV/Excel. **Sem** WhatsApp oficial, Google Calendar, API pública ou webhooks de saída | `BE services/billing.py`, `tasks/email.py` | citar só o que existe |
| 25 | Inteligência artificial | **D** | nenhuma | — | — |
| 26 | Administração da plataforma | **A** | cadastro autoatendido, assistente de primeiro acesso, e-mails de reativação (3/7/15 dias), console do super-admin, programa de parceiros, cortesia e degustação | `BE api/v1/admin.py`, `tasks/onboarding.py` | uso interno |
| 26b | Exclusão da conta pela igreja | **D** | hoje só o super-admin exclui | `BE api/v1/admin.py:150` | — |
| 26c | Retenção automática (LGPD) | **B** | existe, mas vem desligada por padrão | `BE tasks/retention.py`, `config.py` | não detalhar |

## Segurança — o que pode ser afirmado

| Afirmação permitida | Base |
|---|---|
| "CPF, telefone e endereço dos membros são criptografados no banco" | `BE models/member.py:61-89` |
| "Senhas não são guardadas em texto" (Argon2) | `BE core/security.py` |
| "Confirmação em duas etapas disponível" (opcional, por usuário) | `BE services/twofa.py` |
| "Os dados de cada igreja ficam separados, em duas camadas" (aplicação + RLS no Postgres) | migrações 0004 e seguintes |
| "Trilha de auditoria de quem alterou o quê", imutável | migração 0018 |
| "Consentimento por finalidade, termo versionado e exportação dos dados do membro" | `BE services/consent.py`, `services/portal.py` |

**Não** afirmar: que os dados são ilegíveis para um invasor (nome, data de nascimento, bairro e
cidade ficam em texto), que o acesso indevido é impossível, 2FA obrigatório, nem conformidade
"garantida" com a LGPD.

## Oportunidades de produto (ordenadas por impacto comercial percebido)

1. **Secretaria**: declaração de membro, carta de transferência e carteirinha — pedidos clássicos
   de igreja, hoje ausentes, e que sustentariam uma página `/secretaria-de-igreja/`.
2. **Anexo de comprovante** no lançamento financeiro: a objeção mais provável de um tesoureiro.
3. **Presença em cultos e células**: habilitaria todo o vocabulário de "gestão de células".
4. **Escalas de voluntários**: busca com intenção própria e alto uso semanal.
5. **SEO do site das igrejas** (SSR ou pré-render, meta/OG, sitemap por igreja): transformaria o
   site incluso em argumento de verdade — hoje ele é bonito, mas invisível para buscadores.
6. **Corrigir o PDF do informe anual** para trazer o nome da igreja.
7. **Anonimização completa** dos campos estruturados de endereço.
