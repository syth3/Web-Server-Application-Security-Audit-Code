Dependencies, compilers/interpreters, and development environments that are necessary to run my code:
 - There is only one dependency for my code, Python 3.x must be installed. Other than Python, there are no additional dependencies to download. This code was tested on Python 3.8.1

How to run my code:
 Usage: HTTP_Server.py ip_address port
 Below is an example of how to run my code.
 - Example:
   sudo python3 HTTP_Server.py 0.0.0.0 80

Note: 
 - In Windows, you may need to substitute "python3" for "python" in the terminal command
 - Please put all resources for your webserver in a Resources directory at the same level as the code
   An example has been submitted with the code
   To make the exampled work, try the following two requests:
     - GET request made to /Test-Nested-Directories/getdemo.php?first=Jake&last=Brown
     - POST request made to /Test-Nested-Directories/Second-Level/postdemo.php with a body of first=Jake&last=Brown
