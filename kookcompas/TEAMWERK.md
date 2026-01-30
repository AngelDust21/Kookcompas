# Kookcompas - Teamwerk Documentatie

## Teamoverzicht

Dit project is gebouwd door 3 teamleden met duidelijke verantwoordelijkheden.

---

## Teamlid 1: Database Developer

### Verantwoordelijke Bestanden

| Bestand | Beschrijving | Status |
|---------|--------------|--------|
| database/schema.sql | Database tabellen en stored procedures | Klaar |
| database/db_connection.py | Database connectie beheer | Klaar |
| database/queries.py | Python wrapper functies voor procedures | Klaar |
| crud/allergenen.py | CRUD menu voor allergenen | Klaar |
| crud/dieetwensen.py | CRUD menu voor dieetwensen | Klaar |

### Taken Overzicht

**Database Ontwerp:**
- 3 tabellen ontworpen (Allergenen, Dieetwensen, Recepten)
- Relaties en constraints gedefinieerd
- Indexes voor performance

**Stored Procedures (14 stuks):**
- sp_voeg_allergie_toe, sp_haal_allergenen_op, sp_verwijder_allergie, sp_zoek_allergie
- sp_voeg_dieet_toe, sp_haal_dieet_op, sp_verwijder_dieet
- sp_voeg_recept_toe, sp_haal_recepten_op, sp_haal_recept_detail
- sp_verwijder_recept, sp_update_notities, sp_zoek_recepten, sp_filter_categorie

**Python Database Code:**
- Connectie maken/sluiten
- Procedure uitvoeren met error handling
- Query functies voor elke stored procedure

**CRUD Allergenen:**
- Lijst tonen
- Toevoegen met suggesties
- Verwijderen met bevestiging
- Sub-menu

**CRUD Dieetwensen:**
- Lijst tonen
- Toevoegen met suggesties
- Verwijderen met bevestiging
- Sub-menu

### Hoe Anderen Mijn Code Gebruiken

```python
# Database connectie (in main.py)
from database.db_connection import maak_connectie, sluit_connectie

# Bij opstarten
if not maak_connectie():
    print("Database fout")
    return

# Bij afsluiten
sluit_connectie()
```

```python
# Allergenen ophalen (in ai/recepten_ai.py)
from crud.allergenen import haal_allergie_namen

namen = haal_allergie_namen()  # Returns: ['noten', 'lactose', ...]
```

```python
# Menu starten (in main.py)
from crud.allergenen import allergenen_menu
from crud.dieetwensen import dieetwensen_menu

allergenen_menu()    # Start allergenen sub-menu
dieetwensen_menu()   # Start dieetwensen sub-menu
```

### Database Setup Instructies

1. Open MySQL Workbench of terminal
2. Voer schema.sql uit:
   ```sql
   SOURCE C:/pad/naar/kookcompas/database/schema.sql
   ```
3. Controleer of tabellen bestaan:
   ```sql
   USE kookcompas;
   SHOW TABLES;
   ```
4. Test stored procedures:
   ```sql
   CALL sp_haal_allergenen_op();
   ```

---

## Teamlid 2: AI Developer

### Verantwoordelijke Bestanden

| Bestand | Beschrijving | Status |
|---------|--------------|--------|
| ai/recepten_ai.py | Volledige AI integratie | Klaar (wacht op API key) |

### Taken Overzicht

**API Integratie:**
- Anthropic library configuratie
- Client aanmaken met API key
- Error handling voor alle API fouten

**Prompt Engineering:**
- Systeem prompt: Chef-kok rol
- Gebruiker prompt: Ingredienten + allergenen + dieet
- Output formaat: Gestructureerd recept

**Response Parsing:**
- Titel, categorie, tijd, personen extraheren
- Ingredienten lijst opbouwen
- Bereidingsstappen opbouwen
- Fallback waarden bij parsing fouten

**Extra Functies:**
- Boodschappenlijst genereren
- API verbinding testen

### Hoe Anderen Mijn Code Gebruiken

```python
# In main.py - recept genereren
from ai.recepten_ai import genereer_recept, check_api_configuratie

# Eerst checken of API werkt
if not check_api_configuratie():
    print("API niet geconfigureerd")
    return

# Recept genereren
recept = genereer_recept(
    ingredienten_lijst=['pasta', 'tomaat', 'ui'],
    allergenen_lijst=['noten', 'lactose'],
    dieet_lijst=['vegetarisch']
)

# Recept is een dictionary:
# {
#     'titel': 'Pasta Pomodoro',
#     'categorie': 'Diner',
#     'bereidingstijd': 25,
#     'personen': 2,
#     'ingredienten': '- 250g pasta\n- 4 tomaten\n...',
#     'instructies': '1. Kook de pasta\n2. ...'
# }
```

```python
# Boodschappenlijst maken
from ai.recepten_ai import genereer_boodschappenlijst

boodschappen = genereer_boodschappenlijst(recept)
print(boodschappen)
# Output:
# [ ] 250g pasta
# [ ] 4 tomaten
# [ ] 1 ui
```

### API Key Setup

1. Ga naar console.anthropic.com
2. Maak account aan
3. Ga naar API Keys
4. Klik Create Key
5. Kopieer key (begint met sk-ant-)
6. Plak in .env bestand:
   ```
   ANTHROPIC_API_KEY=sk-ant-jouw-key-hier
   ```

### Prompt Structuur

**Systeem Prompt:**
```
Je bent een ervaren chef-kok die Nederlandse recepten maakt.
Je houdt altijd rekening met allergenen en dieetwensen.
Je geeft duidelijke, stapsgewijze bereidingsinstructies.
Je antwoordt altijd in het Nederlands.
```

**Gebruiker Prompt:**
```
Maak een recept met deze ingredienten: [lijst]

BELANGRIJK - Allergenen om te VERMIJDEN: [lijst]
BELANGRIJK - Dieetwensen: [lijst]

Geef het recept in EXACT dit formaat:
TITEL: [naam]
CATEGORIE: [Ontbijt/Lunch/Diner/Snack/Dessert]
TIJD: [minuten]
PERSONEN: [aantal]

INGREDIENTEN:
- [ingredient 1]
...

BEREIDING:
1. [stap 1]
...
```

---

## Teamlid 3: CLI Developer

### Verantwoordelijke Bestanden

| Bestand | Beschrijving | Status |
|---------|--------------|--------|
| main.py | Hoofdapplicatie en menu | Klaar |
| config.py | Configuratie en constanten | Klaar |
| utils/helpers.py | Helper functies | Klaar |
| crud/recepten.py | CRUD menu voor recepten | Klaar |

### Taken Overzicht

**Hoofdapplicatie (main.py):**
- Welkomstscherm
- Profiel weergave (allergenen + dieet)
- Hoofdmenu met 5 opties
- Menu loop
- Recept generatie flow
- Integratie alle modules

**Configuratie (config.py):**
- Database instellingen uit .env
- AI instellingen uit .env
- App naam en versie
- Categorieen lijst
- Standaard allergenen/dieet lijsten

**Helpers (utils/helpers.py):**
- maak_scherm_leeg() - Terminal clearen
- vraag_tekst() - Tekst input met validatie
- vraag_getal() - Getal input met bereik
- vraag_ja_nee() - Ja/nee vraag
- wacht_op_enter() - Pauze
- toon_lijn() - Visuele scheiding
- splits_ingredienten() - Komma-tekst naar lijst

**Recepten CRUD (crud/recepten.py):**
- Overzicht met tabel
- Details bekijken
- Zoeken op tekst
- Filteren op categorie
- Notities bewerken
- Verwijderen

### Hoe Anderen Mijn Code Gebruiken

```python
# Helpers gebruiken
from utils.helpers import vraag_tekst, vraag_getal, vraag_ja_nee

naam = vraag_tekst("Naam: ")
keuze = vraag_getal("Kies 1-5: ", 1, 5)
if vraag_ja_nee("Opslaan? "):
    # opslaan
```

```python
# Config gebruiken
from config import APP_NAAM, VERSIE, CATEGORIEEN

print(f"{APP_NAAM} v{VERSIE}")
for cat in CATEGORIEEN:
    print(cat)
```

```python
# Recepten menu starten
from crud.recepten import recepten_menu

recepten_menu()  # Start recepten sub-menu
```

### Menu Structuur

```
HOOFDMENU
├── 1. Recept genereren
│   ├── Toon profiel
│   ├── Vraag ingredienten
│   ├── Genereer met AI
│   ├── Toon recept
│   ├── Opslaan vraag
│   └── Boodschappenlijst vraag
│
├── 2. Mijn allergenen (-> Teamlid 1)
│   ├── Toon lijst
│   ├── 1. Toevoegen
│   ├── 2. Verwijderen
│   └── 0. Terug
│
├── 3. Mijn dieetwensen (-> Teamlid 1)
│   ├── Toon lijst
│   ├── 1. Toevoegen
│   ├── 2. Verwijderen
│   └── 0. Terug
│
├── 4. Opgeslagen recepten
│   ├── Toon overzicht
│   ├── 1. Details bekijken
│   ├── 2. Zoeken
│   ├── 3. Filter categorie
│   ├── 4. Verwijderen
│   └── 0. Terug
│
└── 0. Afsluiten
```

---

## Samenwerking en Integratie

### Hoe De Modules Samenwerken

```
                    main.py (Teamlid 3)
                         |
         +---------------+---------------+
         |               |               |
    config.py       helpers.py      crud/recepten.py
   (Teamlid 3)     (Teamlid 3)      (Teamlid 3)
         |               |               |
         +-------+-------+-------+-------+
                 |               |
          crud/allergenen.py  crud/dieetwensen.py
            (Teamlid 1)         (Teamlid 1)
                 |               |
                 +-------+-------+
                         |
                  database/queries.py
                     (Teamlid 1)
                         |
                database/db_connection.py
                     (Teamlid 1)
                         |
                      MySQL


    main.py ook:
         |
    ai/recepten_ai.py
       (Teamlid 2)
         |
    Claude API
```

### Data Flow: Recept Genereren

1. **main.py** vraagt ingredienten aan gebruiker
2. **crud/allergenen.py** -> haal_allergie_namen() geeft allergenen
3. **crud/dieetwensen.py** -> haal_dieet_namen() geeft dieetwensen
4. **ai/recepten_ai.py** -> genereer_recept() maakt API call
5. **main.py** toont recept
6. Als opslaan: **database/queries.py** -> sla_recept_op()

### Afhankelijkheden

**Teamlid 2 (AI) heeft nodig van Teamlid 1:**
- haal_allergie_namen() uit crud/allergenen.py
- haal_dieet_namen() uit crud/dieetwensen.py

**Teamlid 3 (CLI) heeft nodig van Teamlid 1:**
- allergenen_menu() uit crud/allergenen.py
- dieetwensen_menu() uit crud/dieetwensen.py
- maak_connectie(), sluit_connectie() uit database/db_connection.py
- sla_recept_op() uit database/queries.py

**Teamlid 3 (CLI) heeft nodig van Teamlid 2:**
- genereer_recept() uit ai/recepten_ai.py
- genereer_boodschappenlijst() uit ai/recepten_ai.py
- check_api_configuratie() uit ai/recepten_ai.py

---

## Git Workflow

### Branch Strategie

```
main
  |
  +-- feature/database     (Teamlid 1)
  +-- feature/ai           (Teamlid 2)
  +-- feature/cli          (Teamlid 3)
```

### Commit Berichten

Gebruik prefix met teamlid nummer:
- `[T1] Database schema toegevoegd`
- `[T2] AI prompt engineering verbeterd`
- `[T3] Hoofdmenu afgerond`

### Pull Voordat Je Werkt

```bash
git pull origin main
```

### Push Na Je Werk

```bash
git add .
git commit -m "[T1] Beschrijving van wijziging"
git push
```

---

## Testen

### Teamlid 1: Database Testen

```bash
# Test database connectie
python -c "from database.db_connection import test_database_connectie; test_database_connectie()"
```

```sql
-- Test stored procedures in MySQL
CALL sp_haal_allergenen_op();
CALL sp_voeg_allergie_toe('test', 'test beschrijving');
CALL sp_verwijder_allergie(4);
```

### Teamlid 2: AI Testen

```bash
# Test AI verbinding (na API key invullen)
python -c "from ai.recepten_ai import test_ai_verbinding; test_ai_verbinding()"
```

### Teamlid 3: CLI Testen

```bash
# Start de applicatie
python main.py
```

Test scenarios:
1. Menu navigeren
2. Allergie toevoegen/verwijderen
3. Dieetwens toevoegen/verwijderen
4. Recept genereren (na API key)
5. Recept opslaan
6. Recept zoeken

---

## Veelvoorkomende Problemen

### "Module not found"

```bash
# Zorg dat je in de kookcompas map bent
cd kookcompas
python main.py
```

### "Database connectie mislukt"

1. Check of MySQL draait
2. Check wachtwoord in .env
3. Check of database bestaat:
   ```sql
   SHOW DATABASES;
   ```

### "API niet geconfigureerd"

1. Check of ANTHROPIC_API_KEY in .env staat
2. Check of de key correct is (begint met sk-ant-)
3. Check internetverbinding

### Import errors tussen modules

Alle modules hebben dit bovenaan:
```python
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

---

## Contactpunten

### Als je iets nodig hebt van een ander teamlid:

**Van Teamlid 1 nodig:**
- Database functies werken niet -> check schema.sql uitgevoerd?
- Query geeft fout -> check stored procedure parameters

**Van Teamlid 2 nodig:**
- AI geeft geen response -> check API key
- Recept format klopt niet -> check parse_recept_response()

**Van Teamlid 3 nodig:**
- Menu werkt niet -> check main.py imports
- Input validatie nodig -> gebruik helpers.py functies

---

## Checklist Voor Oplevering

### Teamlid 1:
- [ ] Database schema werkt
- [ ] Alle stored procedures getest
- [ ] Allergenen CRUD werkt
- [ ] Dieetwensen CRUD werkt
- [ ] Error handling compleet

### Teamlid 2:
- [ ] API key werkt
- [ ] Recept generatie werkt
- [ ] Allergenen worden vermeden
- [ ] Dieetwensen worden gevolgd
- [ ] Boodschappenlijst werkt

### Teamlid 3:
- [ ] Menu navigatie werkt
- [ ] Alle sub-menu's werken
- [ ] Recept flow compleet
- [ ] Error meldingen duidelijk
- [ ] App start en sluit netjes

### Samen:
- [ ] Alle tests uitgevoerd
- [ ] Demo geoefend
- [ ] Presentatie klaar
- [ ] Git commits netjes
