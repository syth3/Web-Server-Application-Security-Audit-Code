'''
file: HTTPClient.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: HTTP Client that will take in a URL and print external links on the HTML page returned from the URL
    Note: This code only uses the socket library for HTTP communication and basic string parsing libraries for
          HTML parsing
'''

import sys
import logging
import ConnectionUtils
import Parser


def print_usage():
    """Print the usage message of this script
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    print("Usage: HTTPClient.py URL")


def validate_url(url):
    """Validate that a URL scheme is either http or https
    
    Parameters
    ----------
    url : string
        URL to be validated
    
    Returns
    -------
    boolean
        True if the URL uses a valid scheme, False otherwise
    """
    if "://" not in url:
        return False
    scheme_split = url.split("://")
    if len(scheme_split) != 2:
        return False
    
    scheme = scheme_split[0]
    if not(scheme == "http") and not (scheme == "https"):
        return False
    
    # host_and_the_rest = scheme_split[1]
    # host_and_the_rest_split = host_and_the_rest.split("/")

    return True


def gather_input():
    """Gather input from the command line and exit if input is incorrect
    
    Parameters
    ----------
    None

    Returns
    -------
    string
        URL received from command line argument
    """
    if len(sys.argv) != 2:
        print("Error: Did not supply proper arguments")
        print_usage()
        logging.error("Did not supply proper arguments. Arguments supplied: " + str(sys.argv))
        exit(1)
    url = sys.argv[1]

    if not validate_url(url):
        print("Error: URL provided is not a valid URL")
        print("Valid URL: <scheme>://<host>:<port>/[path]")
        print("Scheme must be http or https")
        logging.error("URL provided not valid: " + url)
        exit(1)
    return url


def configure_logger():
    """Configure the logger
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    logging.basicConfig(level=logging.DEBUG, filemode='a', format='%(asctime)s - [%(levelname)s] - %(message)s', filename='HTTPClient.log')


def print_external_references(external_references):
    """Prints external references passed in
    
    Parameters
    ----------
    external_references : list
        External references to be printed

    Returns
    -------
    Nothing
    """
    pass

def main():
    configure_logger()
    url = gather_input()
    web_page = ConnectionUtils.get_page(url)
    external_references = Parser.parse_page_for_external_references(web_page)
    print_external_references(external_references)


main()