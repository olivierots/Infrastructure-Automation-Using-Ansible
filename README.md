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

some useful ansible ad-hoc commands i used & came accross for troubleshooting purposes :
-ansible-playbook <playbook_name> --syntax-check: check for syntax & other errors in the playbook

-ansible --version: shows you the version and main config file localtion

-ansible-config view: show content of your .ansible.cfg file
-ansible-config list: show all config 
-ansible-config dump: show current config 
-ansible-config dump --only-changed ==> show only non default configs
-tree: display the content of a directory in a tree-like format
-ansible all --list-hosts: list the ip adresses of all managed nodes
-ansible-galaxy init roles/<name_of_your_role>: create a role e.g apche, php, mariadb etc. 
-ansible <group> -m ping: check all connected hosts connectivity
-ansible <group> -m yum -a “name= httpd state=absent”: Check if package is not installed
  

