'''
file: Response_Codes.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Functions used to assemble and return HTTP responses
'''

from datetime import datetime


def respond_with_200(body, additional_headers=None):
    """Return a HTTP 1.1 200 OK message with the body and optional headers specified
    
    Parameters
    ----------
    body : string
        Body to append to the HTTP response
    additional_headers : list, optional
        List of headers to add to the response, by default None
    
    Returns
    -------
    string
        HTTP 200 response
    """
    response = "HTTP/1.1 200 OK\r\n"
    response += "Date: " + datetime.now().strftime('%a, %d %b %Y %I:%M:%S') + "\r\n"
    response += "Content-Length: " + str(len(body)) + "\r\n"
    if additional_headers != None:
        for header in additional_headers:
            response += header + "\r\n"
    response += "\r\n"
    response += body
    return response


def respond_with_201(body, location):
    """Return a HTTP 1.1 201 Created message with the body and location specified
    
    Parameters
    ----------
    body : string
        Body to append to the HTTP response
    location : string
        Location of where the created file resides
    
    Returns
    -------
    string
        HTTP 201 response
    """
    response = "HTTP/1.1 200 Created\r\n"
    response += "Content-Location: " + location + "\r\n"
    response += "\r\n"
    response += body
    return response


def respond_with_400():
    """Return a HTTP 1.1 400 Bad Request message
    
    Parameters
    ----------
    None

    Returns
    -------
    string
        HTTP 400 response
    """
    response = "HTTP/1.1 400 Bad Request\r\n"
    response += "\r\n"
    response += "Bad Request"
    return response


def respond_with_403():
    """Return a HTTP 1.1 403 Forbidden message
    
    Parameters
    ----------
    None

    Returns
    -------
    string
        HTTP 403 response
    """
    response = "HTTP/1.1 400 Forbidden\r\n"
    response += "\r\n"
    response += "Forbidden"
    return response


def respond_with_404():
    """Return a HTTP 1.1 404 Not Found message
    
    Parameters
    ----------
    None

    Returns
    -------
    string
        HTTP 404 response
    """
    response = "HTTP/1.1 404 Not Found\r\n"
    response += "\r\n"
    response += "Not Found"
    return response


def respond_with_411():
    """Return a HTTP 1.1 411 Length Required message
    
    Parameters
    ----------
    None

    Returns
    -------
    string
        HTTP 411 response
    """
    response = "HTTP/1.1 411 Length Required\r\n"
    response += "\r\n"
    response += "Length Required"
    return response


def respond_with_500():
    """Return a HTTP 1.1 500 INTERNAL SERVER ERROR message
    
    Parameters
    ----------
    None

    Returns
    -------
    string
        HTTP 500 response
    """
    response = "HTTP/1.1 500 Internal Server Error\r\n"
    response += "\r\n"
    response += "Internal Server Error"
    return response
    

def respond_with_501(body=None):
    """Return a HTTP 1.1 501 Not Implemented message with an optional body specified
    
    Parameters
    ----------
    body : string, optional
        Message to be inserted into the body of the response, by default None
    
    Returns
    -------
    string
        HTTP 501 response
    """
    response = "HTTP/1.1 501 Not Implemented\r\n"
    response += "\r\n"
    if body != None:
        response += body
    else:
        response += "Not Implemented"
    return response


def respond_with_505():
    """Return a HTTP 1.1 505 HTTP Version Not Supported message
    
    Parameters
    ----------
    None

    Returns
    -------
    string
        HTTP 505 response
    """
    response = "HTTP/1.1 505 HTTP Version Not Supported\r\n"
    response += "\r\n"
    response += "HTTP Version Not Supported"
    return response