FROM ubuntu:18.04
RUN apt-get update
ENV TZ=America/Rochester
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 php libapache2-mod-php
    
RUN service apache2 start

COPY vuln.php /var/www/html/
COPY apache2.conf /etc/apache2/apache2.conf
COPY 000-default.conf /etc/apache2/sites-enabled/

COPY startup.sh /usr/local/bin/startup.sh
RUN chmod +x /usr/local/bin/startup.sh

RUN service apache2 restart

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/usr/local/bin/startup.sh"]