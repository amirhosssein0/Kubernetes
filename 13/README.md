Creating Environment Variables with ConfigMap

We said the inline method is not scalable, because we have to write every environment variable and its value manually in the manifest and inject it into the Pod.

There are different ways to use a ConfigMap (for example via a volume), but in this session we’re focusing on envFrom and valueFrom.

If we wanted multiple Pods to share the same set of variables, we would have to repeat them in every Deployment file. But now there is an object called a ConfigMap: we tell the Pods to read this configuration (these variables) and inject them into the containers.

1) 
    kubectl create configmap random-number-api-config --from-env-file=configmap/config.env   --> create configmap object

2) 
    kubectl describe cm/random-number-api-config
    Name:         random-number-api-comgig
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>

    Data
    ====
    HOSTNAME:
    ----
    random-number-api

    STATUS:
    ----
    beta

3) 
    kubectl apply -f random-number-api-deployment.yaml

4) 
    kubectl exec -it deploy/random-number-api-deployment -- sh
    # printenv STATUS
    beta
    # printenv HOSTNAME
    random-number-api

5) 
    kubectl apply -f random-number-client-deployment.yaml -->valuefrom 

6) 
    kubectl exec -it deploy/random-number-client-deployment -- sh
    # printenv STATUS_CN
    beta