import Response_Codes
from pathlib import Path

def process_GET(parsed_request):
    curr_dir = Path.cwd()
    file_name = Path(parsed_request["request_uri"])
    path = curr_dir / "Resources"
    path = Path(str(path) + str(file_name))

    if not path.exists():
        return Response_Codes.respond_with_404()

    try:
        path.open()
    except PermissionError:
        return Response_Codes.respond_with_403()
    
    return Response_Codes.respond_with_200(path.read_text())


def process_POST(parsed_request):
    curr_dir = Path.cwd()
    file_name = Path(parsed_request["request_uri"])
    path = curr_dir / "Resources"
    path = Path(str(path) + str(file_name))

    if not path.exists():
        return Response_Codes.respond_with_404()

    try:
        path.open()
    except PermissionError:
        return Response_Codes.respond_with_403()
    
    return_body = "Body passed in:\n" + parsed_request["body"] + "\n\nFile Contents:\n" + path.read_text()
    return Response_Codes.respond_with_200(return_body)


def process_PUT(parsed_request):
    return Response_Codes.respond_with_200("")


def process_DELETE(parsed_request):
    return Response_Codes.respond_with_200("")


def process_HEAD(parsed_request):
    return Response_Codes.respond_with_200("")