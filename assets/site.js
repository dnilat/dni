(() => {
  const root = document.documentElement;
  const body = document.body;
  const locale = body.dataset.locale === "en" ? "en" : "es";
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");
  const labels = {
    es: {
      light: "Claro",
      dark: "Oscuro",
      pause: "Pausar movimiento",
      play: "Activar movimiento"
    },
    en: {
      light: "Light",
      dark: "Dark",
      pause: "Pause motion",
      play: "Play motion"
    }
  };

  const themeToggle = document.querySelector(".theme-toggle");
  const themeLabel = document.querySelector("[data-theme-label]");
  const themeColor = document.querySelector('meta[name="theme-color"]');
  const motionToggle = document.querySelector(".motion-toggle");
  const motionLabel = document.querySelector("[data-motion-label]");
  const heroVideo = document.querySelector(".hero__video");
  const heroPoster = document.querySelector(".hero__poster");

  const getStoredTheme = () => {
    try {
      const saved = localStorage.getItem("dni-theme");
      return saved === "light" || saved === "dark" ? saved : null;
    } catch {
      return null;
    }
  };

  const setStoredTheme = (theme) => {
    try {
      localStorage.setItem("dni-theme", theme);
    } catch {
      // The visual preference still applies for this visit.
    }
  };

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    if (themeLabel) themeLabel.textContent = labels[locale][theme];
    if (themeToggle) themeToggle.setAttribute("aria-pressed", String(theme === "dark"));
    if (themeColor) themeColor.content = theme === "dark" ? "#09110c" : "#f2f0e8";
  };

  applyTheme(getStoredTheme() || (systemTheme.matches ? "dark" : "light"));

  themeToggle?.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    setStoredTheme(next);
    applyTheme(next);
  });

  const syncSystemTheme = (event) => {
    if (!getStoredTheme()) applyTheme(event.matches ? "dark" : "light");
  };
  systemTheme.addEventListener?.("change", syncSystemTheme);

  let videoLoaded = false;
  const canLoadVideo = () => {
    const saveData = navigator.connection?.saveData;
    return heroVideo?.dataset.videoReady === "true" && !prefersReducedMotion.matches && !saveData;
  };

  const loadHeroVideo = () => {
    if (!heroVideo || videoLoaded || !canLoadVideo()) return;
    heroVideo.querySelectorAll("source[data-src]").forEach((source) => {
      source.src = source.dataset.src;
    });
    heroVideo.load();
    videoLoaded = true;
    heroVideo.addEventListener("canplay", () => {
      heroVideo.classList.add("is-ready");
      heroPoster?.classList.add("is-video-ready");
      if (root.dataset.motion !== "paused") heroVideo.play().catch(() => {});
    }, { once: true });
  };

  const applyMotion = (paused) => {
    const motionLocked = prefersReducedMotion.matches;
    const effectivePaused = motionLocked || paused;
    root.dataset.motion = effectivePaused ? "paused" : "running";
    if (motionToggle) {
      motionToggle.hidden = motionLocked;
      motionToggle.disabled = motionLocked;
      motionToggle.setAttribute("aria-pressed", String(effectivePaused));
    }
    if (motionLabel) motionLabel.textContent = effectivePaused ? labels[locale].play : labels[locale].pause;
    if (!heroVideo) return;
    if (effectivePaused) {
      heroVideo.pause();
    } else {
      loadHeroVideo();
      if (videoLoaded) heroVideo.play().catch(() => {});
    }
  };

  applyMotion(prefersReducedMotion.matches);
  loadHeroVideo();
  motionToggle?.addEventListener("click", () => applyMotion(root.dataset.motion !== "paused"));
  prefersReducedMotion.addEventListener?.("change", (event) => applyMotion(event.matches));

})();
