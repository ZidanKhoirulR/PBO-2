<?php
require_once 'database.php';
require_once 'Gerbong.php';
$db = new MySQLDatabase();
$gerbong = new Gerbong($db);
$id=0;
$id_gerbong=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_gerbong'])){
            $id_gerbong = $_GET['id_gerbong'];
        }
        if($id>0){    
            $result = $gerbong->get_by_id($id);
        }elseif($id_gerbong>0){
            $result = $gerbong->get_by_id_gerbong($id_gerbong);
        } else {
            $result = $gerbong->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new gerbong
        $gerbong->id_gerbong = $_POST['id_gerbong'];
        $gerbong->jumlah_kursi = $_POST['jumlah_kursi'];
       
        $gerbong->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Gerbong created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Gerbong not created.';
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
        if(isset($_GET['id_gerbong'])){
            $id_gerbong = $_GET['id_gerbong'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $gerbong->id_gerbong = $_PUT['id_gerbong'];
        $gerbong->jumlah_kursi = $_PUT['jumlah_kursi'];
        if($id>0){    
            $gerbong->update($id);
        }elseif($id_gerbong<>""){
            $gerbong->update_by_id_gerbong($id_gerbong);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Gerbong updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Gerbong update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_gerbong'])){
            $id_gerbong = $_GET['id_gerbong'];
        }
        if($id>0){    
            $gerbong->delete($id);
        }elseif($id_gerbong>0){
            $gerbong->delete_by_id_gerbong($id_gerbong);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Gerbong deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Gerbong delete failed.';
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