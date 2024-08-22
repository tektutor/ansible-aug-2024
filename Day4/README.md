# Day 4

## Lab - Installing minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

minikube start --addons=ingress,ingress-dns --cni=flannel --install-addons=true --kubernetes-version=stable --memory=16g --cpus=4


```

