--
-- Create database
--

-- CREATE DATABASE IF NOT EXISTS met;
-- USE met;

--
-- Drop tables
-- turn off FK checks temporarily to eliminate drop order issues
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS artist, object_artist, object, department, acquisition, classification, city, country, region, role, nationality, temp_object;
SET FOREIGN_KEY_CHECKS=1;


--
-- MET Departments
--

CREATE TABLE IF NOT EXISTS department
  (
    department_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (department_id)
  )

ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_dept.tsv'
INTO TABLE department
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY '\t'
  -- FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  -- LINES TERMINATED BY '\r\n' 
  (department_name);



--
-- MET Classification
--

CREATE TABLE IF NOT EXISTS classification
  (
    classification_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    classification_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (classification_id)
  )

ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_classification.tsv'
INTO TABLE classification
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY '\t'
  -- FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  -- LINES TERMINATED BY '\r\n' 
  (classification_name);


--
-- MET region
--
CREATE TABLE IF NOT EXISTS region
  (
    region_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    region_name VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (region_id)
  )

ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_region.tsv'
INTO TABLE region
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY '\t'
  -- FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  -- LINES TERMINATED BY '\r\n' 
  (region_name);



--
-- MET Country
--
CREATE TABLE IF NOT EXISTS country
  (
    country_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    country_name VARCHAR(100) UNIQUE,
    PRIMARY KEY (country_id)

  )

ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_country.tsv'
INTO TABLE country
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY '\t'
  -- FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  -- LINES TERMINATED BY '\r\n' 
  (country_name);

--
-- MET City
--
CREATE TABLE IF NOT EXISTS city
  (
    city_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    city_name VARCHAR(100) NOT NULL UNIQUE,
    -- country_id INTEGER,
    PRIMARY KEY (city_id)
    
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_city.tsv'
INTO TABLE city
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY '\t'
  -- FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  -- LINES TERMINATED BY '\r\n' 
  (city_name);




--
-- MET Objects
--
CREATE TABLE IF NOT EXISTS temp_object
  (
    object_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    object_number VARCHAR(25) NULL,
    is_public_domain VARCHAR(5) NULL,
    department_name VARCHAR(100) NULL,
    -- object_name
    object_title VARCHAR(225) NULL,
    artist_role VARCHAR(225) NULL,
    -- artist_prefix,
    -- artist_display_name,
    -- artist_suffix,
    -- artist_alpha_sort,
    -- artist_nationality,
    -- artist_begin_date,
    -- artist_end_date,

    -- artist_id INTEGER NULL,
    object_date VARCHAR(100) NULL,
    object_begin_date INTEGER NULL,
    object_end_date INTEGER NULL,
    -- acquisition_type_id INTEGER NULL,
    acquisition_date INTEGER NULL,
    city VARCHAR(100) NULL,
    country VARCHAR(100) NULL,
    region VARCHAR(100) NULL,
    classification VARCHAR(225) NULL,
    rights_and_reproduction VARCHAR(100) NULL,
    link_resource VARCHAR(100) NULL,
    PRIMARY KEY (object_id)
  )

ENGINE=InnoDB
CHARACTER SET latin1
COLLATE latin1_general_ci;


LOAD DATA LOCAL INFILE 'C:/Users/Lauren/SI664/met/met_artwork_trimmed.csv'
INTO TABLE temp_object
  CHARACTER SET latin1
  FIELDS TERMINATED BY '\t'
  -- FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (object_number, is_public_domain, department_name, @dummy, object_title, artist_role, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, object_date, object_begin_date, object_end_date, @dummy, @dummy, @dummy, acquisition_date, city, country, region, classification, rights_and_reproduction, link_resource, @dummy) 


SET object_number = IF(object_number = '', NULL, object_number),
    is_public_domain = IF(is_public_domain = "TRUE", "Yes", "No"),
    department_name = IF(department_name = '', NULL, department_name),
    object_title = IF(object_title = '', NULL, object_title),
    -- artist_display_name = IF(artist_display_name = '', NULL, artist_display_name),
    object_date = IF(object_date = '', NULL, object_date),
    object_begin_date = IF(object_begin_date = '', NULL, object_begin_date),
    object_end_date = IF(object_end_date = '', NULL, object_end_date),
    -- acquisition_type = IF(acquisition_type = '', NULL, acquisition_type),
    acquisition_date = IF(acquisition_date = '', NULL, acquisition_date),
    city = IF(city = '', NULL, city),
    country = IF(country = '', NULL, country),
    region = IF(region = '', NULL, region),
    classification = IF(classification = '', NULL, classification),
    rights_and_reproduction = IF(rights_and_reproduction = '', NULL, rights_and_reproduction),
   link_resource = IF(link_resource = '', NULL, link_resource);



CREATE TABLE IF NOT EXISTS object
  (
    object_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    object_number VARCHAR(25) NULL,
    is_public_domain  VARCHAR(25) NULL,
    department_id INTEGER NULL,
    object_title VARCHAR(225) NULL,
    -- artist_id INTEGER NULL,
    object_date VARCHAR(100) NULL,
    begin_date INTEGER NULL,
    end_date INTEGER NULL,
    -- acquisition_type_id INTEGER NULL,
    acquisition_date INTEGER NULL,
    city_id INTEGER NULL,
    country_id INTEGER NULL,
    region_id INTEGER NULL,
    classification_id INTEGER NULL,
    rights_and_reproduction VARCHAR(100) NULL,
    link_resource VARCHAR(100) NULL,
    PRIMARY KEY (object_id),
    FOREIGN KEY (department_id) REFERENCES department(department_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    -- FOREIGN KEY (artist_id) REFERENCES object_artist(object_artist_id),
    -- ON DELETE CASCADE ON UPDATE CASCADE,
    -- FOREIGN KEY (acquisition_type_id) REFERENCES acquisition(acquisition_type_id),
    -- ON DELETE CASCADE ON UPDATE CASCADE,   
    FOREIGN KEY (city_id) REFERENCES city(city_id)
    ON DELETE CASCADE ON UPDATE CASCADE, 
    FOREIGN KEY (country_id) REFERENCES country(country_id)
    ON DELETE CASCADE ON UPDATE CASCADE, 
    FOREIGN KEY (region_id) REFERENCES region(region_id)
    ON DELETE CASCADE ON UPDATE CASCADE, 
    FOREIGN KEY (classification_id) REFERENCES classification(classification_id)
    ON DELETE CASCADE ON UPDATE CASCADE
  )

ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO object
(
    object_number,
    is_public_domain,
    department_id,
    object_title,
    -- artist_id,
    object_date,
    begin_date,
    end_date,
    -- acquisition_type_id,
    acquisition_date,
    city_id,
    country_id,
    region_id,
    classification_id,
    rights_and_reproduction,
    link_resource
  )

SELECT temp_object.object_number, temp_object.is_public_domain, d.department_id, temp_object.object_title, temp_object.object_date, temp_object.object_begin_date, temp_object.object_end_date, temp_object.acquisition_date, city.city_id, country.country_id, r.region_id, c.classification_id, temp_object.rights_and_reproduction, temp_object.link_resource
  FROM temp_object
    LEFT JOIN department d
      ON TRIM(temp_object.department_name) = TRIM(d.department_name)
    LEFT JOIN classification c
      ON TRIM(temp_object.classification) = TRIM(c.classification_name)
    LEFT JOIN city
      ON TRIM(temp_object.city) = TRIM(city.city_name)
    LEFT JOIN country
      ON TRIM(temp_object.country) = TRIM(country.country_name)
    LEFT JOIN region r
      ON TRIM(temp_object.region) = TRIM(r.region_name);



      


-- --
-- -- MET Acquistition   
-- --

-- --creating temporary acquisition table with data from met_acquisition tsv (unique acquisitions)
-- CREATE TEMPORARY IF NOT EXISTS temp_acquisition_from
--   (
--     acquisition_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
--     acquisition_from VARCHAR(225) NOT NULL,
--     PRIMARY KEY (acquisition_id)
--     )
-- ENGINE=InnoDB
-- CHARACTER SET utf8mb4
-- COLLATE utf8mb4_0900_ai_ci;

-- LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_acquisition.tsv'
-- INTO TABLE temp_acquisition_from
--   CHARACTER SET utf8mb4
--   FIELDS TERMINATED BY '\t'
--   -- FIELDS TERMINATED BY ','
--   ENCLOSED BY '"'
--   LINES TERMINATED BY '\n'
--   -- LINES TERMINATED BY '\r\n' 
--   (acquisition_from);


-- --creating temporary table when I extract acquisition type and date from larger csv file
-- CREATE TEMPORARY TABLE IF NOT EXISTS temp_acquisition_from_date
--   (
--     acquisition_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
--     acquisition_from VARCHAR(225) NOT NULL,
--     acquisition_date INTEGER NOT NULL,
--     PRIMARY KEY (acquisition_id)
--     )
-- ENGINE=InnoDB
-- CHARACTER SET latin1
-- COLLATE latin1_general_ci;

-- LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_dataset_nov29.csv'
-- INTO TABLE temp_acquisition_from_date
--   CHARACTER SET latin1
--   FIELDS TERMINATED BY '\t'
--   -- FIELDS TERMINATED BY ','
--   ENCLOSED BY '"'
--   LINES TERMINATED BY '\n'
--   -- LINES TERMINATED BY '\r\n' 
--   IGNORE 1 LINES
--   (@dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, acquisition_from, acquisition_date, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy);


-- --creating table that joins the two temp tables where the acquisition type is the same
-- CREATE TABLE IF NOT EXISTS acquisition
--   (
--     acquisition_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
--     acquisition_from VARCHAR(100) NOT NULL UNIQUE,
--     acquisition_date INTEGER NOT NULL,

--     PRIMARY KEY (acquisition_id)
--   )

-- ENGINE=InnoDB
-- CHARACTER SET utf8mb4
-- COLLATE utf8mb4_0900_ai_ci;

-- INSERT IGNORE INTO acquisition (acquisition_from, acquisition_date)
-- SELECT taf.acquisition_from, tafd.acquisition_date
-- FROM temp_acquisition_from taf
-- JOIN temp_acquisition_from_date tafd
-- ON taf.acquisition_from = tafd.acquisition_from
-- ORDER BY taf.acquisition_id;


-- DROP TEMPORARY TABLE temp_acquisition_from, temp_acquisition_from_date; 











--
-- MET Artist (+role and nationality)
--




--
-- MET Object_Artist
--