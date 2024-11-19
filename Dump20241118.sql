CREATE DATABASE  IF NOT EXISTS `beaver_airlines` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `beaver_airlines`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: beaver_airlines
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `airplane`
--

DROP TABLE IF EXISTS `airplane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airplane` (
  `airplane_id` int unsigned NOT NULL AUTO_INCREMENT,
  `manufacturer` varchar(15) DEFAULT NULL,
  `model` varchar(15) DEFAULT NULL,
  `capacity` int NOT NULL,
  PRIMARY KEY (`airplane_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airplane`
--

LOCK TABLES `airplane` WRITE;
/*!40000 ALTER TABLE `airplane` DISABLE KEYS */;
INSERT INTO `airplane` VALUES (1,'Boeing','737',160),(2,'Airbus','A320',180),(3,'Boeing','777',396),(4,'Embraer','E195',120),(5,'Airbus','A380',555),(6,'Bombardier','CRJ200',50),(7,'Boeing','787',242),(8,'Airbus','A350',300),(9,'ATR','72',74),(10,'Sukhoi','Superjet 100',98),(11,'Boeing','747',410),(12,'Airbus','A330',277),(13,'Cessna','208',14),(14,'Bombardier','Q400',78),(15,'Mitsubishi','MRJ90',92),(16,'Airbus','A320',180);
/*!40000 ALTER TABLE `airplane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport` (
  `airport_id` int unsigned NOT NULL AUTO_INCREMENT,
  `airport_name` varchar(100) DEFAULT NULL,
  `city` varchar(25) NOT NULL,
  `country` varchar(25) NOT NULL,
  PRIMARY KEY (`airport_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
INSERT INTO `airport` VALUES (1,'Los Angeles International','Los Angeles','USA'),(2,'Heathrow','London','UK'),(3,'Charles de Gaulle','Paris','France'),(4,'John F. Kennedy','New York','USA'),(5,'Tokyo Narita','Tokyo','Japan'),(6,'Dubai International','Dubai','UAE'),(7,'Frankfurt Airport','Frankfurt','Germany'),(8,'Changi Airport','Singapore','Singapore'),(9,'Madrid Barajas','Madrid','Spain'),(10,'Hong Kong International','Hong Kong','China'),(11,'Sydney Kingsford Smith','Sydney','Australia'),(12,'Toronto Pearson','Toronto','Canada'),(13,'São Paulo Guarulhos','São Paulo','Brazil'),(14,'Incheon International','Seoul','South Korea'),(15,'Schiphol','Amsterdam','Netherlands');
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add airplane',6,'add_airplane'),(22,'Can change airplane',6,'change_airplane'),(23,'Can delete airplane',6,'delete_airplane'),(24,'Can view airplane',6,'view_airplane'),(25,'Can add airport',7,'add_airport'),(26,'Can change airport',7,'change_airport'),(27,'Can delete airport',7,'delete_airport'),(28,'Can view airport',7,'view_airport'),(29,'Can add booking',8,'add_booking'),(30,'Can change booking',8,'change_booking'),(31,'Can delete booking',8,'delete_booking'),(32,'Can view booking',8,'view_booking'),(33,'Can add crew member',9,'add_crewmember'),(34,'Can change crew member',9,'change_crewmember'),(35,'Can delete crew member',9,'delete_crewmember'),(36,'Can view crew member',9,'view_crewmember'),(37,'Can add flight',10,'add_flight'),(38,'Can change flight',10,'change_flight'),(39,'Can delete flight',10,'delete_flight'),(40,'Can view flight',10,'view_flight'),(41,'Can add flight review',11,'add_flightreview'),(42,'Can change flight review',11,'change_flightreview'),(43,'Can delete flight review',11,'delete_flightreview'),(44,'Can view flight review',11,'view_flightreview'),(45,'Can add passenger',12,'add_passenger'),(46,'Can change passenger',12,'change_passenger'),(47,'Can delete passenger',12,'delete_passenger'),(48,'Can view passenger',12,'view_passenger'),(49,'Can add passenger insurance',13,'add_passengerinsurance'),(50,'Can change passenger insurance',13,'change_passengerinsurance'),(51,'Can delete passenger insurance',13,'delete_passengerinsurance'),(52,'Can view passenger insurance',13,'view_passengerinsurance'),(53,'Can add user',14,'add_customuser'),(54,'Can change user',14,'change_customuser'),(55,'Can delete user',14,'delete_customuser'),(56,'Can view user',14,'view_customuser');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beaver_airlines_customuser`
--

DROP TABLE IF EXISTS `beaver_airlines_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beaver_airlines_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beaver_airlines_customuser`
--

LOCK TABLES `beaver_airlines_customuser` WRITE;
/*!40000 ALTER TABLE `beaver_airlines_customuser` DISABLE KEYS */;
INSERT INTO `beaver_airlines_customuser` VALUES (1,'pbkdf2_sha256$870000$DurBBJc7y1x4xPEMIKQspg$CRciYMBmtl1BWhDnAaDRXGER2FTK59d1lBI+/vkJSb8=','2024-11-18 03:40:38.394551',0,'krxllll','','',0,1,'2024-11-18 03:14:30.994871','romankrolyak@gmail.com'),(2,'pbkdf2_sha256$870000$NqmZW9rZu6O2MOcpfw3GVQ$INxCVZBv0BQi5rG6x0owGTm1pF8eKjp0kpNxHkdPEog=','2024-11-18 05:57:12.607040',1,'admin','','',1,1,'2024-11-18 05:46:22.000000','roman.kroliak.shi.2023@lpnu.ua');
/*!40000 ALTER TABLE `beaver_airlines_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beaver_airlines_customuser_groups`
--

DROP TABLE IF EXISTS `beaver_airlines_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beaver_airlines_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `beaver_airlines_customus_customuser_id_group_id_7197766a_uniq` (`customuser_id`,`group_id`),
  KEY `beaver_airlines_cust_group_id_f8781b9b_fk_auth_grou` (`group_id`),
  CONSTRAINT `beaver_airlines_cust_customuser_id_310e3403_fk_beaver_ai` FOREIGN KEY (`customuser_id`) REFERENCES `beaver_airlines_customuser` (`id`),
  CONSTRAINT `beaver_airlines_cust_group_id_f8781b9b_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beaver_airlines_customuser_groups`
--

LOCK TABLES `beaver_airlines_customuser_groups` WRITE;
/*!40000 ALTER TABLE `beaver_airlines_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `beaver_airlines_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beaver_airlines_customuser_user_permissions`
--

DROP TABLE IF EXISTS `beaver_airlines_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beaver_airlines_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `beaver_airlines_customus_customuser_id_permission_8981cc54_uniq` (`customuser_id`,`permission_id`),
  KEY `beaver_airlines_cust_permission_id_a99376d4_fk_auth_perm` (`permission_id`),
  CONSTRAINT `beaver_airlines_cust_customuser_id_6b6f7ad1_fk_beaver_ai` FOREIGN KEY (`customuser_id`) REFERENCES `beaver_airlines_customuser` (`id`),
  CONSTRAINT `beaver_airlines_cust_permission_id_a99376d4_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beaver_airlines_customuser_user_permissions`
--

LOCK TABLES `beaver_airlines_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `beaver_airlines_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `beaver_airlines_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `booking_id` int unsigned NOT NULL AUTO_INCREMENT,
  `flight_id` int unsigned NOT NULL,
  `passenger_id` int unsigned NOT NULL,
  `seat_number` varchar(6) NOT NULL,
  `booking_time` timestamp NOT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `flight_id` (`flight_id`),
  KEY `passenger_id` (`passenger_id`),
  CONSTRAINT `flight_booking_id` FOREIGN KEY (`flight_id`) REFERENCES `flight` (`flight_id`),
  CONSTRAINT `passenger_booking_id` FOREIGN KEY (`passenger_id`) REFERENCES `passenger` (`passenger_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (1,1,1,'A1','2024-10-20 07:00:00'),(2,2,2,'B1','2024-10-20 07:05:00'),(3,3,3,'C1','2024-10-20 07:10:00'),(4,4,4,'A2','2024-10-20 07:15:00'),(5,5,5,'B2','2024-10-20 07:20:00'),(6,6,6,'C2','2024-10-20 07:25:00'),(7,7,7,'A3','2024-10-20 07:30:00'),(8,8,8,'B3','2024-10-20 07:35:00'),(9,9,9,'C3','2024-10-20 07:40:00'),(10,10,10,'A4','2024-10-20 07:45:00'),(11,11,11,'B4','2024-10-20 07:50:00'),(12,12,12,'C4','2024-10-20 07:55:00'),(13,13,13,'A5','2024-10-20 08:00:00'),(14,14,14,'B5','2024-10-20 08:05:00'),(15,15,15,'C5','2024-10-20 08:10:00'),(18,1,1,'C69','2024-11-18 01:52:00'),(21,1,16,'C69','2024-11-18 03:23:33'),(22,2,16,'C69','2024-11-18 03:44:51');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crew_member`
--

DROP TABLE IF EXISTS `crew_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crew_member` (
  `crew_member_id` int unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `position` varchar(50) DEFAULT NULL,
  `airplane_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`crew_member_id`),
  KEY `airplane_id` (`airplane_id`),
  CONSTRAINT `airplane_crew_id` FOREIGN KEY (`airplane_id`) REFERENCES `airplane` (`airplane_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crew_member`
--

LOCK TABLES `crew_member` WRITE;
/*!40000 ALTER TABLE `crew_member` DISABLE KEYS */;
INSERT INTO `crew_member` VALUES (1,'Alice','Adams','Captain',1),(2,'Bob','Baker','First Officer',2),(3,'Charlie','Clark','Flight Attendant',3),(4,'Diana','Davis','Flight Attendant',4),(5,'Ethan','Evans','Captain',5),(6,'Fiona','Fox','First Officer',6),(7,'George','Green','Flight Attendant',7),(8,'Hannah','Harris','Flight Attendant',8),(9,'Ian','Irwin','Captain',9),(10,'Jenna','Jackson','First Officer',10),(11,'Kyle','King','Flight Attendant',11),(12,'Laura','Lewis','Flight Attendant',12),(13,'Matt','Morris','Captain',13),(14,'Nina','Nelson','First Officer',14),(15,'Oscar','Owens','Flight Attendant',15);
/*!40000 ALTER TABLE `crew_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_beaver_ai` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_beaver_ai` FOREIGN KEY (`user_id`) REFERENCES `beaver_airlines_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(6,'beaver_airlines','airplane'),(7,'beaver_airlines','airport'),(8,'beaver_airlines','booking'),(9,'beaver_airlines','crewmember'),(14,'beaver_airlines','customuser'),(10,'beaver_airlines','flight'),(11,'beaver_airlines','flightreview'),(12,'beaver_airlines','passenger'),(13,'beaver_airlines','passengerinsurance'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-11-18 03:13:52.664867'),(2,'contenttypes','0002_remove_content_type_name','2024-11-18 03:13:52.746864'),(3,'auth','0001_initial','2024-11-18 03:13:53.038864'),(4,'auth','0002_alter_permission_name_max_length','2024-11-18 03:13:53.099865'),(5,'auth','0003_alter_user_email_max_length','2024-11-18 03:13:53.104864'),(6,'auth','0004_alter_user_username_opts','2024-11-18 03:13:53.109866'),(7,'auth','0005_alter_user_last_login_null','2024-11-18 03:13:53.116864'),(8,'auth','0006_require_contenttypes_0002','2024-11-18 03:13:53.118865'),(9,'auth','0007_alter_validators_add_error_messages','2024-11-18 03:13:53.123867'),(10,'auth','0008_alter_user_username_max_length','2024-11-18 03:13:53.130865'),(11,'auth','0009_alter_user_last_name_max_length','2024-11-18 03:13:53.135865'),(12,'auth','0010_alter_group_name_max_length','2024-11-18 03:13:53.149866'),(13,'auth','0011_update_proxy_permissions','2024-11-18 03:13:53.154867'),(14,'auth','0012_alter_user_first_name_max_length','2024-11-18 03:13:53.160863'),(15,'beaver_airlines','0001_initial','2024-11-18 03:13:53.560866'),(16,'admin','0001_initial','2024-11-18 03:13:53.705866'),(17,'admin','0002_logentry_remove_auto_add','2024-11-18 03:13:53.712865'),(18,'admin','0003_logentry_add_action_flag_choices','2024-11-18 03:13:53.721863'),(19,'sessions','0001_initial','2024-11-18 03:13:53.758866');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4rim795eyhdb62xizv3mstfehjl47s24','.eJxVjDEOAiEQRe9CbQggs6ClvWcgAzPIqoFk2a2Md1eSLbT9773_EgG3tYSt8xJmEmdhxOF3i5geXAegO9Zbk6nVdZmjHIrcaZfXRvy87O7fQcFevrV3WSWtwTEbp04TQY4JAawlYu8zWGesN5RwspDZqKHlY9Q6Kacwi_cH30g30A:1tCul6:c5-uI2E3s8UUP9yZOo-EramIkoP6Sd0pYZCvH3TS3ds','2024-12-02 05:57:12.612042');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `flight_id` int unsigned NOT NULL AUTO_INCREMENT,
  `airplane_id` int unsigned NOT NULL,
  `departure_airport_id` int unsigned NOT NULL,
  `arrival_airport_id` int unsigned NOT NULL,
  `departure_time` timestamp NULL DEFAULT NULL,
  `arrival_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`flight_id`),
  KEY `airplane_id` (`airplane_id`),
  KEY `departure_airport_id` (`departure_airport_id`),
  KEY `arrival_airport_id` (`arrival_airport_id`),
  CONSTRAINT `arrival_airport_id` FOREIGN KEY (`arrival_airport_id`) REFERENCES `airport` (`airport_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `departure_airport_id` FOREIGN KEY (`departure_airport_id`) REFERENCES `airport` (`airport_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `flight_airplane_id` FOREIGN KEY (`airplane_id`) REFERENCES `airplane` (`airplane_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (1,1,1,2,'2024-11-01 06:00:00','2024-11-01 14:00:00'),(2,2,3,4,'2024-11-02 08:00:00','2024-11-02 16:00:00'),(3,3,5,6,'2024-11-03 12:00:00','2024-11-03 20:00:00'),(4,4,7,8,'2024-11-04 07:00:00','2024-11-04 15:00:00'),(5,5,9,10,'2024-11-05 05:00:00','2024-11-05 13:00:00'),(6,6,11,12,'2024-11-06 09:00:00','2024-11-06 17:00:00'),(7,7,13,14,'2024-11-07 04:00:00','2024-11-07 12:00:00'),(8,8,15,1,'2024-11-08 10:00:00','2024-11-08 18:00:00'),(9,9,2,3,'2024-11-09 08:00:00','2024-11-09 16:00:00'),(10,10,4,5,'2024-11-10 06:00:00','2024-11-10 14:00:00'),(11,11,6,7,'2024-11-11 09:00:00','2024-11-11 17:00:00'),(12,12,8,9,'2024-11-12 07:00:00','2024-11-12 15:00:00'),(13,13,10,11,'2024-11-13 11:00:00','2024-11-13 19:00:00'),(14,14,12,13,'2024-11-14 08:00:00','2024-11-14 16:00:00'),(15,15,14,15,'2024-11-15 06:00:00','2024-11-15 14:00:00');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight_review`
--

DROP TABLE IF EXISTS `flight_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_review` (
  `review_id` int unsigned NOT NULL AUTO_INCREMENT,
  `flight_id` int unsigned NOT NULL,
  `passenger_id` int unsigned NOT NULL,
  `rating` int NOT NULL,
  `comment` text,
  `review_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`),
  KEY `flight_id` (`flight_id`),
  KEY `passenger_id` (`passenger_id`),
  CONSTRAINT `flight_review_id` FOREIGN KEY (`flight_id`) REFERENCES `flight` (`flight_id`),
  CONSTRAINT `passenger_review_id` FOREIGN KEY (`passenger_id`) REFERENCES `passenger` (`passenger_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_review`
--

LOCK TABLES `flight_review` WRITE;
/*!40000 ALTER TABLE `flight_review` DISABLE KEYS */;
INSERT INTO `flight_review` VALUES (1,1,1,5,'Excellent flight, very smooth.','2024-10-23 11:27:58'),(2,2,2,4,'Good flight, a bit delayed.','2024-10-23 11:27:58'),(3,3,3,3,'Average experience, nothing special.','2024-10-23 11:27:58'),(4,4,4,5,'Great service, comfortable seats.','2024-10-23 11:27:58'),(5,5,5,2,'Long delay, uncomfortable seats.','2024-10-23 11:27:58'),(6,6,6,4,'Good overall, staff were helpful.','2024-10-23 11:27:58'),(7,7,7,5,'Amazing experience, highly recommend.','2024-10-23 11:27:58'),(8,8,8,3,'Flight was okay, food could be better.','2024-10-23 11:27:58'),(9,9,9,4,'Pleasant flight, but a bit noisy.','2024-10-23 11:27:58'),(10,10,10,5,'Perfect, will fly again.','2024-10-23 11:27:58'),(11,11,11,2,'Seats were cramped, not great.','2024-10-23 11:27:58'),(12,12,12,3,'Average flight, nothing to complain about.','2024-10-23 11:27:58'),(13,13,13,5,'Great staff, very professional.','2024-10-23 11:27:58'),(14,14,14,4,'Good flight, but no in-flight entertainment.','2024-10-23 11:27:58'),(15,15,15,5,'Excellent, best flight I’ve had.','2024-10-23 11:27:58');
/*!40000 ALTER TABLE `flight_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger`
--

DROP TABLE IF EXISTS `passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger` (
  `passenger_id` int unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` varchar(20) NOT NULL,
  PRIMARY KEY (`passenger_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger`
--

LOCK TABLES `passenger` WRITE;
/*!40000 ALTER TABLE `passenger` DISABLE KEYS */;
INSERT INTO `passenger` VALUES (1,'John','Doe','john.doe@example.com','1234567890'),(2,'Jane','Smith','jane.smith@example.com','0987654321'),(3,'James','Brown','james.brown@example.com','9876543210'),(4,'Emily','Johnson','emily.johnson@example.com','8765432109'),(5,'Michael','Williams','michael.williams@example.com','7654321098'),(6,'Sarah','Jones','sarah.jones@example.com','6543210987'),(7,'David','Garcia','david.garcia@example.com','5432109876'),(8,'Sophia','Martinez','sophia.martinez@example.com','4321098765'),(9,'Robert','Rodriguez','robert.rodriguez@example.com','3210987654'),(10,'Olivia','Lee','olivia.lee@example.com','2109876543'),(11,'Lucas','Hernandez','lucas.hernandez@example.com','1098765432'),(12,'Emma','Lopez','emma.lopez@example.com','9876543212'),(13,'Ethan','Gonzalez','ethan.gonzalez@example.com','8765432108'),(14,'Mia','Moore','mia.moore@example.com','7654321097'),(15,'Liam','Martinez','liam.martinez@example.com','6543210986'),(16,'Roman','Kroliak','romankrolyak@gmail.com','0970853512');
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger_insurance`
--

DROP TABLE IF EXISTS `passenger_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger_insurance` (
  `passenger_id` int unsigned NOT NULL,
  `policy_number` varchar(50) NOT NULL,
  `coverage_amount` decimal(10,2) unsigned NOT NULL,
  `issue_date` date NOT NULL,
  `expiry_date` date NOT NULL,
  PRIMARY KEY (`passenger_id`),
  CONSTRAINT `passenger_insurance_id` FOREIGN KEY (`passenger_id`) REFERENCES `passenger` (`passenger_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger_insurance`
--

LOCK TABLES `passenger_insurance` WRITE;
/*!40000 ALTER TABLE `passenger_insurance` DISABLE KEYS */;
INSERT INTO `passenger_insurance` VALUES (1,'POL123456789',100000.00,'2024-01-01','2025-01-01'),(2,'POL987654321',150000.00,'2024-02-01','2025-02-01'),(3,'POL654321987',200000.00,'2024-03-01','2025-03-01'),(4,'POL321987654',100000.00,'2024-04-01','2025-04-01'),(5,'POL789456123',250000.00,'2024-05-01','2025-05-01'),(6,'POL456123789',300000.00,'2024-06-01','2025-06-01'),(7,'POL123789456',100000.00,'2024-07-01','2025-07-01'),(8,'POL789123456',150000.00,'2024-08-01','2025-08-01'),(9,'POL654789321',200000.00,'2024-09-01','2025-09-01'),(10,'POL321654987',100000.00,'2024-10-01','2025-10-01'),(11,'POL456987123',150000.00,'2024-11-01','2025-11-01'),(12,'POL789321654',250000.00,'2024-12-01','2025-12-01'),(13,'POL123456789',300000.00,'2024-11-01','2025-11-01'),(14,'POL987654321',100000.00,'2024-01-01','2025-01-01'),(15,'POL654321987',150000.00,'2024-02-01','2025-02-01');
/*!40000 ALTER TABLE `passenger_insurance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-18  8:23:29
