# Kookcompas - Praktische Start Handleiding

## Voor Je Begint

Deze handleiding helpt jullie om snel te starten met Kookcompas. Volg de stappen in volgorde.

**Wat je nodig hebt:**
- Computer met Windows, Mac of Linux
- Internet voor API calls
- Ongeveer 2 uur voor complete setup

**Wat je krijgt:**
- Werkende database
- Project structuur
- Eerste werkende code

---

## STAP 1: Software Checken

### Python Checken

Open terminal/command prompt:
```bash
python --version
```

Moet 3.10 of hoger zijn. Zo niet: download van python.org

### MySQL Checken

```bash
mysql --version
```

Of open MySQL Workbench om te zien of het werkt.

### Git Checken

```bash
git --version
```

---

## STAP 2: Claude API Key Verkrijgen

1. Ga naar console.anthropic.com
2. Maak account aan (gratis)
3. Ga naar "API Keys" in menu
4. Klik "Create Key"
5. Kopieer de key (begint met sk-ant-)
6. Bewaar ergens veilig

**Kosten:** Haiku is zeer goedkoop. 1000 recepten kost ongeveer 1 euro.

---

## STAP 3: Project Aanmaken

### GitHub Repository

1. Ga naar github.com
2. Klik "New repository"
3. Naam: kookcompas
4. Vink "Add README" aan
5. Create

### Repository Clonen

```bash
cd Desktop
git clone https://github.com/jouwnaam/kookcompas.git
cd kookcompas
```

### Project Structuur Maken

**Windows (PowerShell):**
```powershell
mkdir database, ai, crud, utils
New-Item main.py, config.py, requirements.txt, .env, .gitignore
New-Item database/schema.sql, database/db_connection.py, database/queries.py
New-Item ai/recepten_ai.py
New-Item crud/allergenen.py, crud/dieetwensen.py, crud/recepten.py
New-Item utils/helpers.py
```

**Mac/Linux:**
```bash
mkdir -p database ai crud utils
touch main.py config.py requirements.txt .env .gitignore
touch database/{schema.sql,db_connection.py,queries.py}
touch ai/recepten_ai.py
touch crud/{allergenen.py,dieetwensen.py,recepten.py}
touch utils/helpers.py
```

### Virtual Environment

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

Je ziet nu (venv) voor je prompt.

---

## STAP 4: Requirements Installeren

Maak `requirements.txt`:
```
mysql-connector-python==8.2.0
anthropic==0.18.1
python-dotenv==1.0.0
tabulate==0.9.0
```

Installeer:
```bash
pip install -r requirements.txt
```

---

## STAP 5: Database Aanmaken

### Database en Tabellen

Open MySQL Workbench of terminal en voer uit:

```sql
-- Database maken
CREATE DATABASE IF NOT EXISTS kookcompas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE kookcompas;

-- Tabellen maken
CREATE TABLE Allergenen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    naam VARCHAR(50) UNIQUE NOT NULL,
    beschrijving VARCHAR(200),
    aangemaakt_op DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Dieetwensen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    naam VARCHAR(50) UNIQUE NOT NULL,
    beschrijving VARCHAR(200),
    aangemaakt_op DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Recepten (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titel VARCHAR(100) NOT NULL,
    categorie ENUM('Ontbijt', 'Lunch', 'Diner', 'Snack', 'Dessert') NOT NULL,
    ingredienten TEXT NOT NULL,
    instructies TEXT NOT NULL,
    bereidingstijd INT,
    personen INT DEFAULT 2,
    notities TEXT,
    opgeslagen_op DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_categorie (categorie)
);

-- Test data
INSERT INTO Allergenen (naam, beschrijving) VALUES
('noten', 'Alle soorten noten inclusief pinda'),
('lactose', 'Melk en zuivelproducten'),
('gluten', 'Tarwe, rogge, gerst');

INSERT INTO Dieetwensen (naam, beschrijving) VALUES
('vegetarisch', 'Geen vlees of vis');
```

### Stored Procedures Toevoegen

```sql
USE kookcompas;

DELIMITER //

-- Allergie toevoegen
CREATE PROCEDURE sp_voeg_allergie_toe(
    IN p_naam VARCHAR(50),
    IN p_beschrijving VARCHAR(200)
)
BEGIN
    INSERT INTO Allergenen (naam, beschrijving)
    VALUES (LOWER(p_naam), p_beschrijving);
    SELECT LAST_INSERT_ID() AS id;
END //

-- Allergenen ophalen
CREATE PROCEDURE sp_haal_allergenen_op()
BEGIN
    SELECT id, naam, beschrijving FROM Allergenen ORDER BY naam;
END //

-- Allergie verwijderen
CREATE PROCEDURE sp_verwijder_allergie(IN p_id INT)
BEGIN
    DELETE FROM Allergenen WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //

-- Dieet toevoegen
CREATE PROCEDURE sp_voeg_dieet_toe(
    IN p_naam VARCHAR(50),
    IN p_beschrijving VARCHAR(200)
)
BEGIN
    INSERT INTO Dieetwensen (naam, beschrijving)
    VALUES (LOWER(p_naam), p_beschrijving);
    SELECT LAST_INSERT_ID() AS id;
END //

-- Dieet ophalen
CREATE PROCEDURE sp_haal_dieet_op()
BEGIN
    SELECT id, naam, beschrijving FROM Dieetwensen ORDER BY naam;
END //

-- Dieet verwijderen
CREATE PROCEDURE sp_verwijder_dieet(IN p_id INT)
BEGIN
    DELETE FROM Dieetwensen WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //

-- Recept toevoegen
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

-- Recepten ophalen
CREATE PROCEDURE sp_haal_recepten_op()
BEGIN
    SELECT id, titel, categorie, bereidingstijd, personen, opgeslagen_op
    FROM Recepten ORDER BY opgeslagen_op DESC;
END //

-- Recept detail
CREATE PROCEDURE sp_haal_recept_detail(IN p_id INT)
BEGIN
    SELECT * FROM Recepten WHERE id = p_id;
END //

-- Recept verwijderen
CREATE PROCEDURE sp_verwijder_recept(IN p_id INT)
BEGIN
    DELETE FROM Recepten WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //

-- Zoeken
CREATE PROCEDURE sp_zoek_recepten(IN p_zoekterm VARCHAR(100))
BEGIN
    SELECT id, titel, categorie, bereidingstijd
    FROM Recepten
    WHERE titel LIKE CONCAT('%', p_zoekterm, '%')
       OR ingredienten LIKE CONCAT('%', p_zoekterm, '%')
    ORDER BY opgeslagen_op DESC;
END //

DELIMITER ;
```

### Test Database

```sql
USE kookcompas;
CALL sp_haal_allergenen_op();
```

Moet 3 allergenen tonen.

---

## STAP 6: Configuratie Bestanden

### .env

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=jouw_wachtwoord
DB_DATABASE=kookcompas
ANTHROPIC_API_KEY=sk-ant-jouw-key-hier
```

### .gitignore

```
__pycache__/
*.py[cod]
venv/
.env
.vscode/
.idea/
.DS_Store
```

### config.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_DATABASE', 'kookcompas')
}

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

APP_NAME = "Kookcompas"
VERSION = "1.0.0"
```

---

## STAP 7: Database Connectie

### database/db_connection.py

```python
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

_connectie = None

def maak_connectie():
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
    global _connectie
    if _connectie and _connectie.is_connected():
        _connectie.close()
        _connectie = None

def voer_procedure_uit(naam, parameters=()):
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

### Test Database Connectie

```python
# test_db.py (tijdelijk testbestand)
from database.db_connection import maak_connectie, sluit_connectie

conn = maak_connectie()
if conn:
    print("Connectie gelukt")
    sluit_connectie()
else:
    print("Connectie mislukt")
```

Run: `python test_db.py`

---

## STAP 8: Eerste Menu

### utils/helpers.py

```python
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def toon_lijn(karakter='=', lengte=40):
    print(karakter * lengte)

def vraag_niet_leeg(prompt):
    while True:
        invoer = input(prompt).strip()
        if invoer:
            return invoer
        print("Invoer mag niet leeg zijn")

def vraag_getal(prompt, min_val=0, max_val=100):
    while True:
        try:
            getal = int(input(prompt).strip())
            if min_val <= getal <= max_val:
                return getal
            print(f"Kies tussen {min_val} en {max_val}")
        except ValueError:
            print("Voer een getal in")

def vraag_ja_nee(prompt):
    while True:
        antwoord = input(prompt).strip().lower()
        if antwoord in ['ja', 'j']:
            return True
        if antwoord in ['nee', 'n']:
            return False
        print("Antwoord ja of nee")

def wacht_op_enter():
    input("\nDruk op Enter om door te gaan...")
```

### main.py

```python
import os
from config import APP_NAME, VERSION
from database.db_connection import maak_connectie, sluit_connectie, voer_procedure_uit
from utils.helpers import clear_screen, toon_lijn, vraag_getal, wacht_op_enter

def toon_profiel():
    allergenen = voer_procedure_uit('sp_haal_allergenen_op')
    dieet = voer_procedure_uit('sp_haal_dieet_op')

    allergie_namen = [a['naam'] for a in allergenen] if allergenen else []
    dieet_namen = [d['naam'] for d in dieet] if dieet else []

    print("\nJouw profiel:")
    print(f"- Allergenen: {', '.join(allergie_namen) if allergie_namen else 'geen'}")
    print(f"- Dieet: {', '.join(dieet_namen) if dieet_namen else 'geen'}")

def toon_header():
    toon_lijn()
    print(f"  {APP_NAME} v{VERSION}")
    toon_lijn()
    toon_profiel()

def toon_menu():
    print("\nHoofdmenu:")
    print("1. Recept genereren")
    print("2. Mijn allergenen")
    print("3. Mijn dieetwensen")
    print("4. Opgeslagen recepten")
    print("0. Afsluiten")

def verwerk_keuze(keuze):
    if keuze == 1:
        print("\n[Recept genereren - nog niet klaar]")
        wacht_op_enter()
    elif keuze == 2:
        print("\n[Allergenen menu - nog niet klaar]")
        wacht_op_enter()
    elif keuze == 3:
        print("\n[Dieetwensen menu - nog niet klaar]")
        wacht_op_enter()
    elif keuze == 4:
        print("\n[Recepten menu - nog niet klaar]")
        wacht_op_enter()
    elif keuze == 0:
        return False
    return True

def main():
    if not maak_connectie():
        print("Database connectie mislukt")
        return

    actief = True
    while actief:
        clear_screen()
        toon_header()
        toon_menu()
        keuze = vraag_getal("\nKies een optie: ", 0, 4)
        actief = verwerk_keuze(keuze)

    print("\nTot ziens")
    sluit_connectie()

if __name__ == "__main__":
    main()
```

### Test Je App

```bash
python main.py
```

Je zou het menu moeten zien met je allergenen uit de database.

---

## STAP 9: Eerste Commit

```bash
git add .
git commit -m "Project setup met database en menu"
git push
```

---

## Week 1 Checklist

Na deze stappen moet je hebben:

- [ ] Python 3.10+ geinstalleerd
- [ ] MySQL draait
- [ ] Git werkt
- [ ] Claude API key verkregen
- [ ] Repository aangemaakt
- [ ] Project structuur compleet
- [ ] Virtual environment actief
- [ ] Dependencies geinstalleerd
- [ ] Database met tabellen
- [ ] Stored procedures werken
- [ ] .env met credentials
- [ ] Menu toont profiel uit database
- [ ] Eerste commit gedaan

---

## Veelvoorkomende Problemen

### "Module not found"

Zorg dat virtual environment actief is:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### "Access denied" bij MySQL

Check wachtwoord in .env bestand. Test handmatig:
```bash
mysql -u root -p
```

### "API key invalid"

Check of key correct gekopieerd is in .env (geen extra spaties).

### Import errors

Zorg dat je in de juiste folder zit:
```bash
cd kookcompas
python main.py
```

---

## Volgende Stappen

Nu de basis werkt, ga verder met:

1. **Week 1 rest:** CRUD voor allergenen afmaken
2. **Week 2:** AI integratie en recept generatie
3. **Week 3:** Recepten CRUD en zoeken
4. **Week 4:** Testing en presentatie

Zie 1_Fases.md voor gedetailleerde taken per week.

---

## Handige Commando's

```bash
# Virtual environment activeren
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# App starten
python main.py

# Git status
git status

# Commit en push
git add .
git commit -m "beschrijving"
git push

# MySQL starten
mysql -u root -p
USE kookcompas;
```

---

Succes met Kookcompas.
