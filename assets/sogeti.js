/* Sogeti HTML artifact helpers — vanilla, dependency-free, ~5KB. */
(function () {
  "use strict";

  var Sogeti = {};

  Sogeti.qs = function (sel, root) { return (root || document).querySelector(sel); };
  Sogeti.qsa = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  Sogeti.toast = function (message) {
    var el = Sogeti.qs("#sogeti-toast");
    if (!el) {
      el = document.createElement("div");
      el.id = "sogeti-toast";
      el.className = "toast";
      el.setAttribute("role", "status");
      el.setAttribute("aria-live", "polite");
      document.body.appendChild(el);
    }
    el.textContent = message;
    el.classList.add("is-on");
    clearTimeout(el._timer);
    el._timer = setTimeout(function () { el.classList.remove("is-on"); }, 2400);
  };

  Sogeti.copy = function (text, message) {
    var done = function () { Sogeti.toast(message || "Copied to clipboard"); };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done).catch(function () { Sogeti.fallbackCopy(text, done); });
    } else {
      Sogeti.fallbackCopy(text, done);
    }
  };

  Sogeti.fallbackCopy = function (text, done) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); done(); } catch (e) { Sogeti.toast("Copy failed — select the text manually"); }
    document.body.removeChild(ta);
  };

  Sogeti.markdownList = function (items) {
    return items.filter(Boolean).map(function (s) { return "- " + s; }).join("\n");
  };

  Sogeti.initNav = function () {
    var toggle = Sogeti.qs("[data-nav-toggle]");
    var nav = Sogeti.qs("#site-nav");
    if (!toggle || !nav) return;
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  };

  Sogeti.initTabs = function () {
    Sogeti.qsa("[data-tabs]").forEach(function (group) {
      var tabs = Sogeti.qsa("[role=tab]", group);
      tabs.forEach(function (tab, i) {
        tab.addEventListener("click", function () { activate(i); });
        tab.addEventListener("keydown", function (e) {
          var next = null;
          if (e.key === "ArrowRight") next = (i + 1) % tabs.length;
          if (e.key === "ArrowLeft") next = (i - 1 + tabs.length) % tabs.length;
          if (e.key === "Home") next = 0;
          if (e.key === "End") next = tabs.length - 1;
          if (next !== null) { e.preventDefault(); activate(next); tabs[next].focus(); }
        });
      });
      function activate(index) {
        tabs.forEach(function (tab, j) {
          var panel = document.getElementById(tab.getAttribute("aria-controls"));
          var on = j === index;
          tab.setAttribute("aria-selected", on ? "true" : "false");
          tab.tabIndex = on ? 0 : -1;
          if (panel) panel.hidden = !on;
        });
      }
    });
  };

  Sogeti.initCopyButtons = function () {
    Sogeti.qsa("[data-copy]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var target = btn.getAttribute("data-copy");
        var text = target ? (Sogeti.qs(target) ? Sogeti.qs(target).innerText : "") : btn.getAttribute("data-copy-text") || "";
        Sogeti.copy(text.trim(), btn.getAttribute("data-copy-message") || "Copied to clipboard");
      });
    });
  };

  Sogeti.initYear = function () {
    Sogeti.qsa("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
  };

  Sogeti.initAnchors = function () {
    Sogeti.qsa('.site-nav a[href^="#"], .site-foot a[href^="#"]').forEach(function (a) {
      var id = a.getAttribute("href");
      if (id && id.length > 1 && !document.querySelector(id)) a.hidden = true;
    });
  };

  Sogeti.initPrint = function () {
    Sogeti.qsa("[data-print]").forEach(function (btn) {
      btn.addEventListener("click", function () { window.print(); });
    });
  };

  Sogeti.clamp = function (n, min, max) { return Math.max(min, Math.min(max, n)); };

  Sogeti.init = function () {
    Sogeti.initNav();
    Sogeti.initTabs();
    Sogeti.initCopyButtons();
    Sogeti.initYear();
    Sogeti.initPrint();
    Sogeti.initAnchors();
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", Sogeti.init);
  else Sogeti.init();

  window.Sogeti = Sogeti;
})();
