import Response_Codes
from pathlib import Path

def process_GET(parsed_request):
    curr_dir = Path.cwd()
    file_name = Path(parsed_request["request_uri"])
    path = curr_dir / "Resources"
    path = Path(str(path) + str(file_name))
    print("PATH TO BE FETCHED:", path)

    if not path.exists():
        return Response_Codes.respond_with_404()

    try:
        path.open()
    except PermissionError:
        return Response_Codes.respond_with_403()
    
    file_contents = ""
    with path.open(mode='r') as read_file:
        file_contents += path.read_text()

    return Response_Codes.respond_with_200(file_contents)


def process_POST(parsed_request):
    return Response_Codes.respond_with_200("")


def process_PUT(parsed_request):
    return Response_Codes.respond_with_200("")


def process_DELETE(parsed_request):
    return Response_Codes.respond_with_200("")


def process_HEAD(parsed_request):
    return Response_Codes.respond_with_200("")