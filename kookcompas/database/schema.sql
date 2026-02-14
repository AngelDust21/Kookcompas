-- Kookcompas Database Schema

CREATE DATABASE IF NOT EXISTS kookcompas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE kookcompas;

-- tabellen 
CREATE TABLE IF NOT EXISTS Allergenen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    naam VARCHAR(50) UNIQUE NOT NULL,
    beschrijving VARCHAR(200),
    aangemaakt_op DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Dieetwensen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    naam VARCHAR(50) UNIQUE NOT NULL,
    beschrijving VARCHAR(200),
    aangemaakt_op DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Recepten (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titel VARCHAR(100) NOT NULL,
    categorie ENUM('Ontbijt', 'Lunch', 'Diner', 'Snack', 'Dessert') NOT NULL,
    ingredienten TEXT NOT NULL,
    instructies TEXT NOT NULL,
    bereidingstijd INT,
    personen INT DEFAULT 2,
    notities TEXT,
    opgeslagen_op DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_categorie (categorie),
    INDEX idx_opgeslagen (opgeslagen_op)
);

-- STORED PROCEDURES
DELIMITER //

-- alergenen
CREATE PROCEDURE sp_voeg_allergie_toe(IN p_naam VARCHAR(50), IN p_beschrijving VARCHAR(200))
BEGIN
    INSERT INTO Allergenen (naam, beschrijving) VALUES (LOWER(p_naam), p_beschrijving);
    SELECT LAST_INSERT_ID() AS id;
END //

CREATE PROCEDURE sp_haal_allergenen_op()
BEGIN
    SELECT id, naam, beschrijving, aangemaakt_op FROM Allergenen ORDER BY naam;
END //

CREATE PROCEDURE sp_verwijder_allergie(IN p_id INT)
BEGIN
    DELETE FROM Allergenen WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //

CREATE PROCEDURE sp_zoek_allergie(IN p_naam VARCHAR(50))
BEGIN
    SELECT id, naam, beschrijving FROM Allergenen WHERE naam LIKE CONCAT('%', LOWER(p_naam), '%');
END //

-- de dieetwense
CREATE PROCEDURE sp_voeg_dieet_toe(IN p_naam VARCHAR(50), IN p_beschrijving VARCHAR(200))
BEGIN
    INSERT INTO Dieetwensen (naam, beschrijving) VALUES (LOWER(p_naam), p_beschrijving);
    SELECT LAST_INSERT_ID() AS id;
END //

CREATE PROCEDURE sp_haal_dieet_op()
BEGIN
    SELECT id, naam, beschrijving, aangemaakt_op FROM Dieetwensen ORDER BY naam;
END //

CREATE PROCEDURE sp_verwijder_dieet(IN p_id INT)
BEGIN
    DELETE FROM Dieetwensen WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //

-- gerechten
CREATE PROCEDURE sp_voeg_recept_toe(IN p_titel VARCHAR(100), IN p_categorie VARCHAR(20), IN p_ingredienten TEXT, IN p_instructies TEXT, IN p_bereidingstijd INT, IN p_personen INT)
BEGIN
    INSERT INTO Recepten (titel, categorie, ingredienten, instructies, bereidingstijd, personen)
    VALUES (p_titel, p_categorie, p_ingredienten, p_instructies, p_bereidingstijd, p_personen);
    SELECT LAST_INSERT_ID() AS id;
END //

CREATE PROCEDURE sp_haal_recepten_op()
BEGIN
    SELECT id, titel, categorie, bereidingstijd, personen, opgeslagen_op FROM Recepten ORDER BY opgeslagen_op DESC;
END //

CREATE PROCEDURE sp_haal_recept_detail(IN p_id INT)
BEGIN
    SELECT * FROM Recepten WHERE id = p_id;
END //

CREATE PROCEDURE sp_verwijder_recept(IN p_id INT)
BEGIN
    DELETE FROM Recepten WHERE id = p_id;
    SELECT ROW_COUNT() AS verwijderd;
END //

CREATE PROCEDURE sp_update_notities(IN p_id INT, IN p_notities TEXT)
BEGIN
    UPDATE Recepten SET notities = p_notities WHERE id = p_id;
    SELECT ROW_COUNT() AS bijgewerkt;
END //

CREATE PROCEDURE sp_zoek_recepten(IN p_zoekterm VARCHAR(100))
BEGIN
    SELECT id, titel, categorie, bereidingstijd, opgeslagen_op FROM Recepten
    WHERE titel LIKE CONCAT('%', p_zoekterm, '%') OR ingredienten LIKE CONCAT('%', p_zoekterm, '%')
    ORDER BY opgeslagen_op DESC;
END //

CREATE PROCEDURE sp_filter_categorie(IN p_categorie VARCHAR(20))
BEGIN
    SELECT id, titel, categorie, bereidingstijd, personen, opgeslagen_op FROM Recepten
    WHERE categorie = p_categorie ORDER BY opgeslagen_op DESC;
END //

CREATE PROCEDURE sp_tel_recepten()
BEGIN
    SELECT COUNT(*) AS aantal FROM Recepten;
END //

DELIMITER ;

-- data om uit te proberen testen
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

INSERT INTO Recepten (titel, categorie, ingredienten, instructies, bereidingstijd, personen, notities) VALUES
('Pasta Pomodoro', 'Diner',
'- 250g pasta\n- 4 rijpe tomaten\n- 1 ui\n- 2 teentjes knoflook\n- 2 el olijfolie\n- Zout, peper, basilicum',
'1. Kook de pasta volgens de verpakking\n2. Fruit de ui in olijfolie\n3. Voeg knoflook toe, bak 1 minuut\n4. Tomaten in blokjes erbij\n5. 10 minuten laten sudderen\n6. Meng pasta door de saus\n7. Garneer met basilicum',
25, 2, 'Voorbeeldrecept');

SELECT 'proficiat je schema is geladen' AS status;
