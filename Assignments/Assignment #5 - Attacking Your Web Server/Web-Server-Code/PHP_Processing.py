'''
file: PHP_Processing.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Functions to process PHP input via GET and POST methods
'''

import os
from pathlib import Path


def process_php_file(request_uri, request_params, http_method, php_files_path):
    """Process a given PHP file with given inputs using the php-cgi
    
    Parameters
    ----------
    request_uri : string
        Name of the PHP file gathered from the request uri in the HTTP request
    request_params : string
        Parameters to pass to the PHP file
    http_method : string
        HTTP method being processed. Only GET and POST supported currently
    php_files_path : pathlib.Path
        Full path to the directory containing the PHP files
    
    Returns
    -------
    list, string
        Return a list of headers and the body parsed from the output
    """
    php_file_path = find_php_file_path(request_uri, php_files_path)

    php_script_output = ""
    if http_method == "GET":
        handle_get_environ_vars(php_file_path, request_params)
        php_script_output = os.popen("php-cgi").read()
        handle_get_environ_vars("", "", remove_vars=True)
    elif http_method == "POST":
        handle_post_environ_vars(php_file_path, request_params)
        php_script_output = os.popen("echo $BODY | php-cgi").read()
        handle_post_environ_vars("", "", remove_vars=True)
    
    return parse_php_output(php_script_output)


def find_php_file_path(file_name, php_files_path):
    """Recursively looks through the php_files_path to get the full path to
    the file_name specified
    
    Parameters
    ----------
    file_name : string
        Name of the PHP file to find
    php_files_path : pathlib.Path
        Full path to the directory containing all PHP files
    
    Returns
    -------
    pathlib.Path
        Full path to the desired PHP script
    """
    globber = php_files_path.rglob('*.php')
    php_file_path = ""
    
    for php_file in globber:
        if php_file.name == file_name.strip("/"):
            php_file_path = php_file

    return php_file_path


def handle_post_environ_vars(script_path, request_params, remove_vars=False):
    """Set and remove the environment variables needed to process a POST request
    in php-cgi
    
    Parameters
    ----------
    script_path : pathlib.Path
        Full path to the PHP script desired
    request_params : string
        Parameters to be passed into the script (used for the BODY environment variable)
    remove_vars : bool, optional
        If true, remove all environment variables set by this function, by default False
    """
    if remove_vars:
        os.environ.pop("GATEWAY_INTERFACE")
        os.environ.pop("SCRIPT_FILENAME")
        os.environ.pop("REQUEST_METHOD")
        os.environ.pop("REDIRECT_STATUS")
        os.environ.pop("SERVER_PROTOCOL")
        os.environ.pop("REMOTE_HOST")
        os.environ.pop("CONTENT_LENGTH")
        os.environ.pop("BODY")
        os.environ.pop("CONTENT_TYPE")
    else:
        os.environ["GATEWAY_INTERFACE"] = "CGI/1.1"
        os.environ["SCRIPT_FILENAME"] = str(script_path)
        os.environ["REQUEST_METHOD"] = "POST"
        os.environ["SERVER_PROTOCOL"] = "HTTP/1.1"
        os.environ["REMOTE_HOST"] = "127.0.0.1"
        os.environ["CONTENT_LENGTH"] = str(len(request_params))
        os.environ["BODY"] = request_params
        os.environ["CONTENT_TYPE"] = "application/x-www-form-urlencoded"
        os.environ["REDIRECT_STATUS"] = "0"


def handle_get_environ_vars(script_path, request_params, remove_vars=False):
    """Set and remove the environment variables needed to process a GET request
    in php-cgi
    
    Parameters
    ----------
    script_path : pathlib.Path
        Full path to the PHP script desired
    request_params : string
        Parameters to be passed into the script (used for the BODY environment variable)
    remove_vars : bool, optional
        If true, remove all environment variables set by this function, by default False
    """
    if remove_vars:
        os.environ.pop("QUERY_STRING")
        os.environ.pop("SCRIPT_FILENAME")
        os.environ.pop("REQUEST_METHOD")
        os.environ.pop("REDIRECT_STATUS")
    else:
        os.environ["QUERY_STRING"] = request_params
        os.environ["SCRIPT_FILENAME"] = str(script_path)
        os.environ["REQUEST_METHOD"] = "GET"
        os.environ["REDIRECT_STATUS"] = "0"


def parse_php_output(php_output_data):
    """Parse the output from phop-cgi into headers and body
    
    Parameters
    ----------
    php_output_data : string
        Output from processing php-cgi
    
    Returns
    -------
    list, string
        Return a list of headers and the body parsed from the output
    """
    output_split = php_output_data.split("\n\n")
    body = output_split[1]

    headers = []
    headers_seperated = output_split[0].split("\n")
    for header in headers_seperated:
        headers.append(header.strip())
    
    return headers, body
