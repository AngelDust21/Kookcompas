
s# Kookcompas - Fases en Planning

## Project Overzicht

**Naam:** Kookcompas - Slimme Recepten Generator met AI
**Type:** CLI Applicatie met AI (OPTIE A)
**Duur:** 4 weken
**Team:** 3 personen
**Niveau:** Beginners
**Technologie:** Python, MySQL, Claude Haiku API

---

## Wat Is Kookcompas

Een command-line tool waarmee gebruikers:
1. Hun allergenen en dieetwensen opslaan (CRUD)
2. Ingredienten invoeren die ze hebben
3. AI vraagt om een recept dat past bij hun restricties
4. Recepten opslaan als favorieten

**Voorbeeld gebruik:**
```
Welkom bij Kookcompas

Jouw profiel:
- Allergenen: noten, lactose
- Dieet: vegetarisch

Welke ingredienten heb je? kip, rijst, paprika, ui

Even denken...

RECEPT: Paprika Kip met Rijst
Categorie: Hoofdgerecht
Tijd: 30 minuten
Personen: 2

Ingredienten:
- 200g kipfilet
- 150g rijst
- 1 paprika
- 1 ui
...

Wil je dit recept opslaan? (ja/nee)
```

---

## Probleem en Oplossing

**Probleem:**
- Mensen weten niet wat te koken met ingredienten die ze hebben
- Allergenen en dieetwensen maken koken lastig
- Recepten zoeken kost tijd

**Oplossing:**
- AI genereert recepten op basis van beschikbare ingredienten
- Systeem onthoudt allergenen en dieet
- Recepten worden automatisch aangepast aan restricties

**Meerwaarde:**
- Tijdswinst: direct recept ipv lang zoeken
- Veiligheid: geen allergenen in recepten
- Personalisatie: past bij dieetwensen
- Geen voedselverspilling: gebruik wat je hebt

---

## CRUD Overzicht

De applicatie heeft duidelijke CRUD operaties:

**CREATE (Toevoegen):**
- Allergie toevoegen aan profiel
- Dieetwens toevoegen aan profiel
- Recept opslaan als favoriet

**READ (Bekijken):**
- Allergenen tonen
- Dieetwensen tonen
- Opgeslagen recepten bekijken
- Recept detail bekijken

**UPDATE (Wijzigen):**
- Allergie aanpassen
- Dieetwens aanpassen
- Recept notities wijzigen

**DELETE (Verwijderen):**
- Allergie verwijderen
- Dieetwens verwijderen
- Opgeslagen recept verwijderen

---

## Taakverdeling (3 Personen)

**Persoon 1: Database Developer**
- Database ontwerp en schema
- Stored procedures
- CRUD functies voor allergenen
- CRUD functies voor dieetwensen
- Database connectie module

**Persoon 2: AI Developer**
- Claude API integratie
- Prompt engineering voor recepten
- Recept generatie functie
- Recept opslaan functie
- Error handling AI calls

**Persoon 3: CLI Developer**
- Menu systeem
- Gebruikers input en validatie
- Recept weergave (mooie output)
- CRUD voor recepten
- Hoofd flow van applicatie

**Samen:**
- Git repository beheer
- Testing
- Documentatie
- Presentatie

---

## FASE 0: Voorbereiding

**Duur:** 1-2 dagen voor start
**Doel:** Alles klaarzetten

### Taken Iedereen

**Voor Docent:**
- [ ] Probleemstelling schrijven (half A4)
- [ ] Scope document (wat wel, wat niet)
- [ ] Taakverdeling schema
- [ ] Planning (dit document)

**Git Setup:**
- [ ] GitHub repository aanmaken: kookcompas
- [ ] Alle teamleden toegang geven
- [ ] README.md met project beschrijving
- [ ] .gitignore aanmaken

**Software Check:**
- [ ] Python 3.10+ geinstalleerd
- [ ] MySQL draait
- [ ] Git werkt
- [ ] Claude API key aangevraagd (console.anthropic.com)

**Communicatie:**
- [ ] Team chat (Discord/WhatsApp/Teams)
- [ ] Afspraak: wanneer werken we samen
- [ ] Afspraak: hoe verdelen we taken

### Wat Inleveren Bij Docent

Kort document met:
- Projectnaam: Kookcompas
- Probleem: Mensen weten niet wat te koken, allergenen zijn lastig
- Oplossing: AI recepten generator met allergie-beheer
- Team: 3 namen
- Planning: 4 weken, zie dit document

---

## FASE 1: Database en Basis

**Duur:** Week 1
**Doel:** Database werkt, menu toont, eerste CRUD

### Taken Persoon 1 (Database)

**Database Aanmaken:**
- [ ] Database kookcompas maken in MySQL
- [ ] schema.sql bestand schrijven

**Tabellen Maken:**
- [ ] Tabel Allergenen:
  - id (INT, AUTO_INCREMENT, PRIMARY KEY)
  - naam (VARCHAR 50, UNIQUE, NOT NULL)
  - beschrijving (VARCHAR 200)
  - aangemaakt_op (DATETIME)
- [ ] Tabel Dieetwensen:
  - id (INT, AUTO_INCREMENT, PRIMARY KEY)
  - naam (VARCHAR 50, UNIQUE, NOT NULL)
  - beschrijving (VARCHAR 200)
  - aangemaakt_op (DATETIME)
- [ ] Tabel Recepten:
  - id (INT, AUTO_INCREMENT, PRIMARY KEY)
  - titel (VARCHAR 100, NOT NULL)
  - categorie (ENUM: Ontbijt, Lunch, Diner, Snack, Dessert)
  - ingredienten (TEXT)
  - instructies (TEXT)
  - bereidingstijd (INT, minuten)
  - personen (INT)
  - notities (TEXT)
  - opgeslagen_op (DATETIME)

**Stored Procedures:**
- [ ] sp_voeg_allergie_toe(naam, beschrijving)
- [ ] sp_haal_allergenen_op()
- [ ] sp_verwijder_allergie(id)
- [ ] sp_voeg_dieet_toe(naam, beschrijving)
- [ ] sp_haal_dieet_op()
- [ ] sp_verwijder_dieet(id)

**Test Data:**
- [ ] 5 standaard allergenen toevoegen (noten, gluten, lactose, ei, schaaldieren)
- [ ] 5 standaard dieetwensen toevoegen (vegetarisch, veganistisch, keto, halal, glutenvrij)

**Database Connectie:**
- [ ] db_connection.py schrijven
- [ ] Connectie testen
- [ ] queries.py met basis functies

### Taken Persoon 2 (AI Setup)

**API Setup:**
- [ ] Account aanmaken op console.anthropic.com
- [ ] API key genereren
- [ ] .env bestand maken met key
- [ ] Test script schrijven om API te testen

**Eerste Prompt:**
- [ ] Simpele test prompt schrijven
- [ ] Response testen
- [ ] Begrijpen hoe Claude API werkt

**Library Installeren:**
- [ ] anthropic library toevoegen aan requirements.txt
- [ ] pip install anthropic
- [ ] Documentatie lezen

### Taken Persoon 3 (CLI Basis)

**Project Structuur:**
```
kookcompas/
├── main.py
├── config.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
├── database/
│   ├── schema.sql
│   ├── db_connection.py
│   └── queries.py
├── ai/
│   └── recepten_ai.py
├── crud/
│   ├── allergenen.py
│   ├── dieetwensen.py
│   └── recepten.py
└── utils/
    └── helpers.py
```

**Config.py:**
- [ ] Database settings
- [ ] API settings
- [ ] Constanten (categorien, etc)

**Main.py Basis:**
- [ ] Welkom bericht
- [ ] Hoofdmenu tonen:
  1. Recept genereren
  2. Mijn allergenen
  3. Mijn dieetwensen
  4. Opgeslagen recepten
  5. Instellingen
  0. Afsluiten
- [ ] Menu loop (while True)
- [ ] Keuze verwerking
- [ ] Placeholder functies

**Helpers:**
- [ ] clear_screen() functie
- [ ] input_met_validatie() functie
- [ ] toon_lijn() functie voor opmaak

### Sprint 1 Review

**Demo Eind Week 1:**
- Menu werkt en toont opties
- Database heeft tabellen met test data
- Allergenen CRUD werkt (toevoegen, tonen, verwijderen)
- API key werkt (simpele test)

**Git Check:**
- Minimaal 3 commits per persoon
- Iedereen heeft gepushed
- Code is gemerged naar main

---

## FASE 2: CRUD Compleet en AI Basis

**Duur:** Week 2
**Doel:** Alle CRUD werkt, AI genereert eerste recepten

### Taken Persoon 1 (CRUD Allergenen en Dieet)

**Allergenen CRUD Compleet:**
- [ ] Functie toon_allergenen()
- [ ] Functie voeg_allergie_toe()
- [ ] Functie verwijder_allergie()
- [ ] Menu integratie sub-menu allergenen:
  1. Toon mijn allergenen
  2. Allergie toevoegen
  3. Allergie verwijderen
  0. Terug

**Dieetwensen CRUD Compleet:**
- [ ] Functie toon_dieetwensen()
- [ ] Functie voeg_dieet_toe()
- [ ] Functie verwijder_dieet()
- [ ] Menu integratie sub-menu dieet:
  1. Toon mijn dieetwensen
  2. Dieetwens toevoegen
  3. Dieetwens verwijderen
  0. Terug

**Stored Procedures Extra:**
- [ ] sp_voeg_recept_toe(alle velden)
- [ ] sp_haal_recepten_op()
- [ ] sp_haal_recept_detail(id)
- [ ] sp_verwijder_recept(id)
- [ ] sp_update_recept_notities(id, notities)

### Taken Persoon 2 (AI Recept Generatie)

**Prompt Engineering:**
- [ ] Hoofd prompt schrijven voor recept generatie
- [ ] Prompt bevat:
  - Rol: Je bent een chef-kok
  - Allergenen lijst meegeven
  - Dieetwensen meegeven
  - Ingredienten die gebruiker heeft
  - Gewenste output formaat (titel, ingredienten, stappen, tijd)
- [ ] Testen met verschillende inputs
- [ ] Prompt verfijnen

**recepten_ai.py Module:**
- [ ] Functie genereer_recept(ingredienten, allergenen, dieet)
- [ ] API call naar Claude Haiku
- [ ] Response parsing
- [ ] Error handling (API errors, timeout)
- [ ] Rate limiting (niet te snel)

**Response Structuur:**
- [ ] Recept titel extraheren
- [ ] Ingredienten lijst extraheren
- [ ] Instructies extraheren
- [ ] Bereidingstijd extraheren
- [ ] Categorie bepalen
- [ ] Return als dictionary

### Taken Persoon 3 (Recept Flow)

**Recept Genereren Flow:**
- [ ] Functie vraag_ingredienten()
  - Vraag: "Welke ingredienten heb je?"
  - Input validatie (niet leeg)
  - Split op komma
- [ ] Functie toon_profiel()
  - Haal allergenen uit database
  - Haal dieetwensen uit database
  - Toon aan gebruiker
- [ ] Functie genereer_en_toon_recept()
  - Roep AI functie aan
  - Toon recept mooi geformatteerd
  - Vraag: "Opslaan als favoriet? (ja/nee)"

**Recept Weergave:**
- [ ] Mooie opmaak in terminal
- [ ] Duidelijke secties (titel, ingredienten, stappen)
- [ ] Leesbaar en overzichtelijk

**Menu Integratie:**
- [ ] Optie 1 werkt volledig
- [ ] Flow: ingredienten -> AI -> toon -> opslaan vraag

### Sprint 2 Review

**Demo Eind Week 2:**
- Allergenen volledig CRUD
- Dieetwensen volledig CRUD
- Recept genereren werkt met AI
- AI houdt rekening met allergenen en dieet
- Recept kan opgeslagen worden

**Git Check:**
- Feature branches gebruikt
- Pull requests gedaan
- Code reviews

---

## FASE 3: Recepten CRUD en Polish

**Duur:** Week 3
**Doel:** Recepten beheer, zoeken, mooie output

### Taken Persoon 1 (Recepten Database)

**Recepten CRUD:**
- [ ] Functie sla_recept_op(recept_dict)
- [ ] Functie haal_recepten_op()
- [ ] Functie haal_recept_detail(id)
- [ ] Functie verwijder_recept(id)
- [ ] Functie update_notities(id, notities)

**Zoekfunctie:**
- [ ] Stored procedure sp_zoek_recepten(zoekterm)
- [ ] Zoeken op titel
- [ ] Zoeken op ingredienten
- [ ] Zoeken op categorie

**Extra Features:**
- [ ] Filter op categorie (Ontbijt, Lunch, etc)
- [ ] Sorteer op datum

### Taken Persoon 2 (AI Verbeteren)

**Prompt Verbeteren:**
- [ ] Aantal personen meegeven
- [ ] Categorie voorkeur meegeven
- [ ] Bereidingstijd limiet meegeven
- [ ] Nederlandse recepten forceren

**Extra AI Functies:**
- [ ] Functie pas_personen_aan(recept, nieuw_aantal)
  - AI herberekent hoeveelheden
- [ ] Functie genereer_variatie(recept)
  - AI maakt variatie op bestaand recept
- [ ] Functie maak_boodschappenlijst(recept)
  - AI maakt lijst van wat te kopen

**Error Handling:**
- [ ] Timeout afhandelen
- [ ] API error afhandelen
- [ ] Fallback bij falen

### Taken Persoon 3 (Recepten Menu en Output)

**Recepten Sub-Menu:**
- [ ] Menu optie 4: Opgeslagen recepten
  1. Toon alle recepten
  2. Zoek recept
  3. Recept details bekijken
  4. Recept verwijderen
  0. Terug

**Recept Lijst Weergave:**
- [ ] Tabel met: ID, Titel, Categorie, Datum
- [ ] Paginering (10 per pagina)
- [ ] Netjes uitgelijnd

**Recept Detail Weergave:**
- [ ] Titel groot/duidelijk
- [ ] Categorie en tijd
- [ ] Ingredienten lijst
- [ ] Genummerde stappen
- [ ] Notities
- [ ] Opties: wijzig notities, verwijder, terug

**Boodschappenlijst:**
- [ ] Na recept generatie: "Boodschappenlijst maken?"
- [ ] Toon lijst van ingredienten
- [ ] Optie om te printen (naar bestand)

### Sprint 3 Review

**Demo Eind Week 3:**
- Alle CRUD werkt (allergenen, dieet, recepten)
- Zoeken werkt
- AI genereert goede recepten
- Output ziet er netjes uit
- Boodschappenlijst werkt

**Alles Werkt:**
- Geen crashes
- Foutmeldingen zijn duidelijk
- Flow is logisch

---

## FASE 4: Testen en Presentatie

**Duur:** Week 4
**Doel:** Alles testen, documentatie, presentatie

### Taken Iedereen (Testing)

**Test Scenarios:**
- [ ] Nieuw profiel (geen allergenen, geen dieet)
- [ ] Profiel met veel allergenen
- [ ] Recept genereren met weinig ingredienten
- [ ] Recept genereren met veel ingredienten
- [ ] Recept opslaan en terugvinden
- [ ] Zoeken op titel
- [ ] Zoeken op ingredienten
- [ ] Lege invoer (moet foutmelding geven)
- [ ] Ongeldige invoer (letters waar cijfer moet)

**Bug Fixing:**
- [ ] Alle gevonden bugs oplossen
- [ ] Crashes fixen
- [ ] Foutmeldingen verbeteren

**Code Cleanup:**
- [ ] Dode code verwijderen
- [ ] Naamgeving consistent
- [ ] Comments waar nodig
- [ ] Formatting netjes

### Taken Persoon 1 (Documentatie Database)

**Database Documentatie:**
- [ ] ERD diagram (kan simpel in tekst)
- [ ] Tabel beschrijvingen
- [ ] Stored procedures uitleg
- [ ] Setup instructies

### Taken Persoon 2 (Documentatie AI)

**AI Documentatie:**
- [ ] Prompt uitleg
- [ ] Hoe AI werkt in de app
- [ ] API setup instructies
- [ ] Voorbeelden van AI output

### Taken Persoon 3 (README en Presentatie)

**README.md Compleet:**
- [ ] Project beschrijving
- [ ] Features
- [ ] Installatie stappen
- [ ] Gebruik met voorbeelden
- [ ] Screenshots (terminal output)
- [ ] Credits

**Presentatie Slides:**
- [ ] Slide 1: Titel en team
- [ ] Slide 2: Probleem
- [ ] Slide 3: Oplossing
- [ ] Slide 4: Demo (live)
- [ ] Slide 5: Techniek (database, AI)
- [ ] Slide 6: Wat hebben we geleerd
- [ ] Slide 7: Vragen

### Presentatie Voorbereiding

**Demo Scenario:**
1. Start applicatie, toon welkom
2. Toon profiel (allergenen: noten, dieet: vegetarisch)
3. Voeg allergie toe: lactose
4. Genereer recept met: pasta, tomaat, ui, knoflook
5. Toon dat AI rekening houdt met allergenen
6. Sla recept op
7. Toon opgeslagen recepten
8. Zoek op "pasta"
9. Maak boodschappenlijst

**Oefenen:**
- [ ] Demo 2x doorlopen
- [ ] Timing checken (max 10 min demo)
- [ ] Backup plan als iets faalt
- [ ] Iedereen weet zijn deel

**Vragen Voorbereiden:**
- Hoe werkt de AI?
- Waarom deze database structuur?
- Wat was het moeilijkste?
- Wat zou je anders doen?

### Sprint 4 Review (Finale)

**Klaar Voor Inleveren:**
- [ ] Code werkt 100%
- [ ] README is compleet
- [ ] Presentatie is klaar
- [ ] Demo is geoefend
- [ ] Git repository is netjes

---

## Minimale vs Ideale Scope

**Minimaal (voor voldoende):**
- Allergenen CRUD (toevoegen, tonen, verwijderen)
- Dieetwensen CRUD (toevoegen, tonen, verwijderen)
- Recept genereren met AI (rekening houdend met profiel)
- Recept opslaan
- Opgeslagen recepten bekijken
- Recept verwijderen
- Stored procedures voor alle database acties
- Werkende demo

**Ideaal (voor hoog cijfer):**
- Alles van minimaal PLUS:
- Zoekfunctie
- Boodschappenlijst genereren
- Personen aanpassen (AI herberekent)
- Recepten categorieen en filters
- Mooie terminal output met kleuren
- Uitgebreide error handling
- Goede documentatie

---

## Weekoverzicht

**Week 1:**
- Database opgezet met tabellen
- Allergenen CRUD basis
- Menu systeem werkt
- AI API werkt (test)

**Week 2:**
- Allergenen CRUD compleet
- Dieetwensen CRUD compleet
- AI genereert recepten
- Recept opslaan werkt

**Week 3:**
- Recepten CRUD compleet
- Zoekfunctie
- Extra AI features
- Mooie output

**Week 4:**
- Testing en bug fixing
- Documentatie
- Presentatie voorbereiden
- Demo oefenen

---

## Tips Voor Succes

**Algemeen:**
- Begin met het makkelijkste eerst
- Test vaak (na elke functie)
- Commit dagelijks
- Vraag hulp als je vastzit

**Database:**
- Test stored procedures in MySQL Workbench eerst
- Maak backup voor grote wijzigingen

**AI:**
- Begin met simpele prompts, maak complexer
- Log AI responses voor debugging
- Hou rekening met kosten (Haiku is goedkoop)

**Git:**
- Pull voordat je begint te werken
- Kleine commits met duidelijke berichten
- Los merge conflicts direct op

**Presentatie:**
- Oefen de demo meerdere keren
- Heb backup plan als iets faalt
- Ken je eigen code

---

Dit is jullie 4-weken planning. Succes met Kookcompas.
