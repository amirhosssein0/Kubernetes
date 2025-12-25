A namespace is a way to split a Kubernetes cluster into different sections.

Why do we need to divide a cluster into separate parts?
For example, we might have dozens of nodes and many teams: one team works on the customer area, another team works on payments, and each team works on its own services independently. Teams don’t need to know the infrastructure details of other teams. The only thing they really need to know is which APIs they can expose to each other—everything else is unnecessary.

So if we want to scale our cluster, we can break it into smaller components that are easier to manage, instead of managing everything in one place as the system grows.

1) 
    kubectl get namespaces
    NAME              STATUS   
    default           Active  
    kube-node-lease   Active  
    kube-public       Active  
    kube-system       Active

    default : This is the namespace that Kubernetes creates by default, and all the Pods, Deployments, and Services we have created so far were placed inside it.

    Some namespaces are created by Kubernetes itself, such as kube-system, where Kubernetes runs internal components it needs. For example, when we create Services, DNS functionality is provided by components running inside the kube-system namespace. These DNS-related systems exist in the cluster but are hidden from us as users.

2)  
    kubectl get pods -n kube-system --> see kube-system pods
    kubectl get svc -n kube-system --> see kube-system services

3) 
    kubectl create namespace prod --> create new namespace
    kubectl apply -f random-number-client-svc.yaml -n prod
    kubectl apply -f random-number-client-deployment.yaml -n prod
    kubectl apply -f random-number-api-svc.yaml -n prod
    kubectl apply -f random-number-api-deployment.yaml -n prod
    kubectl get pods -n prod

I want to see whether we can access a Pod IP in the prod namespace from the default namespace.

We create an NGINX Pod inside the default namespace.

4) 
    kubectl apply -f nginx-pod.yaml 

5) 
    kubectl get pods -n prod -o wide --> copy IP (10.42.0.62)

6) 
    kubectl exec -it nginx-pod -c nginx -- sh
    # curl 10.42.0.62:5000/generate
    {"message":"Random number: 39"}


Next question:
I want to know whether, if we know the name of a Service in one namespace, we can access that Service from a different namespace.

Yes, but there’s an important caveat.

If the Service is in the same namespace, we can access it just like before by calling it by its name only.

But if the Service is in a different namespace, we can’t access it using just the name anymore—we must use the fully qualified address.

For example, suppose we have two namespaces, a and b, and both of them have a Service called x.

If we are inside namespace a and we call x, there is no conflict—it resolves to the Service x in namespace a.

But if we are in a third namespace, c, we can’t just say x. We must provide the full address of the Service (including its namespace).

7)  
    # cat /etc/resolv.conf
    search default.svc.cluster.local svc.cluster.local cluster.local
    nameserver 10.43.0.10
    options ndots:5

    default.svc.cluster.local
    |           |
    ns        address

    # serviceName.namespace.clusteraddress
    # curl random-number-api-svc.prod.svc.cluster.local/generate                                        
    {"message":"Random number: 19"}

