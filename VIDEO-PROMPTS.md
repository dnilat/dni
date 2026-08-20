# Video de portada — prompts y entrega

La portada usa `assets/hero-poster.webp` como fallback estático del video. El video final es decorativo: nunca debe cargar texto, logos ni información necesaria para entender el sitio.

## Dirección recomendada — Jardín sintético

### Prompt maestro (16:9)

> A cinematic abstract landscape that feels like a living product studio, not a natural landscape and not a sci-fi interface. Deep forest-black environment made of layered translucent botanical membranes, soft velvety folds, fine luminous signal threads, and tiny precise points of pale green light responding to one warm amber pulse. The amber pulse represents a single human source; the many pale green responses feel coordinated, intelligent, curious, and calm. Slow lateral camera drift with a subtle forward push, macro-to-architectural scale ambiguity, tactile materials, soft volumetric light, rich shadow detail, premium art direction, restrained palette of near-black, chlorophyll green, warm off-white, and one amber accent. Leave clean low-contrast negative space across the left 48% and lower-left area for large white typography. Motion should be continuous and meditative: membranes breathe almost imperceptibly, signal threads travel in gentle waves, points of light answer asynchronously. Seamless 10-second loop with matching first and last frames. 24 fps, 4K, 16:9, no cuts, no camera shake, no audio.

### Negative prompt

> No text, no letters, no logo, no UI, no dashboard, no people, no faces, no humanoid robots, no literal computer chips, no circuit-board pattern, no neon cyberpunk, no blue or purple tech gradient, no glossy floating spheres, no rolling grassy hills, no moon imagery, no imitation of an existing studio website, no fast particles, no strobe, no sudden brightness, no shallow stock 3D look, no watermark.

### Prompt móvil (9:16)

> Recompose the same synthetic living studio as a vertical 9:16 shot. Keep the warm amber source in the upper-right third and the pale green responses traveling downward through layered organic membranes. Reserve the entire lower-left 55% as calm, dark, low-detail negative space for three lines of large white text and a short paragraph. Slow vertical parallax with a tiny forward camera push. Preserve the exact forest-black, chlorophyll, warm off-white, and amber palette. Seamless 10-second loop, matching first and last frames, 24 fps, 2160x3840, no cuts, no audio. Apply the same negative prompt.

## Alternativa A — Taller nocturno de ideas

> A monumental nocturnal workshop with no visible workers: matte dark-green drafting surfaces, suspended translucent sheets, paper prototypes, thin mechanical arms moving with quiet precision, and one warm desk lamp switching on a chain of pale green task lights. Everything feels handcrafted and computational at the same time. Slow dolly through the space, sparse composition, tactile paper and anodized metal, calm coordinated motion, left side kept dark and simple for typography. Seamless 10-second loop, 4K 16:9, 24 fps, no text, no logos, no humanoid robots, no cyberpunk, no blue-purple gradients, no audio.

## Alternativa B — Materia que aprende

> Extreme macro cinematic study of a dark green organic material learning a rhythm: soft fibers align, fold, and pass a warm amber impulse into many pale green micro-responses. The camera gradually reveals that the material is room-sized, with a calm architectural scale. Restrained, intelligent, tactile, slightly surreal, never biological horror. Left half remains quiet and dark for typography. Seamless 10-second loop, 4K 16:9, 24 fps, no text, no logos, no people, no floating spheres, no tech HUD, no blue-purple palette, no audio.

## Selección y exportación

- **Recomendación:** usar Jardín sintético como hero. Es el mejor puente entre la referencia inmersiva y una identidad propia para DNI.
- Duración: 8–12 segundos.
- Movimiento: una sola toma, sin cortes.
- Frame rate: 24 fps.
- Desktop: 3840×2160 o 1920×1080, 16:9.
- Móvil: 2160×3840 o 1080×1920, 9:16. La implementación actual usa el master 16:9 con `object-fit: cover`; el corte móvil dedicado puede añadirse después con `media` en los `<source>`.
- Sin audio.
- El primer y último frame deben coincidir para que el loop no se note.
- Evitar detalle importante en el lado izquierdo y la franja inferior, donde vive la interfaz.

## Archivos que espera el sitio

1. Los exports activos viven en:
   - `assets/media/dni-hero.webm`
   - `assets/media/dni-hero.mp4`
2. Ambas portadas mantienen `data-video-ready="true"` mientras existan los dos formatos.
3. `assets/hero-poster.webp` es el frame de ImageGen que coincide con el inicio del video y cubre carga, ahorro de datos y movimiento reducido.

### Conversión sugerida

```bash
ffmpeg -i master.mp4 -an -c:v libvpx-vp9 -crf 31 -b:v 0 -row-mt 1 -pix_fmt yuv420p assets/media/dni-hero.webm
ffmpeg -i master.mp4 -an -c:v libx264 -crf 24 -preset slow -pix_fmt yuv420p -movflags +faststart assets/media/dni-hero.mp4
```

Objetivo de peso: **menos de 8 MB por formato** en desktop. Verifica el loop, legibilidad del texto, poster y comportamiento con ahorro de datos y `prefers-reduced-motion` antes de publicar.
