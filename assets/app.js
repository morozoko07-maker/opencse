/* OpenCSE client-side behaviour: theme toggle + search. No dependencies. */
(function () {
  "use strict";

  var root = window.SITE_ROOT || "";
  var htmlEl = document.documentElement;

  /* ---- theme: light, charcoal, pitch-black OLED ---- */
  var themeBtns = document.querySelectorAll("[data-theme-set]");
  var themeMeta = document.querySelector('meta[name="theme-color"]');
  var THEME_COLOURS = { light: "#eeecea", dark: "#121212", midnight: "#000000" };

  function paintTheme() {
    var current = htmlEl.getAttribute("data-theme") || "dark";
    themeBtns.forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-theme-set") === current ? "true" : "false");
    });
    if (themeMeta) themeMeta.setAttribute("content", THEME_COLOURS[current] || "#1c1c1c");
  }
  paintTheme();
  themeBtns.forEach(function (b) {
    b.addEventListener("click", function () {
      var next = b.getAttribute("data-theme-set");
      htmlEl.setAttribute("data-theme", next);
      try { localStorage.setItem("opencse-theme", next); } catch (e) {}
      paintTheme();
    });
  });

  /* ---- search ---- */
  var input = document.getElementById("search");
  var box = document.getElementById("results");
  if (!input || !box) return;

  var index = null;
  var loading = false;
  var selected = -1;

  function load() {
    if (index || loading) return;
    loading = true;
    fetch(root + "search-index.json")
      .then(function (r) { return r.json(); })
      .then(function (data) { index = data; loading = false; run(); })
      .catch(function () { loading = false; });
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function snippet(text, terms) {
    var lower = text.toLowerCase();
    var at = -1;
    for (var i = 0; i < terms.length; i++) {
      var p = lower.indexOf(terms[i]);
      if (p !== -1) { at = p; break; }
    }
    if (at === -1) return "";
    var start = Math.max(0, at - 60);
    return (start > 0 ? "…" : "") + esc(text.slice(start, start + 160)) + "…";
  }

  function run() {
    var q = input.value.trim().toLowerCase();
    selected = -1;
    if (!q) { box.hidden = true; box.innerHTML = ""; return; }
    load();

    var terms = q.split(/\s+/).filter(Boolean);
    var hits = [];
    (index || []).forEach(function (item) {
      var hay = (item.t + " " + item.c + " " + (item.code || "") + " " + item.x).toLowerCase();
      var score = 0;
      var ok = true;
      terms.forEach(function (t) {
        var where = hay.indexOf(t);
        if (where === -1) { ok = false; return; }
        if (item.t.toLowerCase().indexOf(t) !== -1) score += 10;
        if (item.c.toLowerCase().indexOf(t) !== -1) score += 5;
      });
      if (!ok) return;
      hits.push({ item: item, score: score });
    });

    hits.sort(function (a, b) { return b.score - a.score; });
    hits = hits.slice(0, 12);

    if (!hits.length) {
      box.innerHTML = '<div class="empty">No matches for “' + esc(q) + '”.</div>';
      box.hidden = false;
      return;
    }

    box.innerHTML = hits.map(function (h) {
      var it = h.item;
      var meta = it.c + (it.code ? " · " + it.code : "");
      var sn = snippet(it.x, terms);
      return '<a href="' + root + it.u + '">' +
        '<div class="r-title">' + esc(it.t) + "</div>" +
        '<div class="r-meta">' + esc(meta) + (sn ? " — " + sn : "") + "</div></a>";
    }).join("");
    box.hidden = false;
  }

  input.addEventListener("input", run);
  input.addEventListener("focus", load);

  input.addEventListener("keydown", function (e) {
    var links = box.querySelectorAll("a");
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      if (!links.length) return;
      selected += e.key === "ArrowDown" ? 1 : -1;
      if (selected < 0) selected = links.length - 1;
      if (selected >= links.length) selected = 0;
      links.forEach(function (el, i) { el.classList.toggle("sel", i === selected); });
      links[selected].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter" && selected >= 0 && links[selected]) {
      window.location.href = links[selected].href;
    } else if (e.key === "Escape") {
      box.hidden = true;
      input.blur();
    }
  });

  document.addEventListener("click", function (e) {
    if (!box.contains(e.target) && e.target !== input) box.hidden = true;
  });

  document.addEventListener("keydown", function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      input.focus();
      input.select();
    }
  });
})();
