# PROMPT MESTRE — REBRANDING PORTAL DA IGREJA

Você é uma equipe sênior de design de produto, UX/UI, frontend, acessibilidade e engenharia de software. Sua tarefa é **aplicar um rebranding visual completo, elegante, institucional e consistente ao projeto EXISTENTE “Portal da Igreja” (portaldaigreja.com.br)**, incluindo **site público, páginas de autenticação, sistema administrativo, portal do membro e páginas públicas geradas para igrejas**, caso existam no repositório. Preserve o nome **Portal da Igreja** e o domínio existente.

## DIRETRIZ CRÍTICA: REFORMULAR, NÃO RECONSTRUIR

- **NÃO recrie o site ou sistema do zero. NÃO substitua a aplicação existente por templates, demonstrações ou telas estáticas.**
- Inspecione primeiro o repositório real: stack, estrutura, estilos, componentes, rotas, layout, permissões, autenticação, build, testes e contratos de API.
- Preserve banco de dados, dados, regras de negócio, rotas, URLs indexadas, SEO, integrações, Pix, relatórios, exportações, cálculos, filtros, tabelas, formulários e fluxos existentes.
- Não modifique modelos, migrations, endpoints, payloads, schemas de validação nem contratos de integração **somente por razões de aparência**.
- Se alguma alteração funcional for realmente necessária, documente a razão, proponha o menor ajuste compatível e solicite confirmação antes de mudanças destrutivas.
- Não exclua módulos ou controles porque eles não aparecem nos mockups ilustrativos.
- Implemente gradualmente e teste antes/depois. Não simule sucesso de deploy, pagamentos ou testes.

## OBJETIVO DE MARCA

Transformar a percepção do Portal da Igreja em **software de gestão eclesiástica profissional, confiável, acolhedor, moderno e claro**, para igrejas pequenas ou grandes. A estética precisa unir seriedade administrativa e propósito cristão **sem símbolos religiosos excessivos**.

**Nome oficial:** Portal da Igreja  
**Assinatura:** Tecnologia a serviço da sua missão.  
**Símbolo:** arcos de um portal iluminado, sem cruz destacada.  
**Tom:** humano, respeitoso, direto, acolhedor, moderno, sem exagero visual.

## 1. ARQUIVOS E REFERÊNCIAS DISPONÍVEIS

Os arquivos fornecidos com este prompt estão no pacote `Portal_da_Igreja_Kit_Rebranding`:

### Logos em produção
- `logos/horizontal-fundo-claro.svg`: **preferencial no header claro do site público, emails claros, materiais sobre marfim/branco**.
- `logos/horizontal-fundo-escuro.svg`: **header escuro, sidebar escura do sistema e rodapés escuros**. Essa versão traz fundo azul institucional; se precisar de um lockup transparente para fundo escuro, use o símbolo e palavra em branco da mesma identidade, preservando cores e proporções.
- `logos/horizontal-monocromatica.svg`: **impressão simples, situações de uma cor**.
- `logos/vertical-fundo-claro.svg`: **login, onboarding, páginas institucionais e apresentações**.
- `logos/vertical-fundo-escuro.svg`: **materiais escuros, quando houver espaço vertical**.
- `logos/simbolo-colorido.svg`: **marca isolada**, ícones de perfil da marca e cabeçalhos compactos.
- `logos/simbolo-branco.svg`, `simbolo-azul.svg`, `simbolo-preto.svg`: **uso monocromático contextual**.
- Há versões `.png` das logos principais para ambientes que não aceitem SVG.

### Ícones e imagens realmente utilizáveis
- `favicons/favicon.svg`, `favicon-16.png`, `favicon-32.png`: **favicon do navegador**.
- `favicons/apple-touch-icon.png`: **atalho em dispositivos Apple**.
- `favicons/pwa-192.png`, `favicons/pwa-512.png`: **manifest PWA (se o projeto for PWA)**.
- `imagens/hero-arquitetura-abstrata.svg` ou `.png`: **ilustração decorativa abstrata de portal para o HERO público**; pode combinar com foto real autorizada, mas não use screenshot de mockup como imagem do sistema real.
- `imagens/padrao-arcos.svg`: **textura muito sutil para rodapé, banners, destaques e seções institucionais**.
- `imagens/capa-compartilhamento-og.png`: **Open Graph/Twitter cards em 1200×630**.
- `imagens/paleta-oficial.png`: **consulta visual das cores**.

### Apenas referências, NÃO elementos de interface prontos
- `referencias/01_identidade_visual.png`: **conceito de marca, composição, tipografia e fotografia**.
- `referencias/02_site_publico.png`: **direção visual da home e seções**.
- `referencias/03_sistema_dashboard.png`: **direção visual do painel desktop/mobile**.

**IMPORTANTE:** mockups são referências criativas, não prints reais ou um inventário definitivo de módulos. Não use os números, rostos, depoimentos e preços que aparecem ilustrados nesses mockups como dados de verdade. Não recorte logos de dentro dos mockups: use os SVGs oficiais fornecidos.

### Design tokens
- `tokens/design-tokens.json`: **fonte de verdade** para variáveis de cor, tipografia, espaçamento, raio, elevação e estados.
- `tokens/portal-theme.css`: **variáveis CSS e exemplos** que podem ser adaptados ao framework já utilizado. Se o projeto tem Tailwind, MUI, Bootstrap, Chakra, Vuetify ou outro sistema, mapeie os tokens sem duplicar estilos nem trocar a stack.

## 2. PALETA OFICIAL — USO OBRIGATÓRIO POR CONTEXTO

| Token | Hex | Aplicação |
|---|---|---|
| Azul institucional `primary` | `#0F2D4A` | Logotipo, títulos, links principais, botões primários, sidebar, header escuro |
| Azul profundo `primaryDeep` | `#091E32` | Hover de fundos muito escuros, rodapé escuro, áreas de contraste |
| Azul hover `primaryHover` | `#19466E` | Hover de CTA, itens selecionados, links em interação |
| Dourado sóbrio `accent` | `#C6A664` | Filetes, destaques discretos, bordas especiais, pequenos ícones, tags premium |
| Dourado para texto `accentText` | `#86642D` | Texto dourado **sobre fundos claros**, garantindo legibilidade |
| Marfim `ivory` | `#F7F5EF` | Fundo principal do marketing, alternância suave de seções |
| Azul ardósia `slate` | `#4B6478` | Subtítulos, textos secundários, detalhes de navegação |
| Azul claro `sky` | `#6FA9DD` | Gráficos, ícones de apoio, pequenas áreas informativas |
| Branco `surface` | `#FFFFFF` | Cards, tabelas, formulários e conteúdo principal do sistema |
| Fundo interno `canvas` | `#F5F7F9` | Fundo geral do painel administrativo |
| Texto principal `text` | `#172B3D` | Parágrafos, labels, tabelas |
| Texto secundário `muted` | `#5A6F81` | Metadados, placeholders, descrições |
| Bordas `border` | `#DEE5EA` | Separação de componentes e tabelas |
| Verde sucesso | `#168157` | Status ativo, concluído, confirmado |
| Amarelo/âmbar status | `#906013` | Pendências, avisos |
| Vermelho status | `#B83E49` | Cancelado, bloqueado, erros, ações destrutivas |
| Foco de teclado | `#2779B7` | Anel de foco visível e acessível |

**Regras visuais:**
- Azul-marinho = cor estrutural; marfim/branco = respiro; dourado = ACENTO (idealmente menos de 10% da composição).
- **Não usar dourado claro para parágrafos sobre branco.** Use `accentText` nos textos pequenos.
- Não usar verde/vermelho para enfeite ou dashboards genéricos: somente quando possuem significado semântico.
- Evitar gradientes exagerados, efeitos neon, sombras pesadas, cartões saturados e emojis como ícones.
- Usar `border: 1px solid #DEE5EA` nas superfícies e sombras discretas apenas quando necessário.

## 3. TIPOGRAFIA E ESTILO DE COMPONENTES

- Preferencial para títulos: **Manrope**, pesos 600 e 700. Caso o projeto não tenha Manrope e adicionar fonte seja indesejável, use **Inter**.
- Para conteúdo do sistema: **Inter** 400, 500, 600. Fallback `system-ui, sans-serif`.
- H1 marketing: `clamp(36px, 4vw, 56px)`, peso 700, line-height 1.12, máximo 12 a 16 palavras por bloco.
- H2: 32–40px; H3: 22–26px; texto normal 16px/24px; sistema densidade 14–16px.
- Botões e campos: radius 10–12px; cards 16px; seções premium 20–24px.
- Ícones preferenciais **Lucide** ou a biblioteca de ícones JÁ existente: traço 1.8–2.0, tamanhos 18–22px, semanticamente adequados. **Nunca ícones emoji.**
- Grid site: largura máxima 1200px, margem lateral responsiva; espaçamento vertical consistente.
- Grid dashboard: sidebar ~256px no desktop se compatível, topo 64–72px, espaços de 16–24px entre cards.
- Botões: primário `#0F2D4A` com branco; secundário claro com borda azul; dourado apenas para marcação excepcional, nunca todos os CTAs.
- Foco de teclado sempre visível, labels reais, navegação sem mouse, mensagens de erro acessíveis, contrastes WCAG AA.
- Microinterações 150–220ms; respeitar `prefers-reduced-motion`.

## 4. SITE PÚBLICO (MARKETING) — LOCAL EXATO DE APLICAÇÃO

### 4.1 Header fixo ou semi-fixo
- Fundo inicial branco/marfim, separação delicada na rolagem.
- Logo `logos/horizontal-fundo-claro.svg` à esquerda.
- Navegação funcional **com as âncoras, links e rotas reais já implementadas**: Recursos, Como funciona, Segurança, Planos, FAQ, Entrar (ajustar ao conteúdo existente).
- CTA primário azul “Criar conta grátis” ou texto real atual, apontando ao fluxo legítimo de cadastro.
- Mobile: menu navegável, fechamento correto, foco de teclado, botão de ação acessível.

### 4.2 Hero da página inicial
- Fundo marfim `#F7F5EF` com espaço negativo generoso.
- Cabeçalho pequeno: “SISTEMA DE GESTÃO ECLESIÁSTICA”.
- H1 sugerido: **“Sua missão é cuidar de pessoas. A nossa é simplificar sua gestão.”**
- Subtítulo: **“Centralize membros, finanças, contribuições e atividades em uma plataforma segura, organizada e fácil de usar.”**
- CTA azul para cadastro e CTA secundário para conhecer recursos.
- Imagem à direita: preferencialmente **captura REAL da interface redesenhada**, feita do projeto funcionando (com dados fictícios identificados como exemplo e sem vazamento de dados). Como decoração, usar `imagens/hero-arquitetura-abstrata.svg` a baixa intensidade.
- Se fotografia real for usada, preferir comunidades brasileiras autênticas em igreja, luz natural, autorização/licença verificada, rostos diversos e composições não exageradamente devocionais.
- Preservar informações legítimas do produto (ex.: plano grátis, Pix). Não afirmar capacidades que não foram validadas.

### 4.3 Benefícios rápidos e recursos
- Blocos de benefícios com 3 ou 4 cartões: organização, transparência, facilidade de uso e acompanhamento de membros.
- Cards brancos, ícone Lucide em azul, título azul institucional, texto secundário ardósia.
- Mostrar recursos **existentes e auditados no sistema**, incluindo quando presentes: gestão de membros, dízimos/ofertas via Pix, financeiro por categorias, fechamento mensal, contas recorrentes, portal do membro, site da igreja, agenda, pedidos de oração, avisos, famílias/grupos/ministérios, campanhas, dashboard e aniversariantes.
- Não criar links quebrados ou páginas vazias só porque o mockup mostrou um cartão.

### 4.4 Como funciona
- 3 etapas com numeração discreta e setas finas: cadastrar igreja → importar/cadastrar dados → acompanhar a gestão.
- Usar fundo branco ou marfim alternado, título forte e exemplos reais das funcionalidades.

### 4.5 Segurança, confiança e LGPD
- Aparência institucional, ícones de escudo, cadeado, usuário, histórico.
- Reaproveitar as garantias e explicações **que forem verdadeiras no código e na documentação**. Não alegar criptografia específica, conformidade LGPD auditada, MFA ou segregação de dados se não puder comprovar.
- Reservar seção de 2 colunas com texto à esquerda e painel ilustrativo limpo à direita.

### 4.6 Depoimentos e prova social
- Layout elegante, fotos somente autorizadas.
- **Não inventar depoimentos, logomarcas de clientes, estatísticas ou nomes de pessoas.** Confirmar legitimidade do que está publicado antes de destacá-lo. Se não houver evidências, ocultar o bloco ou usar informações verificáveis.

### 4.7 Planos e preços
- **Usar os valores, limites, ciclos e regras do backend/site ATUAL**, não os exemplos dos mockups.
- Cards brancos com borda, opção principal destacada com linha superior dourada, NÃO preencher o card inteiro de ouro.
- Alternância mensal/anual deve manter os cálculos e comportamento existentes, sem alterar regras comerciais.
- CTA de cada plano deve preservar a identidade do plano e o encaminhamento correto.

### 4.8 FAQ e CTA final
- FAQ tipo accordion acessível; reaproveitar perguntas e respostas reais.
- CTA final com fundo azul `#0F2D4A`, texto branco e detalhe de arcos `imagens/padrao-arcos.svg` com opacidade muito baixa; botão de alto contraste.
- Rodapé com logo adequado a fundo escuro, links originais, termos, privacidade e dados reais.

### 4.9 SEO
- Manter domínio, slugs, links internos, canonical, metadados atuais relevantes, robots/sitemap, marcação estruturada válida, performance Core Web Vitals e acessibilidade.
- Atualizar logo de `Organization` e imagem OG com `imagens/capa-compartilhamento-og.png`.
- Não usar renderização pesada para seções estáticas apenas por estética.
- Preservar landing pages SEO existentes e seus textos relevantes. Melhorar hierarquia H1/H2/H3 sem perder conteúdo otimizado.

## 5. SISTEMA ADMINISTRATIVO — LOCAL EXATO DE APLICAÇÃO

### 5.1 Estrutura geral
- Sidebar azul `#0F2D4A`, logo adequado ao fundo escuro, texto branco e ícones lineares discretos.
- Item ativo com fundo `#24557C`, indicador claro ou detalhe dourado extremamente sutil.
- Topbar branca: breadcrumbs, nome da organização ativa, busca se já houver, notificações e conta de usuário.
- Área de trabalho `#F5F7F9`, cards e tabelas brancos, bordas `#DEE5EA`.
- Não expandir a sidebar de forma que quebre a experiência em notebooks; permitir recolher se o sistema existente permitir.
- Respeitar isolamento entre igrejas/contas; nada de dados de uma igreja em outra.

### 5.2 Dashboard
- H1 curto “Visão geral” e subtítulo de contexto da organização.
- Indicadores existentes: membros, contribuições, saldo ou receitas/despesas, contas pendentes, eventos e campanhas — **somente os indicadores que o banco/API de fato permite**.
- KPIs: fundo branco, label secundário, número em azul-marinho, pequenos ícones azuis; verde apenas para variação positiva de fato.
- Gráficos: azul principal `#0F2D4A`, azul apoio `#6FA9DD`, dourado `#C6A664` como destaque pontual. Gráfico acessível, legenda e tooltip.
- Tabelas de próximas atividades e eventos com filtros e ações preservados.
- Cards com `border-radius:16px` e sombra sutil, sem cartões coloridos em excesso.

### 5.3 Membros
- Lista com busca, filtros, ordenação, paginação, exportação e ações reais preservadas.
- Status em badges semânticos; avatars discretos ou iniciais, nunca imagens falsas.
- Perfil individual organizado em seções/abas existentes (dados pessoais, família, ministérios, histórico quando autorizado).
- **Atenção à privacidade:** dados sensíveis, anotações pastorais e histórico de contribuições visíveis apenas a papéis autorizados.

### 5.4 Dízimos, ofertas, Pix e financeiro
- Mesma identidade de cards, tabelas, formulários e diálogos.
- Verde para receitas confirmadas, vermelho para despesas ou erros quando semanticamente pertinente, âmbar para pendências.
- Tela de contribuições deve deixar bem claro o que é **registrado**, **pendente**, **confirmado** e **conciliado**.
- **Não alterar regras de criação de QR Code Pix, chave da igreja, confirmação por extrato, integrações, webhooks, valores, histórico, idempotência e permissões**.
- Em fechamento mensal e relatórios, preservar indicadores, totais, cálculos, exportações (CSV/PDF/Excel conforme existentes) e auditabilidade.

### 5.5 Ministério, grupos, famílias, agenda, campanhas, oração e avisos
- Padronizar visão geral, tabelas, calendários, formulários e estados vazios.
- Ícones Lucide consistentes por módulo; calendários legíveis, chips para horários e status, formulários com labels claros.
- Não expor pedidos de oração privados a membros indevidos.
- Manter fluxos de criação, edição, notificações e exclusão com confirmação apropriada.

### 5.6 Relatórios, configurações e permissões
- Manter visualizações, exportações, filtros de data, links e gráficos existentes.
- Tipografia tabular em valores financeiros; separador de milhares e moeda BRL conforme locale atual.
- No gerenciamento de usuários, nunca simplificar ou remover controles de acesso.
- Mensagens de erro devem permanecer compreensíveis e seguras, sem expor detalhes internos.

### 5.7 Portal do membro e páginas públicas de cada igreja
- Portal do membro: mesma marca quando pertencente ao produto, mas UI mais acolhedora e menos densa que o painel financeiro. Cabeçalho claro, ações principais evidentes, leitura confortável em celular.
- As páginas públicas geradas para igrejas podem ter identidade própria de cada organização: **não force o azul/dourado do produto sobre logotipos ou temas personalizados das igrejas**, caso já exista personalização. Use a marca do Portal da Igreja apenas onde seja realmente apropriado.
- Preservar estritamente os controles e escopo do membro, extrato, informe anual, Pix, eventos e pedidos de oração.

## 6. PADRÕES GLOBAIS DA INTERFACE

- Formularios: rótulos visíveis, descrições curtas, `required` real, mensagens perto do campo, navegação por teclado.
- Tabelas: cabeçalho fixo apenas se útil, filtros funcionais, densidade adequada, ordenação persistente quando existente, scroll horizontal no mobile em vez de truncar valores críticos.
- Estados: carregando, vazio, erro, sem permissão, sucesso, confirmação, offline (se aplicável) coerentes com tokens.
- Feedback: não usar só cor para indicar resultado. Usar texto + ícone.
- Componentes: desenvolver/reutilizar componentes compartilhados (`Button`, `Card`, `Badge`, `Input`, `Select`, `Dialog`, `DataTable`) adaptando à arquitetura atual; não duplicar padrões.
- Layout responsivo: verificar larguras 360px, 390px, 768px, 1024px, 1440px; respeitar safe areas.
- Garantir hit targets adequados (~44px nos controles mobile), foco visível e contraste AA.
- Evitar uso de imagens pesadas que prejudiquem FCP/LCP; lazy-load imagens não críticas, SVG para logos.

## 7. PROCESSO DE EXECUÇÃO — SIGA A ORDEM

**Fase 0 — Inspeção obrigatória (antes de codar):**
1. Mapeie stack, layout, páginas, CSS, biblioteca de componentes, logotipo atual, endpoints consumidos e testes existentes.
2. Liste os fluxos críticos: login/logout, cadastro, permissões, criação/edição de membro, financeiro, Pix, exportação, portal do membro, mudança de plano.
3. Apresente inventário de telas afetadas, arquivos a tocar e potenciais riscos. Preserve backups/controle de versão.
4. Compare com `referencias/*.png`; não tente reproduzir literalmente números, fotos e textos desses mockups.

**Fase 1 — Fundação:**
1. Instale/integre assets reais de `logos/`, `favicons/`, `imagens/` na pasta adequada ao framework.
2. Adicione tokens globais a partir de `tokens/`, respeitando arquitetura existente.
3. Aplique fontes, estilos base de título/corpo, botões, campos, cards, barras, tabelas e estados.
4. Não faça alterações funcionais nessa fase.

**Fase 2 — Site público:**
1. Reformule header, hero, seções, recursos, planos, FAQ, rodapé e páginas SEO existentes.
2. Valide cadastro, login, links de planos, âncoras e navegação responsiva.
3. Verifique imagens, textos, performance, alt text, SEO e links.

**Fase 3 — Sistema:**
1. Reformule sidebar, topbar, dashboard, tabelas, componentes e formulários comuns.
2. Avance por módulo mantendo os fluxos operacionais, estados e permissões.
3. Depois trate mobile, portal do membro e outras superfícies relevantes.

**Fase 4 — Validação:**
1. Execute lint, typecheck, build e testes disponíveis.
2. Faça smoke tests de rotas, CRUD de membros, lançamento e consulta financeira, Pix sem pagamento real, filtros, exportações, formulários, autenticação e RBAC.
3. Revise telas em desktop/tablet/mobile, contraste e teclado.
4. Faça screenshots de antes/depois no ambiente de desenvolvimento e liste diferenças.
5. Entregue resumo de arquivos alterados, componentes criados, testes realizados, riscos/pendências e orientações de deploy sem alegar que houve deploy.

## 8. CRITÉRIOS DE ACEITE

- O site transmite seriedade, confiança e modernidade com **azul-marinho + marfim + dourado discreto**.
- O símbolo oficial é o portal iluminado, **sem cruz grande**.
- O mesmo design system está presente em marketing, login, painel, modal e mobile.
- **Nada deixa de funcionar**: rotas, formulários, módulos, integrações, pagamentos e controles de acesso permanecem ativos.
- Não há dados, depoimentos, preço ou métricas inventadas em produção.
- O layout respeita responsividade, acessibilidade, SEO e performance.
- A execução ocorre **sobre o código atual**, sem reescrever backend ou implantar bibliotecas novas desnecessariamente.

**COMECE AGORA PELA FASE 0.** Antes de alterar arquivos, me mostre o diagnóstico, a lista de telas, a estrutura encontrada e o plano de implementação incremental. Após aprovado o plano, execute cada fase com checagem entre elas.
