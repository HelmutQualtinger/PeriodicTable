# 🧪 Modernes Periodensystem - Interactive Periodic Table

Ein interaktives, modernes Periodensystem mit Dunkelmodus/Hellmodus, detailliertem Info-Panel und Wikipedia-Integration.

## ✨ Features

### 🎨 Design & Styling
- **Dark/Light Theme** - Umschalten zwischen Dunkelmodus (Standard) und Hellmodus mit hohem Kontrast
- **Modernes UI** - Glasmorphismus-Effekte, sanfte Übergänge und responsive Hover-Effekte
- **Farbcodierung** - 11 verschiedene Elementkategorien mit visuellen Unterscheidungen:
  - Alkalimetalle, Erdalkalimetalle, Übergangsmetalle
  - Nichtmetalle, Edelgase, Halogene
  - Halbmetalle, Lanthanide, Actinide
  - Post-Übergansmetalle, Unbekannte Elemente

### 📊 Interaktives Info-Panel
Beim Hovern über ein Element erscheint ein kompaktes Info-Panel mit:
- **Symbol & Name** - Großes Elementsymbol mit deutschem Namen
- **Physikalische Eigenschaften**:
  - Aggregatzustand (Fest, Flüssig, Gasförmig)
  - Dichte (g/cm³)
  - Schmelz- und Siedepunkte (K)
  - Protonen/Neutronen
  - Kategorie
- **Elektronenkonfiguration** - Gekürzte Darstellung
- **Standardatomgewicht** - Atomare Masseneinheiten (u)

### 🔗 Wikipedia Integration
- **📖 Wikipedia-Link** - Klick auf jedes Element öffnet die deutsche Wikipedia-Seite
- **Direkt im Element** - Wikipedia-Icon erscheint beim Hovern auf Element
- **Neue Registerkarte** - Wikipedia öffnet in neuem Tab, Periodensystem bleibt erhalten

### 🌍 Deutsche Sprache
- Alle Elementnamen auf Deutsch
- Deutsche Labels im Info-Panel
- Deutsche Kategorienamen in der Legende

### 📱 Legend
Visual legend mit Farbcodes für alle Elementkategorien - hilft beim schnellen Verständnis der Elementtypen

## 🎯 Verwendung

### Theme wechseln
- Klick auf den Button oben rechts (🌙 Dark / ☀️ Light)
- Die Einstellung wird im Browser gespeichert

### Element-Informationen anzeigen
1. Fahre mit der Maus über ein Element
2. Info-Panel erscheint mit allen Details
3. Bleibe über dem Panel, um es zu lesen

### Zu Wikipedia gehen
1. Fahre über ein Element (📖 Icon erscheint)
2. Klick auf das Element
3. Wikipedia-Seite öffnet sich in neuem Tab

## 🛠️ Technologie-Stack

- **HTML5** - Semantische Struktur
- **CSS3** - Modern Layout (Grid, Flexbox), Glasmorphismus, Gradients
- **JavaScript (Vanilla)** - Keine Dependencies erforderlich
- **API-Integration** - [Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON)

## 💾 Daten

Das Projekt lädt alle 118 Elemente live von einer externen JSON-API:
- Elementsymbole, Namen, Nummern
- Atomare Massen
- Dichte, Schmelz-/Siedepunkte
- Elektronenkonfiguration
- Kategorie-Informationen

## 🎨 Themes

### Dark Theme (Standard)
- Dunkler Hintergrund (#0f172a)
- Helle Schrift
- Kühle Farbtöne

### Light Theme
- Weißer Hintergrund
- Dunkle Schrift
- Hoher Kontrast
- Intensivere Element-Farben

## 📦 Browser-Kompatibilität

- Chrome/Edge (empfohlen)
- Firefox
- Safari
- Erfordert modernes JavaScript (ES6+)

## 🚀 Performance

- Lädt alle 118 Elemente dynamisch
- Optimiert für schnelle Hover-Reaktionen
- Smooth 60fps Animationen
- LocalStorage für Theme-Persistenz

## 📄 Lizenz

Open Source - Frei verwendbar

## 🔗 Quellen

- Element-Daten: [Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON)
- Wikipedia Integration: Deutsche Wikipedia
- Design Inspiration: Moderne Wissenschafts-Apps

---

**Erstellt mit ❤️ für Chemie-Enthusiasten & Studenten**
