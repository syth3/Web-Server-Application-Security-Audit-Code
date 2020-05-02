<?php

    require_once('api.php');

    $request_method = null;
    $request_name = null;
    $request_contents = null;
    
    if (isset($_GET['method'])) {
        $request_method = $_GET['method'];
    }

    if (isset($_GET['name'])) {
        $request_name = $_GET['name'];
    }

    if (isset($_GET['contents'])) {
        $request_contents = $_GET['contents'];
    }

    
    $api = new api($request_method, $request_name, $request_contents, "/tmp/webapp");
    echo $api->process_request();

?>