# ansible_project_2020
automating administration, configuration &amp; deployment of linux-based systems using ansible 
### whats ansible ? ###
A config mngt system, that's agentless (no agent software is needed in the managed nodes). The software only need to be installed on the controller. using playbooks we can configure managed nodes to the desired state.

set up: 2x centos VMs + 1x ubuntu VM. one master and two slaves. the master connect to the hosts using passwordless ssh. 
required packages needed on the crontroller:
sudo yum install epel-release -y
sudo yum install ansible -y 

Below are some of the interesting fun stuffs i've done & learnt:

*  configured & deployed apache web server to remote machines
*  used ansible roles to install, configure & deploy PHP & MariaDB
*  configured & proviosnned my AWS instance
*  managed storage: partititonning, volume group, lvm, file systems & mount points etc.
*  scheduled tasks using ansible 
*  data encription using ansible vault & SSH config
*  user accounts management 
*  defining handlers refenced in playbooks
*  working with files and templates

some useful ansible ad-hoc commands i've come accross used for troubleshooting purposes :
ansible-playbook <playbook_name> --syntax-check: check for syntax & other errors in the playbook
ansible --version: shows you the version and main config file localtion
ansible-config view: show content of your .ansible.cfg file
ansible-config list: show all config 
ansible-config dump: show current config 
ansible-config dump --only-changed ==> show only non default configs
tree: display the content of a directory in a tree-like format
ansible all --list-hosts: list the ip adresses of all managed nodes
ansible-galaxy init roles/<name_of_your_role>: create a role e.g apche, php, mariadb etc. 
ansible <group> -m ping: check all connected hosts connectivity
ansible <group> -m yum -a “name= httpd state=absent”: Check if package is not installed
  

[jenkins@olivier-linux-server ansible]$ tree
.
├── files
│   ├── apache.yml.backup
│   ├── configure_apache_on_localhost.yml
│   ├── host_vars
│   │   └── 192.168.1.85
│   ├── inventory
│   ├── manage_ssh_service.yml
│   └── motd.j2
├── lamp
│   ├── apache.deployment.to.ubuntu.and.centos.yml
│   ├── apache.install.simple.yml
│   ├── apache.install.using.logic.simple.yml
│   ├── aws_ec2_provision.yml
│   ├── deploy.lamp.stack.mariadb.using.roles.yml
│   ├── group_vars
│   │   ├── centos
│   │   └── ubuntu
│   ├── host_vars
│   ├── inventory
│   └── roles
│       ├── apache
│       │   ├── apache
│       │   ├── defaults
│       │   │   └── main.yml
│       │   ├── files
│       │   ├── handlers
│       │   │   ├── apache
│       │   │   └── main.yml
│       │   ├── meta
│       │   │   └── main.yml
│       │   ├── README.md
│       │   ├── tasks
│       │   │   ├── apache
│       │   │   └── main.yml
│       │   ├── templates
│       │   ├── tests
│       │   │   ├── inventory
│       │   │   └── test.yml
│       │   └── vars
│       │       └── main.yml
│       ├── mariadb
│       │   ├── defaults
│       │   │   └── main.yml
│       │   ├── files
│       │   ├── handlers
│       │   │   └── main.yml
│       │   ├── meta
│       │   │   └── main.yml
│       │   ├── README.md
│       │   ├── tasks
│       │   │   └── main.yml
│       │   ├── templates
│       │   ├── tests
│       │   │   ├── inventory
│       │   │   └── test.yml
│       │   └── vars
│       │       └── main.yml
│       └── php
│           ├── defaults
│           │   └── main.yml
│           ├── files
│           │   └── index.php
│           ├── handlers
│           │   └── main.yml
│           ├── meta
│           │   └── main.yml
│           ├── README.md
│           ├── tasks
│           │   └── main.yml
│           ├── templates
│           ├── tests
│           │   ├── inventory
│           │   └── test.yml
│           └── vars
│               └── main.yml
├── README.md
├── storage
│   ├── disk.partition.configure.storage.localhost.yml
│   └── inventory
└── users
    ├── create.devops.account.yml
    ├── create.new.user.using.vault.encryption.yml
    ├── create.user.account.simple.yml
    ├── group_vars
    ├── host_vars
    │   └── 192.168.56.2
    ├── inventory
    ├── make_password.py
    ├── private.yml
    └── schedule.tasks.using.cron.yml

