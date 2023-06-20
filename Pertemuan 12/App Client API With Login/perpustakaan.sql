CREATE TABLE `Buku` (
	`id_buku` INT(10) NOT NULL AUTO_INCREMENT,
	`kode_buku` char(100) NOT NULL UNIQUE,
	`judul_buku` varchar(100) NOT NULL,
	`penulis_buku` varchar(100) NOT NULL,
	`penerbit_buku` varchar(100) NOT NULL,
	`tahun_terbit` char(100) NOT NULL,
	`stok` INT NOT NULL,
	PRIMARY KEY (`id_buku`)
);

CREATE TABLE `Petugas` (
	`id_petugas` INT(10) NOT NULL AUTO_INCREMENT,
	`kode_petugas` char(100) NOT NULL UNIQUE,
	`nama_petugas` varchar(100) NOT NULL,
	`no_telp` char(100) NOT NULL,
	`alamat` varchar(100) NOT NULL,
	PRIMARY KEY (`id_petugas`)
);

CREATE TABLE `Anggota` (
	`id_anggota` INT(100) NOT NULL AUTO_INCREMENT,
	`kode_anggota` char(100) NOT NULL UNIQUE,
	`nama_anggota` varchar(100) NOT NULL,
	`jenis_kelamin` enum('P','L') NOT NULL,
	`prodi` char(100) NOT NULL,
	`no_tlp` char(100) NOT NULL,
	`alamat` varchar(100) NOT NULL,
	PRIMARY KEY (`id_anggota`)
);

CREATE TABLE `Peminjaman` (
	`id_peminjaman` INT(100) NOT NULL AUTO_INCREMENT,
	`kode_peminjaman` char(100) NOT NULL UNIQUE,
	`tanggal_pinjam` DATE NOT NULL,
	`tanggal_kembali` DATE NOT NULL,
	`id_anggota` INT(100) NOT NULL,
	`id_buku` INT(100) NOT NULL,
	`id_petugas` INT(100) NOT NULL,
	PRIMARY KEY (`id_peminjaman`)
);

CREATE TABLE `Pengembalian` (
	`id_pengembalian` INT(100) NOT NULL AUTO_INCREMENT,
	`kode_pengembalian` char(100) NOT NULL UNIQUE,
	`tanggal_pengembalian` DATE NOT NULL,
	`denda` INT(100) NOT NULL,
	`id_buku` INT(100) NOT NULL,
	`id_anggota` INT(100) NOT NULL,
	`id_petugas` INT(100) NOT NULL,
	PRIMARY KEY (`id_pengembalian`)
);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk0` FOREIGN KEY (`id_anggota`) REFERENCES `Anggota`(`id_anggota`);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk1` FOREIGN KEY (`id_buku`) REFERENCES `Buku`(`id_buku`);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk2` FOREIGN KEY (`id_petugas`) REFERENCES `Petugas`(`id_petugas`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk0` FOREIGN KEY (`id_buku`) REFERENCES `Buku`(`id_buku`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk1` FOREIGN KEY (`id_anggota`) REFERENCES `Anggota`(`id_anggota`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk2` FOREIGN KEY (`id_petugas`) REFERENCES `Petugas`(`id_petugas`);






