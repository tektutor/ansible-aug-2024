# Day 3

## Info - Ansible Role Overview
<pre>
- Ansible role is a way one could reuse code in playbooks
- Ansible role recommends a specific folder to be followed
- Ansible roles can't be executed directly
- Ansible roles can only be invoked from Playbooks
</pre>

## Lab - Creating a custom nginx role using ansible galaxy tool
```
cd ~/ansible-aug-2024
git pull
cd Day3
ansible-galaxy init nginx

nginx
tree nginx
```
In the above folders
<pre>
defaults - captures all ready only variables
vars - any other variables your role requires can be captured here
handlers - tasks that must be executed when they receive a notification can be capture here
meta - documentation about role
tasks - typically whatever tasks we write in a playbook will be captured here
templates - the template module will fetch the files from this folder
files - files which are used by copy module must be kept here
tests - folder has a test inventory and playbook to demonstrate how the role can be invoked in your playbook
</pre>

Expected output
![image](https://github.com/user-attachments/assets/ba95c295-e5f6-4bc3-92b0-558b66cba38f)
