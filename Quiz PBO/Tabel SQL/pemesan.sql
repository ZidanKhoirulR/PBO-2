-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2023 at 11:47 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbkereta`
--

-- --------------------------------------------------------

--
-- Table structure for table `pemesan`
--

CREATE TABLE `pemesan` (
  `id` int(20) NOT NULL,
  `id_pemesan` int(15) NOT NULL,
  `nama_pemesan` varchar(25) NOT NULL,
  `kelamin` enum('Pria','Wanita') NOT NULL,
  `alamat_pemesan` varchar(30) NOT NULL,
  `NoTlp` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pemesan`
--

INSERT INTO `pemesan` (`id`, `id_pemesan`, `nama_pemesan`, `kelamin`, `alamat_pemesan`, `NoTlp`) VALUES
(1, 125637, 'Zidan Khoirul Rizki', 'Pria', 'Banjarnegara', 628132242),
(2, 124583, 'Rizqy Wahyu Ningrum', 'Wanita', 'Sidoarjo', 628564767),
(3, 964552, 'Ghailan Arnu Rizqy', 'Pria', 'Karangpucung', 628947247),
(4, 290836, 'Firzatullah Fadhilah', 'Pria', 'Grendeng', 628912344),
(5, 654002, 'Alif Maulana', 'Pria', 'Majenang', 628932622),
(6, 899301, 'Rani Rahayu', 'Wanita', 'Serayu', 628836433),
(7, 372821, 'Dinda Lestari', 'Wanita', 'Wates', 628924724);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pemesan`
--
ALTER TABLE `pemesan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_pemesan` (`id_pemesan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pemesan`
--
ALTER TABLE `pemesan`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
