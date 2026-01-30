# KookKompas UI - Handleiding

Versie: 2.0
Auteur: Senior UI Architect
Project: KookKompas Mobile-First Web App

---

## Inhoudsopgave

1. Vereisten
2. Installatie
3. Ontwikkelen
4. Mobile Testing
5. PWA Installatie
6. Troubleshooting

---

## 1. Vereisten

### Software

- Python 3.10+
- Node.js 18+ (voor TailwindCSS)
- MySQL 8.0 (zelfde als CLI)
- Android telefoon OF Chrome DevTools

### Kennis

- Basis Django
- HTML/CSS (TailwindCSS)
- Mobile-first denken

---

## 2. Installatie

### Stap 2.1: Navigeer naar UI_Django

```bash
cd kookcompas/UI_Django
```

### Stap 2.2: Python Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Stap 2.3: Node Dependencies

```bash
npm install
```

### Stap 2.4: Environment

Gebruik dezelfde .env als de CLI in project root.

---

## 3. Ontwikkelen

### 3.1: Start Development

Open 2 terminals:

**Terminal 1: TailwindCSS**
```bash
npm run watch
```

**Terminal 2: Django**
```bash
python manage.py runserver 0.0.0.0:8000
```

Let op: `0.0.0.0` maakt de server bereikbaar op je netwerk (voor telefoon testen).

### 3.2: Open in Browser

Desktop: http://127.0.0.1:8000
Telefoon: http://[jouw-ip]:8000 (bijv. http://192.168.1.100:8000)

Vind je IP met:
```bash
# Windows
ipconfig

# Mac/Linux
ifconfig
```

### 3.3: Chrome DevTools Mobile Mode

1. Open Chrome DevTools (F12)
2. Klik op "Toggle device toolbar" (Ctrl+Shift+M)
3. Selecteer een Android device (Pixel, Samsung, etc.)
4. Ververs de pagina

---

## 4. Mobile Testing

### 4.1: Test op Echte Telefoon

1. Verbind telefoon met zelfde WiFi als laptop
2. Open Chrome op telefoon
3. Ga naar http://[laptop-ip]:8000
4. Test alle flows met je duim

### 4.2: Checklist per Pagina

- Kunnen alle knoppen makkelijk geraakt worden met duim?
- Is de tekst leesbaar zonder zoomen?
- Werkt scrollen smooth?
- Verschijnt het toetsenbord correct bij input?
- Werkt de terug-knop logisch?
- Is de bottom nav altijd zichtbaar?

### 4.3: Test Scenarios

**Happy path:**
1. Open app
2. Tap "Genereer Recept"
3. Voeg ingredienten toe
4. Tap "Genereer"
5. Bekijk recept
6. Tap "Opslaan"
7. Ga naar Recepten
8. Open opgeslagen recept

**Edge cases:**
- Lege invoer
- Geen internet (als offline mode actief)
- Kleine telefoon (320px breed)
- Landschap orientatie

---

## 5. PWA Installatie

### 5.1: Op Android

1. Open de app in Chrome
2. Tap de 3-puntjes menu
3. Tap "Toevoegen aan startscherm"
4. Geef een naam
5. Tap "Toevoegen"

De app verschijnt nu als icoon op je homescreen en opent fullscreen.

### 5.2: Vereisten voor PWA

- HTTPS (of localhost voor development)
- manifest.json correct geconfigureerd
- Service worker geregistreerd
- Iconen in alle formaten

### 5.3: Test PWA Installatie

Chrome DevTools > Application > Manifest
Check op warnings en errors.

---

## 6. Troubleshooting

### Probleem: Pagina past niet op scherm

Controleer:
- Geen fixed widths groter dan 100vw
- Geen horizontal overflow
- Meta viewport tag aanwezig

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0,
      maximum-scale=1.0, user-scalable=no">
```

### Probleem: Knoppen te klein

Minimum touch target is 48x48px:
```html
<button class="min-h-12 min-w-12 p-3">
```

### Probleem: Input zoom op iOS

Zorg dat font-size minimaal 16px is:
```html
<input class="text-base">  <!-- 16px -->
```

### Probleem: Bottom nav overlapt content

Voeg padding-bottom toe aan content:
```html
<main class="pb-20">  <!-- 80px voor bottom nav -->
```

### Probleem: Notch telefoons

Gebruik safe-area:
```css
padding-bottom: env(safe-area-inset-bottom);
padding-top: env(safe-area-inset-top);
```

### Probleem: HTMX requests werken niet op telefoon

Check:
- Correcte URL (niet localhost)
- CSRF token in form
- Server draait op 0.0.0.0

### Probleem: Service worker cached oude versie

Clear cache:
- Chrome > Settings > Privacy > Clear browsing data
- Of: DevTools > Application > Clear storage

---

## 7. Commando Referentie

```bash
# Start development
npm run watch          # TailwindCSS watcher
python manage.py runserver 0.0.0.0:8000

# Production build
npm run build          # Minified CSS

# Vind lokale IP
ipconfig               # Windows
ifconfig               # Mac/Linux

# Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

---

## 8. Mobile-First Mindset

### DO:

- Test EERST op telefoon, dan desktop
- Ontwerp voor duim-navigatie
- Gebruik grote, duidelijke touch targets
- Houd laadtijden kort
- Denk aan offline gebruik

### DON'T:

- Begin niet met desktop layout
- Geen hover-only interacties
- Geen kleine tekst (< 14px)
- Geen complexe gestures
- Geen zware afbeeldingen

---

## 9. Mapstructuur Herinnering

```
kookcompas/
├── ai/                  # NIET AANRAKEN
├── crud/                # NIET AANRAKEN
├── database/            # NIET AANRAKEN
├── utils/               # NIET AANRAKEN
├── main.py              # NIET AANRAKEN
│
├── UI_Django/           # HIER WERKEN
│   ├── core/            # Django app
│   ├── templates/       # HTML
│   ├── static/          # CSS, JS, icons
│   └── manage.py
│
├── UI_Django_false/     # Mockup HTML
│   └── mockup.html      # Preview in browser
│
├── UI_FASES.md
├── UI_ARCHITECTUUR.md
└── UI_HANDLEIDING.md
```

---

## 10. Volgende Stappen

1. Bekijk de mockup: `UI_Django_false/mockup.html`
2. Lees UI_FASES.md voor het stappenplan
3. Lees UI_ARCHITECTUUR.md voor technische details
4. Begin met Fase 0: Project setup

---

## Contact

Bij problemen:
1. Check dit document
2. Check UI_ARCHITECTUUR.md
3. Django docs: docs.djangoproject.com
4. TailwindCSS docs: tailwindcss.com
5. HTMX docs: htmx.org
