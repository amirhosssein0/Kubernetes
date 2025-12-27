In the previous approach, we ran the Pod imperatively, which is not usually how things are done.
With a manifest, we describe the desired state of our Cluster and tell the system to bring the Pod to that state. This is called the declarative approach.


1) 
    kubectl apply -f pod.yaml

2) 
    kuberctl get pods

If you apply again, it says unchanged. It means, another pod doesnt created.
If you dont have pod, it will be created.
If have have this pod, it will be updated from current situation to desired situation.

3) 
    kubectl delete -f pod.yaml
