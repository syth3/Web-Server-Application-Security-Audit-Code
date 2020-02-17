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
import Input_Args


def print_usage():
    """Print the usage message of this script
    
    Parameters
    ----------
    None

    Returns
    -------
    Nothing
    """
    # print("Usage: HTTP_Server.py ip_address port [x509_path x509_private_key_path]")
    print("Usage: HTTP_Server.py ip_address port")


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
    input_args = Input_Args.Input_Args()

    # HTTP connection
    if len(sys.argv) == 3:
        ip_address = sys.argv[1]
        port = sys.argv[2]

        input_args.set_ip_address(ip_address)
        input_args.set_port(int(port))
        input_args.set_scheme("http")

    # HTTPS connection
    # Note: this section is commented out because of the requirements for the assignment
    # elif len(sys.argv) == 5:
    #     ip_address = sys.argv[1]
    #     port = sys.argv[2]
    #     x509_path = sys.argv[3]
    #     x509_private_key_path = sys.argv[4]

    #     input_args.set_ip_address(ip_address)
    #     input_args.set_port(int(port))
    #     input_args.set_scheme("https")
    #     input_args.set_x509_path(x509_path)
    #     input_args.set_x509_private_key_path(x509_private_key_path)

    #     if input_args.get_x509_path == "invalid" or input_args.get_x509_path_private_key == "invalid":
    #         print_usage()
    #         exit(1)

    # Improper arguments
    else:
        print_usage()
        exit(1)
    
    return input_args


def main():
    input_args = gather_input()
    Connection_Utils.start_server(input_args)
    # input_args.print_input_args()
    # try:
    #     Connection_Utils.start_server(input_args)
    # except Exception:
    #     Response_Codes.respond_with_500()


main()