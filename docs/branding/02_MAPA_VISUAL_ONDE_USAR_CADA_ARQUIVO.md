# Mapa de aplicação — onde usar cada arquivo e cor

## Materiais da marca

| Componente/local | Arquivo | Fundo recomendado | Observações |
|---|---|---|---|
| Site: header | `logos/horizontal-fundo-claro.svg` | Marfim/branco | Logo com área de respiro (mínimo 12px ao redor) |
| Site: rodapé escuro | `logos/horizontal-fundo-escuro.svg` | Azul institucional | Versão já tem fundo azul; alinhar com seção |
| Login / recuperação de senha | `logos/vertical-fundo-claro.svg` | Marfim/branco | Centralizado, acima do formulário |
| Sistema: sidebar | `logos/horizontal-fundo-escuro.svg` ou composição branca | Azul institucional | Evitar cortar logo; preservar legibilidade no estado recolhido |
| Sidebar recolhida | `logos/simbolo-branco.svg` | Azul institucional | Ícone isolado, sem palavra |
| Favicon | `favicons/favicon.svg` | Navegador | Fallback `favicon-32.png` / `favicon-16.png` |
| Apple Touch | `favicons/apple-touch-icon.png` | Sistema operacional | 180×180 |
| PWA | `favicons/pwa-192.png`, `pwa-512.png` | Manifest | Apenas se PWA já existente |
| Compartilhamento da home | `imagens/capa-compartilhamento-og.png` | Meta OG/Twitter | 1200×630, usar caminho público absoluto |
| Hero público | `imagens/hero-arquitetura-abstrata.svg` | Marfim | Posicionar à direita, não atrás de textos sem contraste |
| Banner / rodapé | `imagens/padrao-arcos.svg` | Qualquer fundo neutro | Textura com opacidade 5–12%; nunca disputar atenção |
| Paleta para revisão | `imagens/paleta-oficial.png` | Documentação | Não inserir como seção do site |
| Inspiração da identidade | `referencias/01_identidade_visual.png` | Apenas briefing | Não exibir no frontend |
| Inspiração da home | `referencias/02_site_publico.png` | Apenas briefing | Não exibir no frontend |
| Inspiração do dashboard | `referencias/03_sistema_dashboard.png` | Apenas briefing | Não exibir no frontend |

## Matriz por tela/área

| Área | Fundo principal | Destaques e controles | Padrões específicos |
|---|---|---|---|
| Landing page | `#F7F5EF` | Heading `#0F2D4A`, CTA azul | 2 colunas no hero, blocos leves |
| Header marketing | `#FFFFFF` | CTA azul | Link ativo com sublinhado discreto |
| Cards de recursos | `#FFFFFF` | Ícones azuis, texto ardósia | Bordas finas, radius 16px |
| Planos | `#FFFFFF` | Plano principal com filete dourado | Valores reais do backend |
| Depoimentos | `#F7F5EF` | Aspas/detalhes dourados discretos | Somente dados reais autorizados |
| CTA final | `#0F2D4A` | Texto branco, botão contrastante | Arcos de fundo muito sutis |
| Login/cadastro | `#F7F5EF` | Botão azul | Form centralizado, sem excesso de conteúdo |
| Dashboard | `#F5F7F9` | Cards brancos | KPIs com ícones lineares |
| Sidebar | `#0F2D4A` | Ativo `#24557C` | Texto branco e ícones claros |
| Topbar | `#FFFFFF` | Textos azul escuro | Breadcrumb e organização ativa |
| Membros | `#FFFFFF` | Status semântico | Tabela, busca, filtros, formulário |
| Contribuições/Pix | `#FFFFFF` | Azul/verde/âmbar por significado | Não mexer nas regras financeiras |
| Financeiro | `#FFFFFF` | Gráficos azuis | BRL legível, números tabulares |
| Agenda | `#FFFFFF` | Azul e pequenos realces ouro | Datas e estados acessíveis |
| Ministérios/grupos | `#FFFFFF` | Ícones lineares | Lista ou cards conforme fluxo atual |
| Relatórios | `#FFFFFF` | Azul institucional | Gráficos e exportações preservadas |
| Portal do membro | `#F7F5EF`/branco | Azul CTA, dourado mínimo | Forte usabilidade mobile |
| Sites das igrejas clientes | **Tema de cada igreja** | **Configuração de cada igreja** | Nunca sobrescrever personalização do cliente |

## Como usar as cores de status

- **Ativo / confirmado / conciliado:** `#168157` com fundo `#E7F6ED`.
- **Pendente / atenção:** `#906013` com fundo `#FFF3DC`.
- **Cancelado / negado / falhou:** `#B83E49` com fundo `#FDEDEF`.
- **Não confundir crescimento de receita com melhoria operacional**: a semântica depende dos dados reais.

## Ícones por módulo (nomes sugeridos se usar Lucide)

- Membros: `users`
- Contribuições e dízimos: `hand-coins` ou `wallet`
- Financeiro: `chart-no-axes-combined` ou `wallet-cards`
- Eventos: `calendar-days`
- Ministérios e grupos: `users-round`
- Famílias: `house`
- Relatórios: `chart-column`
- Campanhas: `target`
- Pedidos de oração: `heart-handshake`
- Comunicados: `megaphone`
- Segurança: `shield-check`
- Configurações: `settings`

Manter a biblioteca de ícones já existente se ela for consistente; não instalar dependências por preferência estética.
