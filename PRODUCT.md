# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

The primary audience is people discovering Donde Nacen las Ideas (DNI) and its projects for the first time. Their immediate job is to understand what kind of company DNI is, then discover FactuCat, Libro Chiquito, and Rango without wading through corporate theater.

## Product Purpose

DNI is the corporate home for a small product company. The website should make the company's point of view legible, introduce its three public projects, and provide a simple path to learn more or make contact.

Success means a first-time visitor can quickly explain DNI in plain language and identify all three public projects.

## Positioning

DNI builds useful products for real people with a deliberately unusual team: Omar and Manny are the humans leading the studio, alongside AI agents. Omar retains the final decision. The company favors a few carefully made products over growth theater, bloated platforms, or software that gets in the user's way.

## Capabilities and Constraints

- Static, bilingual Spanish/English website deployed through GitHub Pages at `dni.lat`.
- Preserve light and dark color schemes, keyboard accessibility, reduced-motion support, semantic HTML, and responsive layouts.
- The three public projects are FactuCat (`https://factucat.com/`), Libro Chiquito (`https://librochiquito.com/`), and Rango (`https://rangosalud.com`).
- Rango coordinates medically guided weight-management care, delivery of prescribed medication, and support between appointments through allied doctors and providers. Do not add outcome guarantees, clinical credentials, prices, or specific affiliation claims.
- The site has no account system, contact form, analytics, or first-party cookies in the current implementation; do not imply data collection that does not exist.
- The requested hero supports a user-supplied background video. The implementation must remain complete and legible before that video is delivered, with a poster/fallback and reduced-data/reduced-motion behavior.
- Legal entity: Donde Nacen las Ideas SA de CV. Public business address: AVENIDA GUADALUPE 4872, int 101, Col. JARDINES DE GUADALUPE, Zapopan, Jalisco, C.P. 45030.

## Brand Commitments

- Name: Donde Nacen las Ideas (DNI).
- Core promise: products for humans.
- Voice: calm, candid, playful, colloquial Mexican Spanish; elegant without stiffness; confident without startup hype.
- Company truth: Omar and Manny are the humans leading DNI alongside AI agents. Use only their first names; do not invent titles or responsibilities for Manny.
- Visual direction explicitly requested by the founder: an original, cinematic, motion-led experience informed by the immersive pacing and full-bleed 3D/video atmosphere of RabenRifaie, without copying its proprietary layouts or assets.
- Palette commitment from repository guidance: almost-black, almost-white, and green.
- Existing brand assets: approved DNI artwork under `assets/brand/`, `assets/factucat-logo.svg`, `assets/libro-chiquito-logo.svg`, and the official `assets/rango-icon.svg`. Rango asset provenance is recorded in `README.md`.

## Evidence on Hand

- Current Spanish and English company copy in `index.html` and `en/index.html`.
- Product logos under `assets/`.
- Current live project pages at `factucat.com`, `librochiquito.com`, and `rangosalud.com`.
- Public legal identity and address are published in FactuCat's privacy policy.
- No testimonials, client logos, performance claims, case studies, or company metrics are available; future work must not fabricate them.

## Product Principles

1. Make the company understandable before asking for attention or action.
2. Show a small number of real products with enough specificity to be useful.
3. Let personality come from clear language, product truth, and crafted interaction—not hype.
4. Keep the experience humane: fast, legible, accessible, and calm even when visually ambitious.
5. Treat privacy as a product quality; collect nothing on the corporate site unless a future feature genuinely requires it.

## Accessibility & Inclusion

The site must remain usable with keyboard navigation, visible focus, semantic landmarks, sufficient contrast, responsive text, and `prefers-reduced-motion`. Decorative video must never be required to understand or operate the page.
