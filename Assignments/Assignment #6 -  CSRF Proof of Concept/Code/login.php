<?php
    $password_file = fopen("password.txt", "r");
    $password = fgets($password_file);
    
    $username_file = fopen("username.txt", "r");
    $username = fgets($username_file);

    $submitted_username = $_GET["username"];
    $submitted_password = $_GET["password"];

    if ($submitted_username == $username && $submitted_password == $password) {
        echo $username . ", you have been successfully logged in";
        $cookie_name = "token";
        $cookie_value = $username;
        setcookie($cookie_name, $cookie_value, time()+10*60);
        }
    else {
        echo "Sorry, wrong credentials";
    }


?>