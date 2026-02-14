-- Kookcompas Database Schema
-- Volledige opbouw van de database, stap voor stap.

-- DATABASE
-- Database aanmaken als deze mist.
-- utf8mb4: voor unicode inclusief emoji support (bijvoorbeeld 🥑).
-- Oude encoding (utf8) crasht bij bijzondere karakters.
CREATE DATABASE IF NOT EXISTS kookcompas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE kookcompas;


-- TABELLEN
-- Data structuur vastleggen.

-- Tabel: Allergenen
-- Vaste lijst. Consistente data is cruciaal voor filters later.
CREATE TABLE IF NOT EXISTS Allergenen (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Telt automatisch op.
    naam VARCHAR(50) UNIQUE NOT NULL,         -- Max 50, geen dubbels (UNIQUE).
    beschrijving VARCHAR(200),                -- Extra info, mag leeg zijn.
    aangemaakt_op DATETIME DEFAULT CURRENT_TIMESTAMP -- Automatische tijdstempel.
);

-- Tabel: Dieetwensen
-- Identiek aan Allergenen. Zelfde logica = minder bugs.
CREATE TABLE IF NOT EXISTS Dieetwensen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    naam VARCHAR(50) UNIQUE NOT NULL,
    beschrijving VARCHAR(200),
    aangemaakt_op DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabel: Recepten
-- De kern. Bevat alle data voor de app.
CREATE TABLE IF NOT EXISTS Recepten (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titel VARCHAR(100) NOT NULL,

    -- Categorie: ENUM forceert vaste opties.
    -- Voorkomt typefouten zoals 'Lunsh' of 'Diner '.
    categorie ENUM('Ontbijt', 'Lunch', 'Diner', 'Snack', 'Dessert') NOT NULL,

    -- TEXT: Ingredienten en Instructies kunnen lang zijn.
    -- VARCHAR(255) is te krap. TEXT gaat tot 65k tekens.
    ingredienten TEXT NOT NULL,
    instructies TEXT NOT NULL,

    bereidingstijd INT,          -- Minuten.
    personen INT DEFAULT 2,      -- Default waarde scheelt invulwerk.
    notities TEXT,
    opgeslagen_op DATETIME DEFAULT CURRENT_TIMESTAMP,

    -- INDEXEN: Snelheid.
    -- Versnelt zoeken op categorie en datum aanzienlijk.
    INDEX idx_categorie (categorie),
    INDEX idx_opgeslagen (opgeslagen_op)
);


-- STORED PROCEDURES
-- Functies in de database zelf.
-- Waarom: Veiligheid (SQL injection), schone Python code, snelheid.
DELIMITER $$


-- sp_voeg_recept_toe
-- Python: sla_recept_op() (queries.py)
-- Slaat recept op en geeft direct het nieuwe ID terug.
-- Dat ID hebben we nodig om de gebruiker meteen het resultaat te tonen.
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
END $$


-- sp_voeg_allergie_toe
-- Python: voeg_allergie_toe()
-- Voegt toe met LOWER(naam). Dwingt kleine letters af.
-- Voorkomt dubbele invoer ('Gluten' vs 'gluten'). Houdt data schoon.
CREATE PROCEDURE sp_voeg_allergie_toe(IN p_naam VARCHAR(50), IN p_beschrijving VARCHAR(200))
BEGIN
    INSERT INTO Allergenen (naam, beschrijving) VALUES (LOWER(p_naam), p_beschrijving);
    SELECT LAST_INSERT_ID() AS id;
END $$


-- sp_haal_allergenen_op
-- Python: haal_alle_allergenen()
-- Haalt lijst op, gesorteerd op naam (A-Z).
-- Sorteren in database is sneller dan in Python.
CREATE PROCEDURE sp_haal_allergenen_op()
BEGIN
    SELECT id, naam, beschrijving, aangemaakt_op FROM Allergenen ORDER BY naam;
END $$


-- sp_verwijder_allergie
-- Python: verwijder_allergie()
-- Verwijdert specifiek ID. ROW_COUNT checkt of het gelukt is.
-- Zonder die check weet Python niet of er echt iets gebeurd is.
CREATE PROCEDURE sp_verwijder_allergie(IN p_id INT)
BEGIN
    DELETE FROM Allergenen WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END $$


-- sp_zoek_allergie
-- (Nog niet gebruikt in Python)
-- Zoekt flexibel met wildcards (%).
-- Vindt 'noot' in 'walnoot' en 'hazelnoot'.
CREATE PROCEDURE sp_zoek_allergie(IN p_naam VARCHAR(50))
BEGIN
    SELECT id, naam, beschrijving FROM Allergenen WHERE naam LIKE CONCAT('%', LOWER(p_naam), '%');
END $$


-- sp_voeg_dieet_toe
-- Python: voeg_dieet_toe()
-- Zelfde logica als allergenen. Consistentie.
CREATE PROCEDURE sp_voeg_dieet_toe(IN p_naam VARCHAR(50), IN p_beschrijving VARCHAR(200))
BEGIN
    INSERT INTO Dieetwensen (naam, beschrijving) VALUES (LOWER(p_naam), p_beschrijving);
    SELECT LAST_INSERT_ID() AS id;
END $$

-- sp_haal_dieet_op
-- Python: haal_alle_dieetwensen()
CREATE PROCEDURE sp_haal_dieet_op()
BEGIN
    SELECT id, naam, beschrijving, aangemaakt_op FROM Dieetwensen ORDER BY naam;
END $$

-- sp_verwijder_dieet
-- Python: verwijder_dieet()
CREATE PROCEDURE sp_verwijder_dieet(IN p_id INT)
BEGIN
    DELETE FROM Dieetwensen WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END $$


-- sp_haal_recepten_op
-- Python: haal_alle_recepten()
-- Haalt alleen basisinfo op voor de lijst.
-- Grote teksten (instructies) overslaan maakt het laden veel sneller.
CREATE PROCEDURE sp_haal_recepten_op()
BEGIN
    SELECT id, titel, categorie, bereidingstijd, personen, opgeslagen_op 
    FROM Recepten 
    ORDER BY opgeslagen_op DESC;
END $$


-- sp_haal_recept_detail
-- Python: haal_recept_detail()
-- Haalt ALLES op van één recept.
-- Nu pas laden we de zware tekstvelden, want de gebruiker wil details zien.
CREATE PROCEDURE sp_haal_recept_detail(IN p_id INT)
BEGIN
    SELECT * FROM Recepten WHERE id = p_id;
END $$


-- sp_verwijder_recept
-- Python: verwijder_recept()
CREATE PROCEDURE sp_verwijder_recept(IN p_id INT)
BEGIN
    DELETE FROM Recepten WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END $$


-- sp_update_notities
-- Python: update_recept_notities()
-- Overschrijft notitie van specifiek recept (UPDATE ... WHERE).
-- Zonder WHERE zouden alle recepten dezelfde notitie krijgen.
CREATE PROCEDURE sp_update_notities(IN p_id INT, IN p_notities TEXT)
BEGIN
    UPDATE Recepten SET notities = p_notities WHERE id = p_id;
    SELECT ROW_COUNT() AS bijgewerkt;
END $$


-- sp_zoek_recepten
-- Python: zoek_recepten()
-- Zoekt in titel OF ingredienten (OR).
-- Zoekterm 'kip' vindt dus titel 'Kip Curry' én ingredient 'kipfilet'.
CREATE PROCEDURE sp_zoek_recepten(IN p_zoekterm VARCHAR(100))
BEGIN
    SELECT id, titel, categorie, bereidingstijd, opgeslagen_op FROM Recepten
    WHERE titel LIKE CONCAT('%', p_zoekterm, '%') OR ingredienten LIKE CONCAT('%', p_zoekterm, '%')
    ORDER BY opgeslagen_op DESC;
END $$


-- sp_filter_categorie
-- Python: filter_op_categorie()
-- Filtert exact op categorie (=).
-- Categorie is een vaste lijst (ENUM), dus geen vage zoekopdracht nodig.
CREATE PROCEDURE sp_filter_categorie(IN p_categorie VARCHAR(20))
BEGIN
    SELECT id, titel, categorie, bereidingstijd, personen, opgeslagen_op FROM Recepten
    WHERE categorie = p_categorie ORDER BY opgeslagen_op DESC;
END $$


-- sp_tel_recepten
-- Python: tel_recepten()
-- Telt totaal aantal rijen (COUNT).
-- Handig voor statistieken, bijvoorbeeld in dashboard.
CREATE PROCEDURE sp_tel_recepten()
BEGIN
    SELECT COUNT(*) AS aantal FROM Recepten;
END $$

DELIMITER ;


-- TESTDATA & ROBUUSTHEID
-- Idempotentie: script moet herhaalbaar zijn zonder fouten.

-- INSERT IGNORE:
-- Als data al bestaat, slaat database dit stil over.
-- Voorkomt crashes bij dubbel uitvoeren script (UNIQUE constraints).
-- Maakt het script 'bulletproof'.

INSERT IGNORE INTO Allergenen (naam, beschrijving) VALUES
('noten', 'Alle soorten noten inclusief pinda'),
('lactose', 'Melk en zuivelproducten'),
('gluten', 'Tarwe, rogge, gerst'),
('ei', 'Eieren en ei-producten'),
('schaaldieren', 'Garnalen, krab, kreeft');

INSERT IGNORE INTO Dieetwensen (naam, beschrijving) VALUES
('vegetarisch', 'Geen vlees of vis'),
('veganistisch', 'Geen dierlijke producten'),
('halal', 'Volgens islamitische voedingsregels'),
('glutenvrij', 'Geen gluten bevattende producten'),
('keto', 'Weinig koolhydraten, veel vet');

-- Testrecept. Zorgt voor data bij eerste start.
INSERT INTO Recepten (titel, categorie, ingredienten, instructies, bereidingstijd, personen, notities) VALUES
('Pasta Pomodoro', 'Diner',
'- 250g pasta\n- 4 rijpe tomaten\n- 1 ui\n- 2 teentjes knoflook\n- 2 el olijfolie\n- Zout, peper, basilicum',
'1. Kook de pasta volgens de verpakking\n2. Fruit de ui in olijfolie\n3. Voeg knoflook toe, bak 1 minuut\n4. Tomaten in blokjes erbij\n5. 10 minuten laten sudderen\n6. Meng pasta door de saus\n7. Garneer met basilicum',
25, 2, 'Testrecept');

SELECT 'Schema geladen - klaar voor gebruik' AS status;
