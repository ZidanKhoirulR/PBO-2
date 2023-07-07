<?php
require_once 'database.php';
class Gerbong 
{
    private $db;
    private $table = 'gerbong';
    public $id_gerbong = "";
    public $jumlah_kursi = "";
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
    public function get_by_id_gerbong(int $id_gerbong)
    {
        $query = "SELECT * FROM $this->table WHERE id_gerbong = $id_gerbong";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`id_gerbong`,`jumlah_kursi`) VALUES ('$this->id_gerbong','$this->jumlah_kursi')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET id_gerbong = '$this->id_gerbong', jumlah_kursi = '$this->jumlah_kursi' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_id_gerbong($id_gerbong): int
    {
        $query = "UPDATE $this->table SET id_gerbong = '$this->id_gerbong', jumlah_kursi = '$this->jumlah_kursi' 
        WHERE id_gerbong = $id_gerbong";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_id_gerbong($id_gerbong): int
    {
        $query = "DELETE FROM $this->table WHERE id_gerbong = $id_gerbong";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>