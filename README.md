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

## Identidad del estudio

La cabecera usa el logo indie aprobado completo, sin volver a escribir su nombre al lado. `assets/brand/originals/` conserva los PNG e ICO originales sin modificar. `dni-indie-v1.png` solo recorta el margen completamente transparente; CSS lo convierte exactamente a blanco sobre el hero y en tema oscuro, conservando su alfa y geometría. En fondos claros conserva el ciruela `#35243D`.

Las cuatro rutas declaran el ICO aprobado, un PNG de 32 px, su variante blanca para pestañas oscuras y un touch icon de 180 px. `/favicon.ico` sirve los mismos bytes aprobados como fallback. Los nombres `v1` y la versión de la hoja de estilos evitan reutilizar la identidad anterior desde caché; incrementarlos si cambia el arte.

Para regenerar derivados desde los originales del repositorio (Python con Pillow):

```bash
python3 scripts/prepare-branding.py
python3 -m unittest discover -s tests -v
node --check assets/site.js
git diff --check
```

La prueba visual debe cubrir portadas y privacidad en ES/EN, temas claro/oscuro, 320–1440 px, teclado, persistencia del tema, video y movimiento reducido. No hay bundler: Pages publica directamente el sitio estático.

## Deploy

El workflow de GitHub Actions publica el contenido en GitHub Pages. `CNAME` configura `dni.lat`.
