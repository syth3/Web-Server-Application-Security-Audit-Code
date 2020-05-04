'''
file: HTTP_Server.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Start a HTTP server
'''

import sys
import logging
from pathlib import Path
import Connection_Utils
import Response_Codes


def print_usage():
    """Print the usage message of this script
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    print("Usage: HTTP_Server.py ip_address port [x509_path x509_private_key_path]")


def gather_input():
    """Gather input from the command line and exit if input is incorrect
    
    Parameters
    ----------
    None

    Returns
    -------
    dict
        Dictionary of input arguments and their values
    """
    arg_dict = {}

    # HTTP connection
    if len(sys.argv) == 3:
        ip_address = sys.argv[1]
        port = sys.argv[2]
        arg_dict["ip_address"] = ip_address
        arg_dict["port"] = int(port)
        arg_dict["scheme"] = "http"
    # HTTPS connection
    elif len(sys.argv) == 5:
        ip_address = sys.argv[1]
        port = sys.argv[2]
        x509_path = Path(sys.argv[3])
        if not(x509_path.exists()):
            print_usage()
            exit(1)
        x509_private_key_path = Path(sys.argv[4])
        if not(x509_private_key_path.exists()):
            print_usage()
            exit(1)
        arg_dict["ip_address"] = ip_address
        arg_dict["port"] = int(port)
        arg_dict["x509_path"] = x509_path
        arg_dict["x509_private_key_path"] = x509_private_key_path
        arg_dict["scheme"] = "https"
    # Improper arguments
    else:
        print_usage()
        exit(1)
    
    return arg_dict


def main():
    args = gather_input()
    try:
        Connection_Utils.start_server(args)
    except Exception:
        Response_Codes.respond_with_500()


main()