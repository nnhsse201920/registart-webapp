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


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `registart`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity`
--

CREATE TABLE `activity` (
  `id` int(11) NOT NULL,
  `name` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `activity`
--

INSERT INTO `activity` (`id`, `name`) VALUES
(5, 'Boy\'s Basketball'),
(1, 'Boy\'s Cross Country'),
(2, 'Boy\'s Track and Field'),
(3, 'Computer Science Club'),
(11, 'DECA'),
(10, 'eSports Team'),
(6, 'Math Team'),
(7, 'National Honor Society'),
(4, 'Robotics'),
(8, 'Spanish National Honor Society');

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('28095aae65f8');

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
-- Table structure for table `connection`
--

CREATE TABLE `connection` (
  `id` int(11) NOT NULL,
  `firstN` varchar(64) DEFAULT NULL,
  `lastN` varchar(64) DEFAULT NULL,
  `ranking` smallint(6) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `connection`
--

INSERT INTO `connection` (`id`, `firstN`, `lastN`, `ranking`, `user_id`) VALUES
(82, 'Aditya', 'Tolia', NULL, 3),
(83, 'Ishaan', 'Mathur', NULL, 3),
(84, 'Jack', 'Cook', NULL, 3),
(85, 'Leo', 'Oberman', NULL, 3),
(86, 'Robert', 'Azarcon', NULL, 3),
(87, 'Vijay', 'Mistry', NULL, 3),
(88, 'Yinuo', 'Qin', NULL, 3),
(89, 'Aditya', 'Tolia', NULL, 2),
(90, 'Ishaan', 'Mathur', NULL, 2),
(91, 'Robert', 'Azarcon', NULL, 2),
(92, 'Vijay', 'Mistry', NULL, 2),
(93, 'Yinuo', 'Qin', NULL, 2),
(94, 'Aditya', 'Tolia', NULL, 1),
(95, 'Ethan', 'Pulvermacher', NULL, 1),
(96, 'Ishaan', 'Mathur', NULL, 1),
(97, 'Jack', 'Cook', NULL, 1),
(98, 'Leo', 'Oberman', NULL, 1),
(99, 'Nicholas', 'Williams', NULL, 1),
(100, 'Robert', 'Azarcon', NULL, 1),
(101, 'Vijay', 'Mistry', NULL, 1),
(102, 'Yinuo', 'Qin', NULL, 1);

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

--
-- Dumping data for table `organizers`
--

INSERT INTO `organizers` (`id`, `firstN`, `lastN`, `username`, `organizationID`, `email`, `password`) VALUES
(1, 'Luke', 'Zhang', 'lukezhangxc', NULL, 'lukezhangxc@gmail.com', 'pbkdf2:sha256:150000$vvZrXBi9$8637f8983a43d4cff39735bdcc9417e2991703f9f6da9f3b3f701abe9c520146'),
(2, 'James', 'Huang', 'jjhuang1', NULL, 'jjhuang1@gmail.com', 'pbkdf2:sha256:150000$5ybzFs5w$631f190f047d93b90b2680b7a091bae42f181c2dfec2dbc390a701ee5ca91d8c'),
(3, 'Tom', 'Carsello', 'tkcarsello', NULL, 'tkcarsello@gmail.com', 'pbkdf2:sha256:150000$d93jkf8Y$bb9c18c3d39e245f96bb621aa228529a4a45801aae413461a5299b91bf8d5d63'),
(4, 'Ethan', 'He', 'ehe', NULL, 'ehe@gmail.com', 'pbkdf2:sha256:150000$WH0lIkjz$35a64acdab8bff6a903a834e3e0977b604d32859525c170dc6eb5937f6806b50');

-- --------------------------------------------------------

--
-- Table structure for table `participants`
--

CREATE TABLE `participants` (
  `organizer_id` int(11) NOT NULL,
  `activity_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `participants`
--

INSERT INTO `participants` (`organizer_id`, `activity_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 3),
(2, 6),
(3, 5),
(3, 11),
(4, 7);

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
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `firstN`, `lastN`, `targetID`, `organizationID`, `isOrganizer`) VALUES
(1, 'Aditya', 'Tolia', NULL, NULL, NULL),
(2, 'Robert', 'Azarcon', NULL, NULL, NULL),
(3, 'Ethan', 'Pulvermacher', NULL, NULL, NULL),
(4, 'Yinuo', 'Qin', NULL, NULL, NULL),
(5, 'Vijay', 'Mistry', NULL, NULL, NULL),
(6, 'Ishaan', 'Mathur', NULL, NULL, NULL),
(71, 'Jack', 'Cook', NULL, NULL, NULL),
(72, 'Nicholas', 'Williams', NULL, NULL, NULL),
(75, 'Leo', 'Oberman', NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity`
--
ALTER TABLE `activity`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `assignments`
--
ALTER TABLE `assignments`
  ADD PRIMARY KEY (`organizerID`),
  ADD UNIQUE KEY `ix_assignments_lastContact` (`lastContact`),
  ADD UNIQUE KEY `ix_assignments_studentID` (`studentID`),
  ADD KEY `ix_assignments_medium` (`medium`),
  ADD KEY `ix_assignments_status` (`status`);

--
-- Indexes for table `connection`
--
ALTER TABLE `connection`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `organizers`
--
ALTER TABLE `organizers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_organizers_email` (`email`),
  ADD UNIQUE KEY `ix_organizers_username` (`username`),
  ADD KEY `ix_organizers_firstN` (`firstN`),
  ADD KEY `ix_organizers_lastN` (`lastN`),
  ADD KEY `ix_organizers_organizationID` (`organizationID`),
  ADD KEY `ix_organizers_password` (`password`);

--
-- Indexes for table `participants`
--
ALTER TABLE `participants`
  ADD PRIMARY KEY (`organizer_id`,`activity_id`),
  ADD KEY `activity_id` (`activity_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_students_isOrganizer` (`isOrganizer`),
  ADD UNIQUE KEY `ix_students_organizationID` (`organizationID`),
  ADD UNIQUE KEY `ix_students_targetID` (`targetID`),
  ADD KEY `ix_students_firstN` (`firstN`),
  ADD KEY `ix_students_lastN` (`lastN`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity`
--
ALTER TABLE `activity`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `assignments`
--
ALTER TABLE `assignments`
  MODIFY `organizerID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `connection`
--
ALTER TABLE `connection`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `organizers`
--
ALTER TABLE `organizers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `connection`
--
ALTER TABLE `connection`
  ADD CONSTRAINT `connection_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `organizers` (`id`);

--
-- Constraints for table `participants`
--
ALTER TABLE `participants`
  ADD CONSTRAINT `participants_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`id`),
  ADD CONSTRAINT `participants_ibfk_2` FOREIGN KEY (`organizer_id`) REFERENCES `organizers` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
