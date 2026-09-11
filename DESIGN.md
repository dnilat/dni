---
version: alpha
name: Donde Nacen las Ideas
description: A cinematic Synthetic Idea Garden for calm, useful products made by two humans and many AI agents.
colors:
  primary: "#09110c"
  surface-paper: "#f2f0e8"
  surface-raised: "#faf9f4"
  text-ink: "#111611"
  text-muted: "#4a544b"
  divider: "#bdc4b9"
  surface-paper-dark: "#0c130f"
  surface-raised-dark: "#111b15"
  text-ink-dark: "#edf2e9"
  text-muted-dark: "#aeb9ad"
  divider-dark: "#344239"
  overlay-paper: "#f6f5ef"
  moss: "#346747"
  leaf: "#a6df91"
  amber-signal: "#f0a74e"
  contact-field: "#173521"
  factucat-surface: "#d8ceef"
  factucat-field: "#241b35"
  factucat-accent: "#c3a8ff"
  factucat-link: "#3a255b"
  factucat-ink: "#14131a"
  factucat-copy: "#edeaf8"
  libro-surface: "#ffb496"
  libro-field: "#5b281c"
  libro-link: "#6d2e1e"
  libro-stage-ink: "#26150f"
  book-paper: "#f7dfb8"
  book-ink: "#3a241b"
  contact-copy: "#edf5e9"
  rango-surface: "#e5eddf"
  rango-ink: "#243e40"
typography:
  hero-display:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "6rem"
    fontWeight: 650
    lineHeight: 0.86
    letterSpacing: "-0.04em"
  section-display:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "6rem"
    fontWeight: 420
    lineHeight: 0.94
    letterSpacing: "-0.04em"
  manifesto-headline:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "4.4rem"
    fontWeight: 310
    lineHeight: 1
    letterSpacing: "-0.035em"
  product-headline:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "4.8rem"
    fontWeight: 420
    lineHeight: 0.95
    letterSpacing: "-0.04em"
  contact-display:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "6rem"
    fontWeight: 260
    lineHeight: 1
    letterSpacing: "-0.04em"
  legal-heading:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "2.7rem"
    fontWeight: 480
    lineHeight: 1
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0em"
  nav-label:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 580
    letterSpacing: "0.08em"
  action-label:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "0.83rem"
    fontWeight: 650
    letterSpacing: "0.08em"
  motion-label:
    fontFamily: "Bricolage Grotesque, Arial Narrow, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 400
    letterSpacing: "0.045em"
spacing:
  gutter-desktop-max: "4.5rem"
  gutter-mobile: "1.15rem"
  section-major-max: "13rem"
rounded:
  none: "0px"
components:
  nav-item-overlay:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.overlay-paper}"
    typography: "{typography.nav-label}"
    rounded: "{rounded.none}"
    padding: "0px"
  theme-toggle-overlay:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.overlay-paper}"
    typography: "{typography.nav-label}"
    rounded: "{rounded.none}"
    padding: "0 0 0 1rem"
  motion-toggle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.overlay-paper}"
    typography: "{typography.motion-label}"
    rounded: "{rounded.none}"
    padding: "0px"
  line-link-paper:
    backgroundColor: "{colors.surface-paper}"
    textColor: "{colors.text-ink}"
    typography: "{typography.action-label}"
    rounded: "{rounded.none}"
    padding: "0px"
  line-link-light:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.overlay-paper}"
    typography: "{typography.action-label}"
    rounded: "{rounded.none}"
    padding: "0px"
  line-link-factucat:
    backgroundColor: "{colors.factucat-surface}"
    textColor: "{colors.factucat-link}"
    typography: "{typography.action-label}"
    rounded: "{rounded.none}"
    padding: "0px"
  line-link-libro:
    backgroundColor: "{colors.libro-surface}"
    textColor: "{colors.libro-link}"
    typography: "{typography.action-label}"
    rounded: "{rounded.none}"
    padding: "0px"
  ledger-row:
    backgroundColor: "{colors.surface-paper}"
    textColor: "{colors.text-ink}"
    rounded: "{rounded.none}"
    padding: "1.2rem 0 1.5rem"
  line-link-rango:
    backgroundColor: "{colors.rango-surface}"
    textColor: "{colors.rango-ink}"
    typography: "{typography.action-label}"
    rounded: "{rounded.none}"
    padding: "0px"
  factucat-message:
    backgroundColor: "{colors.factucat-field}"
    textColor: "{colors.factucat-copy}"
    rounded: "{rounded.none}"
    padding: "1.35rem"
  libro-book:
    backgroundColor: "{colors.book-paper}"
    textColor: "{colors.book-ink}"
    rounded: "{rounded.none}"
    padding: "clamp(1.5rem, 3vw, 2.7rem)"
  contact-callout:
    backgroundColor: "{colors.contact-field}"
    textColor: "{colors.contact-copy}"
    rounded: "{rounded.none}"
    padding: "clamp(7rem, 13vw, 12rem)"
---

# Design System: Donde Nacen las Ideas

## Overview

**Creative North Star: "Synthetic Idea Garden"**

The Synthetic Idea Garden treats DNI as a living field where Omar and Manny work alongside AI agents. The shared world is editorial and cinematic: a full-bleed forest scene opens the homepage, while warm paper and ruled type create long, calm reading stages for the studio, manifesto, products, team, contact, and legal copy.

Density stays low and composition stays asymmetric. Oversized narrow text, generous responsive gaps, square controls, hairline dividers, and three project-specific material worlds supply character without turning the site into a generic card grid. The system is bilingual and theme-aware, with motion enhancement subordinate to static legibility.

**Key Characteristics:**
- Forest-black cinematic fields beside warm editorial paper.
- One variable grotesque family stretched across display, body, label, and legal roles.
- Asymmetric two-column compositions that collapse to a single reading sequence.
- Square controls, hairline rules, and restrained depth.
- Project-specific lavender, peach, and sage stages inside the shared DNI frame.

**Scope boundary.** This document carbonizes the homepage and shared visual system implemented by `index.html`, `en/index.html`, both privacy pages, `assets/styles.css`, `assets/site.js`, the current poster, and the shipped font. It does not define the independent FactuCat or Libro Chiquito product design systems, invent form/modal/chip patterns that do not exist, or prescribe visual content for a future hero video beyond the integration behavior already present.

## Colors

The shared DNI palette moves between forest-black cinematic fields and warm paper editorial surfaces; brighter color is confined to a green signal language and the named project stages.

### Primary
- **Forest Black** (`colors.primary`): fixed hero, manifesto, and footer field; also the homepage theme color.
- **Moss** (`colors.moss`): restrained green emphasis for links, the scrollbar, and human/agent emphasis on light paper.
- **Leaf Signal** (`colors.leaf`): luminous hero phrase, motion indicator, selection field, and dark-theme emphasis.
- **Contact Field** (`colors.contact-field`): a distinct deep-green closing stage rather than another paper section.

### Secondary
- **FactuCat Lavender Surface** (`colors.factucat-surface`): the FactuCat copy half.
- **FactuCat Violet Field** (`colors.factucat-field`): the dark demonstration half and message surfaces.
- **FactuCat Signal Lilac** (`colors.factucat-accent`): labels, borders, dots, and the demo gradient; it remains inside the FactuCat stage.
- **FactuCat Ink and Link** (`colors.factucat-ink`, `colors.factucat-link`, `colors.factucat-copy`): stage-local text roles.

### Tertiary
- **Libro Peach Surface** (`colors.libro-surface`): the Libro Chiquito copy half.
- **Libro Brown Field** (`colors.libro-field`): the illustrated book stage.
- **Book Paper and Ink** (`colors.book-paper`, `colors.book-ink`): the physical book artifact.
- **Rango Sage and Ink** (`colors.rango-surface`, `colors.rango-ink`): a calm copy panel beside Rango's official café image; these colors come from the live Rango site.
- **Amber Human Signal** (`colors.amber-signal`): the single warm pulse in the hero poster; it is not a general interface accent.

### Neutral
- **Warm Paper Set** (`colors.surface-paper`, `colors.surface-raised`, `colors.text-ink`, `colors.text-muted`, `colors.divider`): default light surfaces, text, and rules.
- **Night Paper Set** (`colors.surface-paper-dark`, `colors.surface-raised-dark`, `colors.text-ink-dark`, `colors.text-muted-dark`, `colors.divider-dark`): the same semantic roles after the dark theme override.
- **Overlay Paper** (`colors.overlay-paper`): fixed near-white foreground for the cinematic hero and focus outline.

**The Controlled Field Rule.** Forest black, warm paper, and green carry DNI; lavender, peach, and sage belong to the project worlds, and amber remains a signal inside the hero asset.

## Typography

**Display Font:** Bricolage Grotesque (with Arial Narrow and sans-serif fallbacks)
**Body Font:** Bricolage Grotesque (with Arial Narrow and sans-serif fallbacks)

**Character:** One locally hosted variable grotesque carries every role. Its width axis, unusually broad weight range, tight display leading, and restrained uppercase labels create an editorial voice without introducing a second type family.

### Hierarchy
- **Hero Display** (`typography.hero-display`): the three-line first-viewport statement; it uses `font-stretch: 80%`, with the green middle line reduced to weight 300 and the final line reduced to `0.78em` (`0.62em` below the mobile breakpoint).
- **Section Display** (`typography.section-display`): studio, product intro, team, contact, manifesto, and legal-page titles; it uses `font-stretch: 82%`.
- **Manifesto Headline** (`typography.manifesto-headline`): large, light statements in the ruled manifesto rows; it also uses `font-stretch: 82%`.
- **Product Headline** (`typography.product-headline`): each product's stage headline; the line length is constrained to roughly 12–14 characters of display measure.
- **Contact Display** (`typography.contact-display`): the oversized, underlined email address; it uses the lightest recurring display weight and `font-stretch: 82%`.
- **Legal Heading** (`typography.legal-heading`): privacy-section titles in a tighter editorial reading scale.
- **Body** (`typography.body`): all explanatory copy. Implemented measures generally sit between 47ch and 58ch, with the hero introduction at 48ch.
- **Labels and Actions** (`typography.nav-label`, `typography.action-label`, `typography.motion-label`): compact uppercase navigation/actions and the quieter mixed-case motion control.

**The One-Family Rule.** Bricolage Grotesque carries display, body, labels, and legal copy; hierarchy comes from width, weight, size, case, and spacing rather than a second family.

## Layout

The main `.section-shell` is centered at a maximum width of `91rem`; its fluid gutter tops out at `spacing.gutter-desktop-max`, and below `42rem` it becomes `spacing.gutter-mobile`. Major sections use fluid block spacing up to `spacing.section-major-max` instead of a dense stack of small cards.

The homepage hero fills at least the viewport (`100svh`) and never drops below `45rem`; on small screens its minimum is `43rem`. The desktop header is a three-column overlay, hero copy is anchored low-left, the compact fact ledger is low-right, and the motion control sits at the bottom edge. At `68rem`, the header becomes two columns with primary navigation on a ruled second row, hero facts disappear, and the hero copy remains the dominant reading path.

Core editorial compositions use asymmetric two-column grids: studio statement plus ledger, manifesto/product introductions, team heading plus body, and a `.92fr / 1.08fr` product-stage split. At `68rem`, these become one column. Product stages begin at a `48rem` minimum height on desktop; on screens below `42rem`, they extend edge-to-edge by canceling the page gutter, place copy before illustration, and use explicit compact stage heights.

Legal pages reuse the same header, type, theme, and footer but replace the cinematic overlay with a ruled paper header. Their content uses a narrow sticky summary beside the legal copy; the summary becomes static and the layout becomes one column below `68rem`. The footer uses three columns on wide screens, two below `68rem`, and one below `42rem`.

## Elevation & Depth

The system is flat by default. Depth comes first from hard tonal changes, full-bleed fields, hairline rules, the hero's layered shade, and product-specific illustration—not generic floating cards. The implemented shadow vocabulary is deliberately limited:

### Shadow Vocabulary
- **Keyboard Focus Halo** (`0 0 0 5px #173521`): paired with a two-pixel near-white outline so focus remains visible across light, dark, and colored fields.
- **Hero Signal Shadow** (`0 6px 18px rgb(4 12 7 / .45)`): a small atmospheric lift under synthetic signal squares.
- **Book Cover Lift** (`0 28px 65px rgb(34 12 7 / .44)`): reserved for the rotated physical-book artifact; its separate blurred backing shape deepens the effect.

**The Flat-by-Default Rule.** Editorial surfaces remain flat and square; shadows are reserved for the hero signal, keyboard focus halo, and the physical book artifact.

## Shapes

Interface geometry is square and ruled: header dividers, navigation underlines, action links, product stages, demo messages, ledger rows, legal sections, and controls use straight edges without a shared corner radius. One-pixel borders and underlines carry structure.

Organic shapes belong to imagery and illustration. The hero poster uses layered membranes, arcs, grain, and small square/circular signals. The Libro Chiquito artifact introduces a rotated rectangular cover and one irregular oval mark; these forms are signatures of their specific visual worlds, not a license to round the shared interface.

## Components

### Navigation
- The overlay header uses near-white text over the hero; legal pages use the current paper/ink theme and a solid divider.
- Primary and language links use `typography.nav-label`, a minimum interactive height of `2.75rem`, and a one-pixel underline that grows leftward on hover, keyboard focus, or the current language.
- Below `68rem`, primary navigation occupies a full-width second row. Below `42rem`, the long brand name disappears while the DNI mark remains.

### Theme and Motion Controls
- The theme control is transparent, square, and separated by a one-pixel left rule. It follows the saved `dni-theme` preference; when no preference is saved, it tracks the system scheme. Its `aria-pressed` state and localized label stay synchronized.
- The motion control pairs a small green square with localized copy. It pauses the video and CSS motion; under `prefers-reduced-motion`, it is hidden, disabled, and locked to the paused state.
- Smooth scrolling is removed and animation/transition duration is effectively eliminated under reduced motion.

### Ruled Action Links
- The shared action is an inline text link, not a filled button. It uses `typography.action-label`, a `3rem` minimum height, a one-pixel bottom rule, and a square-stroked arrow.
- Hover and focus expand the text-to-arrow gap from `1rem` to `1.5rem` over the shared ease-out curve. Light and product-colored variants change only foreground color.

### Team Ledger
- The ledger is a definition list built from full-width ruled rows. Each row has an uppercase role label above a two-column definition; below `42rem`, the definition becomes one column.
- Text hierarchy, not a container fill or shadow, separates the person/system name from its explanation.

### Product Stages
- Product stages are material sections, not reusable marketing cards. FactuCat pairs a lavender copy surface with a deep-violet translation diagram; Libro Chiquito pairs a peach copy surface with an angled, shadowed book on a brown geometric field.
- Rango extends the same split stage with sage copy and a self-hosted image from its official site. Its unchanged official icon accompanies the name in DNI typography; no replacement wordmark is drawn. Copy precedes imagery at the existing breakpoint. The photo panel has a 32rem minimum height and uses `object-fit: cover`.
- Each stage preserves the supplied product logo, a large narrow headline, a short body measure, and the shared ruled action link. On mobile the copy and illustration become consecutive full-width panels.

### FactuCat Translation Diagram
- Message panels are square, translucent violet rectangles with one-pixel borders. The agent panel aligns to the opposite edge and strengthens its lilac border.
- Four small lilac squares animate along the translation path with staggered delays. They stop with the site's reduced-motion and manual pause behavior.

### Libro Chiquito Book Artifact
- The book is a `3 / 4` cover rotated four degrees, centered over angular brown fields, with a large reserved shadow. Uppercase microcopy, a narrow title, and the irregular oval provide the cover hierarchy.

### Contact and Legal Content
- Contact is a deep-green full-width field with an oversized underlined email address; there is no contact form.
- Legal content is a paper editorial layout with a sticky responsible-party summary, a constrained copy column, and one-pixel section dividers. It uses the same theme toggle, typography, focus treatment, and footer as the homepage.

### Accessibility, Assets, and Video
- A skip link appears on focus. Semantic landmarks, heading relationships, labelled navigation/controls, localized `aria` text, and visible global `:focus-visible` treatment are part of the component contract.
- Interactive header controls use at least `2.75rem` minimum height; action links use at least `3rem`. The document maintains a `20rem` minimum viewport width.
- Product logos remain real image assets with meaningful `alt` text. The hero media wrapper is decorative (`aria-hidden`), and the duplicate poster image uses empty alternative text.
- The locally hosted Bricolage Grotesque WOFF2 file is preloaded and uses `font-display: swap`.
- The ImageGen WebP poster is the complete, legible default. WebM and H.264 sources are deferred and load only when the video is explicitly marked ready, reduced motion is off, and data saver is off. The video fades over the poster only after `canplay`; the current shipped markup uses `data-video-ready="true"` because both optimized formats are present.

## Do's and Don'ts

### Do:
- **Do** keep the shared DNI world anchored in forest black, warm paper, green signals, oversized narrow type, and hairline rules.
- **Do** keep FactuCat lavender/violet and Libro Chiquito peach/brown inside their respective product stages.
- **Do** preserve the `68rem` and `42rem` layout changes, especially the single-column reading order and edge-to-edge mobile product panels.
- **Do** preserve the poster-first hero, the explicit video-readiness gate, the data-saver check, and reduced-motion behavior.
- **Do** use the supplied product logos and the local variable font without redrawing or substituting them.
- **Do** keep keyboard focus, the skip link, semantic labels, localized control text, and visible motion/theme state when extending existing components.

### Don't:
- **Don't** replace the editorial stages with a generic corporate hero, feature-card grid, or a dense dashboard vocabulary.
- **Don't** promote amber or either product palette into a general-purpose DNI accent system.
- **Don't** add routine rounded containers, pills, gradients, or shadows to the square, ruled shared interface.
- **Don't** make video, animation, or decorative illustration necessary to understand content or operate a control.
- **Don't** invent inputs, modals, chips, testimonials, metrics, or a generalized card library from this implementation.
- **Don't** treat the FactuCat and Libro Chiquito stage treatments as definitions of those products' independent design systems.
