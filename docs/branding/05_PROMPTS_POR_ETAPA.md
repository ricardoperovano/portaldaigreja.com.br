# Prompts menores — execute em ordem na sua IA de código

O **prompt mestre** (`01_PROMPT_MESTRE_COPIAR_NA_IA.md`) deve ser enviado antes destes para estabelecer a identidade, os tokens, os caminhos e as restrições.

## 1. Diagnóstico do projeto — NÃO ALTERAR CÓDIGO

> Analise a aplicação Portal da Igreja existente. Não modifique arquivos. Liste frameworks, organização de pastas, componentes de layout, CSS/Tailwind, rotas públicas e privadas, módulos, autenticação, RBAC, Pix, banco, integrações e testes. Proponha a aplicação incremental do kit de marca anexado, explicando exatamente quais arquivos precisa alterar na Fase 1, Fase 2 e Fase 3. Não refatore backend por estilo.

## 2. Fundação visual

> Com base no diagnóstico aprovado, adote `tokens/design-tokens.json` e os arquivos de `logos/` e `favicons/` na stack existente. Padronize fonte, cores, botões, campos, cards, badges, tabelas, modais e feedback. Nesta etapa, não modifique endpoints, regras de negócio, banco de dados ou telas além dos componentes visuais compartilhados. Execute build/lint/testes.

## 3. Site público

> Atualize somente as páginas públicas existentes usando `referencias/02_site_publico.png` como direção visual, os SVGs oficiais e o mapa `02_MAPA_VISUAL_ONDE_USAR_CADA_ARQUIVO.md`. Hero marfim, títulos azul institucional, CTAs azuis, destaques dourados discretos e imagens reais autorizadas. Preserve SEO, cadastro, login, preços do sistema, recursos, seções, depoimentos comprovados e links. Não use números fictícios do mockup. Entregue screenshots desktop/mobile e testes de navegação.

## 4. Painel administrativo

> Atualize os layouts e componentes do sistema existente usando `referencias/03_sistema_dashboard.png` como referência, não como tela a copiar. Sidebar azul, área de trabalho muito clara, cards brancos e gráficos azul/azul-claro. Aplique aos módulos já existentes em ordem: dashboard, membros, contribuições/Pix, financeiro, ministérios, agenda, relatórios, configurações e outros encontrados. Não altere cálculos, permissões, endpoints, bancos nem fluxo Pix. Valide os formulários e ações CRUD antes e depois.

## 5. Portal do membro e mobile

> Padronize portal do membro, login e experiência mobile com o mesmo design system, respeitando eventuais temas próprios de sites de igrejas clientes. Preserve escopo do usuário, extrato, informes, Pix e demais fluxos. Teste em 360, 390, 768, 1024 e 1440px. Adicione suporte correto a teclado, leitores de tela e estados vazios.

## 6. Auditoria final

> Faça uma revisão completa do rebranding: mapeie mudanças e riscos, rode build e testes disponíveis, confira SEO/acessibilidade/performance, examine contraste e overflow, teste login, membros, finanças, Pix sem pagamento real, exportações, RBAC e navegação. Mostre lista de arquivos alterados, screenshots antes/depois e pendências. Não afirme testes que não foram executados.
