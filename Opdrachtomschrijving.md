# Opdrachtomschrijving - Waar moeten we op letten?

## Gekozen optie: OPTIE A - Console Applicatie (CLI)

---

## Algemene Vereisten

### Codekwaliteit
- [ ] Duidelijke en consistente naamgeving
- [ ] Correcte inspringing
- [ ] Geen dode code
- [ ] Beperkte duplicatie
- [ ] Commentaar waar nodig (uitleg **waarom**, niet wat)

### Samenwerking en Git
- [ ] Project staat in een Git-repository
- [ ] **Alle groepsleden** leveren commits aan
- [ ] Commits zijn logisch opgebouwd
- [ ] Commits zijn duidelijk benoemd
- [ ] Commits zijn gespreid over de looptijd van het project

---

## MySQL - Minimale Databankvereisten

### Datamodel
- [ ] Minstens **2 tabellen** met een duidelijke relatie
  - 1x 1-N relatie (bv. klant → bestellingen), of
  - 1x N-M via een tussentabel (alleen als het echt nodig is)
- [ ] Elke tabel heeft:
  - PRIMARY KEY
  - Juiste datatypes
  - Minstens één constraint waar zinvol (NOT NULL, UNIQUE, FOREIGN KEY)

> **⚠️ LET OP:** Wij hebben momenteel 3 losstaande tabellen (Allergenen, Dieetwensen, Recepten) zonder relatie. De opdracht eist **minstens 2 tabellen met een duidelijke relatie (1-N of N-M)**. Dit moet opgelost worden!

### SQL-functionaliteit (minimaal)
- [ ] **CREATE** - record toevoegen
- [ ] **READ** - overzicht / detail
- [ ] **UPDATE** - record aanpassen
- [ ] **DELETE** - record verwijderen
- [ ] = volledige CRUD

### Veilig en correct werken met SQL
- [ ] **Stored procedures** gebruiken
- [ ] Input-validatie voordat je queries uitvoert (numerieke keuzes, lege input)
- [ ] Foutafhandeling:
  - Databaseconnectie errors opvangen
  - Foutmeldingen tonen op een begrijpelijke manier

### Setup en reproduceerbaarheid
- [ ] `schema.sql` in de repo (tabellen + constraints + evt. testdata)
- [ ] Korte `README.md` met:
  - Hoe MySQL te starten/instellen
  - Hoe schema te importeren
  - Hoe het programma te runnen

---

## Optie A Specifieke Vereisten (CLI)

### Interactie en gebruikersinterface
- [ ] Programma wordt gestart vanuit de terminal
- [ ] Interactie gebeurt uitsluitend via `input()` en `print()`
- [ ] Duidelijk menu met keuzemogelijkheden
- [ ] Gebruiker kan meerdere acties uitvoeren zonder herstarten
- [ ] Programma stopt **enkel** wanneer de gebruiker hier expliciet voor kiest

### Programmastructuur
- [ ] Code is gestructureerd en leesbaar
- [ ] Logica is opgesplitst in functies en/of klassen
- [ ] Geen "alles-in-één"-functie of script
- [ ] Gebruik van een `main()` functie

---

## Projectaanpak
- [ ] Scrum-aanpak met opvolgingsdocument
- [ ] Docent treedt op als klant

## Vooraf in te dienen
- [ ] Probleemstelling / context
- [ ] Scope
- [ ] Aanpak
- [ ] Taakverdeling
- [ ] Opvolging

## Eindoplevering
- [ ] Pitch
- [ ] Presentatie
- [ ] Live demo

## Evaluatie op
- Samenwerking
- Codekwaliteit
- Git
- Presentatie
- **Individuele kennis**

---

## ⚠️ Kritieke Aandachtspunten voor Kookcompas

1. **Tabelrelaties ontbreken** - We hebben 3 losse tabellen zonder FOREIGN KEY relaties. De opdracht eist minstens 2 tabellen met een 1-N of N-M relatie. Oplossing: voeg een `gebruiker_id` toe, of maak een koppeltabel tussen recepten en allergenen.
2. **UPDATE operatie** - Zorg dat er minstens één duidelijke UPDATE actie is (bijv. notities bewerken bij recepten).
3. **Commits per persoon** - Elke teamgenoot moet zichtbare, gespreide commits hebben. Niet alles op het einde pushen.
4. **Individuele kennis** - Iedereen wordt individueel beoordeeld. Ken je eigen code EN begrijp globaal wat de anderen hebben gedaan.
5. **Geen dode code** - Verwijder ongebruikte functies, uitgecommente code en test-prints voor oplevering.
6. **Commentaar = waarom, niet wat** - Schrijf `# Fallback als API niet bereikbaar is`, niet `# maak een lijst`.
