import Response_Codes

def process_GET():
    print("Inside GET")
    return Response_Codes.respond_with_200()


def process_POST():
    print("Inside POST")
    return Response_Codes.respond_with_200()


def process_PUT():
    print("Inside PUT")
    return Response_Codes.respond_with_200()


def process_DELETE():
    print("Inside DELETE")
    return Response_Codes.respond_with_200()


def process_HEAD():
    print("Inside HEAD")
    return Response_Codes.respond_with_200()