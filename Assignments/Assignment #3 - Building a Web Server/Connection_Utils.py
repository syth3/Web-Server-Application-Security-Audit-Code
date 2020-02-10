import socket
import ssl
import threading

NUM_CONCURRENT_CONNECTIONS = 5


def handler(sock, parsed_request):
    # Process all request methods
    pass


def start_server(input_args):
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind((input_args["ip_address"], input_args["port"]))
    srv_sock.listen(NUM_CONCURRENT_CONNECTIONS)

    while True:
        conn_sock, addr = srv_sock.accept()
        if input_args["scheme"] == "https":
            conn_sock = create_tls_socket(conn_sock, input_args["x509_path"], arg_dict["x509_private_key_path"])
        t = threading.Thread(target=handler, args=(conn_sock))


def create_tls_socket(conn_sock, cert_file, key_file):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_OPTIONAL
    context.load_cert_chain(certfile=cert_file, keyfile=key_file, password=None)

    return context.wrap_socket(conn_sock, server_side=True)

