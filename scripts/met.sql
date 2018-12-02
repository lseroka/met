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
DROP TABLE IF EXISTS artist, object_artist, object, department, acquisition, classification, city, country, region, role, nationality, temp_acquisition_from, temp_acquisition_from_date;
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
-- MET Acquistition   
--

--creating temporary acquisition table with data from met_acquisition tsv (unique acquisitions)
CREATE TEMPORARY IF NOT EXISTS temp_acquisition_from
  (
    acquisition_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    acquisition_from VARCHAR(225) NOT NULL,
    PRIMARY KEY (acquisition_id)
    )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_acquisition.tsv'
INTO TABLE temp_acquisition_from
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY '\t'
  -- FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  -- LINES TERMINATED BY '\r\n' 
  (acquisition_from);


--creating temporary table when I extract acquisition type and date from larger csv file
CREATE TEMPORARY TABLE IF NOT EXISTS temp_acquisition_from_date
  (
    acquisition_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    acquisition_from VARCHAR(225) NOT NULL,
    acquisition_date INTEGER NOT NULL,
    PRIMARY KEY (acquisition_id)
    )
ENGINE=InnoDB
CHARACTER SET latin1
COLLATE latin1_general_ci;

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/met_dataset_nov29.csv'
INTO TABLE temp_acquisition_from_date
  CHARACTER SET latin1
  FIELDS TERMINATED BY '\t'
  -- FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  -- LINES TERMINATED BY '\r\n' 
  IGNORE 1 LINES
  (@dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, acquisition_from, acquisition_date, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy);


--creating table that joins the two temp tables where the acquisition type is the same
CREATE TABLE IF NOT EXISTS acquisition
  (
    acquisition_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    acquisition_from VARCHAR(100) NOT NULL UNIQUE,
    acquisition_date INTEGER NOT NULL,

    PRIMARY KEY (acquisition_id)
  )

ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO acquisition (acquisition_from, acquisition_date)
SELECT taf.acquisition_from, tafd.acquisition_date
FROM temp_acquisition_from taf
JOIN temp_acquisition_from_date tafd
ON taf.acquisition_from = tafd.acquisition_from
ORDER BY taf.acquisition_id;


DROP TEMPORARY TABLE temp_acquisition_from, temp_acquisition_from_date; 






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
    country_name VARCHAR(100) NOT NULL UNIQUE,
    region_id INTEGER,
    PRIMARY KEY (country_id),
    FOREIGN KEY (region_id) REFERENCES region(region_id) ON DELETE RESTRICT ON UPDATE CASCADE
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
    country_id INTEGER,
    PRIMARY KEY (city_id),
    FOREIGN KEY (country_id) REFERENCES country(country_id) ON DELETE RESTRICT ON UPDATE CASCADE
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
-- MET Object
--



--
-- MET Artist (+role and nationality)
--




--
-- MET Object_Artist
--