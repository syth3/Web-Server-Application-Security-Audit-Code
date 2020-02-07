'''
file: Response_Codes.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Response code functions used by HTTP_Parser.py
'''

def respond_with_200():
    """Return a HTTP 1.1 200 OK message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 200 OK\r\n\r\n"


def respond_with_201():
    """Return a HTTP 1.1 201 Created message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 200 Created\r\n\r\n"


def respond_with_400():
    """Return a HTTP 1.1 400 Bad Request message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 400 Bad Request\r\n\r\n"


def respond_with_403():
    """Return a HTTP 1.1 403 Forbidden message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 400 Forbidden\r\n\r\n"


def respond_with_404():
    """Return a HTTP 1.1 404 Not Found message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 404 Not Found\r\n\r\n"


def respond_with_411():
    """Return a HTTP 1.1 411 Length Required message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 411 Length Required\r\n\r\n"


def respond_with_500():
    """Return a HTTP 1.1 500 INTERNAL SERVER ERROR message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\n"
    

def respond_with_501():
    """Return a HTTP 1.1 501 Not Implemented message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 501 Not Implemented\r\n\r\n"


def respond_with_505():
    """Return a HTTP 1.1 505 HTTP Version Not Supported message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    return "HTTP/1.1 505 HTTP Version Not Supported\r\n\r\n"