# CRUD Module

## Overzicht

Deze module bevat alle Create, Read, Update en Delete operaties voor de drie entiteiten:
- Allergenen
- Dieetwensen
- Recepten

## Bestanden

- **allergenen.py**: CRUD voor allergenen beheer
- **dieetwensen.py**: CRUD voor dieetwensen beheer
- **recepten.py**: CRUD voor recepten beheer

## CRUD Operaties

### Allergenen (allergenen.py)

**Functies:**
- `toon_allergenen_lijst()` - READ: Toont alle allergenen
- `allergie_toevoegen()` - CREATE: Voegt allergie toe
- `allergie_verwijderen()` - DELETE: Verwijdert allergie
- `haal_allergie_namen()` - READ: Haalt alleen namen op
- `allergenen_menu()` - Sub-menu voor allergenen

**Menu opties:**
1. Allergie toevoegen
2. Allergie verwijderen
0. Terug

### Dieetwensen (dieetwensen.py)

**Functies:**
- `toon_dieetwensen_lijst()` - READ: Toont alle dieetwensen
- `dieetwens_toevoegen()` - CREATE: Voegt dieetwens toe
- `dieetwens_verwijderen()` - DELETE: Verwijdert dieetwens
- `haal_dieet_namen()` - READ: Haalt alleen namen op
- `dieetwensen_menu()` - Sub-menu voor dieetwensen

**Menu opties:**
1. Dieetwens toevoegen
2. Dieetwens verwijderen
0. Terug

### Recepten (recepten.py)

**Functies:**
- `toon_recepten_overzicht()` - READ: Toont alle recepten (kort)
- `toon_recept_volledig(id)` - READ: Toont recept details
- `bekijk_recept_detail()` - Menu voor details bekijken
- `bewerk_notities(id)` - UPDATE: Wijzigt notities
- `verwijder_recept_actie(id, titel)` - DELETE: Verwijdert recept
- `zoek_in_recepten()` - READ: Zoekt recepten
- `filter_recepten()` - READ: Filtert op categorie
- `recepten_menu()` - Sub-menu voor recepten

**Menu opties:**
1. Recept details bekijken
2. Recept zoeken
3. Filter op categorie
4. Recept verwijderen
0. Terug

## Structuur

Elke module volgt dezelfde structuur:
1. Imports
2. Lijst/Overzicht functies (READ)
3. Toevoeg functies (CREATE)
4. Wijzig functies (UPDATE) - alleen recepten
5. Verwijder functies (DELETE)
6. Helper functies
7. Menu functie

## Gebruik

```python
from crud.allergenen import allergenen_menu, haal_allergie_namen
from crud.dieetwensen import dieetwensen_menu, haal_dieet_namen
from crud.recepten import recepten_menu

# Start een sub-menu
allergenen_menu()

# Haal alleen namen op voor AI
allergenen = haal_allergie_namen()
dieetwensen = haal_dieet_namen()
```

## Relatie met Database

De CRUD modules gebruiken de queries uit database/queries.py:
- Geen directe SQL in deze modules
- Alle database operaties via stored procedures
- Foutafhandeling in database laag
