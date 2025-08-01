-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 01, 2025 at 10:10 AM
-- Server version: 11.8.2-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud_operation_api_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogs`
--

CREATE TABLE `blogs` (
  `id` int(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `sort_description` varchar(500) NOT NULL,
  `image_name` varchar(200) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp(),
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blogs`
--

INSERT INTO `blogs` (`id`, `name`, `description`, `sort_description`, `image_name`, `created_at`, `updated_at`, `status`) VALUES
(1, 'aditya Adhar', 'A blog (short for “Apilog”) is an online journal or informational', '\"A blog (short for “Apilog”)', '', '2025-07-28 00:03:32', '2025-08-01 08:07:54', 1),
(7, 'Apiblog', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', '', '2025-07-28 04:37:41', '2025-08-01 08:08:03', 1),
(9, 'Apiblog', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', '', '2025-07-28 04:47:00', '2025-08-01 08:08:09', 0),
(10, 'Apiblog', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', '', '2025-07-28 05:17:11', '2025-08-01 08:08:17', 0),
(11, 'Apiblog', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/Apiblog_20250801133916.jpg', '2025-07-28 13:41:51', '2025-08-01 08:09:16', 0),
(12, 'Apiblog', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/Apiblog_20250801133921.jpg', '2025-07-25 03:21:22', '2025-08-01 08:09:21', 1),
(13, 'Apiblog', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/Apiblog_20250801133924.jpg', '2025-07-29 03:41:24', '2025-08-01 08:09:24', 0),
(14, 'Apiblog', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/Apiblog_20250801133929.jpg', '2025-07-29 03:48:47', '2025-08-01 08:09:29', 0),
(15, 'xyz', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/xyz_20250801133931.jpg', '2025-07-29 03:54:02', '2025-08-01 08:09:31', 1),
(16, 'xyz', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/xyz_20250801133934.jpg', '2025-07-29 03:56:32', '2025-08-01 08:09:34', 0),
(17, 'xyz', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/xyz_20250801133935.jpg', '2025-07-29 03:57:22', '2025-08-01 08:09:35', 0),
(18, 'aditya Adhar', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/aditya_Adhar_20250801133938.jpg', '2025-07-30 08:03:12', '2025-08-01 08:09:38', 0),
(19, 'aditya Adhar', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/aditya_Adhar_20250801133941.jpg', '2025-07-30 08:07:46', '2025-08-01 08:09:41', 1),
(20, 'flowers', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/flowers_20250801133945.jpg', '2025-07-31 09:40:36', '2025-08-01 08:09:45', 0),
(21, 'flowers', 'A blog (short for “Apilog”) is an online journal or informational', 'A blog (short for “Apilog”) is an online journal or informational', 'blogs/flowers_20250801133949.jpg', '2025-08-01 06:51:17', '2025-08-01 08:09:49', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blogs`
--
ALTER TABLE `blogs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blogs`
--
ALTER TABLE `blogs`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
