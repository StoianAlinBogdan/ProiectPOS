-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`BOOKS`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`BOOKS` ;

CREATE TABLE IF NOT EXISTS `mydb`.`BOOKS` (
  `ISBN` VARCHAR(45) NOT NULL,
  `Title` VARCHAR(45) NULL,
  `Publisher` VARCHAR(45) NULL,
  `Year` VARCHAR(45) NULL,
  `Genre` VARCHAR(45) NULL,
  PRIMARY KEY (`ISBN`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `ISBN_UNIQUE` ON `mydb`.`BOOKS` (`ISBN` ASC) VISIBLE;

CREATE UNIQUE INDEX `Title_UNIQUE` ON `mydb`.`BOOKS` (`Title` ASC) VISIBLE;

CREATE INDEX `IX_YEAR` ON `mydb`.`BOOKS` (`Year` ASC) VISIBLE;

CREATE INDEX `IX_GENRE` ON `mydb`.`BOOKS` (`Genre` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`AUTHORS`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`AUTHORS` ;

CREATE TABLE IF NOT EXISTS `mydb`.`AUTHORS` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `FIRST_NAME` VARCHAR(45) NULL,
  `LAST_NAME` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `ID_UNIQUE` ON `mydb`.`AUTHORS` (`ID` ASC) VISIBLE;

CREATE INDEX `IX_FIRST_NAME` ON `mydb`.`AUTHORS` (`FIRST_NAME` ASC) VISIBLE;

CREATE INDEX `IX_LAST_NAME` ON `mydb`.`AUTHORS` (`LAST_NAME` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`BOOKS_TO_AUTHORS`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`BOOKS_TO_AUTHORS` ;

CREATE TABLE IF NOT EXISTS `mydb`.`BOOKS_TO_AUTHORS` (
  `BOOKS_ISBN` VARCHAR(45) NOT NULL,
  `AUTHORS_ID` INT NOT NULL,
  `index` VARCHAR(45) NULL,
  PRIMARY KEY (`BOOKS_ISBN`, `AUTHORS_ID`),
  CONSTRAINT `fk_BOOKS_has_AUTHORS_BOOKS`
    FOREIGN KEY (`BOOKS_ISBN`)
    REFERENCES `mydb`.`BOOKS` (`ISBN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_BOOKS_has_AUTHORS_AUTHORS1`
    FOREIGN KEY (`AUTHORS_ID`)
    REFERENCES `mydb`.`AUTHORS` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_BOOKS_has_AUTHORS_AUTHORS1_idx` ON `mydb`.`BOOKS_TO_AUTHORS` (`AUTHORS_ID` ASC) VISIBLE;

CREATE INDEX `fk_BOOKS_has_AUTHORS_BOOKS_idx` ON `mydb`.`BOOKS_TO_AUTHORS` (`BOOKS_ISBN` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
