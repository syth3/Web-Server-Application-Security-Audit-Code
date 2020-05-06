FROM ubuntu:18.04
RUN apt-get update
ENV TZ=America/Rochester
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git apache2  libapache2-mod-security2

# Setup files for apache
RUN a2enmod proxy
RUN a2enmod proxy_http
COPY apache2.conf /etc/apache2/apache2.conf
COPY 000-default.conf /etc/apache2/sites-enabled/

RUN service apache2 start

# Setup Modsecurity
COPY modsecurity.conf /etc/modsecurity/modsecurity.conf
RUN service apache2 restart
RUN mv /usr/share/modsecurity-crs /usr/share/modsecurity-crs.bk
RUN git clone https://github.com/SpiderLabs/owasp-modsecurity-crs.git /usr/share/modsecurity-crs
RUN cp /usr/share/modsecurity-crs/crs-setup.conf.example /usr/share/modsecurity-crs/crs-setup.conf
COPY security2.conf /etc/apache2/mods-available/security2.conf

COPY startup.sh /usr/local/bin/startup.sh
RUN chmod +x /usr/local/bin/startup.sh

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/usr/local/bin/startup.sh"]