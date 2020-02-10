'''
file: HTTP_Parser.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: HTTP parser that verifies the syntax of a HTTP request
'''

import sys


PARSED_REQUEST = {}


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


def verify_method(method):
    """Verify that the method used is allowed by a predetermined list.
    Return a 400 code and exit if it is not.
    
    Parameters
    ----------
    method : string
        Method to verify
    
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
        PARSED_REQUEST["response_code"] = 501
    else:
        PARSED_REQUEST["method"] = method.upper()


def verify_request_uri(request_uri):
    """Verify that the request URI is valid. Return a 400 code and exit if it is not.
    Note: This function was not needed for this assignment.
          It will be implemented at a later time when it is needed
    
    Parameters
    ----------
    request_uri : string
        Request URI to verify
    
    Returns
    -------
    Nothing
    """
    PARSED_REQUEST["request_uri"] = request_uri


def verify_http_version(http_version):
    """Verify the HTTP 1.1 is used. Return a 400 code and exit if it is not.
    
    Parameters
    ----------
    http_version : string
        HTTP version string to verify
    
    Returns
    -------
    Nothing
    """
    if http_version != "HTTP/1.1" and http_version != "HTTP/1.0":
        PARSED_REQUEST["response_code"] = 505
    else:
        PARSED_REQUEST["http_version"] = http_version


def verify_request_line(request_line):
    """Verify the syntax of the request line. The syntax should follow the following production rule:
    Request-Line = Method SP Request-Target SP HTTP-Version CRLF
    Return a 400 code and exit if it is not valid.
    
    Parameters
    ----------
    request_line : string
        request line to verify
    
    Returns
    -------
    Nothing
    """
    if request_line.count(" ") != 2:
        PARSED_REQUEST["response_code"] = 400
    
    split_request_line = request_line.split(" ")
    method = split_request_line[0]
    verify_method(method)

    request_uri = split_request_line[1]
    verify_request_uri(request_uri)

    http_version = split_request_line[2]
    verify_http_version(http_version)


def verify_header(header):
    """Verify that the syntax of an individual header is correct
    
    Parameters
    ----------
    header : string
        Individual header to validate
    
    Returns
    -------
    UPDATE
    """
    header = header.replace(" ", "")
    # header_split = header.split(":")
    # header_name = header_split[0]
    # header_value = ""
    # for element in header_split[1:]:
    #     header_value += element
    first_colon_location = header.find(":")
    header_name = header[0:first_colon_location]
    header_value = header[first_colon_location+1:]

    header_tuple = (header_name, header_value)
    PARSED_REQUEST["headers"].append(header_tuple)

def verify_headers(headers):
    """Verify that all headers are syntaxually correct and that the "Host" header is included
    
    Parameters
    ----------
    headers : list
        List of headers to verify
    
    Returns
    -------
    Nothing
    """
    PARSED_REQUEST["headers"] = []
    for header in headers:
        verify_header(header)

    if PARSED_REQUEST["http_version"] == "HTTP/1.1":
        count = 0
        for header in PARSED_REQUEST["headers"]:
            if header[0].lower() == "host":
                count += 1

        if count != 1:
            PARSED_REQUEST["response_code"] = 400


def parse_request(request):
    """Parse a HTTP request and check for syntax. If syntax is correct, respond with a 400 HTTP code.
    Otherwise, respond with a 200 HTTP code.
    
    Parameters
    ----------
    request : list
        HTTP request read from a file in the following way: open(file_name, 'rb').readlines()
    
    Returns
    -------
    Nothing
    """
    PARSED_REQUEST["response_code"] = 200
    request_str = request[2:-1]

    ###### For Testing ######
    # request_str = ""
    # for line in request:
    #     request_str += str(line)[2:-1]
    #########################

    if request_str.count("\\r\\n\\r\\n") != 1:
        PARSED_REQUEST["response_code"] = 400
    
    request_line_and_headers = request_str.split("\\r\\n\\r\\n")[0]

    request_line = request_line_and_headers.split("\\r\\n")[0]
    verify_request_line(request_line)

    request_headers = request_line_and_headers.split("\\r\\n")[1:]
    verify_headers(request_headers)

    return PARSED_REQUEST


def print_parsed_request(parsed_request):
    for key in parsed_request.keys():
        if key == "headers":
            print("headers:")
            for header in parsed_request[key]:
                print("  - " + header[0] + ": " + header[1])
        else:
            print(key + " -> " + str(parsed_request[key]))


def main():
    parsed_request = {}
    http_file = gather_input()
    parsed_request = parse_request(http_file)
    print_parsed_request(parsed_request)
    
if __name__ == "__main__":
    main()