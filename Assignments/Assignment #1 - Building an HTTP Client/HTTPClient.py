import sys
import logging



def print_usage():
    print("Usage: HTTPClient.py URL")


def validate_url(url):
    scheme_split = url.split("://")
    if len(scheme_split) != 2:
        print("len(scheme_split) not enough")
        return False
    
    scheme = scheme_split[0]
    if not(scheme == "http") and not (scheme == "https"):
        print("scheme not http or https")
        return False
    
    host_and_the_rest = scheme_split[1]
    host_and_the_rest_split = host_and_the_rest.split("/")

    return True

def gather_input():
    if len(sys.argv) != 2:
        print("Error: Did not supply proper arguments")
        print_usage()
        logging.error("Did not supply proper arguments. Arguments supplied: " + str(sys.argv))
    url = sys.argv[1]
    if not validate_url(url):
        print("Error: URL provided is not a valid url")
        print("Valid URL: <scheme>://<host>:<port>/[path]")
        print("Scheme must be http or https")
        logging.error("URL provided not valid: " + url)
    return url

def configure_logger():
    logging.basicConfig(level=logging.DEBUG, filemode='a', format='%(asctime)s - [%(levelname)s] - %(message)s', filename='HTTPClient.log')


def main():
    configure_logger()
    url = gather_input()


main()