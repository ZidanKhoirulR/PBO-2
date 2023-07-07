<?php
require_once 'database.php';
class Tiket 
{
    private $db;
    private $table = 'tiket';
    public $id_pemesan = "";
    public $id_kereta = "";
    public $no_kursi = "";
    public $jadwal = "";
    public $kelas = "";
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
        $query = "INSERT INTO $this->table (`id_pemesan`,`id_kereta`,`no_kursi`,`jadwal`,`kelas`) VALUES ('$this->id_pemesan','$this->id_kereta','$this->no_kursi','$this->jadwal','$this->kelas')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET id_pemesan = '$this->id_pemesan', id_kereta = '$this->id_kereta', no_kursi = '$this->no_kursi', jadwal = '$this->jadwal', kelas = '$this->kelas' 
        WHERE id_tiket = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_id_pemesan($id_pemesan): int
    {
        $query = "UPDATE $this->table SET id_pemesan = '$this->id_pemesan', id_kereta = '$this->id_kereta', no_kursi = '$this->no_kursi', jadwal = '$this->jadwal', kelas = '$this->kelas' 
        WHERE id_pemesan = $id_pemesan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_tiket = $id";
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