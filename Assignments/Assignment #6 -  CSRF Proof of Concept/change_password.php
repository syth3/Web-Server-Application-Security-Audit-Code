<?php
    $username_file = fopen("username.txt", "r");
    $username = fgets($username_file);
    if ($_COOKIE["token"] != $username) {
        echo "Sorry, must log in first!";
    }
    else {

        $new_password = $_GET["password"];

        $password_file = fopen("password.txt", "w");
        fwrite($password_file, $new_password);

        $password_file = fopen("password.txt", "r");
        $password_set = fgets($password_file);

        if ($password_set == $new_password) {
            echo $username . ", your password has been changed";
        }
        else {
            echo "Error has occured while changing password";
        }
    }
?>