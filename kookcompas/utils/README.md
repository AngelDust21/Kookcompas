# Utils Module

## Overzicht

Deze module bevat helper functies die door de hele applicatie gebruikt worden.

## Bestanden

- **helpers.py**: Alle helper functies

## Functies

### Scherm en Weergave

- `maak_scherm_leeg()` - Maakt terminal leeg (Windows/Unix)
- `toon_lijn(karakter, breedte)` - Print horizontale lijn
- `toon_titel(tekst, karakter, breedte)` - Toont titel met lijnen
- `toon_menu_opties(opties, titel)` - Toont genummerd menu
- `toon_lijst_genummerd(items, start)` - Toont genummerde lijst

### Gebruikers Input

- `vraag_tekst(prompt, mag_leeg)` - Vraagt tekstinvoer
- `vraag_getal(prompt, min, max)` - Vraagt getal binnen bereik
- `vraag_ja_nee(prompt)` - Vraagt ja/nee antwoord
- `wacht_op_enter(bericht)` - Wacht op Enter toets
- `bevestig_actie(beschrijving)` - Vraagt bevestiging

### Data Verwerking

- `formatteer_datum(datum)` - Formatteert datetime naar string
- `splits_ingredienten(tekst)` - Splitst komma-gescheiden tekst
- `maak_ingredienten_tekst(lijst)` - Maakt bullet point tekst

### Berichten

- `toon_foutmelding(bericht)` - Toont foutmelding
- `toon_succes(bericht)` - Toont succesbericht

## Gebruik

```python
from utils.helpers import (
    maak_scherm_leeg,
    vraag_tekst,
    vraag_getal,
    vraag_ja_nee,
    toon_succes
)

# Scherm leegmaken
maak_scherm_leeg()

# Tekst vragen
naam = vraag_tekst("Naam: ")

# Getal vragen (0-10)
keuze = vraag_getal("Kies: ", 0, 10)

# Ja/nee vragen
if vraag_ja_nee("Opslaan? "):
    toon_succes("Opgeslagen")
```

## Validatie

De input functies doen automatisch validatie:
- `vraag_tekst`: Controleert op lege invoer (tenzij mag_leeg=True)
- `vraag_getal`: Controleert op geldig getal en bereik
- `vraag_ja_nee`: Accepteert ja/j/nee/n (case insensitive)

## Cross-platform

De functies werken op zowel Windows als Mac/Linux:
- `maak_scherm_leeg()` gebruikt 'cls' op Windows, 'clear' op Unix
