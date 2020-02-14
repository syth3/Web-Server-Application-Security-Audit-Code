class Parsed_Request:

    def __init__(self):
        self._body = ""
        self._headers = []
        self._http_version = ""
        self._method = ""
        self._response_code = 200
        self._request_uri = ""
    

    def set_body(self, body):
        self._body = body


    def get_body(self):
        return self._body


    def set_header(self, header_name, header_value):
        header_tuple = (header_name, header_value)
        self._headers.append(header_tuple)
    

    def get_headers(self):
        return self._headers

    
    def set_http_version(self, http_version):
        self._http_version = http_version


    def get_http_version(self):
        return self._http_version

    
    def set_method(self, method):
        self._method = method

    
    def get_method(self):
        return self._method

    
    def set_response_code(self, response_code):
        self._response_code = response_code

    
    def get_response_code(self):
        return self._response_code
    

    def set_request_uri(self, request_uri):
        self._request_uri = request_uri
    

    def get_request_uri(self):
        return self._request_uri


    def print_parsed_request(self):
        print("Response Code:", self.get_response_code())
        print("Method:", self.get_method())
        print("HTTP Version:", self.get_http_version())
        print("Request URI:", self.get_request_uri())
        print("Headers:")
        for header in self.get_headers():
            print("  - " + header[0] + ": " + header[1])
        print("Body:", self.get_body())