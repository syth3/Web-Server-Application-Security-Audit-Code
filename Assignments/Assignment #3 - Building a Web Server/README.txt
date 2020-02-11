Dependencies, compilers/interpreters, and development environments that are necessary to run my code:
 - There is only one dependency for my code, Python 3.x must be installed. Other than Python, there are no additional dependencies to download. This code was tested on Python 3.8.1

How to run my code:
 Usage: HTTP_Server.py ip_address port [x509_path] [x509_private_key_path]
 Below are two examples to run my code. The first is to setup a HTTP server, and the second is to setup a HTTPS server.
 If you want to run a HTTPS server, you must supply both the x509_path and x509_private_key_path parameters
 - Example:
   sudo python3 HTTP_Server.py 0.0.0.0 80
   sudo python3 HTTP_Server.py 0.0.0.0 80 demo.crt demo.key

Note: 
 - In Windows, you may need to substitute "python3" for "python" in the terminal command