<?php
require_once 'database.php';
class Anggota 
{
    private $db;
    private $table = 'anggota';
    public $kode_anggota = "";
    public $nama_anggota = "";
    public $jenis_kelamin = "";
    public $prodi = "";
    public $no_tlp = "";
    public $alamat = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kode_anggota(int $kode_anggota)
    {
        $query = "SELECT * FROM $this->table WHERE kode_anggota = $kode_anggota";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_anggota`,`nama_anggota`,`jenis_kelamin`,`prodi`,`no_tlp`,`alamat`) VALUES ('$this->kode_anggota','$this->nama_anggota','$this->jenis_kelamin','$this->prodi','$this->no_tlp','$this->alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_anggota = '$this->kode_anggota', nama_anggota = '$this->nama_anggota', jenis_kelamin = '$this->jenis_kelamin', prodi = '$this->prodi', no_tlp = '$this->no_tlp', alamat = '$this->alamat' 
        WHERE id_anggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_anggota($kode_anggota): int
    {
        $query = "UPDATE $this->table SET kode_anggota = '$this->kode_anggota', nama_anggota = '$this->nama_anggota', jenis_kelamin = '$this->jenis_kelamin', prodi = '$this->prodi', no_tlp = '$this->no_tlp', alamat = '$this->alamat' 
        WHERE kode_anggota = $kode_anggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_anggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_anggota($kode_anggota): int
    {
        $query = "DELETE FROM $this->table WHERE kode_anggota = $kode_anggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>