# Projectvoorstel: Kookcompas

Groepswerk Python - Optie A (CLI Applicatie)

---

## Het Probleem

Elke dag staan miljoenen mensen voor dezelfde vraag: wat eten we vanavond. De koelkast zit vol met losse ingredienten, maar inspiratie ontbreekt. Online recepten zoeken kost tijd en levert vaak resultaten op die niet passen bij wat er in huis is.

Voor mensen met allergenen of dieetwensen wordt dit nog lastiger. Een notenallergie of vegetarisch dieet betekent eindeloos scrollen door recepten die uiteindelijk toch niet geschikt blijken.

Dit kost tijd, zorgt voor frustratie en leidt regelmatig tot voedselverspilling.

---

## De Oplossing: Kookcompas

Kookcompas is een slimme CLI-tool die recepten genereert op basis van beschikbare ingredienten. De applicatie onthoudt allergenen en dieetwensen, zodat elk gegenereerd recept direct veilig en passend is.

**Hoe het werkt:**

- Gebruiker voert ingredienten in die beschikbaar zijn
- Systeem haalt opgeslagen allergenen en dieetwensen op uit database
- AI genereert een passend recept dat rekening houdt met alle restricties
- Recept kan opgeslagen worden als favoriet voor later

**Voorbeeld sessie:**

```
Welkom bij Kookcompas

Jouw profiel:
- Allergenen: noten, lactose
- Dieet: vegetarisch

Welke ingredienten heb je? pasta, tomaat, ui, knoflook

Even denken...

RECEPT: Pasta Pomodoro
Tijd: 25 minuten
Personen: 2

Dit recept bevat geen noten, geen lactose en is vegetarisch.
```

---

## Waarom Dit Project

**Praktische meerwaarde:**
- Tijdswinst: binnen seconden een passend recept
- Veiligheid: geen vergeten allergenen
- Minder verspilling: koken met wat er is

**Technische uitdaging:**
- Volledige CRUD-functionaliteit
- MySQL database met stored procedures
- AI-integratie via Claude API
- Professionele CLI-structuur

**Haalbaar voor beginners:**
- Geen complexe file parsing nodig
- Duidelijke modulaire opbouw
- Stapsgewijze implementatie mogelijk
- Goed gedocumenteerd stappenplan aanwezig

---

## CRUD Implementatie

De applicatie biedt duidelijke CRUD-operaties op drie entiteiten:

**Allergenen beheer:**
- Toevoegen van nieuwe allergie aan profiel
- Overzicht van alle opgeslagen allergenen
- Allergie verwijderen uit profiel

**Dieetwensen beheer:**
- Dieetwens toevoegen (vegetarisch, veganistisch, keto, halal)
- Overzicht van actieve dieetwensen
- Dieetwens verwijderen

**Recepten beheer:**
- AI-gegenereerde recepten opslaan
- Opgeslagen recepten bekijken
- Zoeken in recepten op titel of ingredienten
- Recepten verwijderen

---

## Database Ontwerp

Drie tabellen met duidelijke structuur:

**Allergenen**
- Primaire sleutel met auto-increment
- Unieke naam per allergie
- Optionele beschrijving
- Timestamp van aanmaak

**Dieetwensen**
- Zelfde structuur als allergenen
- Gescheiden tabel voor flexibiliteit

**Recepten**
- Titel, categorie, ingredienten, bereidingsstappen
- Bereidingstijd en aantal personen
- Notitieveld voor eigen aanvullingen
- Datum van opslaan

**Stored procedures:**
- sp_voeg_allergie_toe
- sp_haal_allergenen_op
- sp_verwijder_allergie
- sp_voeg_dieet_toe
- sp_haal_dieet_op
- sp_verwijder_dieet
- sp_voeg_recept_toe
- sp_haal_recepten_op
- sp_haal_recept_detail
- sp_verwijder_recept
- sp_zoek_recepten

---

## AI Integratie

De applicatie maakt gebruik van Claude Haiku via de Anthropic API.

**Waarom Haiku:**
- Snel: responstijd onder 2 seconden
- Goedkoop: 1000 recepten kost ongeveer 1 euro
- Kwalitatief: begrijpt Nederlands en volgt instructies nauwkeurig

**Werking:**
- Prompt bevat ingredienten, allergenen en dieetwensen
- AI genereert recept in vast formaat
- Response wordt geparsed naar database-structuur
- Gebruiker beslist over opslaan

---

## Taakverdeling

Het team bestaat uit drie personen met duidelijke verantwoordelijkheden:

**Teamlid 1 - Database:**
- Schema ontwerp en implementatie
- Stored procedures schrijven en testen
- CRUD-functies voor allergenen en dieetwensen
- Database connectie module

**Teamlid 2 - AI:**
- Claude API integratie
- Prompt engineering
- Response parsing
- Error handling voor API-calls

**Teamlid 3 - CLI:**
- Menu systeem en navigatie
- Gebruikersinput en validatie
- Receptweergave en formatting
- Hoofdflow van applicatie

---

## Planning

**Week 1:**
- Database opgezet met tabellen en stored procedures
- Basis menu werkend
- Allergenen CRUD functioneel
- API-connectie getest

**Week 2:**
- Dieetwensen CRUD compleet
- AI recept-generatie werkend
- Recepten opslaan in database
- Integratie van alle onderdelen

**Week 3:**
- Recepten CRUD compleet
- Zoekfunctionaliteit
- Verfijning AI-prompts
- Mooie terminal output

**Week 4:**
- Testing en bugfixing
- Documentatie afronden
- Presentatie voorbereiden
- Demo oefenen

---

## Technische Stack

- Python 3.10+
- MySQL 8.0
- Claude Haiku API (Anthropic)
- mysql-connector-python
- python-dotenv
- tabulate

---

## Wat Maakt Dit Project Bijzonder

**Moderne technologie:**
Integratie van AI in een praktische toepassing. Niet zomaar een chatbot, maar een tool die echte meerwaarde levert.

**Duidelijke structuur:**
Gescheiden modules voor database, AI en CLI. Elke teamlid kan zelfstandig werken aan eigen onderdeel.

**Realistische use case:**
Een probleem dat iedereen herkent. Makkelijk te demonstreren en direct bruikbaar.

**Uitbreidbaar:**
Basis is solide, extra features kunnen toegevoegd worden: boodschappenlijst, porties aanpassen, favorieten markeren.

---

## Conclusie

Kookcompas combineert een herkenbaar dagelijks probleem met moderne AI-technologie. Het project voldoet aan alle technische vereisten: CRUD-operaties, stored procedures, duidelijke codestructuur en Git-samenwerking.

De scope is realistisch voor drie beginners in vier weken. Er is ruimte voor basisimplementatie die voldoet aan de eisen, met mogelijkheid tot uitbreiding voor een hoger cijfer.

Het resultaat is een werkende applicatie die direct gedemonstreerd kan worden en echte waarde biedt voor de gebruiker.

---

**Projectnaam:** Kookcompas
**Type:** CLI Applicatie (Optie A)
**Team:** 3 personen
**Doorlooptijd:** 4 weken

---
