---
name: frontend-slides
description: Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Activates when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch/workshop. Helps non-designers discover their aesthetic through visual exploration.
---

# Frontend Slides

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser.

## Trigger Conditions

Automatically activate this skill when:
- User wants to create a talk deck, pitch deck, workshop deck, or internal presentation
- User mentions converting `.ppt` or `.pptx` slides to HTML/web
- User wants to improve an existing HTML presentation's layout, motion, or typography
- User mentions "slides", "presentation", "deck", "PowerPoint", "keynote"

---

## Non-Negotiables

1. **Zero dependencies**: one self-contained HTML file with inline CSS and JS by default.
2. **Viewport fit is mandatory**: every slide must fit inside one viewport — no internal scrolling.
3. **Show, don't tell**: use visual previews instead of abstract style questionnaires.
4. **Distinctive design**: avoid generic purple-gradient, Inter-on-white, template-looking decks.
5. **Production quality**: code must be commented, accessible, responsive, and performant.

---

## Workflow

### 1. Detect Mode

Choose one path:
- **New presentation**: user has a topic, notes, or full draft
- **PPT conversion**: user has `.ppt` or `.pptx`
- **Enhancement**: user already has HTML slides and wants improvements

### 2. Discover Content

Ask only the minimum needed:
- **purpose**: pitch, teaching, conference talk, internal update
- **length**: short (5–10), medium (10–20), long (20+)
- **content state**: finished copy, rough notes, topic only

If the user has content, ask them to paste it before styling.

### 3. Discover Style

Default to visual exploration. If the user already knows the desired preset, skip previews.

Otherwise:
1. Ask what feeling the deck should create: *impressed, energized, focused, inspired*.
2. Generate **3 single-slide preview files** in `.ecc-design/slide-previews/`.
3. Each preview must be self-contained, show typography/color/motion clearly, and stay under ~100 lines of slide content.
4. Ask which preview to keep, or what elements to mix.

### 4. Build the Presentation

Output a single `presentation.html` (or `[name].html`). Use an `assets/` folder only when the deck contains extracted or user-supplied images.

Required structure:
- Semantic slide `<section>` elements
- CSS custom properties for all theme values
- A `PresentationController` class handling keyboard, wheel, and touch navigation
- Intersection Observer for reveal animations
- `prefers-reduced-motion` support

### 5. Enforce Viewport Fit — Hard Gate

```css
/* Every slide — no exceptions */
.slide {
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* All type and spacing scale with clamp() */
h1 { font-size: clamp(2rem, 5vw, 4rem); }
p  { font-size: clamp(0.9rem, 2vw, 1.25rem); }
```

Rules:
- When content does not fit → split into multiple slides
- Never solve overflow by shrinking text below readable sizes
- Never allow scrollbars inside a slide

### 6. Validate

Check the finished deck at:
- 1920×1080
- 1280×720
- 768×1024 (tablet portrait)
- 375×667 (mobile)
- 667×375 (mobile landscape)

If browser automation is available, verify no slide overflows and keyboard navigation works.

### 7. Deliver

- Delete temporary preview files unless the user wants to keep them
- Open the deck with the platform-appropriate opener:
  - macOS: `open file.html`
  - Linux: `xdg-open file.html`
  - Windows: `start "" file.html`
- Summarize: file path, preset used, slide count, and easy theme customization points

---

## PPT / PPTX Conversion

1. Prefer `python3` with `python-pptx` to extract text, images, and notes.
2. If `python-pptx` is unavailable, ask whether to install it or fall back to a manual workflow.
3. Preserve slide order, speaker notes, and extracted assets.
4. After extraction, run the same style-selection workflow as a new presentation.

Do not rely on macOS-only tools when Python can do the job.

---

## Implementation Requirements

### HTML / CSS

- Inline CSS and JS unless the user explicitly wants a multi-file project
- Fonts from Google Fonts or Fontshare
- Prefer atmospheric backgrounds, strong type hierarchy, and a clear visual direction
- Use abstract shapes, gradients, grids, noise, and geometry — not clipart or illustrations

### JavaScript — Required Controller

```javascript
class PresentationController {
  constructor() {
    this.slides = document.querySelectorAll('.slide')
    this.current = 0
    this.bindEvents()
    this.updateProgress()
  }

  go(index) {
    this.slides[this.current].classList.remove('active')
    this.current = Math.max(0, Math.min(index, this.slides.length - 1))
    this.slides[this.current].classList.add('active')
    this.updateProgress()
  }

  next() { this.go(this.current + 1) }
  prev() { this.go(this.current - 1) }

  bindEvents() {
    // Keyboard
    document.addEventListener('keydown', e => {
      if (['ArrowRight', 'ArrowDown', 'Space'].includes(e.code)) this.next()
      if (['ArrowLeft', 'ArrowUp'].includes(e.code)) this.prev()
    })

    // Mouse wheel (debounced)
    let wheelTimeout
    document.addEventListener('wheel', e => {
      clearTimeout(wheelTimeout)
      wheelTimeout = setTimeout(() => {
        e.deltaY > 0 ? this.next() : this.prev()
      }, 50)
    }, { passive: true })

    // Touch / swipe
    let touchStartY
    document.addEventListener('touchstart', e => { touchStartY = e.touches[0].clientY }, { passive: true })
    document.addEventListener('touchend', e => {
      const diff = touchStartY - e.changedTouches[0].clientY
      if (Math.abs(diff) > 50) diff > 0 ? this.next() : this.prev()
    })
  }

  updateProgress() {
    const el = document.getElementById('progress')
    if (el) el.textContent = `${this.current + 1} / ${this.slides.length}`
  }
}

// Reveal animations via Intersection Observer
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.querySelectorAll('[data-reveal]').forEach((el, i) => {
      setTimeout(() => el.classList.add('revealed'), i * 100)
    })
  })
}, { threshold: 0.5 })

document.querySelectorAll('.slide').forEach(s => observer.observe(s))

const deck = new PresentationController()
```

### Reduced Motion Support

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Content Density Limits

| Slide type   | Limit |
|--------------|-------|
| Title        | 1 heading + 1 subtitle + optional tagline |
| Content      | 1 heading + 4–6 bullets or 2 short paragraphs |
| Feature grid | 6 cards max |
| Code         | 8–10 lines max |
| Quote        | 1 quote + attribution |
| Image        | 1 image constrained by viewport |

---

## Style Preset Guide

Map the desired mood to a visual direction:

| Mood | Direction |
|------|-----------|
| Impressed | Dark background, high contrast, dramatic type scale, subtle geometry |
| Energized | Bold color blocks, kinetic layout, strong weight contrast |
| Focused | Minimal, monochrome or two-tone, generous white space |
| Inspired | Warm gradients, editorial type, soft texture or noise |

Avoid:
- Generic startup gradients with no visual identity
- System-font decks unless intentionally editorial
- Long bullet walls
- Code blocks that need internal scrolling
- Fixed-height boxes that break on short screens
- Invalid CSS like `-clamp(...)`

---

## Accessibility Checklist

- Semantic structure: `<main>`, `<section>`, `<nav>`
- Contrast ratio ≥ 4.5:1 for body text, 3:1 for large text
- Keyboard-only navigation works end-to-end
- `prefers-reduced-motion` respected
- `aria-label` on navigation controls

---

## Deliverable Checklist

- [ ] Presentation runs from a local file in a browser
- [ ] Every slide fits the viewport without scrolling
- [ ] Style is distinctive and intentional
- [ ] Animation is meaningful, not noisy
- [ ] Reduced motion is respected
- [ ] File paths and customization points explained at handoff
