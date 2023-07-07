<?php
require_once 'database.php';
require_once 'Tiket.php';
$db = new MySQLDatabase();
$tiket = new Tiket($db);
$id=0;
$id_pemesan=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_pemesan'])){
            $id_pemesan = $_GET['id_pemesan'];
        }
        if($id>0){    
            $result = $tiket->get_by_id($id);
        }elseif($id_pemesan>0){
            $result = $tiket->get_by_id_pemesan($id_pemesan);
        } else {
            $result = $tiket->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new tiket
        $tiket->id_pemesan = $_POST['id_pemesan'];
        $tiket->id_kereta = $_POST['id_kereta'];
        $tiket->no_kursi = $_POST['no_kursi'];
        $tiket->jadwal = $_POST['jadwal'];
        $tiket->kelas = $_POST['kelas'];
       
        $tiket->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Tiket created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Tiket not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_pemesan'])){
            $id_pemesan = $_GET['id_pemesan'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $tiket->id_pemesan = $_PUT['id_pemesan'];
        $tiket->id_kereta = $_PUT['id_kereta'];
        $tiket->no_kursi = $_PUT['no_kursi'];
        $tiket->jadwal = $_PUT['jadwal'];
        $tiket->kelas = $_PUT['kelas'];
        if($id>0){    
            $tiket->update($id);
        }elseif($id_pemesan<>""){
            $tiket->update_by_id_pemesan($id_pemesan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Tiket updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Tiket update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_pemesan'])){
            $id_pemesan = $_GET['id_pemesan'];
        }
        if($id>0){    
            $tiket->delete($id);
        }elseif($id_pemesan>0){
            $tiket->delete_by_id_pemesan($id_pemesan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Tiket deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Tiket delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>