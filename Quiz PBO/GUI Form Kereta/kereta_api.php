<?php
require_once 'database.php';
require_once 'Kereta.php';
$db = new MySQLDatabase();
$kereta = new Kereta($db);
$id=0;
$id_kereta=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_kereta'])){
            $id_kereta = $_GET['id_kereta'];
        }
        if($id>0){    
            $result = $kereta->get_by_id($id);
        }elseif($id_kereta>0){
            $result = $kereta->get_by_id_kereta($id_kereta);
        } else {
            $result = $kereta->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new kereta
        $kereta->id_kereta = $_POST['id_kereta'];
        $kereta->tujuan = $_POST['tujuan'];
        $kereta->id_gerbong = $_POST['id_gerbong'];
       
        $kereta->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kereta created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kereta not created.';
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
        if(isset($_GET['id_kereta'])){
            $id_kereta = $_GET['id_kereta'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $kereta->id_kereta = $_PUT['id_kereta'];
        $kereta->tujuan = $_PUT['tujuan'];
        $kereta->id_gerbong = $_PUT['id_gerbong'];
        if($id>0){    
            $kereta->update($id);
        }elseif($id_kereta<>""){
            $kereta->update_by_id_kereta($id_kereta);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kereta updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kereta update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_kereta'])){
            $id_kereta = $_GET['id_kereta'];
        }
        if($id>0){    
            $kereta->delete($id);
        }elseif($id_kereta>0){
            $kereta->delete_by_id_kereta($id_kereta);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kereta deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kereta delete failed.';
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