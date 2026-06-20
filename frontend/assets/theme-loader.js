(() => {
  const API_URL = "/api/site-theme";
  const FALLBACK_CSS = "assets/arsen-theme.css";
  const THEME_QUERY = "theme";
  const THEME_ASSET_VERSION = "member-selection-layout-v2";

  function themeLink() {
    return (
      document.querySelector('link[data-arsen-theme="active"]') ||
      Array.from(document.querySelectorAll('link[rel="stylesheet"]')).find((link) => {
        const href = link.getAttribute("href") || "";
        return href.includes("arsen-theme.css") || href.includes("assets/themes/");
      })
    );
  }

  function withCache(path, themeId, updatedAt) {
    const cacheKey = encodeURIComponent(`${themeId || "theme"}-${updatedAt || "local"}-${THEME_ASSET_VERSION}`);
    return `${path}${path.includes("?") ? "&" : "?"}v=${cacheKey}`;
  }

  function selectTheme(payload, requestedId) {
    const themes = Array.isArray(payload?.themes) ? payload.themes : [];
    if (requestedId) {
      const requested = themes.find((theme) => theme.id === requestedId && theme.enabled !== false);
      if (requested) return requested;
    }
    return payload?.active_theme || themes.find((theme) => theme.id === payload?.active_theme_id) || null;
  }

  function applyTheme(theme, updatedAt) {
    const link = themeLink();
    if (!link || !theme?.css_path) return null;
    link.dataset.arsenTheme = "active";
    link.dataset.arsenThemeId = theme.id || "";
    link.href = withCache(theme.css_path, theme.id, updatedAt);
    window.dispatchEvent(new CustomEvent("arsen-theme-loaded", { detail: { theme } }));
    return theme;
  }

  async function reloadTheme(explicitThemeId = "") {
    const requestedId = explicitThemeId || new URLSearchParams(window.location.search).get(THEME_QUERY) || "";
    try {
      const response = await fetch(API_URL, { cache: "no-store" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const payload = await response.json();
      const data = payload.data || payload;
      const theme = selectTheme(data, requestedId);
      return applyTheme(theme, data.updated_at);
    } catch (_) {
      const link = themeLink();
      if (link && !link.getAttribute("href")) link.href = FALLBACK_CSS;
      return null;
    }
  }

  window.ArsenTheme = {
    applyTheme,
    reloadTheme,
  };

  reloadTheme();
})();
