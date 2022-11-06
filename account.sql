-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 06, 2022 at 02:29 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythondb`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `Acno` varchar(20) NOT NULL,
  `Pin` varchar(6) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Fname` varchar(20) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `State` varchar(25) NOT NULL,
  `City` varchar(25) NOT NULL,
  `Amount` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`Acno`, `Pin`, `Name`, `Fname`, `Gender`, `Email`, `Phone`, `State`, `City`, `Amount`) VALUES
('SBI101', '123456', 'Anil Singh', 'Anil', 'M', 'annilsingh20022000@gmail.', '9027593493', 'Uttarakhand', 'Dehradun', '300'),
('SBI102', '103161', 'Mayank Ramola', 'Mayank', 'M', 'mayank14324@gmail.com', '9059849665', 'Uttarakhand', 'Tehri', '2500'),
('SBI103', '103161', 'Anjali', 'Anjali', 'F', 'anjali5164615@gmail.com', '8365646575', 'Himachal', 'Shimla', '2200'),
('SBI104', '103161', 'Sumit Kandari', 'Sumit', 'M', 'sumitkandari6544@gmail.co', '7506548695', 'Uttarakhand', 'Srinagar', '3000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`Acno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
