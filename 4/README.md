1)
   kubectl apply -f deployment.yaml 
2)
    kubectl get pods
3)
    kubectl get deployment
    NAME         READY   UP-TO-DATE   AVAILABLE   AGE
    hello-kube   1/1     1            1           2m

4)
    kubectl get pods -l app=hello-kube

5)
    kubectl delete -f deployment.yaml 
6)
    kubectl get deployment
    No resources found in default namespace.