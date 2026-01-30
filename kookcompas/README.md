# Kookcompas

Slimme recepten generator met AI - CLI Applicatie

## Over Kookcompas

Kookcompas is een command-line applicatie die recepten genereert op basis van beschikbare ingredienten. De applicatie houdt rekening met allergenen en dieetwensen van de gebruiker.

## Features

- Recept generatie met AI (Claude Sonnet 4)
- Allergenen beheer (CRUD)
- Dieetwensen beheer (CRUD)
- Recepten opslaan en beheren (CRUD)
- Zoeken in recepten
- Boodschappenlijst genereren

## Vereisten

- Python 3.10 of hoger
- MySQL 8.0
- Anthropic API key (voor AI functionaliteit)

## Installatie

### 1. Repository clonen

```bash
git clone [repository-url]
cd kookcompas
```

### 2. Virtual environment aanmaken

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 3. Dependencies installeren

```bash
pip install -r requirements.txt
```

### 4. Database opzetten

Open MySQL Workbench of terminal en voer uit:

```sql
SOURCE database/schema.sql
```

Of kopieer de inhoud van schema.sql en voer uit in MySQL.

### 5. Configuratie

Kopieer .env.example naar .env en vul in:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=jouw_mysql_wachtwoord
DB_DATABASE=kookcompas
ANTHROPIC_API_KEY=sk-ant-jouw-api-key
```

### 6. API Key verkrijgen

1. Ga naar console.anthropic.com
2. Maak account aan
3. Ga naar API Keys
4. Maak nieuwe key aan
5. Kopieer naar .env

## Gebruik

Start de applicatie:

```bash
python main.py
```

### Hoofdmenu

```
=============================================
  Kookcompas v1.0.0
=============================================

Jouw profiel:
- Allergenen: noten, lactose
- Dieet: vegetarisch

Hoofdmenu:
1. Recept genereren
2. Mijn allergenen
3. Mijn dieetwensen
4. Opgeslagen recepten
0. Afsluiten
```

### Recept genereren

1. Kies optie 1
2. Voer ingredienten in (gescheiden door komma)
3. Wacht op AI respons
4. Kies of je het recept wilt opslaan

## Project Structuur

```
kookcompas/
├── main.py              # Hoofdapplicatie
├── config.py            # Configuratie
├── requirements.txt     # Dependencies
├── .env                 # Credentials (niet in git)
├── .env.example         # Template voor .env
├── .gitignore           # Git ignore
├── README.md            # Deze file
├── database/
│   ├── schema.sql       # Database schema
│   ├── db_connection.py # Connectie beheer
│   ├── queries.py       # Query functies
│   └── README.md        # Database documentatie
├── ai/
│   ├── recepten_ai.py   # AI integratie
│   └── README.md        # AI documentatie
├── crud/
│   ├── allergenen.py    # Allergenen CRUD
│   ├── dieetwensen.py   # Dieetwensen CRUD
│   ├── recepten.py      # Recepten CRUD
│   └── README.md        # CRUD documentatie
└── utils/
    ├── helpers.py       # Helper functies
    └── README.md        # Utils documentatie
```

## Taakverdeling

**Persoon 1 - Database Developer:**
- Database schema ontwerp
- Stored procedures
- Database connectie module
- CRUD functies allergenen/dieetwensen

**Persoon 2 - AI Developer:**
- Claude API integratie
- Prompt engineering
- Response parsing
- Error handling AI

**Persoon 3 - CLI Developer:**
- Menu systeem
- Gebruikers input/validatie
- Recept weergave
- Hoofd flow applicatie

## Technologie

- **Python 3.10+**: Programmeertaal
- **MySQL 8.0**: Database
- **Claude Sonnet 4**: AI model voor recepten
- **mysql-connector-python**: Database driver
- **anthropic**: Claude API library
- **python-dotenv**: Environment variabelen
- **tabulate**: Tabel weergave

## Probleemoplossing

### Database connectie mislukt

- Controleer of MySQL draait
- Check wachtwoord in .env
- Controleer of database bestaat

### AI werkt niet

- Check of API key is ingevuld in .env
- Controleer internetverbinding
- Check of anthropic library is geinstalleerd

### Import errors

- Activeer virtual environment
- Run pip install -r requirements.txt

## Licentie

Groepswerk Python - 2024

## Team

- Database Developer
- AI Developer
- CLI Developer
