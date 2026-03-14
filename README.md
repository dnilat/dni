# dni.lat

Sitio estático bilingüe para Donde Nacen las Ideas.

## Estructura

- `/` contiene la versión en español.
- `/en/` contiene la versión en inglés.
- `/assets/` contiene estilos, scripts y favicon compartidos.

## Desarrollo local

Como es un sitio estático, basta con servir el directorio:

```bash
python3 -m http.server 4173
```

Luego abre `http://localhost:4173`.

## Deploy

El repositorio incluye un workflow de GitHub Actions para publicar el sitio en GitHub Pages y un archivo `CNAME` para `dni.lat`.
