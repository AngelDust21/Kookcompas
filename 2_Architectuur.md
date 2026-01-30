# Kookcompas - Technische Architectuur

## Systeem Overzicht

Kookcompas is een CLI applicatie die gebruikers helpt recepten te genereren met AI, rekening houdend met hun allergenen en dieetwensen.

**Hoofdcomponenten:**
- CLI Menu (gebruikersinterface)
- Database Layer (MySQL opslag)
- AI Module (Claude Haiku)
- CRUD Modules (allergenen, dieet, recepten)

**Data Flow:**
```
Gebruiker -> Menu -> CRUD/AI -> Database
                        |
                        v
                   Claude API
```

---

## Technology Stack

**Backend:**
- Python 3.10 of hoger
- MySQL 8.0

**Libraries:**
- mysql-connector-python (database)
- anthropic (Claude AI)
- python-dotenv (environment variables)
- tabulate (mooie tabellen in terminal)

**AI:**
- Claude Haiku via Anthropic API
- Goedkoop en snel
- Goed voor tekst generatie

---

## Database Design

### Tabellen Overzicht

```
Allergenen
    |
    v
[Gebruiker profiel - opgeslagen allergenen]

Dieetwensen
    |
    v
[Gebruiker profiel - opgeslagen dieetwensen]

Recepten
    |
    v
[Opgeslagen/gegenereerde recepten]
```

### Tabel: Allergenen

**Doel:** Opslag van allergenen van de gebruiker

**Velden:**
- id: INT, AUTO_INCREMENT, PRIMARY KEY
- naam: VARCHAR(50), UNIQUE, NOT NULL
  - Naam van allergie (bijv. "noten", "lactose")
- beschrijving: VARCHAR(200), NULL
  - Optionele uitleg
- aangemaakt_op: DATETIME, DEFAULT CURRENT_TIMESTAMP

**Voorbeelden:**
- noten, "Alle soorten noten inclusief pinda"
- lactose, "Melkproducten"
- gluten, "Tarwe, rogge, gerst"
- ei, "Eieren en ei-producten"
- schaaldieren, "Garnalen, krab, kreeft"

### Tabel: Dieetwensen

**Doel:** Opslag van dieetvoorkeuren van de gebruiker

**Velden:**
- id: INT, AUTO_INCREMENT, PRIMARY KEY
- naam: VARCHAR(50), UNIQUE, NOT NULL
  - Naam van dieet (bijv. "vegetarisch")
- beschrijving: VARCHAR(200), NULL
  - Optionele uitleg
- aangemaakt_op: DATETIME, DEFAULT CURRENT_TIMESTAMP

**Voorbeelden:**
- vegetarisch, "Geen vlees of vis"
- veganistisch, "Geen dierlijke producten"
- keto, "Weinig koolhydraten, veel vet"
- halal, "Volgens islamitische regels"
- glutenvrij, "Geen gluten"

### Tabel: Recepten

**Doel:** Opslag van gegenereerde en opgeslagen recepten

**Velden:**
- id: INT, AUTO_INCREMENT, PRIMARY KEY
- titel: VARCHAR(100), NOT NULL
  - Naam van het recept
- categorie: ENUM('Ontbijt', 'Lunch', 'Diner', 'Snack', 'Dessert'), NOT NULL
  - Type maaltijd
- ingredienten: TEXT, NOT NULL
  - Lijst van ingredienten (als tekst)
- instructies: TEXT, NOT NULL
  - Bereidingsstappen
- bereidingstijd: INT, NULL
  - Tijd in minuten
- personen: INT, DEFAULT 2
  - Aantal porties
- notities: TEXT, NULL
  - Eigen notities van gebruiker
- opgeslagen_op: DATETIME, DEFAULT CURRENT_TIMESTAMP

**Indexes:**
- PRIMARY KEY op id
- INDEX op categorie (voor filtering)
- INDEX op opgeslagen_op (voor sortering)

---

## Stored Procedures

### Waarom Stored Procedures

- Vereist door de opdracht
- Houdt SQL logica bij database
- Veiliger tegen SQL injection
- Makkelijker te testen

### sp_voeg_allergie_toe

**Doel:** Allergie toevoegen

**Parameters:**
- IN p_naam VARCHAR(50)
- IN p_beschrijving VARCHAR(200)

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_voeg_allergie_toe(
    IN p_naam VARCHAR(50),
    IN p_beschrijving VARCHAR(200)
)
BEGIN
    INSERT INTO Allergenen (naam, beschrijving)
    VALUES (LOWER(p_naam), p_beschrijving);

    SELECT LAST_INSERT_ID() AS id;
END //
DELIMITER ;
```

### sp_haal_allergenen_op

**Doel:** Alle allergenen ophalen

**Parameters:** Geen

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_haal_allergenen_op()
BEGIN
    SELECT id, naam, beschrijving, aangemaakt_op
    FROM Allergenen
    ORDER BY naam;
END //
DELIMITER ;
```

### sp_verwijder_allergie

**Doel:** Allergie verwijderen op ID

**Parameters:**
- IN p_id INT

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_verwijder_allergie(
    IN p_id INT
)
BEGIN
    DELETE FROM Allergenen WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //
DELIMITER ;
```

### sp_voeg_dieet_toe

**Doel:** Dieetwens toevoegen

**Parameters:**
- IN p_naam VARCHAR(50)
- IN p_beschrijving VARCHAR(200)

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_voeg_dieet_toe(
    IN p_naam VARCHAR(50),
    IN p_beschrijving VARCHAR(200)
)
BEGIN
    INSERT INTO Dieetwensen (naam, beschrijving)
    VALUES (LOWER(p_naam), p_beschrijving);

    SELECT LAST_INSERT_ID() AS id;
END //
DELIMITER ;
```

### sp_haal_dieet_op

**Doel:** Alle dieetwensen ophalen

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_haal_dieet_op()
BEGIN
    SELECT id, naam, beschrijving, aangemaakt_op
    FROM Dieetwensen
    ORDER BY naam;
END //
DELIMITER ;
```

### sp_verwijder_dieet

**Doel:** Dieetwens verwijderen

**Parameters:**
- IN p_id INT

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_verwijder_dieet(
    IN p_id INT
)
BEGIN
    DELETE FROM Dieetwensen WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //
DELIMITER ;
```

### sp_voeg_recept_toe

**Doel:** Recept opslaan

**Parameters:**
- IN p_titel VARCHAR(100)
- IN p_categorie VARCHAR(20)
- IN p_ingredienten TEXT
- IN p_instructies TEXT
- IN p_bereidingstijd INT
- IN p_personen INT

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_voeg_recept_toe(
    IN p_titel VARCHAR(100),
    IN p_categorie VARCHAR(20),
    IN p_ingredienten TEXT,
    IN p_instructies TEXT,
    IN p_bereidingstijd INT,
    IN p_personen INT
)
BEGIN
    INSERT INTO Recepten (titel, categorie, ingredienten, instructies, bereidingstijd, personen)
    VALUES (p_titel, p_categorie, p_ingredienten, p_instructies, p_bereidingstijd, p_personen);

    SELECT LAST_INSERT_ID() AS id;
END //
DELIMITER ;
```

### sp_haal_recepten_op

**Doel:** Alle recepten ophalen

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_haal_recepten_op()
BEGIN
    SELECT id, titel, categorie, bereidingstijd, personen, opgeslagen_op
    FROM Recepten
    ORDER BY opgeslagen_op DESC;
END //
DELIMITER ;
```

### sp_haal_recept_detail

**Doel:** Een recept ophalen met alle details

**Parameters:**
- IN p_id INT

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_haal_recept_detail(
    IN p_id INT
)
BEGIN
    SELECT * FROM Recepten WHERE id = p_id;
END //
DELIMITER ;
```

### sp_verwijder_recept

**Doel:** Recept verwijderen

**Parameters:**
- IN p_id INT

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_verwijder_recept(
    IN p_id INT
)
BEGIN
    DELETE FROM Recepten WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //
DELIMITER ;
```

### sp_zoek_recepten

**Doel:** Zoeken in recepten

**Parameters:**
- IN p_zoekterm VARCHAR(100)

**SQL:**
```sql
DELIMITER //
CREATE PROCEDURE sp_zoek_recepten(
    IN p_zoekterm VARCHAR(100)
)
BEGIN
    SELECT id, titel, categorie, bereidingstijd, opgeslagen_op
    FROM Recepten
    WHERE titel LIKE CONCAT('%', p_zoekterm, '%')
       OR ingredienten LIKE CONCAT('%', p_zoekterm, '%')
    ORDER BY opgeslagen_op DESC;
END //
DELIMITER ;
```

---

## Code Architectuur

### Project Structuur

```
kookcompas/
├── main.py                 # Start punt, menu loop
├── config.py               # Configuratie
├── requirements.txt        # Dependencies
├── .env                    # API keys (NIET in git)
├── .env.example            # Template
├── .gitignore              # Git ignore
├── README.md               # Documentatie
│
├── database/
│   ├── schema.sql          # Database schema
│   ├── db_connection.py    # Connectie beheer
│   └── queries.py          # Query functies
│
├── ai/
│   └── recepten_ai.py      # Claude API integratie
│
├── crud/
│   ├── allergenen.py       # CRUD allergenen
│   ├── dieetwensen.py      # CRUD dieetwensen
│   └── recepten.py         # CRUD recepten
│
└── utils/
    └── helpers.py          # Helper functies
```

### Module Beschrijvingen

**main.py:**
- Start de applicatie
- Toont welkom bericht
- Menu loop
- Roept CRUD en AI functies aan
- Handelt keuzes af

**config.py:**
- Database configuratie
- API configuratie
- Constanten (categorien, etc)

**database/db_connection.py:**
- Functie maak_connectie()
- Functie sluit_connectie()
- Error handling

**database/queries.py:**
- Wrapper functies voor stored procedures
- Elke stored procedure heeft Python functie

**ai/recepten_ai.py:**
- Functie genereer_recept()
- Prompt bouwen
- API call
- Response parsing

**crud/allergenen.py:**
- Functie toon_allergenen()
- Functie voeg_allergie_toe()
- Functie verwijder_allergie()
- Menu voor allergenen

**crud/dieetwensen.py:**
- Functie toon_dieetwensen()
- Functie voeg_dieet_toe()
- Functie verwijder_dieet()
- Menu voor dieetwensen

**crud/recepten.py:**
- Functie toon_recepten()
- Functie toon_recept_detail()
- Functie sla_recept_op()
- Functie verwijder_recept()
- Functie zoek_recepten()

**utils/helpers.py:**
- Functie clear_screen()
- Functie vraag_input()
- Functie toon_lijn()
- Functie format_datum()

---

## AI Integratie

### Claude Haiku

**Waarom Haiku:**
- Goedkoopste Claude model
- Snel (< 2 seconden response)
- Goed genoeg voor recepten
- Begrijpt Nederlands

**Kosten:**
- Input: $0.25 per miljoen tokens
- Output: $1.25 per miljoen tokens
- 1 recept is ongeveer 500 tokens
- 1000 recepten kost ongeveer $1

### Prompt Structuur

**Systeem Prompt:**
```
Je bent een professionele chef-kok die Nederlandse recepten maakt.
Je houdt altijd rekening met allergenen en dieetwensen.
Je geeft duidelijke, stapsgewijze instructies.
Je antwoordt altijd in het Nederlands.
```

**Gebruiker Prompt:**
```
Maak een recept met de volgende ingredienten: {ingredienten}

Allergenen om te vermijden: {allergenen_lijst}
Dieetwensen: {dieet_lijst}

Geef het recept in dit formaat:
TITEL: [naam van het gerecht]
CATEGORIE: [Ontbijt/Lunch/Diner/Snack/Dessert]
TIJD: [bereidingstijd in minuten]
PERSONEN: [aantal porties]

INGREDIENTEN:
- [ingrediënt 1]
- [ingrediënt 2]
...

BEREIDING:
1. [stap 1]
2. [stap 2]
...
```

### Code Voorbeeld

```python
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC_API_KEY')
)

def genereer_recept(ingredienten, allergenen, dieetwensen):
    """
    Genereer een recept met Claude Haiku

    Args:
        ingredienten: lijst van ingredienten
        allergenen: lijst van allergenen om te vermijden
        dieetwensen: lijst van dieetwensen

    Returns:
        dict met recept informatie
    """

    # Bouw de prompt
    ingredienten_tekst = ", ".join(ingredienten)
    allergenen_tekst = ", ".join(allergenen) if allergenen else "geen"
    dieet_tekst = ", ".join(dieetwensen) if dieetwensen else "geen"

    prompt = f"""Maak een recept met de volgende ingredienten: {ingredienten_tekst}

Allergenen om te vermijden: {allergenen_tekst}
Dieetwensen: {dieet_tekst}

Geef het recept in dit formaat:
TITEL: [naam van het gerecht]
CATEGORIE: [Ontbijt/Lunch/Diner/Snack/Dessert]
TIJD: [bereidingstijd in minuten]
PERSONEN: [aantal porties]

INGREDIENTEN:
- [ingrediënt 1]
- [ingrediënt 2]
...

BEREIDING:
1. [stap 1]
2. [stap 2]
..."""

    try:
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            system="Je bent een professionele chef-kok die Nederlandse recepten maakt. Je houdt altijd rekening met allergenen en dieetwensen.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_tekst = message.content[0].text
        return parse_recept(response_tekst)

    except Exception as fout:
        print(f"AI fout: {fout}")
        return None

def parse_recept(tekst):
    """
    Parse AI response naar dictionary
    """
    recept = {
        'titel': '',
        'categorie': 'Diner',
        'bereidingstijd': 30,
        'personen': 2,
        'ingredienten': '',
        'instructies': ''
    }

    regels = tekst.split('\n')

    huidige_sectie = None
    ingredienten_lijst = []
    instructies_lijst = []

    for regel in regels:
        regel = regel.strip()

        if regel.startswith('TITEL:'):
            recept['titel'] = regel.replace('TITEL:', '').strip()
        elif regel.startswith('CATEGORIE:'):
            cat = regel.replace('CATEGORIE:', '').strip()
            if cat in ['Ontbijt', 'Lunch', 'Diner', 'Snack', 'Dessert']:
                recept['categorie'] = cat
        elif regel.startswith('TIJD:'):
            tijd = regel.replace('TIJD:', '').strip()
            # Haal getal uit tekst
            cijfers = ''.join(c for c in tijd if c.isdigit())
            if cijfers:
                recept['bereidingstijd'] = int(cijfers)
        elif regel.startswith('PERSONEN:'):
            pers = regel.replace('PERSONEN:', '').strip()
            cijfers = ''.join(c for c in pers if c.isdigit())
            if cijfers:
                recept['personen'] = int(cijfers)
        elif regel.startswith('INGREDIENTEN:'):
            huidige_sectie = 'ingredienten'
        elif regel.startswith('BEREIDING:'):
            huidige_sectie = 'bereiding'
        elif huidige_sectie == 'ingredienten' and regel.startswith('-'):
            ingredienten_lijst.append(regel)
        elif huidige_sectie == 'bereiding' and regel:
            instructies_lijst.append(regel)

    recept['ingredienten'] = '\n'.join(ingredienten_lijst)
    recept['instructies'] = '\n'.join(instructies_lijst)

    return recept
```

---

## Database Connectie

### Connection Pattern

```python
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

_connectie = None

def maak_connectie():
    """
    Maak database connectie
    """
    global _connectie

    if _connectie is not None and _connectie.is_connected():
        return _connectie

    try:
        _connectie = mysql.connector.connect(**DB_CONFIG)
        return _connectie
    except Error as fout:
        print(f"Database fout: {fout}")
        return None

def sluit_connectie():
    """
    Sluit database connectie
    """
    global _connectie
    if _connectie and _connectie.is_connected():
        _connectie.close()
        _connectie = None
```

### Query Uitvoering

```python
def voer_procedure_uit(naam, parameters=()):
    """
    Voer stored procedure uit

    Args:
        naam: naam van stored procedure
        parameters: tuple met parameters

    Returns:
        lijst met resultaten of None bij fout
    """
    conn = maak_connectie()
    if not conn:
        return None

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.callproc(naam, parameters)

        resultaten = []
        for result in cursor.stored_results():
            resultaten.extend(result.fetchall())

        cursor.close()
        conn.commit()
        return resultaten

    except Error as fout:
        print(f"Query fout: {fout}")
        return None
```

---

## Menu Structuur

### Hoofdmenu

```
=====================================
     KOOKCOMPAS - Recepten met AI
=====================================

Jouw profiel:
- Allergenen: noten, lactose
- Dieet: vegetarisch

Hoofdmenu:
1. Recept genereren
2. Mijn allergenen
3. Mijn dieetwensen
4. Opgeslagen recepten
0. Afsluiten

Kies een optie:
```

### Sub-menu Allergenen

```
--- Mijn Allergenen ---

Huidige allergenen:
1. noten
2. lactose
3. ei

Opties:
1. Allergie toevoegen
2. Allergie verwijderen
0. Terug naar hoofdmenu

Kies een optie:
```

### Sub-menu Dieetwensen

```
--- Mijn Dieetwensen ---

Huidige dieetwensen:
1. vegetarisch

Opties:
1. Dieetwens toevoegen
2. Dieetwens verwijderen
0. Terug naar hoofdmenu

Kies een optie:
```

### Sub-menu Recepten

```
--- Opgeslagen Recepten ---

ID  Titel                    Categorie  Tijd
--  -----                    ---------  ----
1   Pasta met Tomatensaus    Diner      25 min
2   Pannenkoeken            Ontbijt    20 min
3   Groentesalade           Lunch      15 min

Opties:
1. Recept details bekijken
2. Recept zoeken
3. Recept verwijderen
0. Terug naar hoofdmenu

Kies een optie:
```

### Recept Generatie Flow

```
--- Recept Genereren ---

Welke ingredienten heb je? (gescheiden door komma)
> pasta, tomaat, ui, knoflook, olijfolie

Even denken...

=====================================
PASTA MET TOMATENSAUS
=====================================
Categorie: Diner
Bereidingstijd: 25 minuten
Personen: 2

INGREDIENTEN:
- 250g pasta
- 4 tomaten
- 1 ui
- 2 teentjes knoflook
- 2 el olijfolie
- Zout en peper

BEREIDING:
1. Kook de pasta volgens de verpakking
2. Snipper de ui en knoflook
3. Fruit de ui in olijfolie
4. Voeg de knoflook toe
5. Snijd de tomaten en voeg toe
6. Laat 10 minuten sudderen
7. Meng met de pasta
8. Breng op smaak met zout en peper

=====================================

Wil je dit recept opslaan? (ja/nee)
> ja

Recept opgeslagen.

Druk op Enter om door te gaan...
```

---

## Error Handling

### Soorten Errors

**Database Errors:**
- Connectie mislukt
- Query mislukt
- Duplicate key (allergie bestaat al)

**AI Errors:**
- API key ongeldig
- Rate limit bereikt
- Timeout
- Onverwachte response

**Input Errors:**
- Lege invoer
- Ongeldige keuze
- Niet-bestaand ID

### Error Handling Pattern

```python
def veilige_operatie(functie, *args, fallback=None):
    """
    Voer functie veilig uit met error handling
    """
    try:
        return functie(*args)
    except Exception as fout:
        print(f"Er ging iets mis: {fout}")
        return fallback
```

### Gebruikers Foutmeldingen

**Goed:**
- "Die allergie staat al in je profiel"
- "Geen recept gevonden met die zoekterm"
- "Voer minimaal 1 ingrediënt in"

**Fout:**
- "Error: DuplicateKeyError"
- "Exception occurred"
- "NULL value"

---

## Input Validatie

### Validatie Functies

```python
def vraag_niet_leeg(prompt):
    """
    Vraag input die niet leeg mag zijn
    """
    while True:
        invoer = input(prompt).strip()
        if invoer:
            return invoer
        print("Invoer mag niet leeg zijn")

def vraag_getal(prompt, min_waarde=1, max_waarde=100):
    """
    Vraag een getal binnen bereik
    """
    while True:
        invoer = input(prompt).strip()
        try:
            getal = int(invoer)
            if min_waarde <= getal <= max_waarde:
                return getal
            print(f"Kies een getal tussen {min_waarde} en {max_waarde}")
        except ValueError:
            print("Voer een geldig getal in")

def vraag_ja_nee(prompt):
    """
    Vraag ja of nee
    """
    while True:
        invoer = input(prompt).strip().lower()
        if invoer in ['ja', 'j', 'yes', 'y']:
            return True
        if invoer in ['nee', 'n', 'no']:
            return False
        print("Antwoord met ja of nee")
```

---

## Configuratie

### config.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Database
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_DATABASE', 'kookcompas')
}

# AI
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
AI_MODEL = "claude-3-haiku-20240307"
AI_MAX_TOKENS = 1024

# App
APP_NAME = "Kookcompas"
VERSION = "1.0.0"

# Categorieën
CATEGORIEEN = ['Ontbijt', 'Lunch', 'Diner', 'Snack', 'Dessert']

# Standaard allergenen (voor suggesties)
STANDAARD_ALLERGENEN = [
    'noten',
    'gluten',
    'lactose',
    'ei',
    'schaaldieren',
    'soja',
    'selderij',
    'mosterd'
]

# Standaard dieetwensen (voor suggesties)
STANDAARD_DIEET = [
    'vegetarisch',
    'veganistisch',
    'keto',
    'halal',
    'glutenvrij',
    'lactosevrij'
]
```

### .env.example

```
# Database configuratie
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=jouw_wachtwoord
DB_DATABASE=kookcompas

# Anthropic API
ANTHROPIC_API_KEY=sk-ant-jouw-api-key-hier
```

### .gitignore

```
# Python
__pycache__/
*.py[cod]
venv/

# Environment
.env

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## Testing Checklist

### Database Tests

- [ ] Connectie maken lukt
- [ ] Allergie toevoegen lukt
- [ ] Duplicate allergie geeft foutmelding
- [ ] Allergie verwijderen lukt
- [ ] Niet-bestaande allergie verwijderen geeft melding
- [ ] Dieetwens toevoegen lukt
- [ ] Recept opslaan lukt
- [ ] Recept ophalen lukt
- [ ] Zoeken werkt

### AI Tests

- [ ] API connectie werkt
- [ ] Simpel recept wordt gegenereerd
- [ ] Allergenen worden vermeden
- [ ] Dieetwensen worden gevolgd
- [ ] Response wordt correct geparsed
- [ ] Error bij geen API key

### Menu Tests

- [ ] Hoofdmenu toont correct
- [ ] Alle opties werken
- [ ] Terug naar hoofdmenu werkt
- [ ] Afsluiten werkt
- [ ] Ongeldige input wordt afgehandeld

### Edge Cases

- [ ] Lege allergenen lijst
- [ ] Lege dieet lijst
- [ ] 1 ingrediënt
- [ ] 20 ingredienten
- [ ] Speciale tekens in input
- [ ] Zeer lang recept

---

Dit document beschrijft de volledige technische architectuur van Kookcompas.
