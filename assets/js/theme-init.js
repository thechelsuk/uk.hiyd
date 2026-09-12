// Apply a saved theme override before first paint, so there's no flash of
// the wrong theme. The footer toggle (assets/js/theme-toggle.js) is what
// writes this key. Loaded as a normal blocking <script src> (not
// defer/async) before the stylesheet, on purpose — see _includes/head.html.
(function () {
  try {
    var stored = localStorage.getItem("hiyd-theme");
    if (stored === "light" || stored === "dark") {
      document.documentElement.setAttribute("data-theme", stored);
    }
  } catch (e) {}
})();
