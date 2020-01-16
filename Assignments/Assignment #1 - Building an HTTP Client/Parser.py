'''
file: ConnectionUtils.py
language: python3
author: Jacob Brown jmb7438@rit.edu
description: Parses a web page using only string libraries. Used by HTTPClient.py
'''


def parse_host_from_url(url):
    # print(url)
    try:
        if url[0] == "/":
            return None
    except:
        print("Found execption with: \"" +  url + "\"")
    everything_but_scheme = url
    if "://" in everything_but_scheme:
        everything_but_scheme = url.split("://")[1]
    host = ""
    if ":" in everything_but_scheme:
        host = everything_but_scheme.split(":")[0]
    else:
        host = everything_but_scheme.split("/")[0]
    
    if "www" in host:
        host = host.split("www.")[1]
    # print(host)
    return host


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
    total_link_count = 0
    unique_link_count = 0
    unique_links_set = set()


    web_page = web_page.replace("><", ">\n<")

    # print("Total Links:", total_link_count)
    # print("Unique Links:", unique_link_count)
    return unique_links_set, unique_link_count, total_link_count


def extract_link(match):
    hyperlink_start_position = match.find('href="') + len('href="')
    first_half_string = match[hyperlink_start_position:]
    hyperlink_end_position = first_half_string.find('"')
    return first_half_string[:hyperlink_end_position]


# parse_host_from_url("https://www.facebook.com")
# parse_host_from_url("https://www.facebook.com:80")
# parse_host_from_url("https://www.facebook.com/test/test2")
# parse_host_from_url("https://www.facebook.com:80/test/test2")
# parse_host_from_url("/test/test2")
# parse_host_from_url("www.facebook.com")
# parse_host_from_url("www.facebook.com:80")
# parse_host_from_url("www.facebook.com/test/test2")
# parse_host_from_url("www.facebook.com:80/test/test2")
# parse_host_from_url("www.domain.facebook.com")
# parse_host_from_url("www.domain.facebook.com:80")
# parse_host_from_url("www.domain.facebook.com/test/test2")
# parse_host_from_url("www.domain.facebook.com:80/test/test2")
# parse_host_from_url("facebook.com")
# parse_host_from_url("facebook.com:80")
# parse_host_from_url("facebook.com/test/test2")
# parse_host_from_url("facebook.com:80/test/test2")
