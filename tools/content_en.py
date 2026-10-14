"""English page content, aimed at Brazilian churches abroad.

The buyer is a Brazilian pastor, treasurer or secretary leading a congregation in
the United States, Europe or Japan. English is for being found and for the
second generation; the system itself is in Portuguese and billed in Brazilian
reais, which is said plainly on every page (see NOTICE in build_pages.py).

Same rule as the Portuguese content: only what the product actually does. Check
docs/CATALOGO-FUNCIONALIDADES-IGREJAS.md before adding a sentence.
"""

PAGES: list[dict] = [
    {
        "slug": "church-management-software",
        "title": "Church Management System | Portal da Igreja",
        "description": ("Members, tithes and offerings, finances, reports and a member portal in "
                        "one system. Free plan for up to 50 members."),
        "kicker": "Church management",
        "h1": "Church management software, from the member list to the monthly report",
        "lead": ("One place for the secretary, the treasurer and the leadership: member records, "
                 "tithes and offerings, church finances, reports that are ready to present and a "
                 "portal where each member sees their own giving. Start on the free plan, no "
                 "credit card."),
        "blocks": [
            {"type": "prose", "kicker": "The problem", "h2": "The spreadsheet got you this far",
             "paras": [
                 "In most churches the information is scattered: the member list in a spreadsheet, "
                 "the cash book on paper, the tithes in a notepad and the receipts in somebody's "
                 "phone. When the accountability meeting comes, someone spends a weekend putting "
                 "it all together again.",
                 "Portal da Igreja brings those controls into one system, built for people who are "
                 "not from a technical background: in the cloud, on a computer or a phone, with "
                 "nothing to install."]},
            {"type": "features", "kicker": "What the system does", "h2": "The modules your church uses every week",
             "sub": "Every feature below is available on any plan, including the free one. What changes between plans is how many members the church can register, plus the church website, which comes with the paid plans.",
             "items": [
                 ("👥", "ic-blue", "Member records",
                  "Contact details, address, date of birth, baptism, marital status and role in the church. Families, groups, cells and ministries linked to each person.",
                  "/en/church-member-database/"),
                 ("💝", "ic-green", "Tithes and offerings",
                  "Tithe, offering, anonymous plate offering and campaign donation. Members give by Pix and the treasurer confirms each one against the bank statement.",
                  "/en/church-tithes-offerings/"),
                 ("💰", "ic-green", "Church finances",
                  "Income and expenses by category, fixed bills posted automatically and the monthly closing as a PDF for the board.",
                  "/en/church-accounting-software/"),
                 ("🌐", "ic-blue", "Church website",
                  "A public site with pages, a gallery, service times, the calendar and Pix, edited without writing code. Included in the paid plans.",
                  "/en/church-website-builder/"),
                 ("📑", "ic-blue", "Financial accountability",
                  "The board report, the transparency report with no donor names and each member's annual giving statement.",
                  "/en/church-financial-reports/"),
                 ("🧾", "ic-blue", "Member portal", None),
                 ("📅", "ic-blue", "Calendar and notices", None),
                 ("🙏", "ic-green", "Prayer requests", None),
             ],
             "plain": {
                 "Member portal": "Each member signs in, sees what they have given, downloads the annual statement as a PDF, sends a prayer request and reads the notices.",
                 "Calendar and notices": "Services and events entered once show up on the dashboard, in the member portal and on the church website. The notice board highlights what is urgent.",
                 "Prayer requests": "The request reaches the leadership, who mark it as being prayed for and can send an answer back to the member.",
             }},
            {"type": "steps", "kicker": "Getting started", "h2": "Three steps away from the spreadsheet",
             "items": [
                 ("Create the church account", "It takes a few minutes and asks for no credit card. You are the first administrator."),
                 ("Bring the members in", "Import the spreadsheet the church already keeps: the system reads the file, you check the columns, and only then is anything saved."),
                 ("Record what happens", "Enter tithes, offerings and expenses, mark the fixed bills as recurring and watch the month close itself."),
             ]},
            {"type": "prose", "kicker": "Built in Brazil", "h2": "Why a Brazilian system, abroad",
             "paras": [
                 "Portal da Igreja was made for Brazilian churches, and that is exactly why it fits "
                 "a Brazilian congregation overseas: the system speaks Portuguese, giving works "
                 "through Pix into the church's own Brazilian account, and support answers in "
                 "Portuguese over WhatsApp.",
                 "If your congregation collects locally — in dollars, euros or yen — you can still "
                 "record those entries by hand in the finance module; what the system automates is "
                 "Pix. Talk to us before subscribing so we can tell you honestly whether it fits."]},
        ],
        "faq": [
            ("Is the system available in English?",
             "Not yet. The software interface is in Portuguese, and so is support. The English pages exist so Brazilian churches abroad can find us; the product itself speaks Portuguese."),
            ("Can I pay in dollars or euros?",
             "No. Subscriptions are charged in Brazilian reais (BRL) by card or boleto, through Stripe. An international card usually works, with the currency conversion your bank applies."),
            ("Can we bring the list of members we already have?",
             "Yes. The import assistant reads Excel (.xlsx, .xls) and CSV files, suggests which field each column maps to and shows everything for you to review before saving. Duplicates are blocked by document number, e-mail or name."),
            ("How many people from our team can use it?",
             "As many as the church needs, on any plan. Pastor, treasurer and secretary get separate logins with their own permissions. The plan limit is on registered members, not on users."),
        ],
    },
    {
        "slug": "church-member-database",
        "title": "Church Member Database Software | Portal da Igreja",
        "description": ("Member records with families, groups and ministries, spreadsheet import "
                        "and duplicate blocking, for churches that outgrew the spreadsheet."),
        "kicker": "Members",
        "h1": "A church member database that stays organised",
        "lead": ("The secretary with a record for each person, households linked together, the "
                 "groups and ministries each member serves in — and the old spreadsheet imported "
                 "without typing everything again."),
        "blocks": [
            {"type": "features", "kicker": "The record", "h2": "What each member record holds",
             "items": [
                 ("🗂️", "ic-blue", "Member record", None),
                 ("👨‍👩‍👧", "ic-green", "Families", None),
                 ("🤝", "ic-blue", "Groups, cells and ministries", None),
                 ("📥", "ic-green", "Spreadsheet import", None),
                 ("🚫", "ic-blue", "No duplicate records", None),
                 ("🎂", "ic-green", "Birthdays and anniversaries", None),
                 ("🔑", "ic-blue", "Portal access", None),
                 ("📜", "ic-green", "Consent and privacy", None),
             ],
             "plain": {
                 "Member record": "Contact details, full address, date of birth, baptism date, marital status and wedding date, role in the church, occupation and pastoral notes.",
                 "Families": "People in the same household are linked as head, spouse, child or relative, which also feeds the wedding anniversary reminders.",
                 "Groups, cells and ministries": "Register worship, children's ministry, cells and departments, each with a leader, meeting information and the role of every participant.",
                 "Spreadsheet import": "An assistant reads your Excel or CSV file, finds where the table starts, suggests a field for each column and shows the result before anything is saved. Phone numbers and documents are tidied up along the way.",
                 "No duplicate records": "The same person cannot be entered twice: the system compares document number, e-mail and name, and blocks repetition during the import too. For duplicates you already have, there is a review screen.",
                 "Birthdays and anniversaries": "Birthdays of the week and wedding anniversaries appear on the dashboard and reach the team by e-mail every morning.",
                 "Portal access": "Anyone with an e-mail address can be given a member portal login. Passwords are never e-mailed: the person sets their own through a first-access link.",
                 "Consent and privacy": "Consent is recorded per purpose, with history and with your church's own terms, versioned. A member's data can be exported whenever they ask.",
             }},
            {"type": "prose", "kicker": "Migration", "h2": "The spreadsheet you already keep will do",
             "paras": [
                 "There is no need to tidy the file first. The assistant accepts Excel and CSV, "
                 "copes with title rows above the table and fixes names typed in all capitals.",
                 "When a value makes no sense — an impossible date, an incomplete phone number — "
                 "the row is not thrown away: that one field is left out with a warning, so nobody "
                 "is lost because of a single cell."]},
        ],
        "faq": [
            ("What file formats can I import?",
             "Excel (.xlsx and .xls) and CSV. You choose which column is which field, and there is also a template to download if you prefer to start from scratch."),
            ("What if the same person is entered twice?",
             "The system blocks it: same document number, same e-mail or same name, unless the dates of birth differ. For older duplicates there is a \"review duplicates\" screen."),
            ("Can members update their own details?",
             "Members sign in to the portal, see their record, their giving and the annual statement, and can request an export of their data."),
            ("Is there a limit on how many members I can register?",
             "Yes, by plan: 50 on the free plan, 150 on Essencial, 500 on Crescimento and 1,000 on Avançado. The count includes every record that has not been deleted, visitors and inactive members included."),
        ],
    },
    {
        "slug": "church-tithes-offerings",
        "title": "Church Tithes and Offerings Software | Portal da Igreja",
        "description": ("Record tithes, offerings and campaign donations, receive by Pix straight "
                        "into the church account and give each member an annual statement."),
        "kicker": "Tithes and offerings",
        "h1": "Tithes and offerings, with Pix straight into the church's own account",
        "lead": ("Every contribution recorded with its date, method and, when there is one, the "
                 "member who gave it. Pix money lands directly in the church's Brazilian account, "
                 "with no middleman, and the treasurer confirms each entry against the statement."),
        "blocks": [
            {"type": "features", "kicker": "How it works", "h2": "From the envelope to the report",
             "items": [
                 ("💝", "ic-green", "Four kinds of entry", None),
                 ("📱", "ic-blue", "Pix with a QR code", None),
                 ("✅", "ic-green", "Confirmed by the treasurer", None),
                 ("🧾", "ic-blue", "Annual giving statement", None),
                 ("🎯", "ic-green", "Campaigns with a goal", None),
                 ("📊", "ic-blue", "Who gave, and who stopped", None),
             ],
             "plain": {
                 "Four kinds of entry": "Tithe (tied to a member), offering, anonymous plate offering — the one with no name attached — and donation to a campaign. Each lands in the right totals.",
                 "Pix with a QR code": "You register the church's Pix key and the system produces the QR code and the copy-and-paste code. The member picks an amount in the portal and pays from their banking app; the money goes straight to the church account, with no middleman.",
                 "Confirmed by the treasurer": "A Pix sent by a member stays pending until someone from the treasury checks the bank statement and confirms it. Nothing reaches the reports before that check, and every request carries the identifier that shows up on the statement.",
                 "Annual giving statement": "In the portal, members see what they gave during the year and download the statement as a PDF, which spares the treasurer most of the questions.",
                 "Campaigns with a goal": "A building, missions or outreach campaign with a goal and live progress, plus a report for that campaign alone.",
                 "Who gave, and who stopped": "A report for the leadership shows who gave in the period, who gave for the first time and who used to give and stopped — a pastoral care list, for internal use.",
             }},
            {"type": "prose", "kicker": "Being honest about Pix", "h2": "What this is, and what it is not",
             "paras": [
                 "Portal da Igreja is not a bank and does not process payments: the Pix code is "
                 "generated from the church's own key and the money never passes through us. That "
                 "also means there is no automatic reconciliation — someone from the treasury "
                 "checks the statement and confirms, which keeps control with the church.",
                 "Pix is a Brazilian payment method and requires a Brazilian bank account. If your "
                 "congregation collects in dollars, euros or yen, those entries can be recorded by "
                 "hand in the finance module, but the system will not generate codes for them."]},
        ],
        "faq": [
            ("Do we need a card reader or a payment company?",
             "No. Pix uses the church's own key and the money lands in the church account. There is no middleman between the member and the church."),
            ("Does Pix work outside Brazil?",
             "Pix is a Brazilian system and needs a Brazilian bank account for the church. Members abroad can pay it from a Brazilian banking app. Giving in local currency can be recorded manually."),
            ("What about offerings with no name on them?",
             "There is an \"anonymous offering\" type for exactly that. It counts towards the church's offering totals without inventing a member."),
            ("Who can see how much each person gave?",
             "Only people with administration or management permission. The report shared with the congregation shows totals only, with no names."),
        ],
    },
    {
        "slug": "church-accounting-software",
        "title": "Church Accounting Software | Portal da Igreja",
        "description": ("Track church income and expenses by category, post fixed bills "
                        "automatically and close the month as a PDF for the board."),
        "kicker": "Finances",
        "h1": "Church accounting software for the treasurer who closes the month",
        "lead": ("Income and expenses organised by category, fixed bills posted on their own and "
                 "the meeting report coming out as a PDF — without building a spreadsheet."),
        "blocks": [
            {"type": "features", "kicker": "Treasury", "h2": "The whole month in one place",
             "items": [
                 ("💰", "ic-green", "Income and expenses", None),
                 ("🏷️", "ic-blue", "Your church's categories", None),
                 ("🔁", "ic-green", "Recurring fixed bills", None),
                 ("📑", "ic-blue", "Monthly closing as a PDF", None),
                 ("📂", "ic-green", "Report by category", None),
                 ("📤", "ic-blue", "Export for the accountant", None),
             ],
             "plain": {
                 "Income and expenses": "Every entry with its date, amount, category and description, split between money in and money out, and totalled automatically for the period you choose.",
                 "Your church's categories": "A list of categories per kind, which you rename and organise. Renaming updates the older entries too; merging two categories merges their history.",
                 "Recurring fixed bills": "Rent, salaries, power and internet become a weekly, monthly or yearly template. The system posts them on the right date every time, and you can pause or end them whenever you want.",
                 "Monthly closing as a PDF": "Money in, money out, the comparison with the previous month, income by contribution type, expenses by category with each one's share, the largest outflows and what is already expected for the next 30 days.",
                 "Report by category": "Pick the categories and campaigns you need to account for and get a report with every entry and its subtotals, as a PDF with space for signatures or as an Excel file.",
                 "Export for the accountant": "Entries, contributions, campaigns and members export to CSV, which opens in Excel and in any accounting system.",
             }},
            {"type": "prose", "kicker": "Being clear about limits", "h2": "What does not exist yet",
             "paras": [
                 "So there is no surprise after you subscribe: the system does not do automatic "
                 "bank reconciliation, does not store receipt attachments, has no accounts payable "
                 "with due-date clearing and no budget by cost centre. What it does is entries, "
                 "categories, recurring bills and reports.",
                 "It also does not replace your accountant and issues no tax documents. Amounts are "
                 "recorded in Brazilian reais."]},
        ],
        "faq": [
            ("Does the system post fixed bills by itself?",
             "Yes. Mark a bill as recurring, with its frequency and day, and the entry is created automatically on the right date. If you add one whose start date has passed, the overdue entries are posted straight away."),
            ("Can I get a report for the board meeting?",
             "Yes. The monthly closing comes out as a PDF with letterhead, numbered pages and the comparison with the previous month. The report by category also has signature lines."),
            ("Who on the team can see the finances?",
             "Only people with administration or management permission. Operators and members have no access to the treasury."),
            ("Which currency does it use?",
             "Brazilian reais. Entries in another currency can be recorded, but the system does not convert currencies."),
        ],
    },
    {
        "slug": "church-financial-reports",
        "title": "Church Financial Reports | Portal da Igreja",
        "description": ("A board report, a transparency report with no donor names and annual "
                        "giving statements, ready from the system."),
        "kicker": "Accountability",
        "h1": "Church financial reports your congregation can actually trust",
        "lead": ("The accountability meeting should not cost a weekend of spreadsheet work. The "
                 "system produces the monthly closing for the board, the transparency report for "
                 "the congregation — without saying who gave what — and each member's annual "
                 "statement."),
        "blocks": [
            {"type": "prose", "kicker": "The problem", "h2": "Trust is built with open numbers",
             "paras": [
                 "When a church does not know where the money goes, suspicion grows — and it is "
                 "almost never bad faith, it is the lack of a clear report. At the same time, "
                 "nobody wants to expose how much each family gave.",
                 "The answer is two separate documents: an open report for the congregation, with "
                 "totals and no names, and a detailed one for those responsible for the accounts. "
                 "The system produces both from the same entries."]},
            {"type": "features", "kicker": "The documents", "h2": "What comes ready out of the system",
             "items": [
                 ("📑", "ic-blue", "Monthly closing", None),
                 ("👁️", "ic-green", "Transparency report", None),
                 ("📂", "ic-blue", "Report by category", None),
                 ("🧾", "ic-green", "Annual giving statement", None),
                 ("🎯", "ic-blue", "Campaign accounts", None),
                 ("🔎", "ic-green", "Audit trail", None),
             ],
             "plain": {
                 "Monthly closing": "For the board meeting: money in and out, the comparison with the previous month, income by contribution type, expenses by category with each one's share, the largest outflows and what is expected for the next 30 days. A PDF with letterhead and numbered pages.",
                 "Transparency report": "Monthly totals, with no donor identified. This is the document to read at a members' meeting, post on the board or send to the congregation without embarrassing anyone. Available as PDF and Excel.",
                 "Report by category": "Pick the categories and campaigns to account for and get every entry, the subtotals and the total per side. The PDF has signature lines for the treasurer and the council; the Excel file has summary, detail and entry tabs.",
                 "Annual giving statement": "Members download their own statement for the year from the portal, without asking the treasurer.",
                 "Campaign accounts": "A building, missions or outreach campaign with its goal, how much has come in and a report for that campaign alone — for accounting to those who gave for a specific purpose.",
                 "Audit trail": "The system records who created, changed or deleted each entry, in a history that cannot be edited or erased. If someone questions a number, you can show where it came from.",
             }},
            {"type": "prose", "kicker": "Who sees what", "h2": "Each report for the right audience",
             "paras": [
                 "Per-person amounts stay with people who have administration or management "
                 "permission. Operators and members have no access to the treasury, and the report "
                 "shared with the congregation never carries names.",
                 "For the accountant, entries, contributions and campaigns export to CSV. Portal da "
                 "Igreja does not replace accounting and issues no tax documents: it organises the "
                 "numbers and hands over the report."]},
        ],
        "faq": [
            ("Can we show the accounts without exposing who gave?",
             "Yes, and that is the default. The transparency report shows monthly totals, with no names and no individual amounts. Per-person giving is visible only to people with treasury or leadership permission."),
            ("Is the report good enough for a board meeting?",
             "Yes. The monthly closing comes out as a PDF with letterhead, numbered pages, the comparison with the previous month, expenses by category and the largest outflows. The report by category adds signature lines."),
            ("What if someone questions an entry?",
             "The system keeps a record of who created or changed it, in a history that cannot be edited or erased."),
            ("Does it replace our accountant?",
             "No. The system organises the entries and produces the reports; accounting and tax obligations stay with your accountant, who can receive everything as CSV or Excel."),
        ],
    },
    {
        "slug": "church-website-builder",
        "title": "Church Website Builder, Included | Portal da Igreja",
        "description": ("Build your church website with no coding: pages, service times, gallery, "
                        "a calendar tied to the system and Pix. Included in every paid plan."),
        "kicker": "Church website",
        "h1": "A church website builder tied to the management system",
        "lead": ("Build your church page from ready-made blocks: service times, ministries, photo "
                 "gallery, map, contact and the Pix code for anyone who wants to give. The "
                 "calendar is the same one the secretary already keeps inside the system — enter "
                 "an event once and it shows up on the site."),
        "blocks": [
            {"type": "features", "kicker": "The builder", "h2": "Blocks you arrange and edit",
             "items": [
                 ("🧱", "ic-blue", "Pages and blocks", None),
                 ("⛪", "ic-green", "Service times", None),
                 ("📅", "ic-blue", "Calendar tied to the system", None),
                 ("💝", "ic-green", "Pix on the site", None),
                 ("🖼️", "ic-blue", "Gallery and photos", None),
                 ("🎨", "ic-green", "Your church's look", None),
                 ("📍", "ic-blue", "Map and contact", None),
                 ("📱", "ic-green", "Works on phones", None),
             ],
             "plain": {
                 "Pages and blocks": "A home page plus whatever else you need (About, Ministries, Contact). Each page is built from blocks: hero, text, image with text, cards, gallery, YouTube video, call to action, contact, calendar, map, service times, testimonials and Pix.",
                 "Service times": "A block just for the week's services and meetings — the first thing someone looking for a church wants to know.",
                 "Calendar tied to the system": "Events marked as public in the internal calendar appear on the site automatically. No updating the schedule in two places.",
                 "Pix on the site": "The church's own QR code, available to anyone who wants to give through the site, with no middleman.",
                 "Gallery and photos": "Upload photos from services and events (PNG, JPG or WEBP, up to 5 MB each) and build the gallery.",
                 "Your church's look": "Logo, cover photo, primary and secondary colours, top bar, footer and links to Instagram, Facebook, YouTube and WhatsApp.",
                 "Map and contact": "Address with a map, phone and e-mail, for people trying to find you.",
                 "Works on phones": "The site adapts to the visitor's screen, which most of the time is a phone following a link from WhatsApp or an Instagram bio.",
             }},
            {"type": "prose", "kicker": "Where it lives", "h2": "The address of your church site",
             "paras": [
                 "Once published, the site is available at a Portal da Igreja address, in the form "
                 "<code>app.portaldaigreja.com.br/yourchurch/portal</code>. That is the link the "
                 "church shares on Instagram, on WhatsApp and in print.",
                 "If your church already owns a domain, talk to us on WhatsApp: connecting a domain "
                 "is arranged case by case with our team.",
                 "Being straight with you: these church sites are built for visitors who already "
                 "have the link, not for search engines. They do not carry per-church meta tags or "
                 "a sitemap, so do not expect the site alone to make your church appear in Google "
                 "results."]},
            {"type": "prose", "kicker": "Included in the plan", "h2": "Nothing extra to buy",
             "paras": [
                 "The website is included in every paid plan — Essencial, Crescimento and Avançado "
                 "— at no additional cost and with no separate hosting. On the free plan the "
                 "editor is locked; the rest of the system stays available.",
                 "Because the site and the management system are the same product, the calendar, "
                 "the photos and the Pix key are entered only once."]},
        ],
        "faq": [
            ("Do I need to know how to code, or hire someone?",
             "No. You pick the blocks, write the text, upload the images and publish from the same panel you use to manage the church."),
            ("Is the website really included?",
             "Yes, in every paid plan, at no extra cost. Only the free plan is without the site editor."),
            ("Can we use the domain our church already owns?",
             "Connecting your own domain is arranged case by case with our team. Talk to us on WhatsApp before subscribing."),
            ("Will the site help our church show up on Google?",
             "Not on its own. These sites are rendered for visitors rather than for search engines, and they carry no per-church meta tags or sitemap. Treat it as the page you share, not as a search strategy."),
        ],
    },
]
