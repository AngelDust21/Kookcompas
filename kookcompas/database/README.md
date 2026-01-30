# Database Module

## Overzicht

Deze module beheert alle database operaties voor Kookcompas.

## Bestanden

- **schema.sql**: Database schema met tabellen en stored procedures
- **db_connection.py**: Database connectie beheer
- **queries.py**: Python wrapper functies voor stored procedures

## Database Schema

### Tabellen

**Allergenen**
- id (INT, AUTO_INCREMENT, PRIMARY KEY)
- naam (VARCHAR 50, UNIQUE, NOT NULL)
- beschrijving (VARCHAR 200)
- aangemaakt_op (DATETIME)

**Dieetwensen**
- id (INT, AUTO_INCREMENT, PRIMARY KEY)
- naam (VARCHAR 50, UNIQUE, NOT NULL)
- beschrijving (VARCHAR 200)
- aangemaakt_op (DATETIME)

**Recepten**
- id (INT, AUTO_INCREMENT, PRIMARY KEY)
- titel (VARCHAR 100, NOT NULL)
- categorie (ENUM: Ontbijt, Lunch, Diner, Snack, Dessert)
- ingredienten (TEXT)
- instructies (TEXT)
- bereidingstijd (INT)
- personen (INT, DEFAULT 2)
- notities (TEXT)
- opgeslagen_op (DATETIME)

## Stored Procedures

### Allergenen
- sp_voeg_allergie_toe(naam, beschrijving)
- sp_haal_allergenen_op()
- sp_verwijder_allergie(id)
- sp_zoek_allergie(naam)

### Dieetwensen
- sp_voeg_dieet_toe(naam, beschrijving)
- sp_haal_dieet_op()
- sp_verwijder_dieet(id)

### Recepten
- sp_voeg_recept_toe(titel, categorie, ingredienten, instructies, bereidingstijd, personen)
- sp_haal_recepten_op()
- sp_haal_recept_detail(id)
- sp_verwijder_recept(id)
- sp_update_notities(id, notities)
- sp_zoek_recepten(zoekterm)
- sp_filter_categorie(categorie)
- sp_tel_recepten()

## Setup

1. Start MySQL
2. Open MySQL Workbench of terminal
3. Voer schema.sql uit:
   ```sql
   SOURCE pad/naar/schema.sql
   ```
4. Vul de database gegevens in .env

## Gebruik

```python
from database.queries import haal_alle_allergenen, voeg_allergie_toe

# Allergenen ophalen
allergenen = haal_alle_allergenen()

# Allergie toevoegen
voeg_allergie_toe('noten', 'Alle soorten noten')
```

## Foutafhandeling

De module vangt database fouten op en geeft gebruiksvriendelijke meldingen:
- Duplicate entry: "Deze waarde bestaat al"
- Connection error: "Kon geen verbinding maken"
- Query error: Technische details worden gelogd
