# KookKompas UI - Ontwikkelfases

Versie: 2.0
Auteur: Senior UI Architect
Project: KookKompas Mobile-First Web App

---

## Filosofie: Mobile-First Android

90% van de gebruikers zit op mobiel. Desktop is secundair.
We bouwen een Progressive Web App (PWA) die op Android voelt als een native app.

**Core principes:**
- Touch-first: grote knoppen (min 48px), swipe gebaren
- Bottom navigation: duim-vriendelijk, zoals echte apps
- Snelle laadtijden: geen onnodige assets
- Offline capable: basisdata werkt zonder internet
- Add to homescreen: installeerbaar als app

---

## Overzicht

Dit document beschrijft de gefaseerde aanpak voor het bouwen van de mobile-first web app.
Elke fase bouwt voort op de vorige en levert een werkend tussenproduct op.

---

## Fase 0: Voorbereiding

**Doel:** Projectstructuur opzetten, mobile-first fundament leggen

Stappen:
- Map UI_Django aanmaken in project root
- Django project initialiseren
- TailwindCSS configureren met mobile breakpoints
- HTMX integreren voor snelle interacties
- PWA manifest.json aanmaken
- Service worker voorbereiden

Deliverable: Draaiende Django server met mobile viewport

---

## Fase 1: App Shell

**Doel:** Native app-achtige navigatie en layout

Stappen:
- Bottom navigation bar (Home, Genereer +, Recepten)
- Sticky header per pagina met terug-knop
- Full-height layout zonder scroll bounce
- Touch feedback op alle interactieve elementen
- Safe area support voor notch-telefoons
- Page transitions (slide animaties)

Deliverable: Navigeerbare app shell die voelt als Android app

---

## Fase 2: Home en Profiel

**Doel:** Dashboard met profiel overzicht

Stappen:
- Welkom header met gradient
- Grote "Genereer Recept" call-to-action
- Profiel kaarten (allergenen count, dieet count)
- Tags overzicht van actieve voorkeuren
- Recente recepten lijst (horizontal scroll)
- Pull-to-refresh gesture

Deliverable: Werkende homepage met profiel samenvatting

---

## Fase 3: Profielbeheer

**Doel:** CRUD voor allergenen en dieetwensen

Stappen:
- Allergenen pagina
  - Lijst met swipe-to-delete
  - Tap om toe te voegen (suggestie chips)
  - Custom invoer met grote input
  - Haptic feedback simulatie (visueel)
- Dieetwensen pagina
  - Zelfde structuur, ander kleurthema
- Toast notificaties voor feedback

Deliverable: Volledig werkend profielbeheer op mobiel

---

## Fase 4: Recept Generatie

**Doel:** AI-gestuurde receptgeneratie, mobile-optimized

Stappen:
- Ingredienten invoer
  - Grote touch-vriendelijke tags
  - Suggestie chips onderaan
  - Soft keyboard handling
- Generatie flow
  - Full-screen loading state
  - Animatie tijdens wachten
- Recept weergave
  - Card-based layout
  - Collapsible secties (ingredienten, bereiding)
  - Sticky "Opslaan" button onderaan
- Boodschappenlijst
  - Bottom sheet modal
  - Checkboxes voor afvinken

Deliverable: Complete recept flow, thumb-friendly

---

## Fase 5: Receptenbeheer

**Doel:** Opgeslagen recepten bekijken en beheren

Stappen:
- Zoekbalk met soft keyboard
- Horizontale filter chips (scroll)
- Recept cards met thumbnail
- Recept detail pagina
  - Full-screen view
  - Share button
  - Delete met swipe of long-press
- Empty state met CTA

Deliverable: Recepten bibliotheek, mobile-native feel

---

## Fase 6: PWA Features

**Doel:** App-achtige ervaring completeren

Stappen:
- manifest.json voor installatie
- App iconen (alle formaten)
- Splash screen
- Service worker voor caching
- Offline fallback pagina
- Add to homescreen prompt

Deliverable: Installeerbare PWA op Android

---

## Fase 7: Polish

**Doel:** Van werkend naar premium

Stappen:
- Micro-animaties (buttons, cards)
- Skeleton loaders
- Dark mode toggle
- Error states met retry
- Lege states met illustraties
- Performance optimalisatie

Deliverable: Production-ready mobile app

---

## Afhankelijkheden

```
Fase 0 --> Fase 1 --> Fase 2 --> Fase 3 --|
                                          |--> Fase 6 --> Fase 7
Fase 0 --> Fase 1 --> Fase 4 --> Fase 5 --|
```

Fase 3 (profiel) en Fase 4-5 (recepten) kunnen parallel na Fase 2.
Fase 6 (PWA) vereist dat core features werken.

---

## Technische Stack

- **Django 5.x**: Backend, server-side rendering
- **TailwindCSS**: Utility-first CSS, mobile classes
- **HTMX**: Dynamische updates zonder JavaScript frameworks
- **PWA**: manifest.json, service worker
- **Geen React/Vue/Angular**: Te zwaar voor dit project

---

## Mobile-First Checklist per Fase

Elke fase moet voldoen aan:

- Touch targets minimaal 48x48px
- Tekst minimaal 16px (geen zoom op iOS)
- Geen hover-only interacties
- Werkt in portrait EN landscape
- Werkt op 320px breed (kleine telefoons)
- Geen horizontal scroll (behalve bewust)
- Laadtijd onder 3 seconden op 3G

---

## Device Testing

Test op:
- Android Chrome (primair)
- Android Firefox
- Samsung Internet
- iOS Safari (secundair)

Minimum support: Android 8.0+, iOS 13+

---

Volgende stap: Zie UI_ARCHITECTUUR.md voor technische details
