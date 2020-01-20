'''
file: ConnectionUtils.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Parses a web page using only string libraries. Used by HTTPClient.py
'''


def validate_url(url):
    """Validate that the URL meets some basic criteria
    
    Parameters
    ----------
    url : string
        URL to be validated
    
    Returns
    -------
    boolean
        True if URL meets criteria, False otherwise
    """
    if len(url) == 0:
        return False
    if url[0] == "/":
        return False
    if "http://" not in url and "https://" not in url and "www" not in url:
        return False
    return True


def clean_url(url):
    """Clean the URL given to just the scheme and host portion
    
    Parameters
    ----------
    url : string
        URL to be cleaned
    
    Returns
    -------
    string
        Cleaned URL
    """
    url = url.replace("\\", "")

    # Grab data between first quote and last quote
    first_quote = url.find('"')
    last_quote = url.rfind('"')
    url = url[first_quote + len('"'):last_quote]
    
    if "'" in url:
        if url[0] == "'":
            url = url[1:]

    scheme = ""
    everything_but_scheme = ""

    if "://" in url:
        scheme = url.split("://")[0]
        everything_but_scheme = url.split("://")[1]
    if len(scheme) > 5:
        if "https" in scheme:
            scheme = "https"
        else:
            scheme = "http"

    if ":" in everything_but_scheme:
        everything_but_scheme = everything_but_scheme.split(":")[0]
    if "/" in everything_but_scheme:
        everything_but_scheme = everything_but_scheme.split("/")[0]
    if "?" in everything_but_scheme: 
        everything_but_scheme = everything_but_scheme.split("?")[0]

    if len(scheme) == 0:
        url = everything_but_scheme
    else:
        url = scheme + "://" + everything_but_scheme
    
    return url


def extract_url(attribute, data):
    """Extract a URL from the data given
    
    Parameters
    ----------
    attribute : string
        Attribute being looked at
    data : string
        Data attached to the attribute tag given
    
    Returns
    -------
    list
        List of URLs found
    """
    urls_found = []
    for search_text in data.split(" "):
        if attribute + "=" in search_text:
            url = search_text[search_text.find(attribute) + len(attribute) + 1:]
            if validate_url(url):
                url = clean_url(url)
                if not(len(url) == 0):
                    urls_found.append(url)
    return urls_found


def parse_web_page_for_external_references(web_page):
    """Parse a web page and extract external urls
    
    Parameters
    ----------
    web_page : string
        web page to be parsed
    
    Returns
    -------
    set
        Set of external references
    """
    unique_urls_set = set()
    attributes_of_interest = [
        "action", 
        "background",
        "cite",
        "code",
        "codebase",
        "data",
        "href",
        "manifest",
        "poster",
        "src",
        "srcset",
        "value"
        ]
    web_page = web_page.replace("><", ">\n<")

    for data in web_page.split("\n"):
        for attribute in attributes_of_interest:
            if attribute + "=" in data:
                urls_found = extract_url(attribute, data)
                for url in urls_found:
                    unique_urls_set.add(url)

    return sorted(unique_urls_set)
