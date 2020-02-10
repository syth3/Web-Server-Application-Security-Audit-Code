import socket
import ssl
import threading
import HTTP_Parser
import Response_Codes
import Process_Request_Methods


NUM_CONCURRENT_CONNECTIONS = 5


def handler(sock):
    # Process all request methods
    response = ""
    try:
        request = get_request(sock)
        parsed_request = HTTP_Parser.parse_request(request)
        HTTP_Parser.print_parsed_request(parsed_request)

        if parsed_request["response_code"] != 200:
            response = return_http_code(parsed_request["response_code"])
        else:
            response = execute_method(parsed_request["method"])
    except Exception:
        response = Response_Codes.respond_with_500()

    sock.send(response.encode())
    sock.close()


def return_http_code(response_code):
    if response_code == "400":
        return Response_Codes.respond_with_400()
    elif response_code == "501":
        return Response_Codes.respond_with_501()
    elif response_code == "505":
        return Response_Codes.respond_with_505()


def execute_method(method):
    response = ""
    if method == "GET":
        response = Process_Request_Methods.process_GET()
    elif method == "POST":
        response = Process_Request_Methods.process_POST()
    elif method == "PUT":
        response = Process_Request_Methods.process_PUT()
    elif method == "DELETE":
        response = Process_Request_Methods.process_DELETE()
    elif method == "HEAD":
        response = Process_Request_Methods.process_HEAD()
    
    return response
    

def get_request(sock):
    # request = ""
    # data = str(sock.recv(1024))
    # while data != "":
    #     data = str(sock.recv(1024))
    #     if not data:
    #         break
    #     request += data
    
    return str(sock.recv(1024))


def start_server(input_args):
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind((input_args["ip_address"], input_args["port"]))
    srv_sock.listen(NUM_CONCURRENT_CONNECTIONS)

    while True:
        conn_sock, addr = srv_sock.accept()
        # conn_sock.send(Response_Codes.respond_with_200().encode())
        if input_args["scheme"] == "https":
            conn_sock = create_tls_socket(conn_sock, input_args["x509_path"], input_args["x509_private_key_path"])
        t = threading.Thread(target=handler, args=(conn_sock,))
        t.start()


def create_tls_socket(conn_sock, cert_file, key_file):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_OPTIONAL
    context.load_cert_chain(certfile=cert_file, keyfile=key_file, password=None)

    return context.wrap_socket(conn_sock, server_side=True)
