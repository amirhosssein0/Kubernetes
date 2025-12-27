1) 
    kubectl apply -f deployment.yaml 

2) 
    kubectl exec deploy/hello-kube -c web -it -- sh

3) 
    hostname -i => ip of pod (containers have ip of their pod)

4) 
    wget -o - http://localhost | head -n 50

5) 
    kubectl logs deploy/hello-kube -c web --tail=5