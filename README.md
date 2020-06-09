# ansible_project_2020
automating administration, configuration &amp; deployment of linux-based systems using ansible 
### whats ansible ? ###
A config mngt system, that's agentless (no agent software is needed in the managed nodes). The software only need to be installed on the controller. using playbooks we can configure managed nodes to the desired state when ansible executes & leverages SSH to communicate between servers. Modules are programs that perform the actual work of the tasks of a play. 
to summarise, its basically an open source automation platform that makes your apps & systems easier to deploy, it can help you with config mngt, apps deployment & task automation

## Limitations ##
ansible cant install an OS, you'd have to do that with kickstart then use ansible to add packages etc
ansible does not track what changes are made to files on a system, not does it track what user or process
made those changes

## architecture ##
host inventory file: list of clients you're going to manage
modules: ansible comes with 100s of modules that get executed when you run a playbook and taks include your modules
ansible.cfg: main ansible config file that contains stuffs like your remote users, privileges & your inventory etc.
Playbooks: describe automation jobs and playbook uses a very simple language YAML.


## my set up ##
2x centos VMs + 1x ubuntu VM. one master and two slaves. the master connect to the hosts using passwordless ssh. 
required packages needed on the crontroller:
sudo yum install epel-release -y
sudo yum install ansible -y 

## projects ##
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

## useful commands ##
some useful ansible ad-hoc commands i used & came accross for troubleshooting purposes :
- ansible-playbook <playbook_name> --syntax-check: check for syntax & other errors in the playbook

- ansible --version: shows you the version and main config file localtion

- ansible-config view: show content of your .ansible.cfg file

- ansible-config list: show all config 

- ansible-config dump: show current config 

- ansible-config dump --only-changed ==> show only non default configs

- tree: display the content of a directory in a tree-like format

- ansible all --list-hosts: list the ip adresses of all managed nodes

- ansible-galaxy init roles/<name_of_your_role>: create a role e.g apche, php, mariadb etc. 

- ansible <group> -m ping: check all connected hosts connectivity
  
- ansible <group> -m yum -a “name= httpd state=absent”: Check if package is not installed
  

