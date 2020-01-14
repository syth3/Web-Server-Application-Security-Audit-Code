'''
file: ConnectionUtils.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Utilities for connecting to a URL over a python socket. Used by HTTPClient.py
'''

import socket


def connect_over_http(url):
    pass


def connect_over_https(url):
    pass


def get_page(url):
    """Get web page at provided URL and return it
    
    Parameters
    ----------
    url : string
        URL to grab the web page from
    
    Returns
    -------
    string
        Web page grabbed form URL
    """
    url_scheme = url.split("://")[0]
    if url_scheme == "http":
        connect_over_http(url)
    if url_scheme == "https":
        connect_over_https(url)
    
    return ""
