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

After refactoring our ansible role folder looks as shown below
![image](https://github.com/user-attachments/assets/c63a8759-2346-49ab-b661-f800eaba8ed8)
![image](https://github.com/user-attachments/assets/c76e4460-22fa-474a-96b8-bfca5b17d0cf)

Let's run the ansible playbook
```
cd ~/ansible-aug-2024
git pull
cd Day3/AnsibleRoles
ansible-playbook playbook.yml
```

Expected output
![image](https://github.com/user-attachments/assets/84ce7543-b8ac-49f9-a433-5d5bdda9ae30)
![image](https://github.com/user-attachments/assets/858636f6-7e3d-44c2-ba3f-db549407c2c0)
![image](https://github.com/user-attachments/assets/23b78566-708d-4b7b-80ae-c62a576d5155)

## Lab - Executing the refactored nginx ansible role
```
cd ~/ansible-aug-2024
git pull
cd Day3/AnsibleRolesAfterRefactoring
ansible-playbook playbook.yml
```

Expected output
![image](https://github.com/user-attachments/assets/1e9f0f62-9267-4e9a-be23-990a0929aacc)
![image](https://github.com/user-attachments/assets/2eb81aa1-96bc-472b-83da-1b0355b7951e)
![image](https://github.com/user-attachments/assets/89642e70-9aec-4347-9d54-8fcbeab0d953)
![image](https://github.com/user-attachments/assets/c446c0ee-42f9-4fd3-9cdd-a61a2da8c9a9)
![image](https://github.com/user-attachments/assets/f581ae31-15b6-4d26-9998-706a0237f65a)
![image](https://github.com/user-attachments/assets/0ef7865c-64dc-4498-83e9-62854d393d66)
