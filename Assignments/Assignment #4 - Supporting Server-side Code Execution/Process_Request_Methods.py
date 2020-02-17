'''
file: Process_Request_Methods.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Functions to parse different HTTP methods
'''

import Response_Codes
from pathlib import Path

def process_GET(parsed_request):
    """Process a GET request by returning the contents of the resource requested 
    
    Parameters
    ----------
    parsed_request : Parsed_Object.Parsed_Object
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    string
        HTTP message to return to the client
    """
    if parsed_request.get_request_uri() == "/":
        parsed_request.set_request_uri("/index.html")

    curr_dir = Path.cwd()
    file_name = Path(parsed_request.get_request_uri())
    path = curr_dir / "Resources"
    path = Path(str(path) + str(file_name))

    if not path.exists():
        return Response_Codes.respond_with_404()

    try:
        path.open()
    except PermissionError:
        return Response_Codes.respond_with_403()
    return Response_Codes.respond_with_200(path.read_text())


def process_POST(parsed_request):
    """Process a POST request by sending the date in the body of the HTTP request to the endpoint in the request-uri
    
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

    if not found_content_length:
        return Response_Codes.respond_with_411()

    #Process POST request
    return_body = "Body passed in:\n\t" + parsed_request.get_body() + "\nRequest-URI: " + parsed_request.get_request_uri()

    return Response_Codes.respond_with_200(return_body)


def process_PUT(parsed_request):
    """Process a PUT request by creating/replacing a file with the contents of the body of the HTTP request
    
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
    path = curr_dir / "Resources"
    path = Path(str(path) + str(file_name))

    if path.is_dir():
        print("This is a dir:", path)
        print(type(path))
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
    path = curr_dir / "Resources"
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