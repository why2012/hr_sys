-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: hr_db
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user group menu item',7,'add_usergroupmenuitem'),(26,'Can change user group menu item',7,'change_usergroupmenuitem'),(27,'Can delete user group menu item',7,'delete_usergroupmenuitem'),(28,'Can view user group menu item',7,'view_usergroupmenuitem'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add menu item',9,'add_menuitem'),(34,'Can change menu item',9,'change_menuitem'),(35,'Can delete menu item',9,'delete_menuitem'),(36,'Can view menu item',9,'view_menuitem'),(37,'Can add user group',10,'add_usergroup'),(38,'Can change user group',10,'change_usergroup'),(39,'Can delete user group',10,'delete_usergroup'),(40,'Can view user group',10,'view_usergroup'),(41,'Can add key value',11,'add_keyvalue'),(42,'Can change key value',11,'change_keyvalue'),(43,'Can delete key value',11,'delete_keyvalue'),(44,'Can view key value',11,'view_keyvalue'),(45,'Can add department',12,'add_department'),(46,'Can change department',12,'change_department'),(47,'Can delete department',12,'delete_department'),(48,'Can view department',12,'view_department'),(49,'Can add employee attendance',13,'add_employeeattendance'),(50,'Can change employee attendance',13,'change_employeeattendance'),(51,'Can delete employee attendance',13,'delete_employeeattendance'),(52,'Can view employee attendance',13,'view_employeeattendance'),(53,'Can add employee position',14,'add_employeeposition'),(54,'Can change employee position',14,'change_employeeposition'),(55,'Can delete employee position',14,'delete_employeeposition'),(56,'Can view employee position',14,'view_employeeposition'),(57,'Can add employ promote history',15,'add_employpromotehistory'),(58,'Can change employ promote history',15,'change_employpromotehistory'),(59,'Can delete employ promote history',15,'delete_employpromotehistory'),(60,'Can view employ promote history',15,'view_employpromotehistory'),(61,'Can add employee',16,'add_employee'),(62,'Can change employee',16,'change_employee'),(63,'Can delete employee',16,'delete_employee'),(64,'Can view employee',16,'view_employee'),(65,'Can add employee level',17,'add_employeelevel'),(66,'Can change employee level',17,'change_employeelevel'),(67,'Can delete employee level',17,'delete_employeelevel'),(68,'Can view employee level',17,'view_employeelevel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$dv8kC2751VdW$D2gaqYz3f5WE5QgTrWo/ZDESHycZWk++t4JSVHKKGE4=','2019-02-25 13:33:04.201425',1,'why','','','11111@qq.com',1,1,'2019-02-17 12:21:30.559587');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-02-18 15:36:42.289829','1','MenuItem object (1)',1,'[{\"added\": {}}]',9,1),(2,'2019-02-18 15:41:57.270981','2','MenuItem object (2)',1,'[{\"added\": {}}]',9,1),(3,'2019-02-18 15:43:29.746871','3','MenuItem object (3)',1,'[{\"added\": {}}]',9,1),(4,'2019-02-18 16:03:45.963303','4','MenuItem object (4)',1,'[{\"added\": {}}]',9,1),(5,'2019-02-18 16:04:11.439059','5','MenuItem object (5)',1,'[{\"added\": {}}]',9,1),(6,'2019-02-18 16:04:41.040745','6','MenuItem object (6)',1,'[{\"added\": {}}]',9,1),(7,'2019-02-18 16:05:37.935597','7','MenuItem object (7)',1,'[{\"added\": {}}]',9,1),(8,'2019-02-18 16:07:31.250193','7','MenuItem object (7)',2,'[]',9,1),(9,'2019-02-18 16:08:38.228323','1','UserGroupMenuItem object (1)',1,'[{\"added\": {}}]',7,1),(10,'2019-02-18 16:08:48.129560','2','UserGroupMenuItem object (2)',1,'[{\"added\": {}}]',7,1),(11,'2019-02-18 16:08:56.172377','3','UserGroupMenuItem object (3)',1,'[{\"added\": {}}]',7,1),(12,'2019-02-18 17:24:04.001676','4','MenuItem object (4)',2,'[{\"changed\": {\"fields\": [\"icon_url\", \"link_url\"]}}]',9,1),(13,'2019-02-19 09:55:13.857909','4','MenuItem object (4)',2,'[{\"changed\": {\"fields\": [\"icon_url\"]}}]',9,1),(14,'2019-02-19 09:57:11.746541','4','MenuItem object (4)',2,'[{\"changed\": {\"fields\": [\"icon_url\"]}}]',9,1),(15,'2019-02-19 09:58:03.523236','7','MenuItem object (7)',2,'[{\"changed\": {\"fields\": [\"icon_url\"]}}]',9,1),(16,'2019-02-19 16:51:42.375390','1','Department object (1)',1,'[{\"added\": {}}]',12,1),(17,'2019-02-19 16:52:22.394430','2','Department object (2)',1,'[{\"added\": {}}]',12,1),(18,'2019-02-19 16:52:27.896673','3','Department object (3)',1,'[{\"added\": {}}]',12,1),(19,'2019-02-19 16:52:45.499649','4','Department object (4)',1,'[{\"added\": {}}]',12,1),(20,'2019-02-19 16:52:54.484679','5','Department object (5)',1,'[{\"added\": {}}]',12,1),(21,'2019-02-19 16:53:48.217817','6','Department object (6)',1,'[{\"added\": {}}]',12,1),(22,'2019-02-19 16:54:22.317520','7','Department object (7)',1,'[{\"added\": {}}]',12,1),(23,'2019-02-19 16:54:31.324554','8','Department object (8)',1,'[{\"added\": {}}]',12,1),(24,'2019-02-19 17:50:24.405991','8','MenuItem object (8)',1,'[{\"added\": {}}]',9,1),(25,'2019-02-20 05:48:48.758932','1','EmployeeLevel object (1)',1,'[{\"added\": {}}]',17,1),(26,'2019-02-20 05:49:17.130342','2','EmployeeLevel object (2)',1,'[{\"added\": {}}]',17,1),(27,'2019-02-20 06:53:17.186943','9','MenuItem object (9)',1,'[{\"added\": {}}]',9,1),(28,'2019-02-20 06:55:16.990513','4','MenuItem object (4)',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(29,'2019-02-20 08:53:15.886522','1','EmployeePosition object (1)',1,'[{\"added\": {}}]',14,1),(30,'2019-02-20 08:53:28.690415','2','EmployeePosition object (2)',1,'[{\"added\": {}}]',14,1),(31,'2019-02-20 08:53:38.424613','3','EmployeePosition object (3)',1,'[{\"added\": {}}]',14,1),(32,'2019-02-20 08:53:50.106252','4','EmployeePosition object (4)',1,'[{\"added\": {}}]',14,1),(33,'2019-02-20 09:25:40.914891','1','Employee object (1)',1,'[{\"added\": {}}]',16,1),(34,'2019-02-20 10:52:33.451363','4','MenuItem object (4)',2,'[{\"changed\": {\"fields\": [\"link_url\"]}}]',9,1),(35,'2019-02-20 12:44:22.289877','10','MenuItem object (10)',1,'[{\"added\": {}}]',9,1),(36,'2019-02-20 13:06:14.729346','11','MenuItem object (11)',1,'[{\"added\": {}}]',9,1),(37,'2019-02-20 13:07:34.054265','10','MenuItem object (10)',2,'[{\"changed\": {\"fields\": [\"icon_url\"]}}]',9,1),(38,'2019-02-20 15:46:54.329368','7','Employee object (7)',2,'[{\"changed\": {\"fields\": [\"induction_date\"]}}]',16,1),(39,'2019-02-20 16:30:00.834642','5','MenuItem object (5)',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(40,'2019-02-20 16:30:22.691579','6','MenuItem object (6)',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(41,'2019-02-20 16:30:49.663672','7','MenuItem object (7)',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',9,1),(42,'2019-02-20 16:31:58.073125','12','MenuItem object (12)',1,'[{\"added\": {}}]',9,1),(43,'2019-02-20 16:32:26.537555','13','MenuItem object (13)',1,'[{\"added\": {}}]',9,1),(44,'2019-02-20 16:32:55.800165','14','MenuItem object (14)',1,'[{\"added\": {}}]',9,1),(45,'2019-02-21 14:11:18.909382','5','MenuItem object (5)',2,'[{\"changed\": {\"fields\": [\"link_url\"]}}]',9,1),(46,'2019-02-21 14:22:00.307270','12','MenuItem object (12)',2,'[{\"changed\": {\"fields\": [\"icon_url\"]}}]',9,1),(47,'2019-02-21 14:22:27.564427','13','MenuItem object (13)',2,'[{\"changed\": {\"fields\": [\"icon_url\"]}}]',9,1),(48,'2019-02-21 14:22:50.418589','14','MenuItem object (14)',2,'[{\"changed\": {\"fields\": [\"icon_url\"]}}]',9,1),(49,'2019-02-21 15:15:30.886517','12','MenuItem object (12)',2,'[{\"changed\": {\"fields\": [\"link_url\"]}}]',9,1),(50,'2019-02-21 15:45:00.689301','13','MenuItem object (13)',2,'[{\"changed\": {\"fields\": [\"link_url\"]}}]',9,1),(51,'2019-02-21 16:46:02.809776','14','MenuItem object (14)',2,'[{\"changed\": {\"fields\": [\"link_url\"]}}]',9,1),(52,'2019-02-22 19:30:16.014822','6','MenuItem object (6)',2,'[{\"changed\": {\"fields\": [\"link_url\"]}}]',9,1),(53,'2019-02-23 12:26:09.997295','7','MenuItem object (7)',2,'[{\"changed\": {\"fields\": [\"link_url\"]}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'hr_sys','department'),(16,'hr_sys','employee'),(13,'hr_sys','employeeattendance'),(17,'hr_sys','employeelevel'),(14,'hr_sys','employeeposition'),(15,'hr_sys','employpromotehistory'),(11,'hr_sys','keyvalue'),(9,'hr_sys','menuitem'),(8,'hr_sys','user'),(10,'hr_sys','usergroup'),(7,'hr_sys','usergroupmenuitem'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-02-17 12:16:18.954198'),(2,'auth','0001_initial','2019-02-17 12:16:19.109233'),(3,'admin','0001_initial','2019-02-17 12:16:19.177249'),(4,'admin','0002_logentry_remove_auto_add','2019-02-17 12:16:19.186250'),(5,'admin','0003_logentry_add_action_flag_choices','2019-02-17 12:16:19.195253'),(6,'contenttypes','0002_remove_content_type_name','2019-02-17 12:16:19.229261'),(7,'auth','0002_alter_permission_name_max_length','2019-02-17 12:16:19.237262'),(8,'auth','0003_alter_user_email_max_length','2019-02-17 12:16:19.247264'),(9,'auth','0004_alter_user_username_opts','2019-02-17 12:16:19.256270'),(10,'auth','0005_alter_user_last_login_null','2019-02-17 12:16:19.272270'),(11,'auth','0006_require_contenttypes_0002','2019-02-17 12:16:19.275271'),(12,'auth','0007_alter_validators_add_error_messages','2019-02-17 12:16:19.283272'),(13,'auth','0008_alter_user_username_max_length','2019-02-17 12:16:19.294276'),(14,'auth','0009_alter_user_last_name_max_length','2019-02-17 12:16:19.305278'),(15,'sessions','0001_initial','2019-02-17 12:16:19.318281'),(16,'hr_sys','0001_initial','2019-02-18 12:10:10.577589'),(17,'hr_sys','0002_auto_20190219_2339','2019-02-19 15:39:43.326278');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2hpdn06v20hcuxzf2dtshlt11gruov48','ZDFmYzJkYWMwZjVjZTFlMWNlYTU3MDM5MjliMTZhYTM2MDNjNWY5NTp7InVzZXJuYW1lIjoid2h5IiwidXNlcmlkIjoxfQ==','2019-02-22 17:05:15.317118'),('cx1mi9kowa5xhlt8y5zaivvde13lbvvx','YWZmMjcyMWZmOWY1ODIxMmY0NmMzZjBhYjc2MTA4NjZhMDlkMDI0NTp7InVzZXJuYW1lIjoid2h5IiwidXNlcmlkIjoxLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzVhZTQ0MGNiZjhjNTM1YmYxM2MxNzU4MjEwNjdkMGRhMmVlMjIyYyJ9','2019-02-26 13:33:04.204426'),('fcpu00cpist04b8dl6i9kj6fxi1mfiw8','ZTQyOTVlNDc3MjdmYmQ2NGZiMDlmNjg5NGVkNTJiNzBiMzk3YzQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NWFlNDQwY2JmOGM1MzViZjEzYzE3NTgyMTA2N2QwZGEyZWUyMjJjIn0=','2019-02-19 14:48:52.215471'),('fe98fh1jd7g33mxionsc1akhnr8tz9mw','ZDFmYzJkYWMwZjVjZTFlMWNlYTU3MDM5MjliMTZhYTM2MDNjNWY5NTp7InVzZXJuYW1lIjoid2h5IiwidXNlcmlkIjoxfQ==','2019-02-21 15:44:44.726092'),('hnenuoe8yj9pwqw6o8tpl54g7y7mwukp','ZDFmYzJkYWMwZjVjZTFlMWNlYTU3MDM5MjliMTZhYTM2MDNjNWY5NTp7InVzZXJuYW1lIjoid2h5IiwidXNlcmlkIjoxfQ==','2019-02-25 08:26:29.012171'),('iqqkyi0vvgir9s68yogqpi82i4t6q76n','ZTQyOTVlNDc3MjdmYmQ2NGZiMDlmNjg5NGVkNTJiNzBiMzk3YzQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NWFlNDQwY2JmOGM1MzViZjEzYzE3NTgyMTA2N2QwZGEyZWUyMjJjIn0=','2019-02-21 15:42:29.636579'),('l6e7lhbd2axrpjf7ujr3eqcj8p9bsx9v','ZDFmYzJkYWMwZjVjZTFlMWNlYTU3MDM5MjliMTZhYTM2MDNjNWY5NTp7InVzZXJuYW1lIjoid2h5IiwidXNlcmlkIjoxfQ==','2019-02-19 14:38:51.143693'),('rg2z7plzuw7t5osutr8sbl4zn5ikcbu3','ZDFmYzJkYWMwZjVjZTFlMWNlYTU3MDM5MjliMTZhYTM2MDNjNWY5NTp7InVzZXJuYW1lIjoid2h5IiwidXNlcmlkIjoxfQ==','2019-02-20 15:13:22.805249'),('seyyck4pfj5j5hny06v903zadd569x11','ZTQyOTVlNDc3MjdmYmQ2NGZiMDlmNjg5NGVkNTJiNzBiMzk3YzQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NWFlNDQwY2JmOGM1MzViZjEzYzE3NTgyMTA2N2QwZGEyZWUyMjJjIn0=','2019-02-22 15:44:54.322863'),('t0aqejf8q8qgqbneprvusy6lkz4khygr','ZTQyOTVlNDc3MjdmYmQ2NGZiMDlmNjg5NGVkNTJiNzBiMzk3YzQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NWFlNDQwY2JmOGM1MzViZjEzYzE3NTgyMTA2N2QwZGEyZWUyMjJjIn0=','2019-02-23 19:30:06.474666'),('x0fajrg7rbn4l9hsvaw9fx7df4h2mft4','ZDFmYzJkYWMwZjVjZTFlMWNlYTU3MDM5MjliMTZhYTM2MDNjNWY5NTp7InVzZXJuYW1lIjoid2h5IiwidXNlcmlkIjoxfQ==','2019-02-23 20:02:46.502422'),('yweesu55q0d360nt3oblixw9x5k6i20n','ZTQyOTVlNDc3MjdmYmQ2NGZiMDlmNjg5NGVkNTJiNzBiMzk3YzQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NWFlNDQwY2JmOGM1MzViZjEzYzE3NTgyMTA2N2QwZGEyZWUyMjJjIn0=','2019-02-20 15:34:19.746183');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_department`
--

DROP TABLE IF EXISTS `hr_sys_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `parent_id` int(11) NOT NULL,
  `manager_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hr_sys_department_employee_id` (`manager_id`),
  CONSTRAINT `hr_sys_department_employee_id` FOREIGN KEY (`manager_id`) REFERENCES `hr_sys_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_department`
--

LOCK TABLES `hr_sys_department` WRITE;
/*!40000 ALTER TABLE `hr_sys_department` DISABLE KEYS */;
INSERT INTO `hr_sys_department` VALUES (1,'互动娱乐事业群',-1,1),(2,'梦幻事业部',1,NULL),(3,'天下事业部',1,NULL),(4,'大话事业部',1,NULL),(5,'海神事业部',1,NULL),(6,'技术中心',1,NULL),(7,'移动应用',6,NULL),(16,'测试开发',6,NULL),(17,'服务端开发',6,NULL),(19,'ooo',17,NULL);
/*!40000 ALTER TABLE `hr_sys_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_employee`
--

DROP TABLE IF EXISTS `hr_sys_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `manager_id` int(11) NOT NULL,
  `province_name` varchar(50) NOT NULL,
  `city_name` varchar(50) NOT NULL,
  `salary` int(10) unsigned NOT NULL,
  `status` smallint(6) NOT NULL,
  `department_id` int(11) NOT NULL,
  `level_id` int(11) NOT NULL,
  `position_id` int(11) NOT NULL,
  `induction_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hr_sys_employee_department_id_063a4d68_fk_hr_sys_department_id` (`department_id`),
  KEY `hr_sys_employee_level_id_6f63278a_fk_hr_sys_employeelevel_id` (`level_id`),
  KEY `hr_sys_employee_position_id_d9fa2646_fk_hr_sys_em` (`position_id`),
  CONSTRAINT `hr_sys_employee_department_id_063a4d68_fk_hr_sys_department_id` FOREIGN KEY (`department_id`) REFERENCES `hr_sys_department` (`id`),
  CONSTRAINT `hr_sys_employee_level_id_6f63278a_fk_hr_sys_employeelevel_id` FOREIGN KEY (`level_id`) REFERENCES `hr_sys_employeelevel` (`id`),
  CONSTRAINT `hr_sys_employee_position_id_d9fa2646_fk_hr_sys_em` FOREIGN KEY (`position_id`) REFERENCES `hr_sys_employeeposition` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_employee`
--

LOCK TABLES `hr_sys_employee` WRITE;
/*!40000 ALTER TABLE `hr_sys_employee` DISABLE KEYS */;
INSERT INTO `hr_sys_employee` VALUES (1,'李湘','1','11111111@qq.com','11111111111',-1,'北京市','丰台区',20,0,3,2,4,'2019-02-19 00:19:54.000000'),(2,'李彤','1','22222222@qq.com','2222222222',-1,'北京市','海淀区',20,0,2,2,3,'2019-02-20 00:19:25.000000'),(4,'李健','0','','',-1,'北京市','房山区',30,1,3,3,2,'2019-02-21 00:19:25.000000'),(6,'王丹','1','33333333@qq.com','33333333333',1,'四川省','成都市',22,0,1,2,3,'2019-02-21 00:19:08.000000'),(7,'王丹丹','1','444444444@qq.com','44444444444',2,'四川省','成都市',10,0,2,2,2,'2019-02-20 06:00:00.000000'),(8,'张浩','0','55555555@163.com','55555555555',-1,'四川省','成都市',25,0,6,2,2,'2019-02-20 00:05:54.000000');
/*!40000 ALTER TABLE `hr_sys_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_employeeattendance`
--

DROP TABLE IF EXISTS `hr_sys_employeeattendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_employeeattendance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` smallint(6) NOT NULL,
  `standard_time` varchar(20) NOT NULL,
  `check_time` datetime(6) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hr_sys_employeeatten_employee_id_a9978b32_fk_hr_sys_em` (`employee_id`),
  CONSTRAINT `hr_sys_employeeatten_employee_id_a9978b32_fk_hr_sys_em` FOREIGN KEY (`employee_id`) REFERENCES `hr_sys_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_employeeattendance`
--

LOCK TABLES `hr_sys_employeeattendance` WRITE;
/*!40000 ALTER TABLE `hr_sys_employeeattendance` DISABLE KEYS */;
INSERT INTO `hr_sys_employeeattendance` VALUES (1,0,' 10:00\n','2019-02-22 19:29:00.903855',1),(2,0,' 10:00\n','2019-02-22 19:29:00.903855',2),(3,0,' 10:00\n','2019-02-22 19:29:00.903855',6),(4,0,' 10:00\n','2019-02-22 19:29:00.903855',7),(5,0,' 10:00\n','2019-02-22 19:29:00.903855',8),(6,0,' 10:00\n','2019-02-22 19:35:06.284391',1),(7,1,' 10:00\n','2019-02-22 19:35:06.284391',2),(8,1,' 10:00\n','2019-02-22 19:35:06.284391',6),(9,0,' 10:00\n','2019-02-22 19:35:06.284391',7),(10,0,' 10:00\n','2019-02-22 19:35:06.284391',8),(11,0,' 10:00\n','2019-02-25 13:53:04.897159',1),(12,0,' 10:00\n','2019-02-25 13:53:04.897159',2),(13,0,' 10:00\n','2019-02-25 13:53:04.897159',6),(14,0,' 10:00\n','2019-02-25 13:53:04.897159',7),(15,0,' 10:00\n','2019-02-25 13:53:04.897159',8);
/*!40000 ALTER TABLE `hr_sys_employeeattendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_employeelevel`
--

DROP TABLE IF EXISTS `hr_sys_employeelevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_employeelevel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `order` int(11) NOT NULL,
  `next_level_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_employeelevel`
--

LOCK TABLES `hr_sys_employeelevel` WRITE;
/*!40000 ALTER TABLE `hr_sys_employeelevel` DISABLE KEYS */;
INSERT INTO `hr_sys_employeelevel` VALUES (1,'P1',1,2),(2,'P2',2,3),(3,'P3',3,7),(7,'P4',4,-1);
/*!40000 ALTER TABLE `hr_sys_employeelevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_employeeposition`
--

DROP TABLE IF EXISTS `hr_sys_employeeposition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_employeeposition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_employeeposition`
--

LOCK TABLES `hr_sys_employeeposition` WRITE;
/*!40000 ALTER TABLE `hr_sys_employeeposition` DISABLE KEYS */;
INSERT INTO `hr_sys_employeeposition` VALUES (1,'JAVA研发'),(2,'技术支持'),(3,'人力资源'),(4,'产品经理'),(5,'游戏策划');
/*!40000 ALTER TABLE `hr_sys_employeeposition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_employpromotehistory`
--

DROP TABLE IF EXISTS `hr_sys_employpromotehistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_employpromotehistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` smallint(6) NOT NULL,
  `log_time` datetime(6) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `from_level_id` int(11) NOT NULL,
  `to_level_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hr_sys_employpromote_employee_id_25cbb624_fk_hr_sys_em` (`employee_id`),
  KEY `hr_sys_employpromote_from_level_id_06e0cc8b_fk_hr_sys_em` (`from_level_id`),
  KEY `hr_sys_employpromote_to_level_id_2d08fff7_fk_hr_sys_em` (`to_level_id`),
  CONSTRAINT `hr_sys_employpromote_employee_id_25cbb624_fk_hr_sys_em` FOREIGN KEY (`employee_id`) REFERENCES `hr_sys_employee` (`id`),
  CONSTRAINT `hr_sys_employpromote_from_level_id_06e0cc8b_fk_hr_sys_em` FOREIGN KEY (`from_level_id`) REFERENCES `hr_sys_employeelevel` (`id`),
  CONSTRAINT `hr_sys_employpromote_to_level_id_2d08fff7_fk_hr_sys_em` FOREIGN KEY (`to_level_id`) REFERENCES `hr_sys_employeelevel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_employpromotehistory`
--

LOCK TABLES `hr_sys_employpromotehistory` WRITE;
/*!40000 ALTER TABLE `hr_sys_employpromotehistory` DISABLE KEYS */;
INSERT INTO `hr_sys_employpromotehistory` VALUES (1,0,'2019-02-21 14:10:23.803934',1,2,3),(2,2,'2019-02-21 14:10:40.980815',1,3,2),(3,0,'2019-02-21 14:11:37.759640',7,1,2);
/*!40000 ALTER TABLE `hr_sys_employpromotehistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_keyvalue`
--

DROP TABLE IF EXISTS `hr_sys_keyvalue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_keyvalue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(255) NOT NULL,
  `value` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_keyvalue`
--

LOCK TABLES `hr_sys_keyvalue` WRITE;
/*!40000 ALTER TABLE `hr_sys_keyvalue` DISABLE KEYS */;
/*!40000 ALTER TABLE `hr_sys_keyvalue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_menuitem`
--

DROP TABLE IF EXISTS `hr_sys_menuitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_menuitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `icon_url` varchar(255) DEFAULT NULL,
  `link_url` varchar(255) DEFAULT NULL,
  `type` smallint(6) NOT NULL,
  `order` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_menuitem`
--

LOCK TABLES `hr_sys_menuitem` WRITE;
/*!40000 ALTER TABLE `hr_sys_menuitem` DISABLE KEYS */;
INSERT INTO `hr_sys_menuitem` VALUES (1,'员工管理','-','-',0,0,-1),(2,'部门管理','-','-',0,1,-1),(3,'用户管理','-','-',0,2,-1),(4,'员工总表','icon-large-clipart','employee_list',1,0,1),(5,'职级变动','icon-large-shapes','employee_promote_list',1,1,1),(6,'考勤录入','icon-large-smartart','employee_attandance',1,2,1),(7,'员工图表','icon-large-chart','employee_person_stat',1,3,1),(8,'部门列表','icon-large-list-01','department_list',1,0,2),(9,'职级管理','icon-large-level-01','employee_level',1,2,2),(10,'职位管理','icon-large-position','position_list',1,3,2),(11,'部门主管','icon-large-manager','department_manager',1,4,2),(12,'录入用户','icon-large-user','add_a_user',1,1,3),(13,'录入用户组','icon-large-group','add_a_usergroup',1,2,3),(14,'用户组权限','icon-large-priv','group_priv',1,3,3);
/*!40000 ALTER TABLE `hr_sys_menuitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_user`
--

DROP TABLE IF EXISTS `hr_sys_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  KEY `hr_sys_user_user_group_id_054d7dbd_fk_hr_sys_usergroup_id` (`user_group_id`),
  CONSTRAINT `hr_sys_user_user_group_id_054d7dbd_fk_hr_sys_usergroup_id` FOREIGN KEY (`user_group_id`) REFERENCES `hr_sys_usergroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_user`
--

LOCK TABLES `hr_sys_user` WRITE;
/*!40000 ALTER TABLE `hr_sys_user` DISABLE KEYS */;
INSERT INTO `hr_sys_user` VALUES (1,'why','529570509@qq.com','pbkdf2_sha256$120000$abc123.+$mdFXzN7FIs8F0qSmaKJolA0NX93Nlz9G9WVL93rmPZE=',1),(3,'aaa','BBB','pbkdf2_sha256$120000$abc123.+$L6LNxWcP3AQUxsuSrk+xnkIhr1oaTJ0Ifs3sbf9Z/jk=',3);
/*!40000 ALTER TABLE `hr_sys_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_usergroup`
--

DROP TABLE IF EXISTS `hr_sys_usergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_usergroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `remark` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_usergroup`
--

LOCK TABLES `hr_sys_usergroup` WRITE;
/*!40000 ALTER TABLE `hr_sys_usergroup` DISABLE KEYS */;
INSERT INTO `hr_sys_usergroup` VALUES (1,'admin_group','这是备注'),(3,'normal_group','remark');
/*!40000 ALTER TABLE `hr_sys_usergroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hr_sys_usergroupmenuitem`
--

DROP TABLE IF EXISTS `hr_sys_usergroupmenuitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hr_sys_usergroupmenuitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_item_id` int(11) NOT NULL,
  `user_group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hr_sys_usergroupmenu_menu_item_id_b13981c5_fk_hr_sys_me` (`menu_item_id`),
  KEY `hr_sys_usergroupmenu_user_group_id_cab30075_fk_hr_sys_us` (`user_group_id`),
  CONSTRAINT `hr_sys_usergroupmenu_menu_item_id_b13981c5_fk_hr_sys_me` FOREIGN KEY (`menu_item_id`) REFERENCES `hr_sys_menuitem` (`id`),
  CONSTRAINT `hr_sys_usergroupmenu_user_group_id_cab30075_fk_hr_sys_us` FOREIGN KEY (`user_group_id`) REFERENCES `hr_sys_usergroup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_sys_usergroupmenuitem`
--

LOCK TABLES `hr_sys_usergroupmenuitem` WRITE;
/*!40000 ALTER TABLE `hr_sys_usergroupmenuitem` DISABLE KEYS */;
INSERT INTO `hr_sys_usergroupmenuitem` VALUES (1,1,1),(2,2,1),(3,3,1),(6,4,3),(7,8,1),(8,8,3),(10,7,3);
/*!40000 ALTER TABLE `hr_sys_usergroupmenuitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-25 22:46:14
