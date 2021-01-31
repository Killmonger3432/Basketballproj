-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `newteam`
--

DROP TABLE IF EXISTS `newteam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `newteam` (
  `Jersey_number` char(2) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Position` char(2) NOT NULL,
  `Overall` int NOT NULL,
  `Shooting_Outside` int NOT NULL,
  `Shooting_Inside` int NOT NULL,
  `Defense_Outside` int NOT NULL,
  `Defense_Inside` int NOT NULL,
  `Passing` int NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `points` int NOT NULL DEFAULT '0',
  `img1` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `newteam`
--

LOCK TABLES `newteam` WRITE;
/*!40000 ALTER TABLE `newteam` DISABLE KEYS */;
INSERT INTO `newteam` VALUES ('11','Kyrie Irving','PG',94,97,95,88,84,94,'kyrieirving.png',0,'im3'),('11','Kyrie Irving','PG',94,97,95,88,84,94,'kyrieirving.png',0,'im3'),('20','John Collins','PF',92,91,95,90,90,92,'johncollins.png',0,'pf6'),('13','Paul George','SG',94,92,96,97,93,92,'paulgeorge.png',0,'a3'),('3','Andre Drummond','C',85,81,93,86,94,82,'andredrummond.png',0,'i2');
/*!40000 ALTER TABLE `newteam` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-31 14:51:23
