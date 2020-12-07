-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `authusers`;
CREATE TABLE `authusers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `ruolo` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_authusers_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `authusers` (`id`, `username`, `password_hash`, `ruolo`) VALUES
(1,	'coopadmin',	'pbkdf2:sha1:1000$FlU9XUrY$a8853860e06b641f3bc814b69aee934a2139cb4f',	'admin');

DROP TABLE IF EXISTS `sezioni`;
CREATE TABLE `sezioni` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `sezioni` (`id`, `nome`) VALUES
(1,	'Consigli Comunali'),
(3,	'Avv');

DROP TABLE IF EXISTS `video`;
CREATE TABLE `video` (
  `id` int NOT NULL AUTO_INCREMENT,
  `codice` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sez` int NOT NULL,
  `desc` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sez` (`sez`),
  CONSTRAINT `video_ibfk_1` FOREIGN KEY (`sez`) REFERENCES `sezioni` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `video` (`id`, `codice`, `sez`, `desc`) VALUES
(1,	'jdYJf_ybyVo',	1,	''),
(2,	'uF4xDwJaI1s',	1,	'video 2'),
(3,	'HdS7i6xy7_w',	1,	'video 3'),
(4,	'D7T4XbZRVFE',	1,	'video 4'),
(5,	'V5MDB4GPcE0',	1,	'Hirundinidae - Un po\' come le rondini...'),
(6,	'0MtBWt4dfBY',	1,	'Mammagamma Alan Parson Project'),
(7,	'lu2oo5cqasg',	1,	'Toto - Rosanna (Live)'),
(8,	'V5MDB4GPcE0',	1,	'Hirundinidae - Un po\' come le rondini...'),
(9,	'qwIrXOtZyvQ',	3,	'Frank Zappa - Muffin Man'),
(10,	'9X_ViIPA-Gc',	3,	'sda');

-- 2020-12-07 14:28:00
