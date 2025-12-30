Multi containers in one Pod


Up to now, our Pod had one container, but we know that in theory a Pod can contain multiple containers.

If our Pod includes multiple containers, those containers can communicate with each other through localhost. For example, one can run on port 5000 and another on 8080, and they can talk to each other via localhost:5000 or localhost:8080. The containers’ IP address is actually the same as the Pod’s IP.

We also know that containers have their own filesystems, but containers inside the same Pod can share the same volumes.

In today’s example, we have a Flask app (an API generator) as one container, but we want to add another container called fluentd whose job is to manage logs. That means the fluentd container reads the API container’s logs from a file called apps.log and processes them, then writes them to stdout.

So logs/apps.log is shared as a volume between the two containers: the API container writes to it, and fluentd reads from it.


kubectl apply -f multi-number/

kubectl logs deploy/multi-container-pod -c fluentd-sidecar