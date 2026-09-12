// Footer light/dark theme toggle. Pairs with assets/js/theme-init.js and the
// data-theme CSS rules in assets/css/main.css.
(function () {
  var STORAGE_KEY = "hiyd-theme";
  var btn = document.getElementById("theme-toggle");
  if (!btn) return;
  var mql = window.matchMedia("(prefers-color-scheme: dark)");

  function storedTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function currentTheme() {
    var stored = storedTheme();
    return stored === "light" || stored === "dark" ? stored : (mql.matches ? "dark" : "light");
  }

  function updateLabel() {
    var next = currentTheme() === "dark" ? "light" : "dark";
    btn.setAttribute("aria-label", "Switch to " + next + " theme");
  }

  // Keep the mobile browser-chrome colour (theme-color) matching an
  // explicit override — its `media` attribute only tracks the OS
  // preference, so once overridden both metas get the same colour.
  function updateThemeColorMeta(theme) {
    var color = theme === "dark" ? "#17130c" : "#f8f4e9";
    ["theme-color-light", "theme-color-dark"].forEach(function (id) {
      var meta = document.getElementById(id);
      if (meta) meta.setAttribute("content", color);
    });
  }

  btn.addEventListener("click", function () {
    var next = currentTheme() === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try {
      localStorage.setItem(STORAGE_KEY, next);
    } catch (e) {}
    updateLabel();
    updateThemeColorMeta(next);
  });

  updateLabel();
  if (storedTheme()) updateThemeColorMeta(storedTheme());
})();
