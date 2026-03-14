(() => {
  const root = document.documentElement;
  const toggle = document.querySelector(".theme-toggle");
  const themeLabel = document.querySelector("[data-theme-label]");
  const themeColorMeta = document.querySelector('meta[name="theme-color"]');
  const locale = document.body.dataset.locale || "es";
  const labels = {
    es: { light: "Claro", dark: "Oscuro" },
    en: { light: "Light", dark: "Dark" }
  };

  const getPreferredTheme = () => {
    const storedTheme = localStorage.getItem("dni-theme");
    if (storedTheme === "light" || storedTheme === "dark") {
      return storedTheme;
    }

    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  };

  const updateThemeUi = (theme) => {
    if (!toggle || !themeLabel) {
      return;
    }

    themeLabel.textContent = labels[locale][theme];
    toggle.setAttribute("aria-pressed", String(theme === "dark"));
  };

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    if (themeColorMeta) {
      themeColorMeta.setAttribute("content", theme === "dark" ? "#131917" : "#f6f4ef");
    }
    updateThemeUi(theme);
  };

  const initialTheme = getPreferredTheme();
  applyTheme(initialTheme);

  if (toggle) {
    toggle.addEventListener("click", () => {
      const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
      localStorage.setItem("dni-theme", nextTheme);
      applyTheme(nextTheme);
    });
  }

  const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
  const handleSystemThemeChange = (event) => {
    if (localStorage.getItem("dni-theme")) {
      return;
    }

    applyTheme(event.matches ? "dark" : "light");
  };

  if (typeof mediaQuery.addEventListener === "function") {
    mediaQuery.addEventListener("change", handleSystemThemeChange);
  } else if (typeof mediaQuery.addListener === "function") {
    mediaQuery.addListener(handleSystemThemeChange);
  }

  const revealItems = document.querySelectorAll(".reveal");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (reducedMotion) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.18, rootMargin: "0px 0px -8% 0px" }
  );

  revealItems.forEach((item) => observer.observe(item));
})();
