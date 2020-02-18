#!/bin/bash

export GATEWAY_INTERFACE="CGI/1.1"
export SCRIPT_FILENAME="/home/jake/Documents/Web-Server-Application-Security-Audit-Code/Assignments/Assignment #4 - Supporting Server-side Code Execution/Resources/postdemo.php"
export REQUEST_METHOD="POST"
export SERVER_PROTOCOL="HTTP/1.1"
export REMOTE_HOST="127.0.0.1"
export CONTENT_LENGTH="29"
export BODY="example1=Hello&example2=World"
export CONTENT_TYPE="application/x-www-form-urlencoded"
export "REDIRECT_STATUS"=0

echo "$BODY" | php-cgi
