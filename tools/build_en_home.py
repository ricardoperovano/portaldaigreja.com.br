#!/usr/bin/env python3
"""Gera /en/index.html a partir da home em português.

A home da raiz é escrita à mão; esta ferramenta a traduz para inglês mantendo a
MESMA estrutura e o mesmo CSS, para não existirem dois layouts a manter. Depois
de mexer na home em português, rode:

    python3 tools/build_en_home.py && python3 tools/seo_check.py

Se uma frase nova da home não estiver no mapa abaixo, o script AVISA e sai com
erro, em vez de publicar um trecho em português no site em inglês.

Público: igrejas brasileiras no exterior. Por isso a versão em inglês mantém os
preços em reais e diz, em um bloco próprio, que o sistema e o suporte são em
português — ver NOTICE.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://portaldaigreja.com.br"

TITLE = "Church Management Software | Portal da Igreja"
DESCRIPTION = ("Church management, tithes by Pix, finances and a church website in one system. "
               "Built for Brazilian churches, including congregations abroad.")

HEAD = f"""  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{TITLE}</title>
  <meta name="description" content="{DESCRIPTION}" />
  <meta name="author" content="Portal da Igreja" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#0b1f3a" />

  <link rel="canonical" href="{SITE}/en/" />
  <link rel="alternate" hreflang="pt-BR" href="{SITE}/" />
  <link rel="alternate" hreflang="en" href="{SITE}/en/" />
  <link rel="alternate" hreflang="x-default" href="{SITE}/" />

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Portal da Igreja" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:url" content="{SITE}/en/" />
  <meta property="og:title" content="{TITLE}" />
  <meta property="og:description" content="{DESCRIPTION}" />
  <meta property="og:image" content="{SITE}/assets/images/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Portal da Igreja — church management software" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{TITLE}" />
  <meta name="twitter:description" content="{DESCRIPTION}" />
  <meta name="twitter:image" content="{SITE}/assets/images/og-image.jpg" />

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

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Portal da Igreja",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "url": "{SITE}/en/",
    "description": "Church management software in the cloud for Brazilian churches: member records, tithes and offerings by Pix, finances with categories and recurring entries, monthly closing, campaigns, member portal and a church website. Interface and support in Portuguese; billed in Brazilian reais.",
    "inLanguage": "en",
    "offers": [
      {{ "@type": "Offer", "name": "Gratuito", "price": "0", "priceCurrency": "BRL" }},
      {{ "@type": "Offer", "name": "Essencial", "price": "79.90", "priceCurrency": "BRL" }},
      {{ "@type": "Offer", "name": "Crescimento", "price": "149.90", "priceCurrency": "BRL" }},
      {{ "@type": "Offer", "name": "Avançado", "price": "299.90", "priceCurrency": "BRL" }}
    ]
  }}
  </script>
"""

NOTICE = """    <section class="section">
      <div class="container container-narrow">
        <p class="pricing-note" style="font-size:.95rem;">
          <strong>Before you sign up:</strong> the software interface and support are in
          Portuguese, and subscriptions are charged in Brazilian reais (BRL). Portal da Igreja is
          built for Brazilian churches, including Brazilian congregations abroad. Giving through
          Pix requires a Brazilian bank account for the church.
          <a href="https://wa.me/5527998553591">Talk to us on WhatsApp</a> if you are unsure
          whether it fits your church.
        </p>
      </div>
    </section>
"""

# Pares (português, inglês). Aplicados na ordem, do mais longo para o mais curto,
# para uma frase curta não estragar outra maior que a contenha.
PAIRS: list[tuple[str, str]] = [
    # --- navegação e botões
    ("Criar conta grátis →", "Create free account →"),
    ("Criar conta grátis", "Create free account"),
    (">Criar conta\n              grátis<", ">Create free\n              account<"),
    ("Acessar o sistema", "Sign in to the system"),
    ("Como funciona", "How it works"),
    ("Recursos", "Features"),
    ("Planos e preços", "Plans and prices"),
    ("Planos", "Plans"),
    ("Segurança", "Security"),
    ("Contato", "Contact"),
    ("Entrar\n              em contato", "Contact\n              us"),
    (">Entrar<", ">Sign in<"),
    (">Começar\n              agora<", ">Get started<"),
    # --- hero
    ("Sistema completo de gestão para igrejas", "Complete church management system"),
    ("Chega de planilha. Gerencie", "No more spreadsheets. Manage"),
    ("membros, dízimos e finanças", "members, giving and finances"),
    ("da sua igreja em um só lugar.", "of your church in one place."),
    ("Pare de perder tempo com controles manuais e prestações de contas confusas.\n            Organize tudo em minutos, com transparência total e a tranquilidade de saber\n            que os dados da sua igreja estão seguros.",
     "Stop losing time to manual controls and confusing accountability meetings. Organise\n            everything in minutes, with full transparency and the peace of mind of knowing\n            your church's data is protected."),
    ("✅ Grátis · Sem cartão de crédito · Dízimo por Pix incluso",
     "✅ Free to start · No credit card · Tithing by Pix included"),
    ("🔒 Dados criptografados · LGPD · Autenticação em 2 fatores",
     "🔒 Encrypted data · Brazilian privacy law (LGPD) · Two-factor sign-in"),
    # --- mockup
    ("Exemplo ilustrativo do painel do Portal da Igreja, com números fictícios",
     "Illustrative example of the Portal da Igreja dashboard, with fictional numbers"),
    (">Painel<", ">Dashboard<"),
    (">Exemplo<", ">Example<"),
    (">Membros<", ">Members<"),
    (">Dízimos<", ">Tithes<"),
    (">Saldo<", ">Balance<"),
    ("Arrecadação por mês", "Giving by month"),
    ("Logo Portal da Igreja", "Portal da Igreja logo"),
    # --- faixa
    ("🇧🇷 Feito no Brasil", "🇧🇷 Made in Brazil"),
    ("para igrejas brasileiras", "for Brazilian churches"),
    ("💬 Suporte", "💬 Support"),
    ("em português, por WhatsApp", "in Portuguese, over WhatsApp"),
    ("🆓 Plano gratuito", "🆓 Free plan"),
    ("sem cartão de crédito", "no credit card"),
    ("📜 LGPD", "📜 Privacy"),
    ("consentimento e exportação de dados", "consent records and data export"),
    # --- recursos
    ("Tudo o que sua igreja precisa, em um só lugar", "Everything your church needs, in one place"),
    ("Módulos pensados para a realidade da gestão eclesiástica, do cadastro à prestação de contas.",
     "Modules built for the reality of church administration, from member records to accountability."),
    ("Gestão de Membros", "Member management"),
    ("Ficha completa de cada pessoa: contatos, batismo, membro desde quando, estado civil, função na igreja, ministério e anotações pastorais. Veja as contribuições e a constância de cada membro, e fale com ele pelo WhatsApp em um clique.",
     "A full record for each person: contact details, baptism, member since, marital status, role in the church, ministry and pastoral notes. See each member's giving and how regular it is, and reach them on WhatsApp in one click."),
    ("Dízimos &amp; Ofertas por Pix", "Tithes &amp; offerings by Pix"),
    ("O membro escolhe o valor no portal, lê o QR Code no app do banco e pronto: o dinheiro cai direto na conta da igreja, sem intermediário e sem taxa. A tesouraria confirma no extrato e o valor entra no extrato do membro. Sem nome? Tem a oferta avulsa.",
     "The member picks an amount in the portal, scans the QR code in their banking app and that is it: the money lands straight in the church's account, with no middleman. The treasurer confirms it against the bank statement and it shows up in the member's own history. No name attached? Use the anonymous offering."),
    ("Fechamento do Mês", "Monthly closing"),
    ("Quanto entrou, quanto saiu, comparação com o mês anterior, de onde veio e para onde foi por categoria, maiores despesas e o que já está previsto. Pronto para apresentar à diretoria.",
     "Money in, money out, the comparison with the previous month, where it came from and where it went by category, the largest expenses and what is already expected. Ready to present to the board."),
    ("Financeiro com categorias", "Finances by category"),
    ("Receitas e despesas organizadas por categoria, escolhidas numa lista que a sua igreja personaliza.",
     "Income and expenses organised by category, chosen from a list your church customises."),
    ("Contas recorrentes", "Recurring bills"),
    ("Aluguel, salários e energia lançados sozinhos na data certa, todo mês. Pause ou encerre quando quiser.",
     "Rent, salaries and power posted on their own, on the right date, every month. Pause or end them whenever you want."),
    ("Portal do Membro", "Member portal"),
    ("Cada membro vê o próprio extrato e baixa o informe anual em PDF para o imposto de renda.",
     "Each member sees their own giving history and downloads the annual statement as a PDF."),
    ("Site da Igreja", "Church website"),
    ("Site público com páginas, galeria, horários de culto e contatos, sem saber programar. Incluso nos planos pagos.",
     "A public site with pages, a gallery, service times and contact details, with no coding. Included in the paid plans."),
    ("Agenda da igreja", "Church calendar"),
    ("Cultos e eventos cadastrados uma vez aparecem no site, no portal do membro e no dashboard.",
     "Services and events entered once appear on the website, in the member portal and on the dashboard."),
    ("Pedidos de oração", "Prayer requests"),
    ("O membro envia pelo portal, a liderança acompanha e marca quando Deus responde.",
     "Members send them through the portal; the leadership follows up and marks the answer."),
    ("Mural de avisos", "Notice board"),
    ("Recados da liderança no portal do membro, com destaque para o que é urgente.",
     "Messages from the leadership in the member portal, with the urgent ones pinned."),
    ("Famílias, grupos e ministérios", "Families, groups and ministries"),
    ("Cônjuge e filhos ligados na ficha; louvor, células e departamentos com líder e lista de pessoas.",
     "Spouse and children linked on the record; worship, cells and departments with a leader and their people."),
    ("Campanhas", "Campaigns"),
    ("Crie campanhas com metas e acompanhe o progresso em tempo real.",
     "Create campaigns with goals and follow the progress as it comes in."),
    ("Dashboard com o pulso da igreja", "Dashboard with the church's pulse"),
    ("Novos membros, aniversários da semana, quem deixou de contribuir, contas a pagar e os últimos 12 meses.",
     "New members, this week's birthdays, who stopped giving, upcoming bills and the last 12 months."),
    ("Transparência &amp; LGPD", "Transparency &amp; privacy"),
    ("Prestação de contas aos membros sem expor quem deu quanto, trilha de auditoria e proteção de dados dentro da lei.",
     "Accountability to the congregation without exposing who gave what, an audit trail and data protection under Brazilian law."),
    ("Aniversariantes", "Birthdays"),
    ("Nascimento e casamento: lembrete todo dia de manhã para a liderança cuidar de quem faz parte da igreja.",
     "Birthdays and wedding anniversaries: a reminder every morning so the leadership can care for their people."),
    ("Quer ver um módulo por dentro?", "Want to see a module in detail?"),
    ("Sistema de gestão para igrejas", "Church management software"),
    ("Controle de dízimos e ofertas", "Tithes and offerings"),
    ("Cadastro de membros", "Member database"),
    ("Dízimos e ofertas", "Tithes and offerings"),
    ("Financeiro para igrejas", "Church accounting"),
    ("Prestação de contas", "Financial reports"),
    ("Site para igrejas", "Church website builder"),
    (">Financeiro<", ">Finances<"),
    (">Site da igreja<", ">Website<"),
    # --- como funciona
    ("Comece em três passos", "Start in three steps"),
    ("Sem instalação, sem complicação. Tudo na nuvem.",
     "Nothing to install, nothing complicated. All in the cloud."),
    ("Crie a conta da sua igreja", "Create your church account"),
    ("Cadastre sua igreja em minutos e convide a sua equipe.",
     "Register your church in minutes and invite your team."),
    ("Cadastre membros e lançamentos", "Add members and entries"),
    ("Importe a planilha de membros, registre dízimos e ofertas e marque as contas fixas como recorrentes.",
     "Import your member spreadsheet, record tithes and offerings and mark the fixed bills as recurring."),
    ("Acompanhe relatórios e transparência", "Follow reports and transparency"),
    ("Veja indicadores em tempo real e compartilhe a prestação de contas.",
     "See the numbers as they come in and share the accountability report."),
    # --- segurança
    ("Os dados da sua igreja em boas mãos", "Your church's data in good hands"),
    ("Você cuida das pessoas. A gente cuida da segurança — sem você precisar entender de tecnologia.",
     "You take care of people. We take care of security — with no technical knowledge needed on your side."),
    ("Dados sensíveis criptografados", "Sensitive data encrypted"),
    ("CPF, telefone e endereço dos membros ficam embaralhados (criptografados) no banco de dados, e as senhas nunca são guardadas em texto. O acesso ao sistema é sempre por conexão segura.",
     "Document number, phone and address of members are encrypted in the database, and passwords are never stored as text. Access to the system always runs over a secure connection."),
    ("Só você entra na sua conta", "Only you get into your account"),
    ("Cada pessoa pode ativar a confirmação em duas etapas: além da senha, o sistema pede um código do celular. Você também vê os aparelhos conectados e pode desconectar qualquer um.",
     "Anyone can turn on two-step confirmation: besides the password, the system asks for a code from the phone. You also see the connected devices and can disconnect any of them."),
    ("Dentro da lei (LGPD)", "Under Brazilian privacy law (LGPD)"),
    ("Consentimento registrado por finalidade, termo da sua igreja com versão, exportação dos dados do membro e trilha de auditoria de quem mexeu em quê — como pede a LGPD.",
     "Consent recorded per purpose, your church's own terms with versioning, export of a member's data and an audit trail of who changed what — as the Brazilian data protection law requires."),
    ("Cada igreja no seu espaço", "Each church in its own space"),
    ("Os dados de cada igreja ficam separados dos das demais, com a divisão aplicada em duas camadas: no sistema e no próprio banco de dados.",
     "Each church's data is kept apart from every other church's, with the separation enforced in two layers: in the application and in the database itself."),
    # --- planos
    ("Escolha o plano ideal para sua igreja", "Choose the plan that fits your church"),
    ("Todos os planos pagos têm os mesmos recursos: o que muda é quantos membros a sua igreja pode cadastrar. O site da igreja está incluso em todos eles.",
     "Every paid plan has the same features: what changes is how many members your church can register. The church website is included in all of them. Prices are in Brazilian reais (BRL)."),
    ("Escolher periodicidade de cobrança", "Choose billing period"),
    (">Mensal<", ">Monthly<"),
    ("\n            Anual <span", "\n            Annual <span"),
    ("para sempre", "forever"),
    ("Até 50 membros", "Up to 50 members"),
    ("Membros, dízimos e financeiro", "Members, giving and finances"),
    ("Portal do membro com Pix", "Member portal with Pix"),
    ("Relatórios e fechamento do mês", "Reports and monthly closing"),
    ("Sem o site da igreja", "Without the church website"),
    ("/mês", "/mo"),
    ("Cobrança mensal", "Billed monthly"),
    ("Cobrado anualmente (R$&nbsp;767,04/ano)", "Billed annually (R$&nbsp;767.04/yr)"),
    ("Cobrado anualmente (R$&nbsp;1.439,04/ano)", "Billed annually (R$&nbsp;1,439.04/yr)"),
    ("Cobrado anualmente (R$&nbsp;2.879,04/ano)", "Billed annually (R$&nbsp;2,879.04/yr)"),
    ("Até 150 membros", "Up to 150 members"),
    ("Até 500 membros", "Up to 500 members"),
    ("Até 1.000 membros", "Up to 1,000 members"),
    ("Todos os recursos do sistema", "Every feature of the system"),
    ("Site da igreja incluso", "Church website included"),
    ("Usuários da equipe sem limite", "Unlimited team users"),
    ("Suporte por WhatsApp e e-mail", "Support over WhatsApp and e-mail"),
    ("Sob consulta", "Let's talk"),
    ("Para redes e grandes igrejas", "For networks and large churches"),
    ("Membros sem limite", "Unlimited members"),
    ("Condições combinadas com a equipe", "Terms agreed with our team"),
    ("🔒 Plano gratuito para sempre · Cancele quando quiser · Sem fidelidade e sem taxa de cancelamento",
     "🔒 Free plan forever · Cancel whenever you want · No contract and no cancellation fee"),
    ("Igreja maior ou precisa de ajuda para escolher?",
     "Larger church, or need help choosing?"),
    ("📅 Agendar uma demonstração", "📅 Book a demonstration"),
    # --- FAQ
    ("Dúvidas frequentes", "Frequently asked"),
    ("Perguntas que outras igrejas fizeram", "Questions other churches asked"),
    ("Não encontrou a sua resposta? Fale com a gente no WhatsApp — respondemos rapidinho.",
     "Did not find your answer? Message us on WhatsApp — we reply quickly."),
    ("Posso importar membros de uma planilha?", "Can I import members from a spreadsheet?"),
    ("Sim. Você pode importar a sua lista de membros a partir de uma planilha (Excel/CSV), sem precisar digitar tudo de novo. Assim a migração das suas informações leva minutos, não dias.",
     "Yes. You can import your member list from a spreadsheet (Excel/CSV), with no retyping. The migration takes minutes, not days."),
    ("Os membros podem dizimar por Pix?", "Can members tithe by Pix?"),
    ("Sim. Com a chave Pix da igreja cadastrada, o membro escolhe o valor no portal e recebe um QR Code para pagar pelo app do banco. O dinheiro cai direto na conta da igreja, sem intermediário e sem taxa. A tesouraria confirma cada Pix ao conferir o extrato, e a contribuição entra no financeiro e no extrato do membro.",
     "Yes, with the church's Pix key registered. The member picks an amount in the portal and gets a QR code to pay from their banking app. The money goes straight to the church's Brazilian account, with no middleman. The treasurer confirms each Pix against the bank statement, and it then counts in the finances and in the member's history."),
    ("O sistema lança contas fixas sozinho?", "Does the system post fixed bills by itself?"),
    ("Sim. Aluguel, salários, energia e outras contas fixas podem ser marcadas como recorrentes. O sistema lança automaticamente na data certa, todo mês, semana ou ano, e você pode pausar ou encerrar quando quiser.",
     "Yes. Rent, salaries, power and other fixed bills can be marked as recurring. The system posts them automatically on the right date — weekly, monthly or yearly — and you can pause or end them whenever you want."),
    ("Tem relatório para apresentar à diretoria?", "Is there a report for the board meeting?"),
    ("Sim. O fechamento do mês mostra quanto entrou, quanto saiu, a comparação com o mês anterior, de onde veio e para onde foi o dinheiro por categoria, as maiores despesas e o que já está previsto para os próximos 30 dias. Ele também aponta quem contribuiu, quem contribuiu pela primeira vez e quem parou de contribuir, para o cuidado pastoral.",
     "Yes. The monthly closing shows money in, money out, the comparison with the previous month, where the money came from and went by category, the largest expenses and what is expected for the next 30 days. It also points out who gave, who gave for the first time and who stopped giving, for pastoral care."),
    ("O site da igreja está incluso?", "Is the church website included?"),
    ("Sim. Todos os planos pagos incluem o site da igreja, com páginas, galeria de fotos, horários de culto e contatos, editável sem saber programar. Ele já vem com um exemplo pronto para você só ajustar.",
     "Yes. Every paid plan includes the church website, with pages, a photo gallery, service times and contact details, editable without coding. It comes with an example site ready for you to adjust."),
    ("E quando a oferta vem sem nome?", "What about offerings with no name?"),
    ("Existe o tipo \"oferta avulsa\" para o dinheiro que chega no gazofilácio sem identificação. Ele entra nos totais de ofertas da igreja sem precisar inventar um membro.",
     "There is an \"anonymous offering\" type for money that comes in without identification. It counts towards the church's offering totals without inventing a member."),
    ("Meus dados ficam seguros?", "Is my data safe?"),
    ("Dados sensíveis como CPF, telefone e endereço são criptografados, o acesso pode exigir confirmação em duas etapas e os dados da sua igreja ficam separados dos de outras igrejas. Há registro de consentimento, exportação dos dados do membro e trilha de auditoria, como pede a LGPD.",
     "Sensitive data such as document number, phone and address is encrypted, access can require two-step confirmation, and your church's data is kept apart from other churches'. There are consent records, member data export and an audit trail, as Brazilian privacy law requires."),
    ("Posso cancelar a qualquer momento?", "Can I cancel at any time?"),
    ("Sim, sem burocracia. Não há fidelidade nem taxa de cancelamento: você cancela quando quiser pela própria tela de assinatura e a conta volta para o plano gratuito, com os seus dados preservados.",
     "Yes, with no paperwork. There is no contract and no cancellation fee: you cancel from the subscription screen and the account goes back to the free plan, with your data kept."),
    ("O sistema funciona no celular?", "Does it work on a phone?"),
    ("Funciona. O Portal da Igreja é 100% na nuvem e se adapta a celular, tablet e computador. Você acessa de qualquer lugar, sem instalar nada.",
     "It does. Portal da Igreja runs entirely in the cloud and adapts to phone, tablet and computer. You get in from anywhere, with nothing to install."),
    ("Tem suporte em português?", "Which language is support in?"),
    ("Sim, todo o suporte é em português e feito por pessoas que entendem a realidade das igrejas brasileiras. Você também pode falar com a gente pelo WhatsApp.",
     "Support is in Portuguese, by people who understand how Brazilian churches work. The software interface is in Portuguese too. You can reach us on WhatsApp."),
    ("O plano gratuito tem limite de tempo?", "Does the free plan expire?"),
    ("Não. O plano gratuito é para sempre, sem cartão de crédito e sem prazo para acabar. Você usa à vontade e só evolui de plano quando a sua igreja precisar de mais recursos.",
     "No. The free plan lasts forever, with no credit card and no deadline. You move to a paid plan only when your church needs more room."),
    ("Quantos usuários posso cadastrar?", "How many users can I create?"),
    ("Quantos a sua equipe precisar, em qualquer plano: pastores, tesoureiros, secretários e líderes, cada um com a sua permissão. O que muda de um plano para o outro é o limite de membros cadastrados, não o número de usuários.",
     "As many as your team needs, on any plan: pastors, treasurers, secretaries and leaders, each with their own permissions. What changes between plans is the limit of registered members, not the number of users."),
    ("Como funciona o Portal do Membro?", "How does the member portal work?"),
    ("Cada membro pode acessar o próprio extrato de contribuições e baixar o informe anual em PDF. Isso reduz as perguntas para a tesouraria e aumenta a transparência com toda a igreja.",
     "Each member can see their own giving history and download the annual statement as a PDF. That cuts down the questions to the treasurer and builds trust across the church."),
    # --- CTA final e rodapé
    ("Sua igreja merece organização. Comece hoje — é gratuito.",
     "Your church deserves order. Start today — it is free."),
    ("Crie a conta da sua igreja em poucos minutos, no plano gratuito, e organize membros, dízimos e finanças com mais transparência.",
     "Create your church account in a few minutes, on the free plan, and organise members, giving and finances with more transparency."),
    ("Gestão completa, segura e transparente para a sua igreja — na nuvem.",
     "Church management, giving and website in one system — in the cloud."),
    (">Produto<", ">Product<"),
    (">Empresa<", ">Company<"),
    ("© 2026 Portal da Igreja. Todos os direitos reservados.",
     "© 2026 Portal da Igreja. All rights reserved."),
    ("Política de Privacidade", "Privacy Policy"),
    ("Termos de Uso", "Terms of Use"),
    ("Fale conosco no WhatsApp", "Talk to us on WhatsApp"),
    ("Portal da Igreja — sistema de gestão para igrejas", "Portal da Igreja — church management software"),
    ("Portal da Igreja - início", "Portal da Igreja - home"),
    ("Navegação principal", "Main navigation"),
    ("Abrir menu", "Open menu"),
    ("Ol%C3%A1!%20Vim%20pelo%20site%20do%20Portal%20da%20Igreja%20e%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es.",
     "Hello!%20I%20came%20from%20the%20Portal%20da%20Igreja%20website%20and%20would%20like%20more%20information."),
    ("Ol%C3%A1!%20Gostaria%20de%20agendar%20uma%20demonstra%C3%A7%C3%A3o%20do%20Portal%20da%20Igreja.",
     "Hello!%20I%20would%20like%20to%20book%20a%20demonstration%20of%20Portal%20da%20Igreja."),
]

# Âncoras internas (ids das seções) traduzidas junto com os links.
ANCHORS = {"recursos": "features", "como-funciona": "how-it-works", "planos": "plans",
           "seguranca": "security", "contato": "contact", "hero": "hero", "faq": "faq"}

# Palavras que denunciam texto em português esquecido na página em inglês.
PT_MARKERS = re.compile(
    r"\b(igreja|igrejas|membros|dízimo|dízimos|ofertas|planos|gratuito|mensal|anual|"
    r"você|sua|para|com|não|sim|todos|conta)\b", re.I)


def translate(src: str) -> str:
    out = src
    for pt, en in sorted(PAIRS, key=lambda p: -len(p[0])):
        out = out.replace(pt, en)
    for pt_id, en_id in ANCHORS.items():
        out = out.replace(f'id="{pt_id}"', f'id="{en_id}"')
        out = out.replace(f'href="#{pt_id}"', f'href="#{en_id}"')
        out = out.replace(f'aria-controls="{pt_id}"', f'aria-controls="{en_id}"')
    return out


def main() -> int:
    src = (ROOT / "index.html").read_text(encoding="utf-8")

    # 1. cabeçalho próprio (metadados, hreflang e dados estruturados em inglês)
    head_start = src.index("<head>") + len("<head>")
    head_end = src.index("</head>")
    gtag = src[head_start:head_end]
    gtag = gtag[:gtag.index("<meta charset")]          # mantém o GA4 como está
    out = src[:head_start] + gtag + HEAD + src[head_end:]

    # 2. corpo traduzido
    body_start = out.index("<body>")
    out = out[:body_start] + translate(out[body_start:])

    # 3. caminhos relativos -> absolutos (a página vive em /en/)
    out = out.replace('href="styles.css"', 'href="/styles.css"')
    out = out.replace('src="script.js"', 'src="/script.js"')
    out = re.sub(r'(src|srcset)="assets/', r'\1="/assets/', out)
    out = out.replace('href="#hero" class="nav-logo"', 'href="/en/" class="nav-logo"')

    # 4. idioma, aviso e troca de idioma
    out = out.replace('<html lang="pt-BR">', '<html lang="en">', 1)
    out = out.replace("  <main>\n", "  <main>\n", 1)
    first_section = out.index('    <section class="hero"')
    end_hero = out.index("</section>", first_section) + len("</section>\n")
    out = out[:end_hero] + NOTICE + out[end_hero:]
    out = out.replace('<a href="/sistema-gestao-igrejas/">', '<a href="/en/church-management-software/">')
    for pt_slug, en_slug in (("cadastro-membros-igreja", "church-member-database"),
                             ("controle-dizimos-ofertas", "church-tithes-offerings"),
                             ("financeiro-para-igrejas", "church-accounting-software"),
                             ("prestacao-de-contas-igreja", "church-financial-reports"),
                             ("site-para-igrejas", "church-website-builder")):
        out = out.replace(f'href="/{pt_slug}/"', f'href="/en/{en_slug}/"')
    out = out.replace('<a href="mailto:suporte@portaldaigreja.com.br">',
                      '<a href="/" hreflang="pt-BR" lang="pt-BR">Português</a>\n'
                      '        <a href="mailto:suporte@portaldaigreja.com.br">', 1)

    # 5. conferência: sobrou português?
    body = out[out.index("<body>"):]
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    visible = " ".join(l.strip() for l in re.sub(r"<[^>]+>", "\n", body).splitlines() if l.strip())
    visible = visible.replace("suporte@portaldaigreja.com.br", "")
    leftovers = sorted(set(m.group(0) for m in PT_MARKERS.finditer(visible))
                       # nomes dos planos ficam como no sistema, de propósito
                       - {"Portal", "Igreja", "Gratuito"})
    if leftovers:
        print("ERRO: texto em português na página em inglês:", ", ".join(leftovers))
        print("Acrescente o par que falta em PAIRS e rode de novo.")
        return 1

    dest = ROOT / "en" / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out, encoding="utf-8")
    print("escrito: en/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
