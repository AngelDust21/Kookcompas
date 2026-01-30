## Page 1

GROEPSWERK 1: PYTHON
1. Doel van het groepswerk
In dit groepswerk werken cursisten in team aan een softwareproject zoals dat in een
De focus ligt op samenwerken, projectmatig werken (scrum), logisch programmeren in
Python en presenteren.
2. Samenstelling van de groepen
Groepen bestaan uit 3-4 cursisten, sluit je aan bij een project dat je interessant vindt.
3. Keuze van het project
Elke groep kiest één projectvorm.
Al gemene vereisten:
Codekwaliteit
• Duidelijke en consistente naamgeving
• Correcte inspringing
• Geen dode code
• Beperkte duplicatie
• Commentaar waar nodig (uitleg waarom, niet wat)
Samenwerking en Git
• Het project staat in een Git-repository.
• Alle groepsleden leveren commits aan.
• Commits zijn:
o logisch opgebouwd,
o duidelijk benoemd,

## Page 2

o gespreid over de looptijd van het project.
MySQL :minimale databankvereisten
Datamodel
• Minstens 2 tabellen met een duidelijke relatie:
o 1x 1-N (bv. klant → bestellingen), of
o 1x N-M via een tussentabel (alleen als het echt nodig is).
• Elke tabel heeft:
o PRIMARY KEY
o juiste datatypes
o minstens één constraint waar zinvol (NOT NULL, UNIQUE, FOREIGN
KEY).
SQL-functionaliteit (minimaal)
De applicatie moet minstens kunnen:
• CREATE (record toevoegen)
• READ (overzicht / detail)
• UPDATE (record aanpassen)
• DELETE (record verwijderen)
= volledige CRUD
Veilig en correct werken met SQL
• Stored procedures gebruiken
• Input-validatie voor je queries uitvoert (bv. numerieke keuzes, lege input).
• Foutafhandeling:
o databaseconnectie errors opvangen,
o foutmeldingen tonen op een begrijpelijke manier.
Setup en reproduceerbaarheid
In de repo zit:
• schema.sql (tabellen + constraints + evt. testdata)

## Page 3

• korte README.md met:
o hoe MySQL te starten/instellen,
o hoe schema te importeren,
o hoe het programma te runnen.
Opties
OPTIE A : Console applicatie (Python)
Een console applicatie (CLI) is een Python-programma dat volledig via de terminal
werkt.
De gebruiker communiceert met het programma via tekstinput en tekstoutput.
Vereisten:
1. Interactie en gebruikersinterface (CLI)
• Het programma wordt gestart vanuit de terminal.
• Interactie gebeurt uitsluitend via:
o input()
o print()
• De applicatie bevat een duidelijk menu met keuzemogelijkheden.
• De gebruiker kan meerdere acties uitvoeren zonder het programma opnieuw te
starten.
• Het programma stopt enkel wanneer de gebruiker hier expliciet voor kiest
2. Programmastructuur
• De code is gestructureerd en leesbaar.
• Logica is opgesplitst in:
o functies en/of

## Page 4

o klassen (zie OOP).
• Er is geen “alles-in-één”-functie of script.
• Gebruik van een main()-functie is sterk aanbevolen.

## Page 5

OPTIE B : Eenvoudige webapp (Python backend)
Kleine webapp met Python backend (Flask).
Beschrijving
Een kleine webapplicatie waarbij Python de backend verzorgt (Flask). De webapp lost
een concreet probleem op met beperkte scope.
Kenmerken
• Python draait als backend (bv. Flask).
• Gebruiker kan data invoeren via formulieren.
• Server-side verwerking en logica.
• Resultaat wordt dynamisch weergegeven.
• Rechtstreekse interactie met database.
Wat een webapp doet
• Data toevoegen, wijzigen of verwijderen
• Overzichten genereren op basis van input
• Logica uitvoeren op server-side
• CRUD-functionaliteit aanbieden
Wat een webapp niet mag zijn (in deze opdracht)
• Volwaardig platform
• Complex gebruikersbeheer
• Rollen en rechten
• Overengineering
1. Scope
• De scope moet klein blijven: maximaal 3–5 kernfunctionaliteiten.
• Geen “platformdenken” (geen CRM, geen volledige webshop, geen
rollen/permissions-systeem).
2. Frontend (basis)

## Page 6

• Eenvoudige HTML-templates (bv. Jinja).
• Minstens:
o 2 pagina’s (routes) met zichtbare content
o 1 formulier dat data verstuurt naar de backend
• Styling mag minimaal zijn (geen focus).
3. Backend (verplicht)
• Python backend met duidelijke structuur:
o routes/controllers
o logica in aparte functies/klassen
• Input-validatie op server-side (minstens basis: leeg, type, lengte).
• Foutafhandeling met begrijpelijke meldingen.

## Page 7

OPTIE C: Website + Python-script
Website gecombineerd met een Python-script met duidelijke logica.
De website dient voor presentatie en uitleg, het Python-script voor verwerking en logica.
Voor OPTIE C wordt de website gebouwd met HTML/CSS (eventueel beperkte
JavaScript).De Pyth;on-logica draait los van de website en verwerkt data via MySQL.
Vereisten: Website
• Minstens 3 HTML-pagina’s.
• Duidelijke structuur en inhoud (geen lorem ipsum).
• De website legt uit:
o het probleem dat wordt opgelost,
o wat de Python-tool doet,
o hoe de tool gebruikt wordt,
o hoe de resultaten geïnterpreteerd worden.
• Website is niet interactief:
o geen formulieren die data verwerken,
o geen CRUD-functionaliteit,
o geen backend.

## Page 8

OPTIE D : Automatiserings- of hulpprogramma
Beschrijving
Een Python-tool die een repetitieve of administratieve taak automatiseert of sterk
vereenvoudigt, zoals in een echte bedrijfscontext.
Vereisten:
De tool werkt via:
• een menu-gestuurde CLI, of
• vaste commando’s/parameters.
De gebruiker kan meerdere acties uitvoeren zonder het programma opnieuw te starten
(tenzij logisch anders).
• Duidelijke workflow:
o input → verwerking → output.
o data toevoegen,
o overzicht of zoekfunctie,
o rapport of verwerking.
• De automatisering levert aantoonbare meerwaarde (tijdswinst, foutreductie,
overzicht).
5. Projectaanpak
Scrum-aanpak met opvolgingsdocument. Docent treedt op als klant.
6. Vooraf in te dienen
Probleemstelling/ context
Scope,
Aanpak:
Taakverdeling

## Page 9

Opvolging.
7. Eindoplevering
Pitch, presentatie en live demo.
8. Evaluatie
Samenwerking, codekwaliteit, Git, presentatie en individuele kennis.
