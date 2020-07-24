=======
```
=== Project description ===
Automating the administration & configuration of LAMP using ansible
Deployment of linux-based systems using ansible
kernel patching using ansible
```

```
=== Whats ansible ? ===
A config mngt system, that's agentless (no agent software is needed in the managed nodes). The software only need 
to be installed on the controller. using playbooks we can configure managed nodes to the desired state when ansible 
executes & leverages SSH to communicate between servers. Modules are programs that perform the actual work of the
tasks of a play, Ansible executes each module, usually on the remote target node, and collects return values.. 
to summarise, its basically an open source automation platform that makes your apps & systems easier to deploy, it
can help you with config mngt, apps deployment & task automation.
```

```
=== Ansible limitations ===
ansible cant install an OS, you'd have to do that with kickstart then use ansible to add packages etc
ansible does not track what changes are made to files on a system, nor does it track what user or process
made those changes
```

```
=== Ansible architecture ===
* host inventory file: list of clients you're going to manage
* modules: ansible comes with 100s of modules that get executed when you run a playbook and taks include your modules
           They are reusable, standalone scripts that can be used by the Ansible API, or by ansible-playbook 
           programs e.g yum, service, copy, lineinfile etc.
* ansible.cfg: main ansible config file that contains stuffs like your remote users, privileges & your inventory etc.
* playbooks: describe automation jobs and playbook uses a very simple language YAML.
* roles: roles are ways of splitting ansible tasks into files which are easier to manipulate with. 
```

```
== My set up ==
2x centos VMs + 1x ubuntu VM. one master and two slaves. the master connect to the hosts using passwordless ssh. 
required packages needed on the crontroller:
sudo yum install epel-release -y
sudo yum install ansible -y 
```

```
=== Tasks ===
Below are some of the interesting fun stuff i've done & learnt:

*  configured & deployed apache web server to remote machines
*  used ansible roles to install, configure & deploy PHP & MariaDB
*  configured & proviosnned my AWS instance
*  managed storage: partititonning, volume group, lvm, file systems & mount points etc.
*  scheduled tasks using ansible 
*  data encription using ansible vault & SSH config
*  user accounts management 
*  defining handlers refenced in playbooks
*  working with files and templates
*  kernel upgrade
```

```
=== below are some useful commands i've learnt & used throughout my learning path ===
some useful ansible ad-hoc commands i used & came accross for troubleshooting purposes :
- ansible-playbook <playbook_name> --syntax-check: check for syntax & other errors in the playbook
- ansible --version: shows you the version and main config file localtion
- ansible-config view: show content of your .ansible.cfg file
- ansible-config list: show all config 
- ansible-config dump: show current config 
- ansible-config dump --only-changed ==> show only non default configs
- ansible -m ping <your_server_group> ==> ping a group of servers defined in your inventory
- tree: display the content of a directory in a tree-like format
- ansible all --list-hosts: list the ip adresses of all managed nodes
- ansible-galaxy init roles/<name_of_your_role>: create a role e.g apche, php, mariadb etc. 
- ansible <group> -m ping: check all connected hosts connectivity
- ansible <group> -m yum -a “name= httpd state=absent”: Check if package is not installed
```  
```
http://www.yamllint.com/ is a good tool that also checks for errors in your yaml files
```
