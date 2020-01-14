'''
file: ConnectionUtils.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Parses a web page using only string libraries. Used by HTTPClient.py
'''


def validate_external_link(link):
    return True


def parse_web_page_for_external_references(web_page):
    """Parse a web page and extract external links
    
    Parameters
    ----------
    web_page : string
        web page to be parsed
    
    Returns
    -------
    list
        list of external references
    """
    links = 0
    # web_page.replace("\n", " ")
    web_page.replace("\r", " ")
    web_page.replace("\t", " ")
    for part in web_page.split("\n"):
        if "<link" in part:
            print(part.strip())
            links += 1
    print("Total Links:", links)
    return []
