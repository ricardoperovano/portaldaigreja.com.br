# Checklist de aprovação do rebranding

## Marca

- [ ] Nome oficial “Portal da Igreja” preservado.
- [ ] Símbolo do portal sem cruz grande nas interfaces.
- [ ] Logos carregando em fundos claros e escuros sem distorção.
- [ ] Favicon atualizado, cache e manifest revisados.
- [ ] Cores implementadas por tokens, sem dezenas de HEX duplicados.
- [ ] Textos e CTAs com contraste AA.

## Site

- [ ] Hero legível e CTA de cadastro com destino correto.
- [ ] Menu mobile abre/fecha e suporta teclado.
- [ ] Todas as seções e links atuais preservados.
- [ ] Preços, descontos, limites e benefícios são os valores reais atuais.
- [ ] Prova social e depoimentos comprovados; sem dados fabricados.
- [ ] SEO: títulos, headings, canonical, structured data, sitemap, redirects preservados.
- [ ] Imagens têm alt apropriado e tamanhos otimizados.
- [ ] Site em 360, 390, 768, 1024 e 1440px não apresenta overflow acidental.

## Sistema

- [ ] Login/logout, recuperação de conta e autenticação sem regressões.
- [ ] Multi-igreja/multi-tenant e permissões preservados.
- [ ] Cadastro, edição, exclusão e importação de membros funcionando.
- [ ] Dados sensíveis e histórico financeiro visíveis só aos papéis autorizados.
- [ ] Pix: geração, confirmação e conciliação sem mudanças indevidas.
- [ ] Receitas, despesas, totais e fechamentos iguais antes e depois.
- [ ] Contas recorrentes, campanhas, eventos e ministérios preservados.
- [ ] Relatórios, filtros e exportações continuam funcionando.
- [ ] Portal do membro acessível e isolado por usuário.
- [ ] Mensagens de sucesso/erro, confirmação e estados vazios revisados.
- [ ] Tabelas e formulários utilizáveis em telas pequenas.

## Engenharia

- [ ] Branch/commit de segurança antes das alterações.
- [ ] Componentes existentes reutilizados ao máximo.
- [ ] Nenhuma migration destrutiva ou reescrita de backend por estética.
- [ ] Lint, testes, typecheck e build executados conforme stack.
- [ ] Screenshots antes/depois feitos no ambiente de desenvolvimento.
- [ ] Relatório final com arquivos alterados, cobertura e pendências.
