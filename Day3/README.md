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

## Python Basics
<pre>
- scripting language
- dynamically typed language
- python is used
  - to develop scientific applications
  - AI/ML/DL
  - to develop web applications using flask/django frameworks
  - to develop GUI based desktop applications using Qt/QML (C++ GUI Framework)
  - to develop games
  - in academic projects
  - in big-data applications
- there are 2 major versions
  - Python2 and
    - orginally doesn't support object oriented principles
    - one could only develop structured application ( non-object oriented application development )
    - many libraries were developed for Python2, hence the industry wasn't ready to adapt python3
  
  - Python3
    - they introducted OOPs concepts
    - though Python3 supported OOPs concepts, the same set of libraries that were there for Python2 was not supported for Python3
    - some of the Python3 features were back-ported(integrated) in Python2 
    - these days Python3 is used in most of the projects
    - latest versions of Ansible also supports only Python3
</pre>

## Lab - Running your first python script
```
cd ~/ansible-aug-2024
git pull
cd Day3/python/lab1
python3 --version
cat hello.py
python3 ./hello.py
```

Alternatively, you could make the hello.py an executable file 
```
chmod +x ./hello.py
./hello.py
```

Expected output
![image](https://github.com/user-attachments/assets/664016aa-de0c-4264-b4bc-f7a36135b467)

## Lab - Simple python function
```
cd ~/ansible-aug-2024
git pull
cd Day3/python/lab2
cat function.py
python3 ./function.py

chmod +x ./function.py
python3 ./function.py
```

Expected output
![image](https://github.com/user-attachments/assets/f3c57eae-65c8-49a2-9177-8e3c42c11e65)

## Lab - Python function with arguments
```
cd ~/ansible-aug-2024
git pull
cd Day3/python/lab3
cat function-with-args.py
python3 ./function-with-args.py

chmod +x ./function-with-args.py
./function-with-args.py
```

Expected output
![image](https://github.com/user-attachments/assets/b4792313-3b73-4c2f-8075-1d4515f5c22b)


## Lab - Python main equivalent entrypoint function
```
cd ~/ansible-aug-2024
git pull
cd Day3/python/lab4
cat hello.py
python3 ./hello.py

chmod +x ./hello.py
./hello.py
```

Expected output
![image](https://github.com/user-attachments/assets/1db4b0c8-9cd1-4b9a-b4c9-518abd01f1fd)

## Lab - Python class
```
cd ~/ansible-aug-2024
git pull
cd Day3/python/lab5
cat hello.py
python3 ./hello.py

chmod +x ./hello.py
./hello.py
```

Expected output
![image](https://github.com/user-attachments/assets/ca37a207-f38a-4200-a97e-53068ac35765)

## Lab - Python Inheritance
```
cd ~/ansible-aug-2024
git pull
cd Day3/python/lab6
cat myclass.py
python3 ./myclass.py

chmod +x ./myclass.py
./myclass.py
```

Expected output
![image](https://github.com/user-attachments/assets/f6573944-44c4-46fb-86cf-fa638ee5dc52)
![image](https://github.com/user-attachments/assets/917d3d32-be7f-4bca-9671-7cc41227e3e8)


## Lab - Using dynamic inventory while running ansible playbooks
```
cd ~/ansible-aug-2024
git pull
cd Day3/AnsibleDynamicInventory
python3 ./dynamic-inventory.py
./dynamic-inventory.py

cd ../AnsibleRolesAfterRefactoring/
ansible-playbook -i ../AnsibleDynamicInventory/dynamic-inventory.py ./playbook.yml
```

Expected output
![image](https://github.com/user-attachments/assets/c495787d-5aad-4719-ac96-e069e9f961a4)
![image](https://github.com/user-attachments/assets/87a81cc1-025f-4853-825b-f239f968c13f)
![image](https://github.com/user-attachments/assets/770202e9-e7cb-419b-bb06-1a8842a4abdb)

![image](https://github.com/user-attachments/assets/695bebee-e4a6-4f9d-9e1d-813743ffdc7f)
![image](https://github.com/user-attachments/assets/abcd8f2e-5f96-4695-a162-da00c614ce32)

![image](https://github.com/user-attachments/assets/18479d87-f4b7-42a5-99b2-767e2b0497f1)

## Lab - Developing a custom ansible module and invoking it from a playbook
```
cd ~/ansible-aug-2024
git pull
cd Day3/CustomAnsibleModule
tree
cat library/hello.py
cat playbook.yml
ansible-playbook playbook.yml
```

Expected output
![image](https://github.com/user-attachments/assets/9421d7ac-a2f1-48e4-88f1-268cf0b7020f)
![image](https://github.com/user-attachments/assets/6d323f5f-fdf6-4bdb-b4c7-42716c87448f)
![image](https://github.com/user-attachments/assets/c956715d-c891-4dba-8be7-7a4c9f7d28db)
