<?php
require_once 'database.php';
require_once 'Pemesan.php';
$db = new MySQLDatabase();
$pemesan = new Pemesan($db);
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
            $result = $pemesan->get_by_id($id);
        }elseif($id_pemesan>0){
            $result = $pemesan->get_by_id_pemesan($id_pemesan);
        } else {
            $result = $pemesan->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pemesan
        $pemesan->id_pemesan = $_POST['id_pemesan'];
        $pemesan->nama_pemesan = $_POST['nama_pemesan'];
        $pemesan->kelamin = $_POST['kelamin'];
        $pemesan->alamat_pemesan = $_POST['alamat_pemesan'];
        $pemesan->NoTlp = $_POST['NoTlp'];
       
        $pemesan->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pemesan created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pemesan not created.';
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
        $pemesan->id_pemesan = $_PUT['id_pemesan'];
        $pemesan->nama_pemesan = $_PUT['nama_pemesan'];
        $pemesan->kelamin = $_PUT['kelamin'];
        $pemesan->alamat_pemesan = $_PUT['alamat_pemesan'];
        $pemesan->NoTlp = $_PUT['NoTlp'];
        if($id>0){    
            $pemesan->update($id);
        }elseif($id_pemesan<>""){
            $pemesan->update_by_id_pemesan($id_pemesan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pemesan updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pemesan update failed.';
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
            $pemesan->delete($id);
        }elseif($id_pemesan>0){
            $pemesan->delete_by_id_pemesan($id_pemesan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pemesan deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pemesan delete failed.';
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