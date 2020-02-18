'''
file: Connection_Utils.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Functions to handle socket connections
'''

import socket
import ssl
import threading
import Handler
import Response_Codes


NUM_CONCURRENT_CONNECTIONS = 5
    

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
    input_args : Input_Args.Input_Args
        Object representing all the input arguments
    """
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind((input_args.get_ip_address(), input_args.get_port()))
    srv_sock.listen(NUM_CONCURRENT_CONNECTIONS)

    while True:
        conn_sock, addr = srv_sock.accept()
        if input_args.get_scheme() == "https":
            conn_sock = create_tls_socket(conn_sock, input_args.get_x509_path(), input_args.get_x509_private_key_path())
        t = threading.Thread(target=Handler.handler, args=(conn_sock,))
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
