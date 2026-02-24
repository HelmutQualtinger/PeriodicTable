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
   - Element tiles: 60×60px (compact), gap 6px
   - Elements dynamically positioned based on `xpos` and `ypos` from API
   - Each element is an interactive card with category-colored hover effects
   - Wikipedia icon appears on hover, click to open German Wikipedia page

2. **Info Panel** (Ultra-Compact 4-Column Layout)
   - **Position:** grid-column 3/13, grid-row 1/4 (between Beryllium and Boron)
   - **Layout:** 4 columns × 2 rows = 8 fields
   - **Fields displayed:**
     - Row 1: Zustand | Dichte | Schmelzpunkt | Siedepunkt
     - Row 2: P/N | Kategorie | A-Gewicht | E-Config
   - **Smart Hover Logic:** 150ms delay + `:hover` check prevents panel hide during transition
   - **Responsive:** Stays visible when hovering from element to panel

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
- **Element appearance**: Modify `.element` (currently 60×60px) and `.cat-*` category classes
  - Font sizes: `.el-symbol` (0.95rem), `.el-name` (0.45rem), `.el-number` (0.55rem)
  - Adjust `grid-template-columns: repeat(18, 60px)` for different element sizes
- **Info panel sizing**: Edit `.info-grid` (currently `grid-template-columns: 1fr 1fr 1fr 1fr`)
  - Item sizes: `.info-label` (0.4rem), `.info-value` (0.5rem)
  - Panel dimensions: grid-column 3/13, grid-row 1/4, padding 0.8rem
- **Theme colors**: Edit `:root` (dark) or `body.light-theme` CSS variables
- **Hover effects**: Category-specific glows in `.cat-*:hover` rules

### Adding Features
- **New info field**: Add `<div class="info-item">` to `.info-grid` in HTML
  - Update `updateInfo()` JavaScript function to set value: `document.getElementById('id').textContent = ...`
  - Adjust `.info-grid` column count if adding more than 8 fields
- **Element click behavior**: Modify `elDiv.addEventListener('click', ...)`
- **New theme**: Add `body.new-theme { --bg-color: ..., --text-main: ..., etc }` rules
- **Category filtering**: Add button with `addEventListener('click', () => { document.querySelectorAll('.cat-NAME').forEach(...) })`

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

- **118 elements** created dynamically on page load (no pre-rendering)
- **Compact layout:** 60×60px elements + 6px gap fit entire periodic table on most screens
- **Smooth animations:** CSS `transition` with `cubic-bezier(0.4, 0, 0.2, 1)` easing
- **Hover effects:** Category-colored glows (`box-shadow`) and scale transforms (GPU-accelerated)
- **Smart timeouts:** 150ms delay on element mouseleave prevents flickering during panel hover
- **LocalStorage:** Theme preference saved to avoid recalculation
- **No dependencies:** Vanilla JavaScript = fast load, no bundle overhead
- **API caching:** Browser caches JSON fetch within session

## Browser Requirements

- ES6+ JavaScript support (arrow functions, template literals, modern DOM APIs)
- CSS Grid and Flexbox support
- CSS custom properties (CSS variables)
- Modern browsers (Chrome, Firefox, Safari, Edge)
