'''
file: HTTP_Parser.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: HTTP parser that verifies the syntax of a HTTP request
'''

import sys
import Parsed_Request


def print_usage():
    """Print the usage message of this script
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    print("Usage: HTTP_Parser.py path_to_http_file")


def gather_input():
    """Gather input from the command line and exit if input is incorrect
    
    Parameters
    ----------
    None

    Returns
    -------
    string
        File with HTTP request opened for reading in binary mode 
    """
    if len(sys.argv) != 2:
        print_usage()
        exit(1)
    else:
        return open(sys.argv[1], 'rb').readlines()


def verify_method(method, parsed_request):
    """Verify that the method used is allowed by a predetermined list.
    Return a 400 code and exit if it is not.
    
    Parameters
    ----------
    method : string
        Method to verify
    parsed_request : Parsed_Request
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    Nothing
    """ 
    allowed_methods = [
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "HEAD"
    ]

    if method.upper() not in allowed_methods:
        parsed_request.set_response_code(501)
    else:
        parsed_request.set_method(method.upper())


def verify_request_uri(request_uri, parsed_request):
    """Verify that the request URI is valid. Return a 400 code and exit if it is not.
    Note: This function was not needed for this assignment.
          It will be implemented at a later time when it is needed
    
    Parameters
    ----------
    request_uri : string
        Request URI to verify
    parsed_request : Parsed_Request
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    Nothing
    """
    parsed_request.set_request_uri(request_uri)


def verify_http_version(http_version, parsed_request):
    """Verify the HTTP 1.1 is used. Return a 400 code and exit if it is not.
    
    Parameters
    ----------
    http_version : string
        HTTP version string to verify
    parsed_request : Parsed_Request
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    Nothing
    """
    if http_version != "HTTP/1.1" and http_version != "HTTP/1.0":
        parsed_request.set_response_code(505)
    else:
        parsed_request.set_http_version(http_version)


def verify_request_line(request_line, parsed_request):
    """Verify the syntax of the request line. The syntax should follow the following production rule:
    Request-Line = Method SP Request-Target SP HTTP-Version CRLF
    Return a 400 code and exit if it is not valid.
    
    Parameters
    ----------
    request_line : string
        request line to verify
    parsed_request : Parsed_Request
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    Nothing
    """
    if request_line.count(" ") != 2:
        parsed_request.set_response_code(400)
    
    split_request_line = request_line.split(" ")
    method = split_request_line[0]
    verify_method(method, parsed_request)

    request_uri = split_request_line[1]
    verify_request_uri(request_uri, parsed_request)

    http_version = split_request_line[2]
    verify_http_version(http_version, parsed_request)


def verify_header(header, parsed_request):
    """Verify that the syntax of an individual header is correct
    
    Parameters
    ----------
    header : string
        Individual header to validate
    parsed_request : Parsed_Request
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    UPDATE
    """
    header = header.replace(" ", "")
    first_colon_location = header.find(":")
    header_name = header[0:first_colon_location]
    header_value = header[first_colon_location+1:]

    parsed_request.set_header(header_name, header_value)


def verify_headers(headers, parsed_request):
    """Verify that all headers are syntaxually correct and that the "Host" header is included
    
    Parameters
    ----------
    headers : list
        List of headers to verify
    parsed_request : Parsed_Request
        Parsed_Request object that represents the HTTP request parsed
    
    Returns
    -------
    Nothing
    """
    for header in headers:
        verify_header(header, parsed_request)

    if parsed_request.get_http_version() == "HTTP/1.1":
        count = 0
        for header in parsed_request.get_headers():
            if header[0].lower() == "host":
                count += 1

        if count != 1:
            parsed_request.set_response_code(400)


def parse_request(request):
    """Parse a HTTP request and check for syntax. If syntax is correct, respond with a 400 HTTP code.
    Otherwise, respond with a 200 HTTP code.
    
    Parameters
    ----------
    request : string
        HTTP request read as a byte stream and converted to a string
    
    Returns
    -------
    Nothing
    """
    parsed_request = Parsed_Request.Parsed_Request()

    if request.count("\\r\\n\\r\\n") != 1:
        parsed_request.set_response_code(400)
        return parsed_request

    request_line_and_headers = request.split("\\r\\n\\r\\n")[0]
    request_body = request.split("\\r\\n\\r\\n")[1]
    parsed_request.set_body(request_body)

    request_line = request_line_and_headers.split("\\r\\n")[0]
    verify_request_line(request_line, parsed_request)

    request_headers = request_line_and_headers.split("\\r\\n")[1:]
    verify_headers(request_headers, parsed_request)

    return parsed_request


def main():
    http_file = gather_input()

    request_str = ""
    for line in http_file:
        request_str += str(line)[2:-1]
    
    parsed_request = parse_request(request_str)
    parsed_request.print_parsed_request()
    
if __name__ == "__main__":
    main()