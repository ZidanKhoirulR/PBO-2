-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2023 at 11:46 PM
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
-- Table structure for table `gerbong`
--

CREATE TABLE `gerbong` (
  `id` int(15) NOT NULL,
  `id_gerbong` int(15) NOT NULL,
  `jumlah_kursi` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gerbong`
--

INSERT INTO `gerbong` (`id`, `id_gerbong`, `jumlah_kursi`) VALUES
(1, 1, 12),
(2, 2, 12),
(3, 3, 12),
(4, 4, 12),
(5, 5, 12),
(6, 6, 12),
(7, 7, 12);

-- --------------------------------------------------------

--
-- Table structure for table `kereta`
--

CREATE TABLE `kereta` (
  `id` int(15) NOT NULL,
  `id_kereta` int(15) NOT NULL,
  `tujuan` varchar(20) NOT NULL,
  `id_gerbong` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kereta`
--

INSERT INTO `kereta` (`id`, `id_kereta`, `tujuan`, `id_gerbong`) VALUES
(1, 125637, 'Magelang', 1),
(2, 124583, 'Kebumen', 2),
(3, 964552, 'Cilacap', 3),
(4, 290836, 'Tegal', 4),
(5, 654002, 'Semarang', 5),
(6, 899301, 'Kudus', 6),
(7, 372821, 'Yogyakarta', 7);

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

-- --------------------------------------------------------

--
-- Table structure for table `tiket`
--

CREATE TABLE `tiket` (
  `id_tiket` int(15) NOT NULL,
  `id_pemesan` int(15) NOT NULL,
  `id_kereta` int(10) NOT NULL,
  `no_kursi` int(10) NOT NULL,
  `jadwal` date NOT NULL,
  `kelas` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tiket`
--

INSERT INTO `tiket` (`id_tiket`, `id_pemesan`, `id_kereta`, `no_kursi`, `jadwal`, `kelas`) VALUES
(1, 125637, 82748274, 1, '2023-06-12', 'BNS'),
(2, 124583, 46572828, 10, '2023-07-30', 'BNS'),
(3, 964552, 46572828, 3, '2023-06-29', 'EXS'),
(4, 290836, 24804729, 12, '2023-07-21', 'EXS'),
(5, 654002, 73272749, 7, '2023-07-20', 'EXS'),
(6, 899301, 27427482, 8, '2023-07-12', 'EKM'),
(7, 372821, 67859785, 5, '2023-07-27', 'EKM');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `rolename` enum('admin','dosen','mahasiswa') NOT NULL DEFAULT 'mahasiswa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `passwd`, `rolename`) VALUES
(1, 'tatang', '202cb962ac59075b964b07152d234b70', 'admin'),
(2, 'sokid', '202cb962ac59075b964b07152d234b70', 'dosen'),
(3, 'farhan', '202cb962ac59075b964b07152d234b70', 'mahasiswa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gerbong`
--
ALTER TABLE `gerbong`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_gerbong` (`id_gerbong`);

--
-- Indexes for table `kereta`
--
ALTER TABLE `kereta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_kereta` (`id_kereta`);

--
-- Indexes for table `pemesan`
--
ALTER TABLE `pemesan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_pemesan` (`id_pemesan`);

--
-- Indexes for table `tiket`
--
ALTER TABLE `tiket`
  ADD PRIMARY KEY (`id_tiket`),
  ADD UNIQUE KEY `id_pemesan` (`id_pemesan`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idx` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gerbong`
--
ALTER TABLE `gerbong`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `kereta`
--
ALTER TABLE `kereta`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `pemesan`
--
ALTER TABLE `pemesan`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tiket`
--
ALTER TABLE `tiket`
  MODIFY `id_tiket` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
