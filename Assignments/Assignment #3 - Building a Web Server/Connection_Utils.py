'''
file: Connection_Utils.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Functions to handle socket connections
'''

import socket
import ssl
import logging
import threading
import HTTP_Parser
import Response_Codes
import Process_Request_Methods


NUM_CONCURRENT_CONNECTIONS = 5


def log_data(first_line_of_request):
    """Log request data
    
    Parameters
    ----------
    first_line_of_request : Method, request-uri, and http version
        Data to be logged
    
    Returns
    -------
    Nothing
    """
    logging.basicConfig(level=logging.DEBUG, filename='HTTP Server Log.txt', filemode='a', format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info(first_line_of_request)


def handler(sock):
    """Handle connection with client
    
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
        request = get_request(sock)
        parsed_request = HTTP_Parser.parse_request(request)

        request_line = parsed_request["method"] + " " + parsed_request["request_uri"] + " " + parsed_request["http_version"]
        log_data(request_line)

        HTTP_Parser.print_parsed_request(parsed_request)

        if parsed_request["response_code"] != 200:
            response = return_http_code(parsed_request["response_code"])
        else:
            response = execute_method(parsed_request)
    except Exception:
        response = Response_Codes.respond_with_500()

    sock.send(response.encode())
    sock.close()


def return_http_code(response_code):
    """Return a error response code
    
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
    parsed_request : dict
        Dictionary of the HTTP request parsed
    
    Returns
    -------
    string
        HTTP message to return to the client
    """
    response = ""
    method = parsed_request["method"]
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
    

def get_request(sock):
    """Receive data from client
    
    Parameters
    ----------
    sock : socket.socket
        Socket to receive data from
    
    Returns
    -------
    string
        Request sent by the client
    """ 
    return str(sock.recv(1024))


def start_server(input_args):
    """Start the server with the arguments given
    
    Parameters
    ----------
    input_args : dict
        Dictionary of all the input arguments
    """
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind((input_args["ip_address"], input_args["port"]))
    srv_sock.listen(NUM_CONCURRENT_CONNECTIONS)

    while True:
        conn_sock, addr = srv_sock.accept()
        # conn_sock.send(Response_Codes.respond_with_200().encode())
        if input_args["scheme"] == "https":
            conn_sock = create_tls_socket(conn_sock, input_args["x509_path"], input_args["x509_private_key_path"])
        t = threading.Thread(target=handler, args=(conn_sock,))
        t.start()


def create_tls_socket(conn_sock, cert_file, key_file):
    """Create TLS socket to be used for communication
    
    Parameters
    ----------
    conn_sock : socket.socket
        Socket to wrap
    cert_file : string
        Path to cert file
    key_file : string
        Path to key file
    
    Returns
    -------
    SSLContext
        SSL socket to communicate over
    """
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_OPTIONAL
    context.load_cert_chain(certfile=cert_file, keyfile=key_file, password=None)

    return context.wrap_socket(conn_sock, server_side=True)
