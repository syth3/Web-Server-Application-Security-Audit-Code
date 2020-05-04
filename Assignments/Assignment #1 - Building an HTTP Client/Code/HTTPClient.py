'''
file: HTTPClient.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: HTTP Client that will take in a URL and print external links on the HTML page returned from the URL
    Note: This code only uses the socket library for HTTP communication and basic string parsing libraries for
          HTML parsing
'''

import sys
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
    """Validate that a URL has a scheme and that is either http or https
    
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
        exit(1)
    url = sys.argv[1]

    if not validate_url(url):
        print("Error: URL provided is not a valid URL")
        print("Valid URL: <http/https>://<host>:[port]/[path]")
        print("Note: Please include www if you did not")
        exit(1)
    return url


def print_external_references(unique_external_references, original_url):
    """Prints external references passed in
    
    Parameters
    ----------
    unique_external_references : list
        External references to be printed

    Returns
    -------
    Nothing
    """
    for reference in unique_external_references:
        # pass
        if not(reference == original_url):
            print(reference)
    print()
    print("**********************************************")
    if original_url in unique_external_references:
        print("Unique External References Found:", len(unique_external_references) - 1)
    else:
        print("Unique External References Found:", len(unique_external_references))
    print("**********************************************")
    # print("Total Links:", total_external_references_count)


def print_response_headers_and_exit(http_code, response_headers):
    """Print the response headers and exit the program
    
    Parameters
    ----------
    http_code : int
        HTTP code from the response
    response_headers : string
        Headers returned that will be printed
    
    Returns
    -------
    Nothing
    """
    print("Problem encountered. See response headers below:")
    print()
    print(response_headers)
    exit(1)


def main():
    url = gather_input()
    web_page, http_code, response_headers = ConnectionUtils.get_page(url)
    if not(http_code == 200):
        print(type(http_code))
        print_response_headers_and_exit(http_code, response_headers)
    unique_external_references = Parser.parse_web_page_for_external_references(web_page)
    print_external_references(unique_external_references, url)


main()