import os
from pathlib import Path


def process_php_file(request_uri, request_params, http_method, php_files_path):
    php_file_paths = find_php_file_path(request_uri, php_files_path)

    php_script_output = ""
    for path in php_file_paths:
        if path.stem + path.suffix == request_uri.strip("/") and http_method == "GET":
            handle_get_environ_vars(path, request_params)
            php_script_output = os.popen("php-cgi").read()
            handle_get_environ_vars("", "", remove_vars=True)
        elif path.stem + path.suffix == request_uri.strip("/") and http_method == "POST":
            handle_post_environ_vars(path, request_params)
            php_script_output = os.popen("echo $BODY | php-cgi").read()
            handle_post_environ_vars("", "", remove_vars=True)
    
    return parse_php_output(php_script_output)


def find_php_file_path(file_name, php_files_path):
    globber = php_files_path.rglob('*.php')
    all_php_file_paths = []
    
    for php_file in globber:
        all_php_file_paths.append(Path(php_file))

    return all_php_file_paths


def handle_post_environ_vars(script_path, request_params, remove_vars=False):
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


def handle_get_environ_vars(script_path, query_string, remove_vars=False):
    if remove_vars:
        os.environ.pop("QUERY_STRING")
        os.environ.pop("SCRIPT_FILENAME")
        os.environ.pop("REQUEST_METHOD")
        os.environ.pop("REDIRECT_STATUS")
    else:
        os.environ["QUERY_STRING"] = query_string
        os.environ["SCRIPT_FILENAME"] = str(script_path)
        os.environ["REQUEST_METHOD"] = "GET"
        os.environ["REDIRECT_STATUS"] = "0"


def parse_php_output(php_output_data):
    output_split = php_output_data.split("\n\n")
    body = output_split[1]

    headers = []
    headers_seperated = output_split[0].split("\n")
    for header in headers_seperated:
        headers.append(header.strip())
    
    return headers, body

# 1) get full file path
# 2) handle the environment variables
# 3) call php-cgi from os.system or something like that