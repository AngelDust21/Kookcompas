# Kookcompas - Setup Handleiding

Stap-voor-stap instructies om het project werkend te krijgen.

---

## Stap 1: Repository Clonen (Iedereen)

```bash
git clone [repository-url]
cd kookcompas
```

---

## Stap 2: Virtual Environment (Iedereen)

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

Je ziet nu `(venv)` voor je prompt.

---

## Stap 3: Dependencies Installeren (Iedereen)

```bash
pip install -r requirements.txt
```

Dit installeert:
- mysql-connector-python (database)
- anthropic (AI)
- python-dotenv (configuratie)
- tabulate (tabellen)

---

## Stap 4: Configuratie Bestand (Iedereen)

Open `.env` en vul in:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=JOUW_MYSQL_WACHTWOORD
DB_DATABASE=kookcompas
ANTHROPIC_API_KEY=
```

De API key komt later (Stap 6).

---

## Stap 5: Database Aanmaken (Teamlid 1)

### Optie A: MySQL Workbench

1. Open MySQL Workbench
2. Maak nieuwe connectie of gebruik bestaande
3. Open `database/schema.sql`
4. Klik Execute (bliksem icoon)

### Optie B: Command Line

```bash
mysql -u root -p < database/schema.sql
```

Of:

```bash
mysql -u root -p
```

Dan in MySQL:
```sql
SOURCE C:/volledig/pad/naar/kookcompas/database/schema.sql;
```

### Verificatie

```sql
USE kookcompas;
SHOW TABLES;
```

Output moet zijn:
```
+----------------------+
| Tables_in_kookcompas |
+----------------------+
| Allergenen           |
| Dieetwensen          |
| Recepten             |
+----------------------+
```

Test stored procedures:
```sql
CALL sp_haal_allergenen_op();
```

Output moet 3 allergenen tonen (noten, lactose, gluten).

---

## Stap 6: API Key Aanvragen (Teamlid 2)

1. Ga naar https://console.anthropic.com
2. Klik "Sign Up" (of "Log In" als je account hebt)
3. Verifieer email
4. Ga naar "API Keys" in het menu
5. Klik "Create Key"
6. Geef een naam: "Kookcompas"
7. Kopieer de key (begint met `sk-ant-`)

### Key Invullen

Open `.env` en vul in:
```
ANTHROPIC_API_KEY=sk-ant-api03-jouw-volledige-key-hier
```

### Kosten

- Claude Sonnet 4 is betaalbaar
- Je krijgt gratis credits bij aanmelden

---

## Stap 7: Test de Applicatie (Iedereen)

### Basis Test (zonder AI)

```bash
python main.py
```

Je moet zien:
```
=============================================
  Welkom bij Kookcompas v1.0.0
=============================================

Slimme recepten generator met AI
Houdt rekening met allergenen en dieetwensen

Druk op Enter om te beginnen...
```

Test deze onderdelen:
1. Menu toont correct
2. Optie 2 (Allergenen) werkt
3. Optie 3 (Dieetwensen) werkt
4. Optie 4 (Recepten) toont het voorbeeldrecept

### AI Test (na API key)

```bash
python -c "from ai.recepten_ai import test_ai_verbinding; test_ai_verbinding()"
```

Output moet zijn: "AI verbinding werkt"

Dan in de app:
1. Kies optie 1 (Recept genereren)
2. Voer in: pasta, tomaat, ui
3. Wacht op recept
4. Test opslaan

---

## Stap 8: Dagelijks Werken

### Bij Start Van Je Sessie

```bash
cd kookcompas
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
git pull
```

### Bij Einde Van Je Sessie

```bash
git add .
git commit -m "[T1/T2/T3] Beschrijving"
git push
```

---

## Troubleshooting

### "python not found"

Gebruik `python3` in plaats van `python`:
```bash
python3 main.py
```

### "mysql not found"

MySQL is niet in PATH. Gebruik volledige pad of voeg toe aan PATH:
- Windows: `C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe`

### "Access denied for user 'root'"

Verkeerd wachtwoord in .env. Check je MySQL wachtwoord.

### "Unknown database 'kookcompas'"

Database nog niet aangemaakt. Voer schema.sql uit (Stap 5).

### "No module named 'mysql'"

Dependencies niet geinstalleerd:
```bash
pip install -r requirements.txt
```

### "anthropic.AuthenticationError"

API key onjuist of niet ingevuld. Check .env bestand.

---

## Handige Commando's

### Python

```bash
# App starten
python main.py

# Database test
python -c "from database.db_connection import test_database_connectie; test_database_connectie()"

# AI test
python -c "from ai.recepten_ai import test_ai_verbinding; test_ai_verbinding()"
```

### MySQL

```sql
-- Alle data bekijken
USE kookcompas;
SELECT * FROM Allergenen;
SELECT * FROM Dieetwensen;
SELECT * FROM Recepten;

-- Database resetten
DROP DATABASE kookcompas;
SOURCE schema.sql;
```

### Git

```bash
# Status bekijken
git status

# Wijzigingen bekijken
git diff

# Alles committen
git add .
git commit -m "Bericht"
git push

# Updates ophalen
git pull
```

---

## Mappenstructuur Na Setup

```
kookcompas/
├── venv/                 # Virtual environment (NIET in git)
├── __pycache__/          # Python cache (NIET in git)
├── .env                  # Credentials (NIET in git)
├── .env.example          # Template
├── .gitignore
├── requirements.txt
├── README.md
├── TEAMWERK.md
├── SETUP.md              # Dit bestand
├── VOORTGANG.md
├── main.py
├── config.py
├── database/
│   ├── __init__.py
│   ├── schema.sql
│   ├── db_connection.py
│   ├── queries.py
│   └── README.md
├── ai/
│   ├── __init__.py
│   ├── recepten_ai.py
│   └── README.md
├── crud/
│   ├── __init__.py
│   ├── allergenen.py
│   ├── dieetwensen.py
│   ├── recepten.py
│   └── README.md
└── utils/
    ├── __init__.py
    ├── helpers.py
    └── README.md
```

---

## Klaar

Na deze stappen heb je een werkende Kookcompas applicatie.

Volgende stappen:
1. Lees TEAMWERK.md voor samenwerking
2. Lees de README.md in je eigen map
3. Begin met testen en verfijnen
