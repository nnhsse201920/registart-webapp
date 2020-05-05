-- Table structure for table assignments'	SET time_zone = "+00:00";
--	
DROP DATABASE IF EXISTS registart;	
CREATE DATABASE registart;	
CREATE USER 'registart'@'%' identified by 'database7';	
GRANT ALL PRIVILEGES on registart.* to 'registart'@'%';	
use registart;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Table structure for table `activity`
--

CREATE TABLE `activity` (
  `id` int NOT NULL,
  `name` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `activity`
--

INSERT INTO `activity` (`id`, `name`) VALUES
(5, 'Boy\'s Basketball'),
(1, 'Boy\'s Cross Country'),
(12, 'Boy\'s Gymnastics'),
(2, 'Boy\'s Track and Field'),
(13, 'Chess Team'),
(3, 'Computer Science Club'),
(11, 'DECA'),
(10, 'eSports Team'),
(16, 'Mandarin Club'),
(6, 'Math Team'),
(7, 'National Honor Society'),
(15, 'Ping Pong Club'),
(4, 'Robotics'),
(8, 'Spanish National Honor Society'),
(14, 'Table Tennis Team');

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
('45716b484161');

-- --------------------------------------------------------

--
-- Table structure for table `assignments`
--

CREATE TABLE `assignments` (
  `organizerID` int NOT NULL,
  `studentID` int DEFAULT NULL,
  `lastContact` datetime DEFAULT NULL,
  `status` int DEFAULT NULL,
  `medium` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `connection`
--

CREATE TABLE `connection` (
  `id` int NOT NULL,
  `firstN` varchar(64) DEFAULT NULL,
  `lastN` varchar(64) DEFAULT NULL,
  `ranking` smallint DEFAULT NULL,
  `user_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `connection`
--

INSERT INTO `connection` (`id`, `firstN`, `lastN`, `ranking`, `user_id`) VALUES
(103, 'Enoch', 'Qin', 4, 5),
(104, 'Ethan', 'He', 2, 5),
(105, 'Ishaan', 'Mathur', 3, 5),
(106, 'James', 'Huang', 4, 5),
(108, 'Joshua', 'Robinson', 3, 5),
(109, 'Omeed', 'Jamali', 4, 5),
(110, 'Tom', 'Carsello', 3, 5),
(111, 'Yinuo', 'Qin', 4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `organizers`
--

CREATE TABLE `organizers` (
  `id` int NOT NULL,
  `firstN` varchar(255) DEFAULT NULL,
  `lastN` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `organizationID` int DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `organizers`
--

INSERT INTO `organizers` (`id`, `firstN`, `lastN`, `username`, `organizationID`, `email`, `password`) VALUES
(5, 'Luke', 'Zhang', 'lukezhang37', NULL, 'lukezhangxc@gmail.com', 'pbkdf2:sha256:150000$daCDKQt4$7bf1f690580110f9dcd14a24aa81005d5728ed9b7f69b6ce1c7d85bcb76ec2bd');

-- --------------------------------------------------------

--
-- Table structure for table `participants`
--

CREATE TABLE `participants` (
  `organizer_id` int NOT NULL,
  `activity_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `participants`
--

INSERT INTO `participants` (`organizer_id`, `activity_id`) VALUES
(5, 1),
(5, 2),
(5, 3);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int NOT NULL,
  `firstN` varchar(255) DEFAULT NULL,
  `lastN` varchar(255) DEFAULT NULL,
  `targetID` varbinary(255) DEFAULT NULL,
  `organizationID` int DEFAULT NULL,
  `isOrganizer` smallint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `firstN`, `lastN`, `targetID`, `organizationID`, `isOrganizer`) VALUES
(1, 'James', 'Huang', NULL, NULL, NULL),
(2, 'Tom', 'Carsello', NULL, NULL, NULL),
(3, 'Ethan', 'He', NULL, NULL, NULL),
(4, 'Enoch', 'Qin', NULL, NULL, NULL),
(5, 'Yinuo', 'Qin', NULL, NULL, NULL),
(6, 'Joshua', 'Robinson', NULL, NULL, NULL),
(7, 'Omeed', 'Jamali', NULL, NULL, NULL),
(8, 'Ishaan', 'Mathur', NULL, NULL, NULL),
(9, 'James', 'Tom', NULL, NULL, NULL);

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
  ADD UNIQUE KEY `ix_students_targetID` (`targetID`),
  ADD KEY `ix_students_firstN` (`firstN`),
  ADD KEY `ix_students_lastN` (`lastN`),
  ADD KEY `ix_students_isOrganizer` (`isOrganizer`),
  ADD KEY `ix_students_organizationID` (`organizationID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity`
--
ALTER TABLE `activity`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `assignments`
--
ALTER TABLE `assignments`
  MODIFY `organizerID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `connection`
--
ALTER TABLE `connection`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;

--
-- AUTO_INCREMENT for table `organizers`
--
ALTER TABLE `organizers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

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
