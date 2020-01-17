'''
file: ConnectionUtils.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Parses a web page using only string libraries. Used by HTTPClient.py
'''


def validate_url(url):
    if len(url) == 0:
        # print("\tLength of URL is zero")
        return False
    if url[0] == "/":
        # print("\tURL Starts with a /")
        return False
    if "http://" not in url and "https://" not in url and "www" not in url:
        # print("\thttp(s):// and www not in the URL")
        # print("\tThe URL is:", url)
        return False
    return True


def clean_url(url):
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

    if ":" in everything_but_scheme:
        everything_but_scheme = everything_but_scheme.split(":")[0]
    else:
        everything_but_scheme = everything_but_scheme.split("/")[0]

    if len(scheme) == 0:
        url = everything_but_scheme
    else:
        url = scheme + "://" + everything_but_scheme
    # print("Scheme:", scheme)
    # print("Everything but scheme:", everything_but_scheme)
    return url
    # return scheme + "://" + everything_but_scheme


def extract_url(attribute, data):
    urls_found = []
    for search_text in data.split(" "):
        if attribute + "=" in search_text:
            # print("search_text:", search_text)
            # print("Attribute:", attribute)
            url = search_text[search_text.find(attribute) + len(attribute) + 1:]
            # print("Passing URL to validated:", url)
            if validate_url(url):
                # print("URL validation SUCCESS")
                # print("Cleaning URL:", url)
                url = clean_url(url)
                # print("Cleaned URL:", url)
                if not(len(url) == 0):
                    urls_found.append(url)
            # else:
                # print("URL validation FAILURE")
            # print()
    return urls_found


def parse_web_page_for_external_references(web_page):
    """Parse a web page and extract external urls
    
    Parameters
    ----------
    web_page : string
        web page to be parsed
    
    Returns
    -------
    list
        list of external references
    """
    unique_url_count = 0
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
    # # print(web_page)
    web_page = web_page.replace("><", ">\n<")

    for data in web_page.split("\n"):
        for attribute in attributes_of_interest:
            # # print("Checking:", attribute)
            if attribute + "=" in data:
                # print("---------------------Attribute Found---------------------")
                urls_found = extract_url(attribute, data)
                for url in urls_found:
                    unique_urls_set.add(url)

    # # print("Unique URLs:", len(unique_urls_set))

    return sorted(unique_urls_set)
