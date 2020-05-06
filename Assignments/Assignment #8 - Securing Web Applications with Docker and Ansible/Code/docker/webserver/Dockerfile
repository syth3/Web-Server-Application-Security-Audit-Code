FROM ubuntu:18.04

# Install Packages
RUN apt-get update
ENV TZ=America/Rochester
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 php libapache2-mod-php

# Setup files for apache
COPY vuln.php /var/www/html/
COPY apache2.conf /etc/apache2/apache2.conf
COPY 000-default.conf /etc/apache2/sites-enabled/
RUN a2enmod ssl
COPY security.conf /etc/apache2/conf-enabled/security.conf
COPY priv.pem /etc/apache2/
COPY pubcert.pem /etc/apache2/

COPY startup.sh /usr/local/bin/startup.sh
RUN chmod +x /usr/local/bin/startup.sh

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/usr/local/bin/startup.sh"]