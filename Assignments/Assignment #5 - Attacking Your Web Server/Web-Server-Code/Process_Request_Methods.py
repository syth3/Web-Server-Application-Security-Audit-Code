'''
file: Process_Request_Methods.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Functions to process different HTTP methods
'''

import Response_Codes
import PHP_Processing
from pathlib import Path


RESOURCES_DIR_NAME = "Resources"


def process_GET(parsed_request):
    """Process a GET request by running a PHP script or returning the contents of the resource requested 
    
    Parameters
    ----------
    parsed_request : Parsed_Object.Parsed_Object
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    string
        HTTP message to return to the client
    """
    # Make default request-uri /index.html
    if parsed_request.get_request_uri() == "/":
        parsed_request.set_request_uri("/index.html")

    # Parse request parameters out of the request-uri
    request_uri = parsed_request.get_request_uri().split("?")[0]
    request_params = ""
    if len(parsed_request.get_request_uri().split("?")) > 1:
        request_params = parsed_request.get_request_uri().split("?")[1]

    # Assemble path to use to fetch the desired resource
    curr_dir = Path.cwd()
    file_name = Path(request_uri)
    resources_dir = curr_dir / RESOURCES_DIR_NAME
    path = Path(str(resources_dir) + str(file_name))

    # Return 404 if file is not found
    if not path.exists():
        return Response_Codes.respond_with_404()

    # Process PHP files
    if path.suffix == ".php" and request_params != "":
        php_output_headers, php_output_body = PHP_Processing.process_php_file(
            file_name.name, request_params, parsed_request.get_method(), resources_dir)
        return Response_Codes.respond_with_200(php_output_body, additional_headers=php_output_headers)
    # If not a PHP file, return contents of file requested
    else:
        try:
            path.open()
        except PermissionError:
            return Response_Codes.respond_with_403()
        except IsADirectoryError:
            return Response_Codes.respond_with_404()
        return Response_Codes.respond_with_200(path.read_text())


def process_POST(parsed_request):
    """Process a POST request by executing a PHP script or returning the body and request-uri sent in
    
    Parameters
    ----------
    parsed_request : Parsed_Object.Parsed_Object
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    string
        HTTP message to return to the client
    """
    # Check that the Content-Length header is present
    found_content_length = False
    for header in parsed_request.get_headers():
        if header[0].lower() == "content-length":
            found_content_length = True
        if header[0] == "Content-Type" and header[1] != "application/x-www-form-urlencoded":
            return Response_Codes.respond_with_501("Only supported Content-Type is application/x-www-form-urlencoded")

    if not found_content_length:
        return Response_Codes.respond_with_411()

    # Process PHP
    request_uri_path = Path(parsed_request.get_request_uri())
    resources_dir = Path.cwd() / RESOURCES_DIR_NAME
    if request_uri_path.suffix == ".php":
        php_output_headers, php_output_body = PHP_Processing.process_php_file(
            request_uri_path.name, parsed_request.get_body(), parsed_request.get_method(), resources_dir)
        return Response_Codes.respond_with_200(php_output_body, additional_headers=php_output_headers)
    # Process POST request
    else:
        return_body = "Body passed in:\n\t" + \
            parsed_request.get_body() + \
            "\nRequest-URI: " + \
            parsed_request.get_request_uri()
        return Response_Codes.respond_with_200(return_body)


def process_PUT(parsed_request):
    """Process a PUT request by creating a file or replacing the contents of a file with the contents of the body in the HTTP request
    
    Parameters
    ----------
    parsed_request : Parsed_Object.Parsed_Object
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    string
        HTTP message to return to the client
    """
    curr_dir = Path.cwd()
    file_name = Path(parsed_request.get_request_uri())
    path = curr_dir / RESOURCES_DIR_NAME
    path = Path(str(path) + str(file_name))

    if path.is_dir():
        return Response_Codes.respond_with_404()
    
    body = parsed_request.get_body()
    path.write_text(body)

    return Response_Codes.respond_with_201(body, str(file_name))


def process_DELETE(parsed_request):
    """Process a DELETE request by deleting the file specified
    
    Parameters
    ----------
    parsed_request : Parsed_Object.Parsed_Object
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    string
        HTTP message to return to the client
    """
    curr_dir = Path.cwd()
    file_name = Path(parsed_request.get_request_uri())
    path = curr_dir / RESOURCES_DIR_NAME
    path = Path(str(path) + str(file_name))

    if not path.exists():
        return Response_Codes.respond_with_404()

    path.unlink()

    return Response_Codes.respond_with_200("Deleted Successfully")


def process_HEAD(parsed_request):
    """Process a HEAD request by returning headers
    
    Parameters
    ----------
    parsed_request : Parsed_Object.Parsed_Object
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    string
        HTTP message to return to the client
    """
    return Response_Codes.respond_with_200("")