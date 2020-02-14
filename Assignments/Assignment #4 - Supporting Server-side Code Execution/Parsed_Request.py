class Parsed_Request:

    def __init__(self):
        self.body = ""
        self.headers = []
        self.http_version = ""
        self.method = ""
        self.response_code = 200
        self.request_uri = ""
    
    def add_header(self, header_name, header_value):
        header_tuple = (header_name, header_value)
        self.headers.append(header_tuple)

    def print_parsed_request(self):
        print("Response Code:", self.response_code)
        print("Method:", self.method)
        print("HTTP Version:", self.http_version)
        print("Request URI:", self.request_uri)
        print("Headers:")
        for header in self.headers:
            print("  - " + header[0] + ": " + header[1])
        print("Body:", self.body)