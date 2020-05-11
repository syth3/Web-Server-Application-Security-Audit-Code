Command to execute my playbook: ansible-playbook playbook.yml --ask-pass --ask-become

Important Notes:
 - This command does not require authentication keys or anything of the like to be set up to run the playbook.
 - This command assumes that the file located at /etc/ansible/hosts contains the IP address of your target(s)
 - It is very important that the the directory structure be as follows:
    .
    ├── docker
    │   ├── modsecurity
    │   └── webserver
    └── playbook.yml
