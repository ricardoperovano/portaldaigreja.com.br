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
        gtag('event', 'conversion_cadastro', {
          event_category: 'CTA',
          event_label: btn.textContent.trim()
        });
        // Evento de conversão para Google Ads (adicionar tag de conversão do Ads depois)
        gtag('event', 'conversion', {
          send_to: 'AW-CONVERSION_ID/CONVERSION_LABEL' // substituir ao criar campanha no Google Ads
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
          event_label: 'WhatsApp Flutuante'
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
          event_label: 'Botão Entrar'
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
  });

});
