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
import re

SITE = "https://portaldaigreja.com.br"
APP = "https://app.portaldaigreja.com.br"
SIGNUP = f"{APP}/register-church"
LOGIN = f"{APP}/login"
WA = ("https://wa.me/5527998553591?text=Ol%C3%A1!%20Vim%20pelo%20site%20do%20Portal%20"
      "da%20Igreja%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.")
ROOT = pathlib.Path(__file__).resolve().parent.parent

# --------------------------------------------------------------- conteúdo
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
                 ("👥", "ic-blue", "Cadastro de membros",
                  "Ficha com contato, endereço, nascimento, batismo, estado civil e função na igreja. Famílias, grupos, células e ministérios ligados a cada pessoa.",
                  "/cadastro-membros-igreja/"),
                 ("💝", "ic-green", "Dízimos e ofertas",
                  "Dízimo, oferta, oferta avulsa (aquela sem nome) e doação por campanha. O membro gera o Pix pelo portal e a tesouraria confirma ao conferir o extrato.",
                  "/controle-dizimos-ofertas/"),
                 ("💰", "ic-green", "Financeiro da igreja",
                  "Receitas e despesas por categoria, contas fixas lançadas sozinhas e o fechamento do mês em PDF para levar à diretoria.",
                  "/financeiro-para-igrejas/"),
                 ("🌐", "ic-blue", "Site da igreja",
                  "Site público com páginas, galeria, horários de culto, agenda e Pix, editável sem saber programar. Incluso nos planos pagos.",
                  "/site-para-igrejas/"),
                 ("🧾", "ic-blue", "Portal do membro", None),
                 ("📅", "ic-blue", "Agenda e avisos", None),
                 ("🙏", "ic-green", "Pedidos de oração", None),
                 ("📊", "ic-green", "Relatórios e indicadores", None),
             ],
             "plain": {
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
             "Quantas a igreja precisar, em qualquer plano. Pastor, tesoureiro, secretária e líderes têm logins separados, cada um com a sua permissão. O limite dos planos é de membros cadastrados, não de usuários."),
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
                 ("💝", "ic-green", "Quatro tipos de entrada", None),
                 ("📱", "ic-blue", "Pix com QR Code", None),
                 ("✅", "ic-green", "Confirmação pela tesouraria", None),
                 ("🧾", "ic-blue", "Informe anual do membro", None),
                 ("🎯", "ic-green", "Campanhas com meta", None),
                 ("📊", "ic-blue", "Quem contribuiu e quem parou", None),
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
                 "sem dizer quem deu quanto. Os valores por pessoa ficam restritos a quem tem "
                 "permissão de tesouraria ou direção.",
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
             "Somente quem tem permissão de administração ou gestão. O relatório aberto à igreja mostra apenas totais, sem nomes."),
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
                 ("🗂️", "ic-blue", "Ficha do membro", None),
                 ("👨‍👩‍👧", "ic-green", "Famílias", None),
                 ("🤝", "ic-blue", "Grupos, células e ministérios", None),
                 ("📥", "ic-green", "Importação da planilha", None),
                 ("🚫", "ic-blue", "Sem cadastros repetidos", None),
                 ("🎂", "ic-green", "Aniversários", None),
                 ("🔑", "ic-blue", "Acesso ao portal", None),
                 ("📜", "ic-green", "Consentimento e LGPD", None),
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
                 ("💰", "ic-green", "Receitas e despesas", None),
                 ("🏷️", "ic-blue", "Categorias da sua igreja", None),
                 ("🔁", "ic-green", "Contas fixas recorrentes", None),
                 ("📑", "ic-blue", "Fechamento do mês em PDF", None),
                 ("📂", "ic-green", "Relatório por categoria", None),
                 ("📤", "ic-blue", "Exportação para o contador", None),
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
             "Somente quem tem permissão de administração ou gestão. Operadores e membros não acessam a tesouraria."),
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
                 ("🧱", "ic-blue", "Páginas e blocos", None),
                 ("⛪", "ic-green", "Horários de culto", None),
                 ("📅", "ic-blue", "Agenda ligada ao sistema", None),
                 ("💝", "ic-green", "Pix no site", None),
                 ("🖼️", "ic-blue", "Galeria e fotos", None),
                 ("🎨", "ic-green", "Cara da sua igreja", None),
                 ("📍", "ic-blue", "Mapa e contato", None),
                 ("📱", "ic-green", "Funciona no celular", None),
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
                 ("📑", "ic-blue", "Fechamento do mês", None),
                 ("👁️", "ic-green", "Transparência para a igreja", None),
                 ("📂", "ic-blue", "Relatório por categoria", None),
                 ("🧾", "ic-green", "Informe anual do membro", None),
                 ("🎯", "ic-blue", "Contas de cada campanha", None),
                 ("🔎", "ic-green", "Trilha de auditoria", None),
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
                 "Os valores por pessoa ficam restritos a quem tem permissão de administração ou "
                 "gestão. Operadores e membros não acessam a tesouraria, e o relatório aberto à "
                 "igreja nunca traz nomes.",
                 "Para o contador, os lançamentos, as contribuições e as campanhas saem em CSV, que "
                 "abre no Excel e em qualquer sistema contábil. O Portal da Igreja não substitui a "
                 "contabilidade nem emite documento fiscal: ele organiza os números e entrega o "
                 "relatório pronto."]},
        ],
        "faq": [
            ("Dá para mostrar as contas sem expor quem contribuiu?",
             "Dá, e é o padrão. O relatório de transparência mostra os totais por mês, sem nomes nem valores individuais. Quanto cada pessoa contribuiu só aparece para quem tem permissão de tesouraria ou direção."),
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
]

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

# --------------------------------------------------------------- template
def esc(text: str) -> str:
    """Escapa para HTML, preservando as poucas tags que o conteúdo usa."""
    out = html.escape(text, quote=False)
    return out.replace("&lt;code&gt;", "<code>").replace("&lt;/code&gt;", "</code>")


def nav(active: str) -> str:
    links = "".join(
        f'        <a href="/{slug}/"{" aria-current=\"page\"" if slug == active else ""}>{label}</a>\n'
        for slug, label in NAV_LABELS.items())
    return links


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
                more = (f'\n            <p><a href="{link}">Ver a página de {esc(name.lower())} →</a></p>'
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


def render_faq(items: list[tuple[str, str]]) -> str:
    rows = "".join(f'''          <details class="faq-item">
            <summary>{esc(q)}</summary>
            <div class="faq-answer"><p>{esc(a)}</p></div>
          </details>
''' for q, a in items)
    return f'''    <section class="section faq" id="faq">
      <div class="container container-narrow">
        <div class="section-head">
          <span class="kicker">Dúvidas frequentes</span>
          <h2>Perguntas de quem está avaliando</h2>
        </div>
        <div class="faq-list">
{rows}        </div>
      </div>
    </section>
'''


def render_related(slug: str) -> str:
    links = "".join(
        f'          <a class="feature" href="/{s}/"><h3>{esc(label)}</h3>'
        f'<p>{esc(RELATED_SUB[s])}</p></a>\n'
        for s, label in RELATED_LABELS.items() if s != slug)
    return f'''    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="kicker">Veja também</span>
          <h2>Outras partes do sistema</h2>
        </div>
        <div class="features-grid">
{links}        </div>
      </div>
    </section>
'''


def jsonld(page: dict) -> str:
    url = f"{SITE}/{page['slug']}/"
    blocks = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{SITE}/"},
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
<html lang="pt-BR">

<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-F49Y1WNQ4H"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-F49Y1WNQ4H');
  </script>

  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#0b1f3a" />
  <link rel="canonical" href="{url}" />

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
        <a class="btn btn-ghost" href="{login}">Entrar</a>
        <a class="btn btn-primary" href="{signup}">Criar conta grátis</a>
      </div>

      <button class="nav-toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false"
        aria-controls="mobileMenu">
        <span></span><span></span><span></span>
      </button>
    </div>

    <div class="mobile-menu" id="mobileMenu" hidden>
{navlinks}      <a href="/#planos">Planos</a>
      <div class="mobile-actions">
        <a class="btn btn-ghost" href="{login}">Entrar</a>
        <a class="btn btn-primary" href="{signup}">Criar conta grátis</a>
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
            <a class="btn btn-primary btn-lg" href="{signup}">Criar conta grátis</a>
            <a class="btn btn-outline btn-lg" href="/#planos">Ver planos e preços</a>
          </div>
          <p class="hero-badge">✅ Plano gratuito até 50 membros · Sem cartão de crédito</p>
        </div>
      </div>
    </section>

{blocks}{faq}{related}
    <section class="cta-band">
      <div class="container cta-inner">
        <h2>Comece hoje, no plano gratuito</h2>
        <p>Crie a conta da sua igreja em poucos minutos e traga a sua lista de membros da planilha.</p>
        <a class="btn btn-white btn-lg" href="{signup}">Criar conta grátis</a>
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
        <p>Gestão completa, segura e transparente para a sua igreja — na nuvem.</p>
      </div>

      <div class="footer-col">
        <h4>Produto</h4>
{footerlinks}      </div>

      <div class="footer-col">
        <h4>Empresa</h4>
        <a href="/#planos">Planos e preços</a>
        <a href="mailto:suporte@portaldaigreja.com.br">suporte@portaldaigreja.com.br</a>
        <a href="https://wa.me/5527998553591" target="_blank" rel="noopener">💬 WhatsApp: (27) 99855-3591</a>
      </div>

      <div class="footer-col">
        <h4>Legal</h4>
        <a href="{app}/privacidade">Política de Privacidade</a>
        <a href="{app}/termos">Termos de Uso</a>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container">
        <p>© 2026 Portal da Igreja. Todos os direitos reservados.</p>
      </div>
    </div>
  </footer>

  <a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="Fale conosco no WhatsApp">
    <span class="wa-tooltip">Fale conosco no WhatsApp</span>
    <svg class="wa-icon" viewBox="0 0 32 32" width="30" height="30" aria-hidden="true" focusable="false">
      <path fill="#fff" d="M16.001 3.2c-7.06 0-12.8 5.74-12.8 12.8 0 2.26.6 4.46 1.73 6.4L3.2 28.8l6.57-1.72a12.73 12.73 0 0 0 6.23 1.6h.01c7.06 0 12.8-5.74 12.8-12.8s-5.75-12.68-12.81-12.68zm0 23.02h-.01a10.6 10.6 0 0 1-5.4-1.48l-.39-.23-3.9 1.02 1.04-3.8-.25-.4a10.57 10.57 0 0 1-1.62-5.65c0-5.86 4.77-10.62 10.63-10.62 2.84 0 5.5 1.11 7.51 3.12a10.55 10.55 0 0 1 3.11 7.51c0 5.86-4.77 10.63-10.62 10.63zm5.83-7.96c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.71.16-.21.32-.82 1.04-1 1.25-.18.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.58-.95-.85-1.59-1.9-1.78-2.22-.18-.32-.02-.49.14-.65.14-.14.32-.37.48-.55.16-.18.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.71-1.72-.98-2.35-.26-.62-.52-.54-.71-.55l-.61-.01c-.21 0-.55.08-.84.4-.29.32-1.1 1.08-1.1 2.63 0 1.55 1.13 3.05 1.29 3.26.16.21 2.22 3.39 5.38 4.76.75.32 1.34.51 1.79.66.75.24 1.44.21 1.98.13.6-.09 1.89-.77 2.16-1.52.27-.75.27-1.39.19-1.52-.08-.13-.29-.21-.61-.37z"/>
    </svg>
  </a>

  <div class="sticky-cta" id="stickyCta" aria-hidden="true">
    <a class="btn btn-primary btn-block" href="{signup}">Criar conta grátis →</a>
  </div>

  <script src="/script.js"></script>
</body>

</html>
"""


def build() -> list[str]:
    written = []
    for page in PAGES:
        url = f"{SITE}/{page['slug']}/"
        html_out = TEMPLATE.format(
            title=esc(page["title"]), description=esc(page["description"]), url=url, site=SITE,
            jsonld=jsonld(page), navlinks=nav(page["slug"]),
            footerlinks="".join(f'        <a href="/{s}/">{label}</a>\n'
                                for s, label in RELATED_LABELS.items()),
            kicker=esc(page["kicker"]), h1=esc(page["h1"]), lead=esc(page["lead"]),
            blocks=render_blocks(page["blocks"]), faq=render_faq(page["faq"]),
            related=render_related(page["slug"]),
            signup=SIGNUP, login=LOGIN, app=APP, wa=WA)
        out = ROOT / page["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html_out, encoding="utf-8")
        written.append(str(out.relative_to(ROOT)))
    return written


if __name__ == "__main__":
    for path in build():
        print("escrito:", path)
