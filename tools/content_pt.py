"""Conteúdo das páginas comerciais em português.

Só entra aqui o que o produto realmente faz — confira em
docs/CATALOGO-FUNCIONALIDADES-IGREJAS.md antes de acrescentar qualquer frase.
Depois de editar, rode: python3 tools/build_pages.py
"""

PAGES: list[dict] = [
    {
        "slug": "sistema-gestao-igrejas",
        "title": "Sistema de Gestão para Igrejas | Portal da Igreja",
        "description": ("Membros, dízimos e ofertas por Pix, financeiro, relatórios e portal do "
                        "membro num sistema só. Plano gratuito até 50 membros."),
        "kicker": "Sistema de gestão",
        "h1": "Sistema de gestão para igrejas, do cadastro de membros ao fechamento do mês",
        "lead": ("Um só lugar para a secretaria, a tesouraria e a liderança: cadastro de membros, "
                 "dízimos e ofertas, contas da igreja, relatórios prontos e o portal onde cada "
                 "membro vê o próprio extrato. Comece no plano gratuito, sem cartão de crédito."),
        "blocks": [
            {"type": "prose", "kicker": "O problema", "h2": "A planilha resolveu até aqui",
             "paras": [
                 "Na maioria das igrejas a informação está espalhada: a lista de membros numa "
                 "planilha, o caixa num caderno, os dízimos num bloco de anotações e as fotos dos "
                 "comprovantes no celular de alguém. Quando chega a reunião de prestação de "
                 "contas, alguém passa o fim de semana juntando tudo de novo.",
                 "O Portal da Igreja junta esses controles num sistema só, pensado para quem não "
                 "é da área de tecnologia: tudo em português, na nuvem, pelo computador ou pelo "
                 "celular, sem instalar nada."]},
            {"type": "features", "kicker": "O que o sistema faz", "h2": "Os módulos que a sua igreja usa toda semana",
             "sub": "Todos os recursos abaixo estão disponíveis em qualquer plano, inclusive no gratuito. O que muda entre os planos é quantos membros a igreja pode cadastrar, e o site da igreja, que entra nos planos pagos.",
             "items": [
                 ("users", "ic-blue", "Cadastro de membros",
                  "Ficha com contato, endereço, nascimento, batismo, estado civil e função na igreja. Famílias, grupos, células e ministérios ligados a cada pessoa.",
                  "/cadastro-membros-igreja/"),
                 ("coins", "ic-green", "Dízimos e ofertas",
                  "Dízimo, oferta, oferta avulsa (aquela sem nome) e doação por campanha. O membro gera o Pix pelo portal e a tesouraria confirma ao conferir o extrato.",
                  "/controle-dizimos-ofertas/"),
                 ("wallet", "ic-green", "Financeiro da igreja",
                  "Receitas e despesas por categoria, contas fixas lançadas sozinhas e o fechamento do mês em PDF para levar à diretoria.",
                  "/financeiro-para-igrejas/"),
                 ("globe", "ic-blue", "Site da igreja",
                  "Site público com páginas, galeria, horários de culto, agenda e Pix, editável sem saber programar. Incluso nos planos pagos.",
                  "/site-para-igrejas/"),
                 ("package", "ic-green", "Patrimônio",
                  "Caixas de som, instrumentos, cadeiras, computadores e veículos cadastrados com local, foto e valor, e o total que a igreja tem investido.",
                  "/controle-patrimonio-igreja/"),
                 ("key", "ic-blue", "Perfis por função", None),
                 ("receipt", "ic-blue", "Portal do membro", None),
                 ("calendar", "ic-blue", "Agenda e avisos", None),
                 ("heart", "ic-green", "Pedidos de oração", None),
                 ("chart-column", "ic-green", "Relatórios e indicadores", None),
             ],
             "plain": {
                 "Perfis por função": "Cada pessoa da equipe entra com o próprio login e um perfil. A secretaria cuida dos membros e da agenda sem ver valores; a tesouraria cuida do dinheiro sem abrir o cadastro de membros.",
                 "Portal do membro": "Cada membro entra com o próprio login, vê o que contribuiu, baixa o informe anual em PDF, manda pedido de oração e lê os avisos.",
                 "Agenda e avisos": "Cultos e eventos cadastrados uma vez aparecem no painel, no portal do membro e no site da igreja. O mural de avisos destaca o que é urgente.",
                 "Pedidos de oração": "O pedido chega para a liderança, que acompanha como \"orando\" e devolve uma resposta ao membro quando for o caso.",
                 "Relatórios e indicadores": "Painel com membros novos, aniversariantes da semana, quem parou de contribuir, contas previstas e os últimos 12 meses.",
             }},
            {"type": "steps", "kicker": "Como começar", "h2": "Três passos para sair da planilha",
             "items": [
                 ("Crie a conta da igreja", "Leva poucos minutos e não pede cartão de crédito. Você já entra com o seu login de administrador."),
                 ("Traga os membros", "Importe a planilha que a igreja já tem: o sistema lê o arquivo, você confere as colunas e só então os dados são salvos."),
                 ("Registre o movimento", "Lance dízimos, ofertas e despesas, marque as contas fixas como recorrentes e acompanhe o fechamento do mês."),
             ]},
            {"type": "prose", "kicker": "Segurança", "h2": "O que protege os dados da sua igreja",
             "paras": [
                 "Dados sensíveis dos membros, como CPF, telefone e endereço, ficam criptografados "
                 "no banco de dados. As senhas nunca são guardadas em texto e cada pessoa pode "
                 "ativar a confirmação em duas etapas.",
                 "Os dados de cada igreja ficam separados dos das demais, com a divisão aplicada "
                 "tanto no sistema quanto no próprio banco de dados. Há registro de consentimento "
                 "por finalidade, exportação dos dados do membro e trilha de auditoria de quem "
                 "alterou o quê, como pede a LGPD."]},
        ],
        "faq": [
            ("Preciso instalar alguma coisa?",
             "Não. O sistema funciona pelo navegador, no computador, no tablet ou no celular. Basta criar a conta e entrar."),
            ("Dá para trazer a lista de membros que já temos?",
             "Dá. O assistente de importação lê planilhas do Excel (.xlsx, .xls) e arquivos CSV, sugere a qual campo cada coluna corresponde e mostra tudo para você conferir antes de salvar. Cadastros repetidos são barrados pelo CPF, pelo e-mail ou pelo nome."),
            ("Quantas pessoas da equipe podem usar?",
             "Quantas a igreja precisar, em qualquer plano. Cada pessoa tem o seu login e um perfil: administrador, gestor, secretaria, tesouraria ou operador. A secretaria cuida dos membros e da agenda sem ver valores, e a tesouraria cuida do dinheiro sem abrir o cadastro de membros. O limite dos planos é de membros cadastrados, não de usuários."),
            ("O plano gratuito tem prazo para acabar?",
             "Não. O plano gratuito atende até 50 membros cadastrados, para sempre, sem cartão de crédito."),
        ],
    },
    {
        "slug": "controle-dizimos-ofertas",
        "title": "Controle de Dízimos e Ofertas com Pix | Portal da Igreja",
        "description": ("Registre dízimos, ofertas e doações por campanha, receba por Pix com QR "
                        "Code na conta da própria igreja e entregue o informe anual ao membro em PDF."),
        "kicker": "Dízimos e ofertas",
        "h1": "Controle de dízimos e ofertas, com Pix na conta da própria igreja",
        "lead": ("Cada contribuição registrada com data, forma de pagamento e, quando houver, o "
                 "membro que contribuiu. O dinheiro do Pix cai direto na conta da igreja, sem "
                 "intermediário, e a tesouraria confirma cada entrada conferindo o extrato."),
        "blocks": [
            {"type": "features", "kicker": "Como funciona", "h2": "Da entrega do envelope ao relatório",
             "items": [
                 ("coins", "ic-green", "Quatro tipos de entrada", None),
                 ("qr-code", "ic-blue", "Pix com QR Code", None),
                 ("circle-check", "ic-green", "Confirmação pela tesouraria", None),
                 ("receipt", "ic-blue", "Informe anual do membro", None),
                 ("target", "ic-green", "Campanhas com meta", None),
                 ("chart-column", "ic-blue", "Quem contribuiu e quem parou", None),
             ],
             "plain": {
                 "Quatro tipos de entrada": "Dízimo (ligado a um membro), oferta, oferta avulsa — a do gazofilácio, que não tem nome — e doação para uma campanha. Cada uma entra nos totais certos.",
                 "Pix com QR Code": "Você cadastra a chave Pix da igreja e o sistema gera o QR Code e o copia e cola. O membro escolhe o valor pelo portal e paga pelo app do banco; o dinheiro vai direto para a conta da igreja, sem intermediário.",
                 "Confirmação pela tesouraria": "O Pix enviado pelo membro fica pendente até alguém da tesouraria conferir o extrato do banco e confirmar. Nada entra nos relatórios antes dessa conferência, e cada pedido traz o identificador que aparece no extrato.",
                 "Informe anual do membro": "No portal, o próprio membro vê o que contribuiu no ano e baixa o informe em PDF, o que acaba com boa parte das perguntas à tesouraria.",
                 "Campanhas com meta": "Campanha de construção, missões ou ação social com meta e acompanhamento do quanto já foi arrecadado, com relatório só daquela campanha.",
                 "Quem contribuiu e quem parou": "Um relatório para a liderança mostra quem contribuiu no período, quem contribuiu pela primeira vez e quem contribuía e parou — uma lista de cuidado pastoral, de uso interno.",
             }},
            {"type": "prose", "kicker": "Transparência", "h2": "Prestação de contas sem expor ninguém",
             "paras": [
                 "O relatório de transparência mostra à igreja quanto entrou e quanto saiu por mês, "
                 "sem dizer quem deu quanto. Os valores por pessoa ficam restritos à direção, à "
                 "tesouraria e a quem lança as contribuições.",
                 "Para a reunião de prestação de contas, o fechamento do mês sai em PDF com a "
                 "comparação com o mês anterior, as entradas por tipo, as despesas por categoria e "
                 "o que já está previsto para os próximos 30 dias."]},
            {"type": "prose", "kicker": "O que o sistema não faz", "h2": "Sendo honesto sobre o Pix",
             "paras": [
                 "O Portal da Igreja não é um banco e não processa pagamentos: o Pix é gerado com a "
                 "chave da própria igreja e o dinheiro nunca passa por nós. Por isso também não "
                 "existe baixa automática — alguém da tesouraria confere o extrato e confirma, o "
                 "que mantém o controle na mão da igreja.",
                 "Tarifas, se houver, são as do banco da igreja. Antes de divulgar uma chave nova, "
                 "faça uma transferência de teste para conferir se cai na conta certa."]},
        ],
        "faq": [
            ("Preciso de maquininha ou de uma empresa de pagamentos?",
             "Não. O Pix usa a chave da própria igreja e o valor cai direto na conta dela. Não há intermediário entre o membro e a igreja."),
            ("E a oferta que chega sem identificação?",
             "Existe o tipo \"oferta avulsa\" justamente para isso. Ela entra nos totais de ofertas sem precisar inventar um membro para o lançamento."),
            ("O membro consegue comprovar quanto contribuiu?",
             "Sim. No portal do membro ele vê o próprio histórico e baixa o informe anual em PDF."),
            ("Quem pode ver quanto cada pessoa contribuiu?",
             "A direção, a tesouraria e os operadores que lançam as contribuições. O perfil de secretaria não vê valores, e cada membro vê só o que ele mesmo deu. O relatório aberto à igreja mostra apenas totais, sem nomes."),
        ],
    },
    {
        "slug": "cadastro-membros-igreja",
        "title": "Cadastro de Membros de Igreja | Portal da Igreja",
        "description": ("Cadastro de membros com ficha completa, famílias, grupos e ministérios, "
                        "importação da planilha que a igreja já tem e bloqueio de cadastros repetidos."),
        "kicker": "Membros",
        "h1": "Cadastro de membros de igreja, organizado e sem repetição",
        "lead": ("A secretaria com a ficha de cada pessoa, as famílias ligadas entre si, os grupos "
                 "e ministérios de cada um — e a planilha antiga importada sem digitar tudo de novo."),
        "blocks": [
            {"type": "features", "kicker": "O cadastro", "h2": "O que fica guardado em cada ficha",
             "items": [
                 ("contact", "ic-blue", "Ficha do membro", None),
                 ("house", "ic-green", "Famílias", None),
                 ("users", "ic-blue", "Grupos, células e ministérios", None),
                 ("upload", "ic-green", "Importação da planilha", None),
                 ("user-check", "ic-blue", "Sem cadastros repetidos", None),
                 ("cake", "ic-green", "Aniversários", None),
                 ("key", "ic-blue", "Acesso ao portal", None),
                 ("shield-check", "ic-green", "Consentimento e LGPD", None),
             ],
             "plain": {
                 "Ficha do membro": "Contato, endereço completo com busca pelo CEP, nascimento, data de batismo, estado civil e data de casamento, função na igreja, profissão e anotações.",
                 "Famílias": "Pessoas da mesma casa ficam ligadas como responsável, cônjuge, filho ou parente, o que também alimenta os aniversários de casamento.",
                 "Grupos, células e ministérios": "Cadastre louvor, infantil, células e departamentos, com líder, informação de reunião e o papel de cada participante dentro do grupo.",
                 "Importação da planilha": "Um assistente lê o arquivo do Excel ou CSV, descobre sozinho onde começa a tabela, sugere o campo de cada coluna e mostra o resultado antes de salvar. Telefone, CPF e CEP são arrumados no caminho.",
                 "Sem cadastros repetidos": "A mesma pessoa não entra duas vezes: o sistema compara CPF, e-mail e nome e barra a repetição, inclusive durante a importação. Para a bagunça que já existe, há uma tela de revisão de repetidos.",
                 "Aniversários": "Aniversariantes da semana e aniversários de casamento aparecem no painel e chegam por e-mail à equipe toda manhã.",
                 "Acesso ao portal": "Quem tem e-mail pode receber um login do portal do membro. A senha nunca é enviada por e-mail: a pessoa define a dela por um link de primeiro acesso.",
                 "Consentimento e LGPD": "O consentimento fica registrado por finalidade, com histórico e com o termo da sua igreja versionado. Os dados de um membro podem ser exportados quando ele pedir.",
             }},
            {"type": "prose", "kicker": "Migração", "h2": "A planilha que a igreja já tem serve",
             "paras": [
                 "Não é preciso arrumar a planilha antes. O assistente aceita Excel e CSV, lida com "
                 "linhas de título acima da tabela, recupera o zero à esquerda do CPF que o Excel "
                 "comeu e corrige nomes digitados todos em maiúsculas.",
                 "Quando um valor não faz sentido — uma data impossível, um telefone incompleto — a "
                 "linha não é descartada: o campo problemático é deixado de fora com um aviso, para "
                 "que a pessoa não se perca por causa de uma célula."]},
        ],
        "faq": [
            ("Dá para importar de qualquer planilha?",
             "O assistente lê .xlsx, .xls e CSV, e você escolhe qual coluna é cada campo. Também há um modelo pronto para baixar, caso prefira começar do zero."),
            ("E se a mesma pessoa for cadastrada duas vezes?",
             "O sistema bloqueia: mesmo CPF, mesmo e-mail ou mesmo nome (a menos que as datas de nascimento sejam diferentes). Para duplicidades antigas existe a tela \"Revisar repetidos\"."),
            ("O membro pode atualizar os próprios dados?",
             "O membro acessa o portal, vê a sua ficha, as suas contribuições e o informe anual, e pode pedir a exportação dos seus dados."),
            ("Existe limite de cadastros?",
             "Sim, por plano: 50 membros no gratuito, 150 no Essencial, 500 no Crescimento e 1.000 no Avançado. A contagem considera todos os cadastros não excluídos, inclusive visitantes e inativos."),
        ],
    },
    {
        "slug": "financeiro-para-igrejas",
        "title": "Sistema Financeiro para Igrejas | Portal da Igreja",
        "description": ("Receitas e despesas por categoria, contas fixas lançadas sozinhas e o "
                        "fechamento do mês em PDF para levar à diretoria."),
        "kicker": "Financeiro",
        "h1": "Sistema financeiro para igrejas: entradas, saídas e o relatório pronto",
        "lead": ("Para o tesoureiro que fecha o caixa no fim do mês: receitas e despesas "
                 "organizadas por categoria, contas fixas lançadas sozinhas e o relatório da "
                 "reunião saindo em PDF, sem montar planilha."),
        "blocks": [
            {"type": "features", "kicker": "Tesouraria", "h2": "O mês inteiro em um lugar",
             "items": [
                 ("wallet", "ic-green", "Receitas e despesas", None),
                 ("tag", "ic-blue", "Categorias da sua igreja", None),
                 ("repeat", "ic-green", "Contas fixas recorrentes", None),
                 ("file-text", "ic-blue", "Fechamento do mês em PDF", None),
                 ("folder-open", "ic-green", "Relatório por categoria", None),
                 ("download", "ic-blue", "Exportação para o contador", None),
             ],
             "plain": {
                 "Receitas e despesas": "Todo lançamento com data, valor, categoria e descrição, separado entre o que entrou e o que saiu, e somado automaticamente no período que você escolher.",
                 "Categorias da sua igreja": "Uma lista de categorias por tipo, que você renomeia e organiza. Renomear arruma também os lançamentos antigos; juntar duas categorias funde o histórico.",
                 "Contas fixas recorrentes": "Aluguel, salários, energia e internet viram um modelo semanal, mensal ou anual. O sistema lança na data certa toda vez, sem alguém precisar lembrar, e você pausa ou encerra quando quiser.",
                 "Fechamento do mês em PDF": "Quanto entrou, quanto saiu, a comparação com o mês anterior, as entradas por tipo de contribuição, as despesas por categoria com o peso de cada uma, as maiores saídas e o previsto para os próximos 30 dias.",
                 "Relatório por categoria": "Escolha as categorias e as campanhas que quer prestar contas e gere um relatório com todos os lançamentos e os subtotais, em PDF com espaço para assinatura ou em Excel.",
                 "Exportação para o contador": "Lançamentos, contribuições, campanhas e membros saem em CSV, que abre no Excel e em qualquer sistema contábil.",
             }},
            {"type": "prose", "kicker": "Transparência", "h2": "Prestação de contas que a igreja entende",
             "paras": [
                 "O relatório de transparência apresenta os totais por mês sem identificar quem "
                 "contribuiu, para ser mostrado à igreja sem expor ninguém. Já o fechamento do mês "
                 "é o documento da reunião de diretoria, com o detalhe que a liderança precisa.",
                 "O painel inicial mostra o movimento recente, as contas já previstas pelos "
                 "lançamentos recorrentes e os últimos doze meses, para a conversa sobre o "
                 "orçamento começar com números e não com impressões."]},
            {"type": "prose", "kicker": "Transparente sobre limites", "h2": "O que ainda não existe",
             "paras": [
                 "Para não haver surpresa depois da contratação: o sistema ainda não faz "
                 "conciliação bancária automática, não guarda anexos de comprovantes, não tem "
                 "contas a pagar com baixa por vencimento nem orçamento por centro de custo. O "
                 "controle é de lançamentos, categorias, recorrências e relatórios."]},
        ],
        "faq": [
            ("O sistema lança as contas fixas sozinho?",
             "Sim. Marque a conta como recorrente, com a frequência e o dia, e o lançamento passa a ser criado automaticamente na data certa. Se você cadastrar uma conta cuja data já passou, os lançamentos atrasados entram na hora."),
            ("Consigo um relatório para levar à reunião?",
             "Sim. O fechamento do mês sai em PDF com papel timbrado, numeração de páginas e o comparativo com o mês anterior. O relatório por categoria também sai em PDF com linhas de assinatura, ou em Excel."),
            ("Quem da equipe vê o financeiro?",
             "A direção e o perfil de tesouraria lançam receitas e despesas e tiram os relatórios. O operador registra dízimos e ofertas e consulta os lançamentos, sem mexer nas contas. A secretaria e os membros não acessam o financeiro."),
            ("Dá para exportar os dados?",
             "Dá. Lançamentos, contribuições e cadastros saem em CSV, e os relatórios de transparência e por categoria saem também em Excel."),
        ],
    },
    {
        "slug": "site-para-igrejas",
        "title": "Site para Igrejas, Incluso no Plano | Portal da Igreja",
        "description": ("Crie o site da sua igreja sem programar: páginas, horários de culto, "
                        "galeria, agenda ligada ao sistema e Pix com QR Code. Incluso em todos os "
                        "planos pagos."),
        "kicker": "Site da igreja",
        "h1": "Site para igrejas, ligado ao sistema de gestão e sem saber programar",
        "lead": ("Monte a página da sua igreja escolhendo blocos prontos: horários de culto, "
                 "ministérios, galeria de fotos, mapa, contato e o Pix para quem quiser contribuir. "
                 "A agenda é a mesma que a secretaria já usa por dentro — cadastrou uma vez, "
                 "aparece no site."),
        "blocks": [
            {"type": "features", "kicker": "O construtor", "h2": "Blocos que você encaixa e edita",
             "items": [
                 ("layout", "ic-blue", "Páginas e blocos", None),
                 ("clock", "ic-green", "Horários de culto", None),
                 ("calendar", "ic-blue", "Agenda ligada ao sistema", None),
                 ("coins", "ic-green", "Pix no site", None),
                 ("image", "ic-blue", "Galeria e fotos", None),
                 ("palette", "ic-green", "Cara da sua igreja", None),
                 ("map-pin", "ic-blue", "Mapa e contato", None),
                 ("smartphone", "ic-green", "Funciona no celular", None),
             ],
             "plain": {
                 "Páginas e blocos": "Home mais as páginas que quiser (Sobre, Ministérios, Contato). Cada página é montada com blocos: destaque, texto, imagem com texto, cartões, galeria, vídeo do YouTube, chamada para ação, contato, agenda, mapa, horários de culto, depoimentos e Pix.",
                 "Horários de culto": "Um bloco só para os cultos e reuniões da semana, que é a primeira coisa que quem procura a igreja quer saber.",
                 "Agenda ligada ao sistema": "Os eventos marcados como públicos na agenda interna aparecem no site automaticamente. Nada de atualizar a programação em dois lugares.",
                 "Pix no site": "O mesmo QR Code da igreja, disponível para quem quiser contribuir pelo site, sem intermediário.",
                 "Galeria e fotos": "Envie as fotos dos cultos e eventos (PNG, JPG ou WEBP, até 5 MB cada) e monte a galeria.",
                 "Cara da sua igreja": "Logo, foto de capa, cores principal e secundária, barra superior, rodapé e os links de Instagram, Facebook, YouTube e WhatsApp.",
                 "Mapa e contato": "Endereço com mapa, telefone e e-mail, para quem está procurando como chegar.",
                 "Funciona no celular": "O site se ajusta à tela do visitante, que na maioria das vezes chega pelo celular, por um link no WhatsApp ou na bio do Instagram.",
             }},
            {"type": "prose", "kicker": "Como fica no ar", "h2": "Onde o site da sua igreja fica publicado",
             "paras": [
                 "Ao publicar, o site fica disponível num endereço do Portal da Igreja, no formato "
                 "<code>app.portaldaigreja.com.br/suaigreja/portal</code>. É esse link que a igreja "
                 "divulga no Instagram, no WhatsApp e nos impressos.",
                 "Se a sua igreja já tem um domínio próprio, fale com a gente pelo WhatsApp: a "
                 "ligação de um domínio é feita junto com o nosso time, caso a caso."]},
            {"type": "prose", "kicker": "Incluído no plano", "h2": "Sem contratar à parte",
             "paras": [
                 "O site está incluso em todos os planos pagos — Essencial, Crescimento e Avançado "
                 "— sem custo adicional e sem hospedagem separada. No plano gratuito o editor fica "
                 "bloqueado; todo o resto do sistema continua disponível.",
                 "Como o site e a gestão são o mesmo sistema, a agenda, as fotos e a chave Pix são "
                 "cadastradas uma vez só."]},
        ],
        "faq": [
            ("Preciso saber programar ou contratar alguém?",
             "Não. Você escolhe os blocos, escreve os textos, envia as imagens e publica pelo próprio painel."),
            ("O site está incluso mesmo ou é cobrado à parte?",
             "Está incluso em todos os planos pagos, sem custo adicional. Só o plano gratuito não tem o editor do site."),
            ("Dá para usar o domínio que a igreja já tem?",
             "A ligação de um domínio próprio é feita junto com o nosso time, caso a caso. Fale com a gente pelo WhatsApp antes de contratar."),
            ("A programação dos cultos atualiza sozinha?",
             "Os eventos marcados como públicos na agenda do sistema aparecem no site automaticamente, sem precisar editar a página."),
        ],
    },
    {
        "slug": "prestacao-de-contas-igreja",
        "title": "Prestação de Contas de Igreja | Portal da Igreja",
        "description": ("Relatório mensal para a diretoria, transparência para os membros sem "
                        "expor quem contribuiu e informe anual em PDF, prontos pelo sistema."),
        "kicker": "Prestação de contas",
        "h1": "Prestação de contas de igreja, pronta para apresentar",
        "lead": ("A reunião de prestação de contas não precisa custar um fim de semana montando "
                 "planilha. O sistema gera o fechamento do mês para a diretoria, o relatório de "
                 "transparência para a igreja — sem dizer quem deu quanto — e o informe anual de "
                 "cada membro."),
        "blocks": [
            {"type": "prose", "kicker": "O problema", "h2": "Confiança se constrói com número aberto",
             "paras": [
                 "Quando a igreja não sabe para onde vai o dinheiro, nasce desconfiança — e quase "
                 "sempre não é por má-fé, é por falta de um relatório claro. Por outro lado, "
                 "ninguém quer expor quanto cada irmão contribuiu.",
                 "A saída é separar os dois documentos: um relatório aberto à igreja, com totais e "
                 "sem nomes, e um relatório detalhado para quem tem responsabilidade sobre as "
                 "contas. O sistema produz os dois a partir dos mesmos lançamentos."]},
            {"type": "features", "kicker": "Os documentos", "h2": "O que sai pronto do sistema",
             "items": [
                 ("file-text", "ic-blue", "Fechamento do mês", None),
                 ("eye", "ic-green", "Transparência para a igreja", None),
                 ("folder-open", "ic-blue", "Relatório por categoria", None),
                 ("receipt", "ic-green", "Informe anual do membro", None),
                 ("target", "ic-blue", "Contas de cada campanha", None),
                 ("search", "ic-green", "Trilha de auditoria", None),
             ],
             "plain": {
                 "Fechamento do mês": "Para a reunião de diretoria: quanto entrou e quanto saiu, a comparação com o mês anterior, as entradas por tipo de contribuição, as despesas por categoria com o peso de cada uma, as maiores saídas e o previsto para os próximos 30 dias. Sai em PDF com papel timbrado e páginas numeradas.",
                 "Transparência para a igreja": "Os totais por mês, sem identificar quem contribuiu. É o documento que pode ser lido em assembleia, afixado no mural ou enviado aos membros sem constranger ninguém. Sai em PDF e em Excel.",
                 "Relatório por categoria": "Escolha as categorias e as campanhas que quer prestar contas e gere um relatório com todos os lançamentos, os subtotais e o total de cada lado. O PDF traz linhas de assinatura para o tesoureiro e o conselho; o Excel vem em abas de resumo, detalhamento e lançamentos.",
                 "Informe anual do membro": "Cada membro entra no portal e baixa o próprio informe do ano em PDF, sem precisar pedir à tesouraria.",
                 "Contas de cada campanha": "Campanha de construção, missões ou ação social com meta, quanto já foi arrecadado e um relatório só daquela campanha, para prestar contas de quem doou para um fim específico.",
                 "Trilha de auditoria": "O sistema registra quem criou, alterou ou apagou cada lançamento, num histórico que não pode ser editado nem apagado. Se alguém questionar um número, dá para mostrar a origem.",
             }},
            {"type": "steps", "kicker": "Na prática", "h2": "Como fica o mês da tesouraria",
             "items": [
                 ("Lance ao longo do mês", "Dízimos, ofertas e despesas entram no dia a dia, cada um na sua categoria. As contas fixas o sistema lança sozinho."),
                 ("Feche o mês em um clique", "No fim do período, gere o fechamento em PDF. Os números já estão somados, comparados com o mês anterior e separados por categoria."),
                 ("Apresente e arquive", "Leve o PDF à reunião, compartilhe o relatório de transparência com a igreja e guarde o arquivo. O histórico fica registrado no sistema."),
             ]},
            {"type": "prose", "kicker": "Quem vê o quê", "h2": "Cada relatório para o público certo",
             "paras": [
                 "Os valores por pessoa ficam restritos à direção, à tesouraria e a quem lança as "
                 "contribuições. A secretaria e os membros não veem valores, e o relatório aberto "
                 "à igreja nunca traz nomes.",
                 "Para o contador, os lançamentos, as contribuições e as campanhas saem em CSV, que "
                 "abre no Excel e em qualquer sistema contábil. O Portal da Igreja não substitui a "
                 "contabilidade nem emite documento fiscal: ele organiza os números e entrega o "
                 "relatório pronto."]},
        ],
        "faq": [
            ("Dá para mostrar as contas sem expor quem contribuiu?",
             "Dá, e é o padrão. O relatório de transparência mostra os totais por mês, sem nomes nem valores individuais. Quanto cada pessoa contribuiu só aparece para a direção, a tesouraria e quem lança as contribuições."),
            ("O relatório serve para a reunião de diretoria?",
             "Serve. O fechamento do mês sai em PDF com papel timbrado, páginas numeradas, comparativo com o mês anterior, despesas por categoria e as maiores saídas. O relatório por categoria ainda traz linhas de assinatura."),
            ("E se alguém questionar um lançamento?",
             "O sistema guarda quem criou ou alterou cada registro, num histórico que não pode ser editado nem apagado."),
            ("O membro consegue comprovar o que contribuiu no ano?",
             "Sim. Ele mesmo baixa o informe anual em PDF pelo portal do membro, sem precisar pedir à secretaria."),
            ("Substitui o contador?",
             "Não. O sistema organiza os lançamentos e gera os relatórios; a contabilidade e as obrigações fiscais continuam com o seu contador, que pode receber tudo em CSV ou Excel."),
        ],
    },
    {
        "slug": "controle-patrimonio-igreja",
        "title": "Controle de Patrimônio da Igreja | Portal da Igreja",
        "description": ("Cadastre os bens da igreja com categoria, local, foto e valor, saiba "
                        "quanto a igreja tem investido e dê baixa sem perder o histórico."),
        "kicker": "Patrimônio",
        "h1": "Controle de patrimônio da igreja: o que ela tem, onde está e quanto vale",
        "lead": ("Caixas de som, mesa de som, instrumentos, cadeiras, bancos, computadores, "
                 "geladeira e veículos cadastrados num lugar só, com local, foto e valor. A "
                 "igreja passa a saber o que tem e quanto já investiu em cada área."),
        "blocks": [
            {"type": "prose", "kicker": "O problema", "h2": "Ninguém sabe ao certo o que a igreja tem",
             "paras": [
                 "Os equipamentos chegam aos poucos: uma doação aqui, uma compra da campanha ali, "
                 "um microfone que alguém trouxe de casa. Anos depois, ninguém sabe dizer quantas "
                 "cadeiras existem, onde foi parar o projetor ou quanto vale o que está no templo.",
                 "O módulo de patrimônio guarda cada bem com a sua categoria, o local e o valor, e "
                 "soma tudo sozinho. Fica fácil conferir o inventário, responder à diretoria e "
                 "ter a lista pronta quando for contratar um seguro."]},
            {"type": "features", "kicker": "Como funciona", "h2": "O que fica registrado de cada bem",
             "items": [
                 ("package", "ic-green", "Cadastro de cada bem", None),
                 ("tag", "ic-blue", "Categorias da sua igreja", None),
                 ("coins", "ic-green", "Quanto a igreja tem investido", None),
                 ("map-pin", "ic-blue", "Onde cada coisa está", None),
                 ("image", "ic-green", "Foto do bem", None),
                 ("archive", "ic-blue", "Baixa sem apagar o histórico", None),
                 ("download", "ic-green", "Planilha para conferência", None),
                 ("search", "ic-blue", "Quem mexeu em quê", None),
             ],
             "plain": {
                 "Cadastro de cada bem": "Nome, categoria, local, quantidade, valor unitário, data de aquisição, estado de conservação (novo, bom, regular ou ruim), número de patrimônio e observações.",
                 "Categorias da sua igreja": "A lista já começa com som e mídia, instrumentos musicais, móveis, informática, cozinha e eletrodomésticos, veículos, imóveis e outros. Renomeie, oculte ou crie as suas.",
                 "Quanto a igreja tem investido": "O sistema multiplica a quantidade pelo valor unitário e mostra o total geral e o total por categoria, com o peso de cada uma. 120 cadeiras de R$ 45,50 viram R$ 5.460,00 sem conta de cabeça.",
                 "Onde cada coisa está": "Cada bem tem o seu local, como templo, salão social ou cozinha. Filtre por local, categoria, situação ou conservação, ou busque pelo nome e pelo número de patrimônio.",
                 "Foto do bem": "Uma foto por bem (PNG, JPG ou WEBP, até 5 MB) ajuda a reconhecer o equipamento e a conferir o estado dele no inventário.",
                 "Baixa sem apagar o histórico": "Quando algo quebra, é vendido, doado ou some, você dá baixa com a data e o motivo. O bem sai do total, mas continua consultável, e a baixa pode ser desfeita.",
                 "Planilha para conferência": "A lista sai em CSV, que abre no Excel, para imprimir o inventário, conferir item por item ou mandar para o contador.",
                 "Quem mexeu em quê": "Cadastro, alteração, baixa e exclusão ficam na trilha de auditoria do sistema, com quem fez e quando.",
             }},
            {"type": "prose", "kicker": "Quem acessa", "h2": "Para quem cuida da casa",
             "paras": [
                 "O patrimônio fica disponível para a direção e para os perfis de secretaria e de "
                 "tesouraria. Operadores e membros não veem a lista de bens.",
                 "O módulo está incluído em todos os planos, inclusive no gratuito, sem custo "
                 "adicional e sem limite de bens cadastrados."]},
            {"type": "prose", "kicker": "Transparente sobre limites", "h2": "O que o módulo não faz",
             "paras": [
                 "Para não haver surpresa: o sistema não calcula depreciação, não controla "
                 "empréstimo de equipamentos nem gera etiquetas. Também não lança a compra no "
                 "financeiro sozinho: o patrimônio é um controle à parte, e a despesa da compra "
                 "continua sendo lançada no financeiro, como sempre."]},
        ],
        "faq": [
            ("O controle de patrimônio custa à parte?",
             "Não. Ele está em todos os planos, inclusive no gratuito, e não há limite de bens cadastrados."),
            ("Dá para saber quanto a igreja tem investido?",
             "Dá. O sistema soma a quantidade vezes o valor unitário de cada bem ativo e mostra o total geral e o total por categoria. Bens doados sem valor informado também podem ser cadastrados."),
            ("E quando um equipamento quebra ou é doado?",
             "Você dá baixa informando a data e o motivo: danificado, vendido, doado, extraviado ou outro. O bem sai do total investido, mas o registro continua no sistema e a baixa pode ser desfeita."),
            ("Quem da equipe pode cadastrar os bens?",
             "A direção e os perfis de secretaria e de tesouraria. Operadores e membros não acessam o patrimônio."),
        ],
    },
]
