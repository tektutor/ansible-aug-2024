# Day 2

## Lab - Running your first Ansible ad-hoc command (ping)
```
cd ~/ansible-aug-2024
git pull
cd Day2/static-inventory
cat inventory
ansible -i inventory all -m ping
```

Expected output
![image](https://github.com/user-attachments/assets/d39e2601-fb89-421e-af11-b77223df6ccf)

## Lab - What happens when we execute the ansible ping ad-hoc command
```
cd ~/ansible-aug-2024
git pull
cd Day2/static-inventory
cat inventory
ansible -i inventory all -m ping -vvvv > output.yml 2>&1
```

<pre>
1. Ansible creates a temp directory on the Ansible Controller Machine (ACM)
2. Ansible parallely connects to ubuntu1 and ubuntu2 using SSH, fetching connection details from the inventory file
3. Ansible creates a temp directory on the ansible nodes(containers)
4. Ansible copies(sftp/ftp) from ACM machine to the ansible nodes into the temp directory
5. Ansible run the python ping.py script on the remote ansible nodes
6. Captures the output of ping.py execution on the remote ubuntu1 and ubuntu2, removes the temp directory that was created earlier
7. On the ACM machine, gives a summary of the output(status) of ping ad-hoc command
</pre>

## Lab - Listing all the ansible modules supported by your ansible version
```
ansible-doc -l
```

Expected output
![image](https://github.com/user-attachments/assets/6f1201ce-994a-4720-890c-c49e12e8f56c)


## Lab - Finding machine facts
```
cd ~/ansible-aug-2024
git pull
cd Day2/static-inventory
ansible -i inventory ubuntu1 -m setup
```

Expected output
![image](https://github.com/user-attachments/assets/a1d8e343-6744-4cd8-afa5-8ee204e55270)
![image](https://github.com/user-attachments/assets/c3e86d20-5689-4d55-aebe-d90985bf039e)

## Lab - Refactoring inventory with group variables
```
cd ~/ansible-aug-2024
git pull
cd Day2/static-inventory
cat inventory
cat hosts
ansible -i hosts all -m ping
```

Expected output
![image](https://github.com/user-attachments/assets/659527ce-a760-48b6-8b22-8f2aafc93f89)
![image](https://github.com/user-attachments/assets/2cca072c-7ab7-4a03-ba39-df13d2d65f8d)

## Info - Structure of ansible playbook
![playbook](playbook.png)

## Lab - Installing Visual studio code using ansible playbook
```
cd ~/ansible-aug-2024
git pull
cd Day2/playbooks
ansible-playbook install-visual-studio-code-locally-playbook.yml --ask-become-pass
```
In the above command, when it prompts for admin password, you need to type 'Password@1' without quotes.

Expected output
![image](https://github.com/user-attachments/assets/5b2eb38d-139d-4286-9289-5de4cbcf83ad)
