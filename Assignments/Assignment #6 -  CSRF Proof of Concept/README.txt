 Installing necessary dependencies:
 - Execute the install.sh script and provide your sudo password. This will install apache2 and libapache2-mod-php

How to execute my code:
 1. Install dependencies using install.sh script
 2. Move my php and html files enclosed in the zip file to the /var/www/html directory
 3. Create two additional files in /var/www/html: username.txt and password.txt
     - Set the permissions of both of these files to -rw-rw-rw-
 4. Enter a username in username.txt and a password in password.txt
     - This will act as the only user for my application

Install.sh Script:
#!/bin/bash

sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-php -y
