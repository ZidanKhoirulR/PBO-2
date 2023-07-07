<?php
require_once 'database.php';
class Kereta 
{
    private $db;
    private $table = 'kereta';
    public $id_kereta = "";
    public $tujuan = "";
    public $id_gerbong = "";
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
    public function get_by_id_kereta(int $id_kereta)
    {
        $query = "SELECT * FROM $this->table WHERE id_kereta = $id_kereta";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`id_kereta`,`tujuan`,`id_gerbong`) VALUES ('$this->id_kereta','$this->tujuan','$this->id_gerbong')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET id_kereta = '$this->id_kereta', tujuan = '$this->tujuan', id_gerbong = '$this->id_gerbong' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_id_kereta($id_kereta): int
    {
        $query = "UPDATE $this->table SET id_kereta = '$this->id_kereta', tujuan = '$this->tujuan', id_gerbong = '$this->id_gerbong' 
        WHERE id_kereta = $id_kereta";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_id_kereta($id_kereta): int
    {
        $query = "DELETE FROM $this->table WHERE id_kereta = $id_kereta";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>