'''
file: Response_Codes.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Response code functions
'''

from datetime import datetime


def respond_with_200(body):
    """Return a HTTP 1.1 200 OK message
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    response = "HTTP/1.1 200 OK\r\n"
    response += "Date: " + datetime.now().strftime('%a, %d %b %Y %I:%M:%S') + "\r\n"
    response += "\r\n"
    response += body
    return response


def respond_with_201(body, location):
    """Return a HTTP 1.1 201 Created message
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
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
    Nothing
    """
    response = "HTTP/1.1 400 Bad Request\r\n"
    response + "\r\n"
    response += "Bad Request"
    response += "\r\n"
    return response


def respond_with_403():
    """Return a HTTP 1.1 403 Forbidden message
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    response = "HTTP/1.1 400 Forbidden\r\n"
    response + "\r\n"
    response += "Forbidden"
    response += "\r\n"
    return response


def respond_with_404():
    """Return a HTTP 1.1 404 Not Found message
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    response = "HTTP/1.1 404 Not Found\r\n"
    response += "\r\n"
    response += "Not Found"
    response += "\r\n"
    return response


def respond_with_411():
    """Return a HTTP 1.1 411 Length Required message
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    response = "HTTP/1.1 411 Length Required\r\n"
    response + "\r\n"
    response += "Length Required"
    response += "\r\n"
    return response


def respond_with_500():
    """Return a HTTP 1.1 500 INTERNAL SERVER ERROR message
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    response = "HTTP/1.1 500 Internal Server Error\r\n"
    response + "\r\n"
    response += "Internal Server Error"
    response += "\r\n"
    return response
    

def respond_with_501():
    """Return a HTTP 1.1 501 Not Implemented message
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    response = "HTTP/1.1 501 Not Implemented\r\n"
    response + "\r\n"
    response += "Not Implemented"
    response += "\r\n"
    return response


def respond_with_505():
    """Return a HTTP 1.1 505 HTTP Version Not Supported message
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    response = "HTTP/1.1 505 HTTP Version Not Supported\r\n"
    response + "\r\n"
    response += "HTTP Version Not Supported"
    response += "\r\n"
    return response