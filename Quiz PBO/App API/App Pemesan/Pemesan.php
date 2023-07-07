<?php
require_once 'database.php';
class Pemesan 
{
    private $db;
    private $table = 'pemesan';
    public $id_pemesan = "";
    public $nama_pemesan = "";
    public $kelamin = "";
    public $alamat_pemesan = "";
    public $NoTlp = "";
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
    public function get_by_id_pemesan(int $id_pemesan)
    {
        $query = "SELECT * FROM $this->table WHERE id_pemesan = $id_pemesan";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`id_pemesan`,`nama_pemesan`,`kelamin`,`alamat_pemesan`,`NoTlp`) VALUES ('$this->id_pemesan','$this->nama_pemesan','$this->kelamin','$this->alamat_pemesan','$this->NoTlp')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET id_pemesan = '$this->id_pemesan', nama_pemesan = '$this->nama_pemesan', kelamin = '$this->kelamin', alamat_pemesan = '$this->alamat_pemesan', NoTlp = '$this->NoTlp' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_id_pemesan($id_pemesan): int
    {
        $query = "UPDATE $this->table SET id_pemesan = '$this->id_pemesan', nama_pemesan = '$this->nama_pemesan', kelamin = '$this->kelamin', alamat_pemesan = '$this->alamat_pemesan', NoTlp = '$this->NoTlp' 
        WHERE id_pemesan = $id_pemesan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_id_pemesan($id_pemesan): int
    {
        $query = "DELETE FROM $this->table WHERE id_pemesan = $id_pemesan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>