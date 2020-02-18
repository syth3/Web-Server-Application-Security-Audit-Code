'''
file: Handler.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Functions to process request
'''

import logging
import Connection_Utils
import HTTP_Parser
import Response_Codes
import Process_Request_Methods


def handler(sock):
    """Process HTTP request
    
    Parameters
    ----------
    sock : socket.socket
        Socket to connect to client with
    
    Returns
    -------
    Nothing
    """
    response = ""
    try:
        request = Connection_Utils.get_request(sock)

        # The [2:-1] gets rid of the b'' around the request
        parsed_request = HTTP_Parser.parse_request(request[2:-1])

        request_line = parsed_request.get_method() + " " + parsed_request.get_request_uri() + " " + parsed_request.get_http_version()
        log_data(request_line)

        # HTTP_Parser.print_parsed_request(parsed_request)
        parsed_request.print_parsed_request()
        print()

        if parsed_request.get_response_code() != 200:
            response = return_http_code(parsed_request.get_response_code())
        else:
            response = execute_method(parsed_request)
    except Exception:
        response = Response_Codes.respond_with_500()

    sock.send(response.encode())
    sock.close()


def log_data(first_line_of_request):
    """Log request data
    
    Parameters
    ----------
    first_line_of_request : string
        The following data gets logged: Method, request-uri, and http version
    
    Returns
    -------
    Nothing
    """
    logging.basicConfig(level=logging.DEBUG, filename='HTTP Server Log.txt', filemode='a', format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info(first_line_of_request)


def return_http_code(response_code):
    """Return an error response code
    
    Parameters
    ----------
    response_code: int
        Response code to send
    
    Returns
    -------
    string
        HTTP message to be send back to the client
    """
    if response_code == "400":
        return Response_Codes.respond_with_400()
    elif response_code == "501":
        return Response_Codes.respond_with_501()
    elif response_code == "505":
        return Response_Codes.respond_with_505()


def execute_method(parsed_request):
    """Execute the right HTTP method
    
    Parameters
    ----------
    parsed_request : Parsed_Request
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    string
        HTTP message to return to the client
    """
    response = ""
    method = parsed_request.get_method()
    if method == "GET":
        response = Process_Request_Methods.process_GET(parsed_request)
    elif method == "POST":
        response = Process_Request_Methods.process_POST(parsed_request)
    elif method == "PUT":
        response = Process_Request_Methods.process_PUT(parsed_request)
    elif method == "DELETE":
        response = Process_Request_Methods.process_DELETE(parsed_request)
    elif method == "HEAD":
        response = Process_Request_Methods.process_HEAD(parsed_request)
    
    return response