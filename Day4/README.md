# Day 4

## Lab - Installing minikube ( From Ubuntu RPS Lab Machine terminal )
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

minikube start --addons=ingress,ingress-dns --cni=flannel --install-addons=true --kubernetes-version=stable --memory=16g --cpus=4

minikube status
sudo snap install kubectl --classic
```

Expected output
![image](https://github.com/user-attachments/assets/3ea99c25-6172-48bf-be03-e9d853a42db0)
![image](https://github.com/user-attachments/assets/c3109110-4da0-4ffb-9ecc-95d62ad3b5bc)
![image](https://github.com/user-attachments/assets/5f9c89c7-f7b9-482d-8095-a8d786f82d8e)


## Lab - Installing Ansible Tower(AWX) into minikube
```
git clone https://github.com/ansible/awx-operator.git
cd awx-operator
git checkout tags/2.19.0
make deploy
kubectl config set-context --current --namespace=awx
kubectl get pods
kubectl get pods -l "app.kubernetes.io/managed-by=awx-operator" -w
```

Expected output
![image](https://github.com/user-attachments/assets/e9f80b39-63c0-471d-9045-0c5cfc787c74)
![image](https://github.com/user-attachments/assets/da57f005-fa4c-45aa-a217-c14fbbc52d43)

Create a file named awx-demo.yml with below content
```
---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-demo
spec:
  service_type: nodeport
```

Run the below command
```
kubectl apply -f awx-demo.yml
kubectl get svc -l "app.kubernetes.io/managed-by=awx-operator"
kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager
kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" | base64 --decode ; echo
```

Expected output
![image](https://github.com/user-attachments/assets/aa3b0fb3-234d-4ef4-8a14-78b0d21e466a)
![image](https://github.com/user-attachments/assets/a12ac0ce-266f-452e-b972-76e765313b67)
![image](https://github.com/user-attachments/assets/19c90fda-141e-4a2e-9dbf-4e993b4b8c3f)
![image](https://github.com/user-attachments/assets/e4359237-e11e-4400-a342-090657c4bb3f)
![image](https://github.com/user-attachments/assets/56258bb5-960d-4bbd-af07-c37f9c013d37)

You can access your Ansible Tower from your Ubuntu RPS Lab web browser.  The port 31577 has to be replaced with your nodeport service port.
```
minikube ip
kubectl get svc -l "app.kubernetes.io/managed-by=awx-operator"
http://192.168.49.2:31577
```
You can retrieve the password as shown below
<pre>
kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" | base64 --decode ; echo  
</pre>
Expected output
![image](https://github.com/user-attachments/assets/f7e5dd87-06a9-4f36-8cc9-69d1ffcd2b4a)

Login credentials
<pre>
username - admin
password - vx6qfhJVrysWvRyUxY9txGz1as3Svc
</pre>
You need to use the password shown by your 'kubectl get secret' command as it would be different for each one of us.

Expected output
![image](https://github.com/user-attachments/assets/cae5bc28-86dc-4794-bdfd-c67f262ba256)
![image](https://github.com/user-attachments/assets/72be4d3e-85d9-44af-a5d8-3cab534e446e)
