'''
file: ConnectionUtils.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Utilities for connecting to a URL over a python socket. Used by HTTPClient.py
'''

import socket
import ssl


def extract_port_and_host(scheme, url):
    """Extracts the port and host from an URL. If no port is given in the URL, assume 80 for HTTP and 443 for HTTPS
    
    Parameters
    ----------
    scheme : string
        What scheme is used in the URL. Only HTTP and HTTPS are supported
    url : string
        URL to parse
    
    Returns
    -------
    string, string
        Returns two string. First string is the host and second is the port
    """
    port = 0
    url_port_split = url.split(":")
    host = url_port_split[0].strip("/")

    if len(url_port_split) != 2:
        if scheme == "http":
            port = 80
        if scheme == "https":
            port = 443
    else:
        port = url_port_split[1]
    
    return host, int(port)


def connect_over_http(host, port):
    """Create a socket and connect to the host and port provided over HTTP
    
    Parameters
    ----------
    host : string
        Host to connect to
    port : int
        Port to connect to
    
    Returns
    -------
    socket.socket
        Socket to send and receive data with
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    return sock


def connect_over_https(host, port):
    """Create a socket and connect to the host and port provided over HTTPS
    
    Parameters
    ----------
    host : string
        Host to connect to
    port : int
        Port to connect to
    
    Returns
    -------
    socket.socket
        Socket to send and receive data with
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    sock = context.wrap_socket(sock, server_hostname=host)
    sock.connect((host, port))

    return sock


def recv_allow_keyboard_interupt(sock):
    """Send data over the given socket, and allow a keyboard interrupt when receiving data
    
    Parameters
    ----------
    sock : socket.socket
        Socket to receive data over
    
    Returns
    -------
    string
        Data received by the socket
    """
    try:
        data = sock.recv(8192).decode(encoding = "utf_8", errors = "ignore")
    except KeyboardInterrupt:
        pass

    return data


def send_and_recieve_over_socket(sock, request):
    """Send the given request over the given socket, receive the response, then return the response
    
    Parameters
    ----------
    sock : socket.socket
        Socket to send and receive data with
    request : string
        Request to send to the socket
    
    Returns
    -------
    string
        Response received from the socket
    """
    sock.send(request.encode())
    response = ""
    data = recv_allow_keyboard_interupt(sock)
    while data != "":
        response += data
        data = recv_allow_keyboard_interupt(sock)

    return response


def craft_request(host):
    """Generate a HTTP/1.1 compliant request using the given host
    
    Parameters
    ----------
    host : string
        Host to use in the "Host" header
    
    Returns
    -------
    string
        HTTP/1.1 compliant request
    """
    request =  "GET / HTTP/1.1\r\n"
    request += "Host: " + host + "\r\n"
    request += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36\r\n"
    request += "Accept-Encoding: identity\r\n"
    request += "Connection: Close\r\n"
    request += "SSL_PROTOCOL: TLSv1.2\r\n"
    request += "\r\n"

    return request


def get_page(url):
    """Get web page at provided URL and return it
    
    Parameters
    ----------
    url : string
        URL to grab the web page from
    
    Returns
    -------
    string
        Web page grabbed from URL
    """
    url_scheme_split = url.split("://")
    url_scheme = url_scheme_split[0]
    url_host_and_rest = url_scheme_split[1]
    host, url_port = extract_port_and_host(url_scheme, url_host_and_rest)
    sock = None
    if url_scheme == "http":
        sock = connect_over_http(host, url_port)
    if url_scheme == "https":
        sock = connect_over_https(host, url_port)
    
    request = craft_request(host)
    # print(request)
    response = send_and_recieve_over_socket(sock, request)
    # print(response)
    response_first_line = response.split("\n")[0]
    http_code = response_first_line.split(" ")[1]
    # print(http_code)
    response_headers = response.split("\r\n\r\n")[0].strip()
    web_page = response.split("\r\n\r\n")[1].strip()
    sock.close()

    return web_page, http_code, response_headers
