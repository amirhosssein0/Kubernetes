Environment Variables

There are variables that can be used globally inside containers.

Some of them are automatically created by Kubernetes inside a Pod’s containers when the Pod starts up.

Question:
Kubernetes has already populated some environment variables automatically. How can we define our own custom environment variables so they get injected into the container?

There are different approaches, and the common, scalable ones are ConfigMaps and Secrets. But for now, we’re defining them inline inside the Pod spec.

1) 
    kubectl apply -f random-number-api-deployment.yaml

2) 
    kubectl exec -it deploy/random-number-api-deployment -- sh
    # printenv HOSTNAME
    random-number-api-deployment-7d894bf754-k6q9z

    # printenv STATUS
    beta

We didn’t change the Dockerfile.
When the container runs, Kubernetes injects the variables into the container—similar to Docker Compose, but at a much larger scale.

Note:
When we run kubectl apply again and it shows “configured”, the hostname changes. Why?
Because Kubernetes is effectively updating the Pod—replacing it with a new container/Pod instance.

Also, this inline method is not great for scaling, because we edited the spec of a specific Pod in its YAML file. That means we would have to add the same variables manually in every Pod spec that needs them.