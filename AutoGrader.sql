-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.24 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.5.0.5332
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for AutoGrader
CREATE DATABASE IF NOT EXISTS `AutoGrader` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `AutoGrader`;

-- Dumping structure for table AutoGrader.submission
CREATE TABLE IF NOT EXISTS `submission` (
  `ID` int(255) NOT NULL AUTO_INCREMENT,
  `TaskID` int(255) NOT NULL DEFAULT '-1',
  `FileName` char(50) NOT NULL,
  `Language` char(4) DEFAULT NULL,
  `Score` float NOT NULL DEFAULT '-1',
  `Status` char(20) NOT NULL DEFAULT 'Pending',
  `Host` int(2) NOT NULL DEFAULT '-1',
  `Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=latin1;

-- Dumping data for table AutoGrader.submission: ~107 rows (approximately)
/*!40000 ALTER TABLE `submission` DISABLE KEYS */;
INSERT INTO `submission` (`ID`, `TaskID`, `FileName`, `Language`, `Score`, `Status`, `Host`, `Date`) VALUES
	(1, 2, 'OneTwoThree_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 18:38:39'),
	(2, 2, 'OneTwoThree_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 18:39:31'),
	(3, 2, 'OneTwoThree_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 18:40:54'),
	(4, 2, 'OneTwoThree_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 18:41:06'),
	(5, 2, 'OneTwoThree_1301180154', 'Go', 0, 'Compile Error : 2', -1, '2019-10-17 18:41:20'),
	(7, 2, 'OneTwoThree_1301180154', 'Go', 0, 'Compile Error : 2', -1, '2019-10-17 18:45:31'),
	(8, 2, 'OneTwoThree_1301180154', 'Go', 0, 'Compile Error : 2', -1, '2019-10-17 18:45:46'),
	(9, 2, 'OneTwoThree_1301180154', 'Go', 0, 'Time Limit Exceeded', -1, '2019-10-17 18:46:19'),
	(10, 3, 'PizzaHutDelivery_1301180154', 'Go', 10, 'Wrong Answer', -1, '2019-10-17 19:03:21'),
	(11, 3, 'PizzaHutDelivery_1301180154', 'Go', 10, 'Wrong Answer', -1, '2019-10-17 19:04:29'),
	(12, 3, 'PizzaHutDelivery_1301180154', 'Go', 20, 'Wrong Answer', -1, '2019-10-17 19:05:30'),
	(13, 3, 'PizzaHutDelivery_1301180154', 'Go', 90, 'Wrong Answer', -1, '2019-10-17 19:28:09'),
	(14, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 19:29:10'),
	(15, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:02:37'),
	(16, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:03:02'),
	(17, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:03:51'),
	(18, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:05:35'),
	(19, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:09:33'),
	(20, 3, 'PizzaHutDelivery_1301180154', 'Go', 90, 'Wrong Answer', -1, '2019-10-17 20:10:15'),
	(21, 3, 'PizzaHutDelivery_1301180154', 'Go', 90, 'Wrong Answer', -1, '2019-10-17 20:13:48'),
	(22, 3, 'PizzaHutDelivery_1301180154', 'Go', 90, 'Wrong Answer', -1, '2019-10-17 20:18:22'),
	(24, 3, 'PizzaHutDelivery_1301180154', 'Go', 90, 'Wrong Answer', -1, '2019-10-17 20:19:41'),
	(25, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:28:39'),
	(26, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:29:52'),
	(27, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:31:19'),
	(28, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:31:42'),
	(29, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:32:16'),
	(30, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:35:30'),
	(31, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:35:51'),
	(32, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:43:31'),
	(34, 3, 'PizzaHutDelivery_1301180154', 'Go', 10, 'Wrong Answer', -1, '2019-10-17 20:46:02'),
	(36, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:49:24'),
	(37, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:49:39'),
	(38, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:52:14'),
	(39, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:52:22'),
	(40, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:54:38'),
	(41, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:54:55'),
	(42, 3, 'PizzaHutDelivery_1301180154', 'Go', 100, 'Accepted', -1, '2019-10-17 20:55:39'),
	(43, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:56:01'),
	(44, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:56:33'),
	(45, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:56:40'),
	(46, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:56:48'),
	(47, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:57:03'),
	(48, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:57:09'),
	(49, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:57:28'),
	(50, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 20:59:59'),
	(51, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:01:01'),
	(52, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:04:09'),
	(53, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:04:18'),
	(54, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:04:25'),
	(55, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:05:24'),
	(56, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:05:36'),
	(57, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:05:41'),
	(59, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:18:03'),
	(60, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:18:15'),
	(61, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:18:20'),
	(62, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:18:27'),
	(63, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:18:37'),
	(64, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:18:45'),
	(65, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:18:53'),
	(66, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:21:22'),
	(67, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 21:21:31'),
	(68, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Compile Error : 2', -1, '2019-10-17 21:55:56'),
	(69, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Compile Error : 2', -1, '2019-10-17 21:56:23'),
	(77, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 22:14:03'),
	(78, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 22:14:28'),
	(79, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 22:14:43'),
	(80, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 22:15:42'),
	(81, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 22:17:06'),
	(82, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 22:19:20'),
	(83, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 22:20:37'),
	(84, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-17 22:20:49'),
	(86, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 05:53:27'),
	(87, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 05:54:04'),
	(88, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 05:54:51'),
	(89, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 06:13:12'),
	(90, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 06:13:42'),
	(91, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 06:14:08'),
	(92, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 06:14:44'),
	(93, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 06:25:15'),
	(94, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:28:23'),
	(95, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:29:07'),
	(96, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:29:23'),
	(97, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:29:29'),
	(99, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:32:43'),
	(100, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:32:53'),
	(101, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:33:17'),
	(103, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:33:31'),
	(104, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:37:07'),
	(105, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:37:32'),
	(108, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Time Limit Exceeded', -1, '2019-10-18 09:39:01'),
	(111, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:41:22'),
	(112, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Time Limit Exceeded', -1, '2019-10-18 09:42:56'),
	(113, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:50:36'),
	(114, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:51:26'),
	(115, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:51:46'),
	(117, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:53:31'),
	(118, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 09:54:57'),
	(119, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 14:13:10'),
	(122, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 14:15:46'),
	(123, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 14:16:20'),
	(124, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 14:16:56'),
	(125, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 14:17:26'),
	(126, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 14:21:43'),
	(127, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 14:33:36'),
	(128, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 14:46:58'),
	(129, 3, 'PizzaHutDelivery_1301180154', 'Go', 0, 'Wrong Answer', -1, '2019-10-18 18:43:32');
/*!40000 ALTER TABLE `submission` ENABLE KEYS */;

-- Dumping structure for table AutoGrader.task
CREATE TABLE IF NOT EXISTS `task` (
  `ID` int(255) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Description` text,
  `InputFormat` text,
  `OutputFormat` text,
  `Constraint` text,
  `Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table AutoGrader.task: ~3 rows (approximately)
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` (`ID`, `Name`, `Description`, `InputFormat`, `OutputFormat`, `Constraint`, `Date`) VALUES
	(1, '6 Bilangan Genap', NULL, NULL, NULL, NULL, '2019-08-30 18:31:01'),
	(2, 'One-Two-Three', NULL, NULL, NULL, NULL, '2019-08-30 21:20:03'),
	(3, 'Pizza Hut Delivery', NULL, NULL, NULL, NULL, '2019-10-17 19:01:31');
/*!40000 ALTER TABLE `task` ENABLE KEYS */;

-- Dumping structure for table AutoGrader.test_case
CREATE TABLE IF NOT EXISTS `test_case` (
  `ID` int(255) NOT NULL AUTO_INCREMENT,
  `TaskID` int(255) NOT NULL DEFAULT '-1',
  `Input` varchar(255) NOT NULL,
  `Output` varchar(255) NOT NULL,
  `Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Dumping data for table AutoGrader.test_case: ~20 rows (approximately)
/*!40000 ALTER TABLE `test_case` DISABLE KEYS */;
INSERT INTO `test_case` (`ID`, `TaskID`, `Input`, `Output`, `Date`) VALUES
	(1, 1, 'TIMESTAMP1', 'TIMESTAMP1', '2019-08-30 18:34:31'),
	(2, 1, 'TIMESTAMP2', 'TIMESTAMP2', '2019-08-30 18:35:08'),
	(3, 1, 'TIMESTAMP3', 'TIMESTAMP3', '2019-08-30 18:35:25'),
	(4, 2, '2_1', '2_1', '2019-08-30 21:21:09'),
	(5, 2, '2_2', '2_2', '2019-08-30 21:21:20'),
	(6, 2, '2_3', '2_3', '2019-08-30 21:21:31'),
	(7, 2, '2_4', '2_4', '2019-08-30 21:21:41'),
	(8, 2, '2_5', '2_5', '2019-08-30 21:21:52'),
	(9, 2, '2_6', '2_6', '2019-08-30 21:22:02'),
	(10, 2, '2_7', '2_7', '2019-08-30 21:22:13'),
	(11, 3, 'Pizza0', 'Pizza0', '2019-10-17 19:02:47'),
	(12, 3, 'Pizza1', 'Pizza1', '2019-10-17 19:02:47'),
	(13, 3, 'Pizza2', 'Pizza2', '2019-10-17 19:02:47'),
	(14, 3, 'Pizza3', 'Pizza3', '2019-10-17 19:02:47'),
	(15, 3, 'Pizza4', 'Pizza4', '2019-10-17 19:02:48'),
	(16, 3, 'Pizza5', 'Pizza5', '2019-10-17 19:02:48'),
	(17, 3, 'Pizza6', 'Pizza6', '2019-10-17 19:02:48'),
	(18, 3, 'Pizza7', 'Pizza7', '2019-10-17 19:02:48'),
	(19, 3, 'Pizza8', 'Pizza8', '2019-10-17 19:02:48'),
	(20, 3, 'Pizza9', 'Pizza9', '2019-10-17 19:02:48');
/*!40000 ALTER TABLE `test_case` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
