'''
file: Response_Codes.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Response code functions used by HTTP_Parser.py
'''

def respond_with_200():
    """Print a HTTP 1.1 200 OK message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    print("HTTP/1.1 200 OK\r\n\r\n")
    exit(0)


def respond_with_400():
    """Print a HTTP 1.1 400 BAD REQUEST message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    print("HTTP/1.1 400 BAD REQUEST\r\n\r\n")
    exit(1)


def respond_with_500():
    """Print a HTTP 1.1 500 INTERNAL SERVER ERROR message and exit
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    print("HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\n")
    exit(2)
    