# Day 4

## Lab - Installing minikube
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
git clone https://github.com:ansible/awx-operator.git
cd awx-operator
git tag
git checkout tags/2.19.0
make deploy
kubectl config set-context --current --namespace=awx
kubectl get pods
kubectl get pods -l "app.kubernetes.io/managed-by=awx-operator"
kubectl get svc -l "app.kubernetes.io/managed-by=awx-operator"
kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager
kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" | base64 --decode ; echo

```

Expected output
![image](https://github.com/user-attachments/assets/e9f80b39-63c0-471d-9045-0c5cfc787c74)
![image](https://github.com/user-attachments/assets/da57f005-fa4c-45aa-a217-c14fbbc52d43)

