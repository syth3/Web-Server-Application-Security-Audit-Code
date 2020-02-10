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
    # Check that the Content-Length header is present
    found_content_length = False
    for header in parsed_request["headers"]:
        if header[0].lower() == "content-length":
            found_content_length = True

    if not found_content_length:
        return Response_Codes.respond_with_411()

    #Process POST request
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
    curr_dir = Path.cwd()
    file_name = Path(parsed_request["request_uri"])
    path = curr_dir / "Files"
    path = Path(str(path) + str(file_name))
    
    body = parsed_request["body"]
    path.write_text(body)

    return Response_Codes.respond_with_201(body, str(file_name))


def process_DELETE(parsed_request):
    curr_dir = Path.cwd()
    file_name = Path(parsed_request["request_uri"])
    path = curr_dir / "Files"
    path = Path(str(path) + str(file_name))

    path.unlink()

    return Response_Codes.respond_with_200("")


def process_HEAD(parsed_request):
    return Response_Codes.respond_with_200("")