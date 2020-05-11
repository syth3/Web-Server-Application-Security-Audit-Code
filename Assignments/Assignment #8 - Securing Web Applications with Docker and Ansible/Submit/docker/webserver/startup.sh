#! /bin/bash
set -e

printf "\n---> Starting the Apache server.\n"

/etc/init.d/apache2 start
/etc/init.d/apache2 status

tail -f /dev/null