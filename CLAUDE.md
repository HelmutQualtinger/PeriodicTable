# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Modernes Periodensystem** - A modern, interactive periodic table with dark/light theme support, detailed element information panel, and Wikipedia integration.

This is a **single-page application** with no build tools. The main file is `gemini_table.html` containing:
- HTML structure
- CSS styling (with theme variables)
- Vanilla JavaScript (ES6+)
- External API integration

## Architecture

### Core Components

1. **Periodic Grid** (CSS Grid Layout)
   - 18 columns × 10 rows for standard periodic table layout
   - Elements dynamically positioned based on `xpos` and `ypos` from API
   - Each element is an interactive card with hover effects

2. **Info Panel**
   - Positioned at grid-column 3/9, grid-row 1/4
   - Shows element details on hover (symbol, name, properties, electron config)
   - Includes 8 information fields in 2x4 grid
   - Smart hide/show logic: Panel stays visible when hovering from element to panel

3. **Theme System**
   - CSS custom properties (variables) for dark/light themes
   - Base theme: dark mode (default)
   - Light theme: `body.light-theme` class adds overrides
   - LocalStorage persistence: `localStorage.getItem/setItem('theme')`
   - Category colors adjust automatically per theme

4. **Element Data Flow**
   - Fetch from: `https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json`
   - Transform: English names → German translations (nameTranslations object)
   - Categorize: Category string → CSS class (getCategoryClass function)
   - Display: Create DOM elements dynamically in grid

### Key Data Structures

```javascript
// Element data from API
{
  number: 1,
  symbol: "H",
  name: "Hydrogen",
  xpos: 1, ypos: 1,
  atomic_mass: 1.008,
  density: 0.08988,
  melt: 13.81,
  boil: 20.28,
  electron_configuration: "1s¹",
  category: "diatomic nonmetal"
}

// Translations (English → German)
nameTranslations: {"Hydrogen": "Wasserstoff", ...}
categoryTranslations: {"diatomic nonmetal": "Nichtmetall", ...}
stateTranslations: {"Solid": "Fest", ...}
```

### Theme Variables

Dark theme (`:root`):
- `--bg-color`: #0f172a
- `--text-main`: #f8fafc
- `--text-muted`: #94a3b8
- 11 category colors (e.g., `--nonmetal`, `--noble-gas`)

Light theme (`body.light-theme`):
- `--bg-color`: #ffffff
- `--text-main`: #000000
- More saturated category colors for contrast

## Common Tasks

### Styling Changes
- **Element appearance**: Modify `.element` and `.cat-*` classes
- **Theme adjustment**: Edit `:root` (dark) or `body.light-theme` rules
- **Info panel layout**: Adjust `.info-panel`, `.info-grid`, `.info-item` dimensions
- **Responsive**: Adjust `grid-template-columns` (currently 18 × 80px), gap sizes

### Adding Features
- **New element property display**: Add `<div class="info-item">` in info-panel HTML, update `updateInfo()` function
- **New theme**: Add `body.new-theme` selectors for all modified properties
- **Category filtering**: Add button that toggles `.hidden` or similar on element categories

### Data Updates
- Element data loads from external API (no local cache)
- German translations are hardcoded in `nameTranslations` object
- To add new translations or update existing: edit the object directly

### Event Handling
- **Element hover**: `mouseenter` → calls `updateInfo()`, `mouseleave` → schedules panel hide
- **Element click**: Opens Wikipedia link in new tab
- **Panel hover**: `mouseenter` clears hide timer, `mouseleave` schedules hide
- **Theme toggle**: Toggles `light-theme` class, updates button text, persists to localStorage

## Key Implementation Details

### Hover Logic (Smart Panel Visibility)
```javascript
// Element mouseleave waits 150ms before hiding
// Then checks if mouse is over panel with :hover selector
if (!infoPanel.matches(':hover')) infoPanel.classList.remove('active');

// Panel mouseenter extends visibility
infoPanel.addEventListener('mouseenter', () => clearTimeout(hideTimeout));
```

### Category Classification
Categories are mapped from JSON category string to CSS class:
- `"alkali metal"` → `.cat-alkali-metal`
- `"transition metal"` → `.cat-transition-metal`
- Fallback: `.cat-unknown` for unrecognized categories

### Theme Persistence
- Default: Dark mode
- On load: Check `localStorage.getItem('theme')`
- On toggle: Save to localStorage, update button UI

## Files

- `gemini_table.html` - Single file with HTML, CSS, JavaScript (all-in-one)
- `README.md` - User documentation
- `CLAUDE.md` - This file

## Performance Considerations

- 118 elements created dynamically (no pre-rendering)
- Animations use CSS `transition` with `cubic-bezier()` easing
- Hover effects: `box-shadow` and `transform` (GPU-accelerated)
- No debouncing needed for hover events (threshold already 150ms)

## Browser Requirements

- ES6+ JavaScript support (arrow functions, template literals, modern DOM APIs)
- CSS Grid and Flexbox support
- CSS custom properties (CSS variables)
- Modern browsers (Chrome, Firefox, Safari, Edge)
