-- MariaDB dump 10.17  Distrib 10.4.11-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: example
-- ------------------------------------------------------
-- Server version	10.4.11-MariaDB-1:10.4.11+maria~bionic


--
-- Table structure for table assignments'
--
DROP DATABASE IF EXISTS registart;
CREATE DATABASE registart;
CREATE USER 'registart'@'%' identified by 'database7';
GRANT ALL PRIVILEGES on registart.* to 'registart'@'%';
use registart;


-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Feb 21, 2020 at 08:01 PM
-- Server version: 10.4.12-MariaDB-1:10.4.12+maria~bionic
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `registart`
--

-- --------------------------------------------------------



--
-- Table structure for table `assignments`
--

CREATE TABLE `assignments` (
  `organizerID` int(11) NOT NULL,
  `studentID` int(11) DEFAULT NULL,
  `lastContact` datetime DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `medium` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `organizations`
--

CREATE TABLE `organizations` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `organizers`
--

CREATE TABLE `organizers` (
  `id` int(11) NOT NULL,
  `firstN` varchar(255) DEFAULT NULL,
  `lastN` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `organizationID` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `firstN` varchar(255) DEFAULT NULL,
  `lastN` varchar(255) DEFAULT NULL,
  `targetID` varbinary(255) DEFAULT NULL,
  `organizationID` int(11) DEFAULT NULL,
  `isOrganizer` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--


--
-- Indexes for table `assignments`
--
ALTER TABLE `assignments`
  ADD PRIMARY KEY (`organizerID`),
  ADD UNIQUE KEY `ix_assignments_lastContact` (`lastContact`),
  ADD UNIQUE KEY `ix_assignments_medium` (`medium`),
  ADD UNIQUE KEY `ix_assignments_status` (`status`),
  ADD UNIQUE KEY `ix_assignments_studentID` (`studentID`);

--
-- Indexes for table `organizations`
--
ALTER TABLE `organizations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_organizations_name` (`name`);

--
-- Indexes for table `organizers`
--
ALTER TABLE `organizers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_organizers_email` (`email`),
  ADD UNIQUE KEY `ix_organizers_firstN` (`firstN`),
  ADD UNIQUE KEY `ix_organizers_lastN` (`lastN`),
  ADD UNIQUE KEY `ix_organizers_organizationID` (`organizationID`),
  ADD UNIQUE KEY `ix_organizers_password` (`password`),
  ADD UNIQUE KEY `ix_organizers_username` (`username`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_students_firstN` (`firstN`),
  ADD UNIQUE KEY `ix_students_isOrganizer` (`isOrganizer`),
  ADD UNIQUE KEY `ix_students_lastN` (`lastN`),
  ADD UNIQUE KEY `ix_students_organizationID` (`organizationID`),
  ADD UNIQUE KEY `ix_students_targetID` (`targetID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assignments`
--
ALTER TABLE `assignments`
  MODIFY `organizerID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `organizations`
--
ALTER TABLE `organizations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `organizers`
--
ALTER TABLE `organizers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
