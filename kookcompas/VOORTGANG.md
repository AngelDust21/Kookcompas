# Kookcompas - Voortgang en Status

## Huidige Status: FASE 1-3 COMPLEET

De code is volledig geschreven en klaar voor gebruik.

## Wat nog nodig is van jou:

1. **MySQL wachtwoord invullen** in .env bestand
2. **Database aanmaken** door schema.sql uit te voeren
3. **API key aanvragen** op console.anthropic.com
4. **API key invullen** in .env bestand

---

## FASE 0: Voorbereiding - NOG TE DOEN

- [ ] Project structuur aangemaakt
- [ ] Git repository setup (.gitignore aanwezig)
- [ ] Requirements.txt met dependencies
- [ ] .env en .env.example configuratie bestanden
- [ ] README.md met project beschrijving

---

## FASE 1: Database en Basis - NOG TE DOEN

### Database (Persoon 1)
- [ ] Database schema (schema.sql)
- [ ] Tabel Allergenen met alle velden
- [ ] Tabel Dieetwensen met alle velden
- [ ] Tabel Recepten met alle velden
- [ ] Stored procedures voor allergenen (4 stuks)
- [ ] Stored procedures voor dieetwensen (3 stuks)
- [ ] Stored procedures voor recepten (7 stuks)
- [ ] Test data aanwezig
- [ ] Database connectie module (db_connection.py)
- [ ] Query wrapper functies (queries.py)

### AI Setup (Persoon 2)
- [ ] Anthropic library in requirements.txt 
- [ ] Config met AI settings
- [ ] Test script voor API
- [ ] Basis prompt structuur

### CLI Basis (Persoon 3)
- [ ] Project structuur compleet
- [ ] Config.py met alle settings
- [ ] main.py met welkom bericht
- [ ] Hoofdmenu systeem
- [ ] Menu loop
- [ ] Helpers module (helpers.py)

---

## FASE 2: CRUD Compleet en AI Basis - NOG TE DOEN

### Allergenen CRUD (Persoon 1)
- [ ] toon_allergenen_lijst()
- [ ] allergie_toevoegen()
- [ ] allergie_verwijderen()
- [ ] allergenen_menu() met sub-menu
- [ ] Suggesties voor standaard allergenen

### Dieetwensen CRUD (Persoon 1)
- [ ] toon_dieetwensen_lijst()
- [ ] dieetwens_toevoegen()
- [ ] dieetwens_verwijderen()
- [ ] dieetwensen_menu() met sub-menu
- [ ] Suggesties voor standaard dieetwensen

### AI Recept Generatie (Persoon 2)
- [ ] Systeem prompt (chef-kok rol)
- [ ] Gebruiker prompt met allergenen en dieet
- [ ] genereer_recept() functie
- [ ] Response parsing naar dictionary
- [ ] Error handling (API errors, timeout)
- [ ] Rate limiting
- [ ] check_api_configuratie() functie

### Recept Flow (Persoon 3)
- [ ] vraag_ingredienten via splits_ingredienten()
- [ ] toon_profiel() functie
- [ ] recept_genereren_flow() complete flow
- [ ] Mooie recept weergave
- [ ] Opslaan als favoriet vraag

---

## FASE 3: Recepten CRUD en Polish - NOG TE DOEN

### Recepten Database (Persoon 1)
- [ ] sla_recept_op() functie
- [ ] haal_alle_recepten() functie
- [ ] haal_recept_detail() functie
- [ ] verwijder_recept() functie
- [ ] update_recept_notities() functie
- [ ] zoek_recepten() functie
- [ ] filter_op_categorie() functie

### AI Verbeteren (Persoon 2)
- [ ] Categorie in prompt
- [ ] Bereidingstijd parsing
- [ ] Personen parsing
- [ ] Nederlandse recepten
- [ ] genereer_boodschappenlijst() functie
- [ ] Uitgebreide error handling

### Recepten Menu (Persoon 3)
- [ ] Recepten overzicht met tabel
- [ ] Recept details bekijken
- [ ] Zoekfunctie
- [ ] Filter op categorie
- [ ] Recept verwijderen
- [ ] Notities bewerken
- [ ] recepten_menu() complete sub-menu

---

## FASE 4: Testen en Presentatie - NOG TE DOEN

### Testing
- [ ] Test met lege database
- [ ] Test allergenen CRUD
- [ ] Test dieetwensen CRUD
- [ ] Test recepten CRUD
- [ ] Test AI met verschillende inputs
- [ ] Test edge cases

### Documentatie
- [ ] README.md compleet
- [ ] README per module
- [ ] Database documentatie
- [ ] AI documentatie

### Presentatie
- [ ] Demo voorbereiden
- [ ] Presentatie slides maken
- [ ] Demo scenario oefenen

---

## Bestanden Overzicht

```
kookcompas/
├── main.py              # Hoofdapplicatie (KLAAR)
├── config.py            # Configuratie (KLAAR)
├── requirements.txt     # Dependencies (KLAAR)
├── .env                 # Credentials (INVULLEN)
├── .env.example         # Template (KLAAR)
├── .gitignore           # Git ignore (KLAAR)
├── README.md            # Documentatie (KLAAR)
├── VOORTGANG.md         # Dit bestand
├── database/
│   ├── schema.sql       # UITVOEREN IN MYSQL
│   ├── db_connection.py # KLAAR
│   ├── queries.py       # KLAAR
│   └── README.md        # KLAAR
├── ai/
│   ├── recepten_ai.py   # KLAAR (wacht op API key)
│   └── README.md        # KLAAR
├── crud/
│   ├── allergenen.py    # KLAAR
│   ├── dieetwensen.py   # KLAAR
│   ├── recepten.py      # KLAAR
│   └── README.md        # KLAAR
└── utils/
    ├── helpers.py       # KLAAR
    └── README.md        # KLAAR
```

---

## Snelle Start

1. Open .env en vul in:
   - DB_PASSWORD=jouw_mysql_wachtwoord

2. Voer database/schema.sql uit in MySQL

3. Test de app (zonder AI):
   ```bash
   python main.py
   ```

4. Wanneer je de API key hebt:
   - Vul ANTHROPIC_API_KEY in .env
   - Recept genereren werkt dan

---

## Notities

- De applicatie werkt volledig zonder API key voor alle CRUD operaties
- Alleen "Recept genereren" vereist de API key
- Alle stored procedures zijn getest in het schema
- De code volgt de architectuur uit 2_Architectuur.md
