# KookKompas UI - Architectuur

Versie: 2.0
Auteur: Senior UI Architect
Project: KookKompas Mobile-First Web App

---

## Architectuur Filosofie

**Mobile-First, Android-First.**

We bouwen geen website die ook op mobiel werkt.
We bouwen een mobiele app die ook op desktop werkt.

```
┌─────────────────────────────────────────────────────────────┐
│                   ANDROID DEVICE                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Chrome / PWA (Add to Homescreen)                    │   │
│  │                                                      │   │
│  │  ┌──────────────────────────────────────────────┐   │   │
│  │  │  Header (sticky, met terug-knop)             │   │   │
│  │  ├──────────────────────────────────────────────┤   │   │
│  │  │                                              │   │   │
│  │  │           CONTENT AREA                       │   │   │
│  │  │           (scrollable)                       │   │   │
│  │  │                                              │   │   │
│  │  ├──────────────────────────────────────────────┤   │   │
│  │  │  Bottom Nav (Home | + | Recepten)            │   │   │
│  │  └──────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ HTTP/HTMX
┌─────────────────────────────────────────────────────────────┐
│                    UI_Django/ (SERVER)                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   Views     │  │    URLs     │  │     Templates       │ │
│  │   (thin)    │  │   (RESTful) │  │   (mobile-first)    │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ imports
┌─────────────────────────────────────────────────────────────┐
│              BESTAANDE CODE (ONGEWIJZIGD)                   │
│     ai/    crud/    database/    utils/    config.py       │
└─────────────────────────────────────────────────────────────┘
```

---

## Mapstructuur UI_Django

```
UI_Django/
│
├── kookcompas_web/              # Django project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/                        # Main app
│   ├── __init__.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── home.py              # Homepage
│   │   ├── allergenen.py        # Allergenen CRUD
│   │   ├── dieetwensen.py       # Dieetwensen CRUD
│   │   ├── recepten.py          # Recepten beheer
│   │   └── generatie.py         # AI recept generatie
│   ├── urls.py
│   └── templatetags/
│       └── ui_tags.py
│
├── templates/
│   ├── base.html                # App shell
│   ├── components/
│   │   ├── bottom_nav.html      # Bottom navigation
│   │   ├── header.html          # Page headers
│   │   ├── toast.html           # Notificaties
│   │   ├── modal.html           # Bottom sheets
│   │   ├── card.html            # Content cards
│   │   ├── tag.html             # Chips/tags
│   │   └── loading.html         # Loading states
│   │
│   ├── pages/
│   │   ├── home.html
│   │   ├── allergenen/
│   │   │   ├── lijst.html
│   │   │   └── partials/
│   │   │       └── item.html
│   │   ├── dieetwensen/
│   │   │   ├── lijst.html
│   │   │   └── partials/
│   │   │       └── item.html
│   │   ├── recepten/
│   │   │   ├── lijst.html
│   │   │   ├── detail.html
│   │   │   └── partials/
│   │   │       └── card.html
│   │   └── generatie/
│   │       ├── invoer.html
│   │       ├── loading.html
│   │       └── resultaat.html
│   │
│   └── pwa/
│       ├── offline.html         # Offline fallback
│       └── install.html         # Install prompt
│
├── static/
│   ├── css/
│   │   ├── input.css            # Tailwind input
│   │   └── output.css           # Compiled
│   ├── js/
│   │   ├── htmx.min.js
│   │   ├── app.js               # Touch handlers, etc
│   │   └── sw.js                # Service worker
│   ├── icons/
│   │   ├── icon-192.png
│   │   ├── icon-512.png
│   │   └── maskable-icon.png
│   └── manifest.json            # PWA manifest
│
├── manage.py
├── requirements.txt
├── tailwind.config.js
├── package.json
└── README.md
```

---

## Mobile-First CSS Strategie

### TailwindCSS Breakpoints

We schrijven mobile CSS eerst, dan desktop overrides:

```html
<!-- Mobile first -->
<div class="p-4 md:p-8 lg:p-12">
    <h1 class="text-xl md:text-2xl lg:text-3xl">Titel</h1>
</div>
```

### Custom Tailwind Config

```javascript
// tailwind.config.js
module.exports = {
    theme: {
        screens: {
            'sm': '640px',   // Grote telefoons
            'md': '768px',   // Tablets
            'lg': '1024px',  // Desktop
        },
        extend: {
            spacing: {
                'safe-bottom': 'env(safe-area-inset-bottom)',
                'safe-top': 'env(safe-area-inset-top)',
            },
            minHeight: {
                'touch': '48px',  // Minimum touch target
            },
        }
    }
}
```

---

## Touch Interaction Patterns

### Touch Feedback

```html
<button class="active:scale-95 active:opacity-90 transition-transform">
    Tap me
</button>
```

### Swipe Actions (met HTMX)

```html
<div class="relative overflow-hidden"
     hx-on:touchstart="startSwipe(event)"
     hx-on:touchend="endSwipe(event)">
    <div class="absolute right-0 bg-red-500 h-full w-20 flex items-center justify-center">
        Verwijder
    </div>
    <div class="bg-white p-4 transition-transform" id="swipe-content">
        Item content
    </div>
</div>
```

### Bottom Sheet Modal

```html
<div id="modal" class="fixed inset-0 bg-black/50 z-50 hidden">
    <div class="absolute bottom-0 left-0 right-0 bg-white rounded-t-3xl p-6
                transform transition-transform translate-y-full"
         id="sheet">
        <!-- Drag handle -->
        <div class="w-12 h-1 bg-gray-300 rounded-full mx-auto mb-4"></div>
        <!-- Content -->
    </div>
</div>
```

---

## HTMX Mobile Patterns

### Loading States

```html
<button hx-post="/genereer/"
        hx-target="#result"
        hx-indicator="#loading"
        class="w-full py-4 bg-primary text-white rounded-2xl">
    Genereer
</button>

<div id="loading" class="htmx-indicator fixed inset-0 bg-white z-50 flex items-center justify-center">
    <div class="text-center">
        <div class="animate-pulse w-16 h-16 bg-primary/20 rounded-full mx-auto mb-4"></div>
        <p>Even denken...</p>
    </div>
</div>
```

### Infinite Scroll

```html
<div hx-get="/recepten/meer/"
     hx-trigger="revealed"
     hx-swap="afterend">
    Loading meer...
</div>
```

### Pull to Refresh

```html
<div hx-get="/refresh/"
     hx-trigger="pulldown"
     hx-swap="innerHTML"
     hx-target="#content">
</div>
```

---

## PWA Configuratie

### manifest.json

```json
{
    "name": "KookKompas",
    "short_name": "KookKompas",
    "description": "Slimme recepten met AI",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#ee7712",
    "orientation": "portrait",
    "icons": [
        {
            "src": "/static/icons/icon-192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/static/icons/icon-512.png",
            "sizes": "512x512",
            "type": "image/png"
        },
        {
            "src": "/static/icons/maskable-icon.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "maskable"
        }
    ]
}
```

### Service Worker Basics

```javascript
// sw.js
const CACHE_NAME = 'kookcompas-v1';
const STATIC_ASSETS = [
    '/',
    '/static/css/output.css',
    '/static/js/htmx.min.js',
    '/offline/'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_ASSETS))
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request).catch(() => {
                return caches.match('/offline/');
            });
        })
    );
});
```

---

## Base Template (App Shell)

```html
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0,
          maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <meta name="theme-color" content="#ee7712">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <link rel="manifest" href="/static/manifest.json">
    <title>KookKompas</title>
    <link rel="stylesheet" href="/static/css/output.css">
    <script src="/static/js/htmx.min.js"></script>
</head>
<body class="bg-gray-50 min-h-screen">

    <div class="h-screen flex flex-col">
        <!-- Header -->
        {% block header %}{% endblock %}

        <!-- Content -->
        <main class="flex-1 overflow-y-auto pb-20">
            {% block content %}{% endblock %}
        </main>

        <!-- Bottom Navigation -->
        {% include 'components/bottom_nav.html' %}
    </div>

    <!-- Toast container -->
    <div id="toast-container" class="fixed top-4 left-4 right-4 z-50"></div>

    <script src="/static/js/app.js"></script>
</body>
</html>
```

---

## Bottom Navigation Component

```html
<!-- components/bottom_nav.html -->
<nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200
            px-6 py-2 flex justify-around items-center z-40"
     style="padding-bottom: max(env(safe-area-inset-bottom), 12px);">

    <a href="/" class="flex flex-col items-center py-2 px-4
                      {% if request.path == '/' %}text-primary{% else %}text-gray-400{% endif %}">
        <svg class="w-6 h-6"><!-- home icon --></svg>
        <span class="text-xs mt-1 font-medium">Home</span>
    </a>

    <a href="/genereer/" class="flex flex-col items-center -mt-4">
        <div class="w-14 h-14 bg-gradient-to-r from-primary to-primary-dark
                    rounded-full flex items-center justify-center shadow-lg">
            <svg class="w-7 h-7 text-white"><!-- plus icon --></svg>
        </div>
    </a>

    <a href="/recepten/" class="flex flex-col items-center py-2 px-4
                               {% if '/recepten/' in request.path %}text-primary{% else %}text-gray-400{% endif %}">
        <svg class="w-6 h-6"><!-- bookmark icon --></svg>
        <span class="text-xs mt-1 font-medium">Recepten</span>
    </a>
</nav>
```

---

## Performance Targets

- First Contentful Paint: < 1.5s
- Time to Interactive: < 3s
- Lighthouse Mobile Score: > 90
- Bundle size: < 100KB (excl. images)

---

## Integratie met Bestaande Code

Geen wijzigingen aan:
- ai/
- crud/
- database/
- utils/
- main.py
- config.py

Django views importeren uit deze modules:

```python
import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, project_root)

from database.queries import haal_alle_allergenen
from ai.recepten_ai import genereer_recept
```

---

Volgende stap: Zie UI_HANDLEIDING.md voor implementatie instructies
