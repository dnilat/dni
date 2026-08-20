# dni.lat

Sitio estático bilingüe de Donde Nacen las Ideas.

## Rutas

- `/` — portada en español.
- `/en/` — portada en inglés.
- `/privacidad/` — política de privacidad en español.
- `/en/privacy/` — política de privacidad en inglés.
- `/assets/` — estilos, scripts, tipografía autoalojada, logos y póster del hero.

## Desarrollo local

```bash
python3 -m http.server 4173
```

Abre `http://localhost:4173`.

## Video del hero

El hero usa `assets/media/dni-hero.webm` con fallback H.264 en `assets/media/dni-hero.mp4`. `assets/hero-poster.webp` mantiene la composición completa antes de `canplay`, con ahorro de datos o con movimiento reducido.

Los prompts y parámetros de regeneración están en [`VIDEO-PROMPTS.md`](VIDEO-PROMPTS.md). El script no carga video cuando el navegador reporta ahorro de datos o `prefers-reduced-motion`.

## Privacidad

El sitio no integra analítica, píxeles publicitarios, formularios ni cookies de seguimiento. Solo guarda la preferencia `dni-theme` en `localStorage`. Si esto cambia, actualiza ambas políticas de privacidad antes de desplegar.

## Deploy

El workflow de GitHub Actions publica el contenido en GitHub Pages. `CNAME` configura `dni.lat`.
