// ===== Navbar shadow on scroll =====
(function () {
  const navbar = document.getElementById('navbar');
  const onScroll = () => {
    navbar.classList.toggle('scrolled', window.scrollY > 8);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

// ===== Mobile menu toggle =====
(function () {
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('mobileMenu');
  if (!toggle || !menu) return;

  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    menu.classList.toggle('open', open);
    menu.hidden = !open;
  };

  toggle.addEventListener('click', () => {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });

  // Close menu when a link is clicked
  menu.querySelectorAll('a').forEach((a) =>
    a.addEventListener('click', () => setOpen(false))
  );

  // Close on resize to desktop
  window.addEventListener('resize', () => {
    if (window.innerWidth > 860) setOpen(false);
  });
})();

// ===== Smooth anchor scrolling (with sticky-nav offset) =====
(function () {
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href');
      if (id === '#' || id.length < 2) return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
})();


// ===== FAQ accordion (only one open at a time) =====
(function () {
  const items = document.querySelectorAll('.faq-item');
  if (!items.length) return;
  items.forEach((item) => {
    item.addEventListener('toggle', () => {
      if (item.open) {
        items.forEach((other) => {
          if (other !== item) other.open = false;
        });
      }
    });
  });
})();

// ===== Pricing billing toggle (Mensal / Anual) =====
(function () {
  const grid = document.getElementById('pricingGrid');
  const btnMonthly = document.getElementById('billMonthly');
  const btnAnnual = document.getElementById('billAnnual');
  if (!grid || !btnMonthly || !btnAnnual) return;

  const apply = (mode) => {
    grid.setAttribute('data-billing', mode);

    grid.querySelectorAll('.amount[data-' + mode + ']').forEach((el) => {
      const val = el.getAttribute('data-' + mode);
      if (val !== null) el.textContent = val;
    });
    grid.querySelectorAll('.price-sub[data-' + mode + ']').forEach((el) => {
      const val = el.getAttribute('data-' + mode);
      if (val !== null) el.textContent = val;
    });

    const isMonthly = mode === 'monthly';
    btnMonthly.classList.toggle('is-active', isMonthly);
    btnAnnual.classList.toggle('is-active', !isMonthly);
    btnMonthly.setAttribute('aria-pressed', String(isMonthly));
    btnAnnual.setAttribute('aria-pressed', String(!isMonthly));
  };

  btnMonthly.addEventListener('click', () => apply('monthly'));
  btnAnnual.addEventListener('click', () => apply('annual'));
})();

// ===== Sticky footer CTA on mobile (after 300px scroll, < 768px) =====
(function () {
  const sticky = document.getElementById('stickyCta');
  if (!sticky) return;

  const update = () => {
    const isMobile = window.innerWidth < 768;
    const show = isMobile && window.scrollY > 300;
    sticky.classList.toggle('is-visible', show);
    sticky.setAttribute('aria-hidden', String(!show));
    document.body.classList.toggle('sticky-active', show);
  };

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
})();



// ============ Rastreamento de Conversões — GA4 ============
document.addEventListener('DOMContentLoaded', function () {

  // Rastrear clique em qualquer botão de cadastro / CTA principal
  document.querySelectorAll('a[href*="register-church"]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (typeof gtag === 'function') {
        // Clique no CTA, não cadastro concluído: o cadastro acontece em app.portaldaigreja.com.br
        // e só pode ser medido lá. Não marque este evento como conversão de cadastro no GA4.
        gtag('event', 'cta_cadastro_click', {
          event_category: 'CTA',
          event_label: btn.textContent.trim(),
          page_path: location.pathname
        });
      }
    });
  });

  // Rastrear clique no botão do WhatsApp
  document.querySelectorAll('a[href*="wa.me"]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (typeof gtag === 'function') {
        gtag('event', 'whatsapp_click', {
          event_category: 'Contato',
          event_label: btn.getAttribute('aria-label') || btn.textContent.trim() || 'WhatsApp',
          page_path: location.pathname
        });
      }
    });
  });

  // Rastrear clique em "Entrar" (login)
  document.querySelectorAll('a[href*="login"]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (typeof gtag === 'function') {
        gtag('event', 'login_click', {
          event_category: 'Navegação',
          event_label: 'Botão Entrar',
          page_path: location.pathname
        });
      }
    });
  });

  // Rastrear scroll profundo (50% e 90% da página) — indica engajamento
  var scrollMilestones = { 50: false, 90: false };
  window.addEventListener('scroll', function () {
    var scrollPct = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
    [50, 90].forEach(function (milestone) {
      if (scrollPct >= milestone && !scrollMilestones[milestone]) {
        scrollMilestones[milestone] = true;
        if (typeof gtag === 'function') {
          gtag('event', 'scroll_depth', {
            event_category: 'Engajamento',
            event_label: milestone + '%'
          });
        }
      }
    });
  }, { passive: true });

});

// ============ Consentimento de cookies (LGPD) ============
// Sem aceite, nada de medição nem de chat: o Consent Mode já entra negado no
// <head> e só é liberado aqui. A escolha fica no navegador da pessoa
// (localStorage), por isso o banner não volta a cada página.
(function () {
  var KEY = 'consent:v1';
  var CHAT = 'https://alb.monitchat.com/widget/wgt_ltXBSBKMhad1VKpQtTPL5LOC8bv3.js';
  // O chat existe só nas páginas onde já existia antes: home (pt/en) e /whatsapp/.
  var CHAT_PAGES = ['/', '/en/', '/whatsapp/', '/index.html', '/en/index.html'];
  var pt = (document.documentElement.lang || 'pt').toLowerCase().indexOf('pt') === 0;

  var TXT = pt ? {
    text: 'Usamos cookies para entender como o site é usado e para o atendimento pelo chat. ' +
          'Você escolhe: nada é carregado antes do seu aceite.',
    accept: 'Aceitar', reject: 'Recusar', policy: 'Política de Privacidade',
    label: 'Aviso de cookies'
  } : {
    text: 'We use cookies to understand how this site is used and to run the support chat. ' +
          'It is your call: nothing loads before you accept.',
    accept: 'Accept', reject: 'Decline', policy: 'Privacy Policy',
    label: 'Cookie notice'
  };

  function read() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function save(value) {
    try { localStorage.setItem(KEY, value); } catch (e) { /* navegação privada */ }
  }

  function loadChat() {
    var path = location.pathname;
    if (CHAT_PAGES.indexOf(path) === -1) return;
    var s = document.createElement('script');
    s.async = true;
    s.src = CHAT;
    document.body.appendChild(s);
  }

  function grant() {
    if (typeof gtag === 'function') {
      gtag('consent', 'update', { analytics_storage: 'granted' });
    }
    loadChat();
  }

  function banner() {
    var box = document.createElement('div');
    box.className = 'cookie-bar';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', TXT.label);
    var p = document.createElement('p');
    p.textContent = TXT.text + ' ';
    var link = document.createElement('a');
    link.href = 'https://app.portaldaigreja.com.br/privacidade';
    link.textContent = TXT.policy;
    p.appendChild(link);
    var actions = document.createElement('div');
    actions.className = 'cookie-actions';
    var no = document.createElement('button');
    no.type = 'button';
    no.className = 'btn btn-ghost';
    no.textContent = TXT.reject;
    var yes = document.createElement('button');
    yes.type = 'button';
    yes.className = 'btn btn-primary';
    yes.textContent = TXT.accept;
    function close() {
      document.body.classList.remove('cookie-open');
      box.remove();
    }
    no.addEventListener('click', function () { save('denied'); close(); });
    yes.addEventListener('click', function () { save('granted'); grant(); close(); });
    actions.appendChild(no);
    actions.appendChild(yes);
    box.appendChild(p);
    box.appendChild(actions);
    document.body.appendChild(box);
    // Enquanto o aviso está aberto, some com o botão do WhatsApp e com a barra
    // fixa do celular: eles cobrem o botão "Aceitar" em telas pequenas.
    document.body.classList.add('cookie-open');
    yes.focus();
  }

  var choice = read();
  if (choice === 'granted') { grant(); } else if (choice !== 'denied') { banner(); }
})();
