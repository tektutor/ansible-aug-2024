# Day 1

## Cloning this repository in Ubuntu lab machine from terminal
```
cd ~
git clone https://github.com/tektutor/ansible-aug-2024.git
cd ansible-aug-2024
tree
```

Expected output
![image](https://github.com/user-attachments/assets/3814fc04-2223-489f-b44c-0f3efee256ea)

## Lab - Installing tree utility in Ubuntu lab machine
```
sudo apt update && sudo apt install -y tree
```

## Checking if all the tools required for the training are installed in your lab machine
```
docker --version
docker images
ansible --version
```

Expected output
![image](https://github.com/user-attachments/assets/523f6a49-aa7e-480d-94ad-dc0a1fa0e783)
![image](https://github.com/user-attachments/assets/931f6701-2ece-4e77-b371-8b5946f15709)

## Info - Hypervisor Overview
<pre>
- is nothing but virtualization technology
- virtualization allows us to run many Operating System side by side, parallely on the same desktop/laptop/workstation/server
- more than 1 OS can be actively running
- each Virtual Machine(VM) represents a fully function Operating System
- each VM has to allocated with dedicated hardware resources
  - CPU cores
  - RAM
  - Storage ( HDD/SSDs )
  - hence it is called heavy-weight virtualization technology
- Hardware + Software Technology
  - we need Processor supports virtualization
  - AMD
    - Virutualization feature is AMD-V
  - Intel Processor
    - VT-X is the virtualization feature
- there are two types of Hypervisor softwares
  - Type 1 aka Bare-Metal Hypervisors
    - is used in Servers/Workstations
    - Virtual Machines can be created without a Host OS
    - the OS installed within Virtual Machine is called Guest OS
    - examples
      - VMWare vSphere/vCenter
  - Type 2
    - is used in laptops/desktops/workstations
    - this requires a Host OS 
    - hypervisor software is installed on top of Host OS ( Windows, Linux, Mac OS-X )
    - examples
      - Microsoft Hyper-V
      - Oracle Virtualbox ( Free )
      - VMWare Workstation ( Windows & Linux )
      - VMWare Fusion ( Mac OS-X )
      - KVM - opensource ( Linux )
</pre>

## Info - Hypervisor High-Level Architecture
![Hypervisor](HypervisorHighLevelArchitecture.png)

## Info - Docker Overview
<pre>
- lightweight - application virtualization technology  
- each container represents one application or an application component
- each container is an application process
- containers doesn't have its own OS Kernels
- containerd don't get their own hardware resources
- container don't represents an Operating System
- container will never be able to replace virtual machines or Operating System
- similarities between virtual machines and containers
  - each container get's its own IP address just like VMs get their own IP address
  - each container has its own network stack just like VMs
  - each container has its own file system just like VMs
  - each container has its own Port range ( 0 - 655535 ) just like VMs
- client/server architecture
- docker client
  - is the software that we use to interact with docker engine 
- docker server
  - runs as a service in the background
</pre>
## Info - Docker High-Level Architecture
![Docker](DockerHighLevelArchitecture.png)

## Info - Docker Image Overview

## Info - Docker Container Overview

## Info - Docker Registry
