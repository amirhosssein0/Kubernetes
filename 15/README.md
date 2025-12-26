Securing Sensitive Data in Kubernetes with Secret

Sometimes the things we need are very critical and sensitive—like a database password, a token, or an SSH key—and they shouldn’t be easily accessible. So we use the Secret object.

It’s very similar to a ConfigMap, but the difference is that the resource we create is of type Secret, and it comes with certain restrictions—for example, not all Pods can access this resource or view its contents.

1) 
    echo -n "postgrespass" | base64 --> cG9zdGdyZXNwYXNz

2) 
    kubectl describe secret/postgres-secret
    Name:         postgres-secret
    Namespace:    default
    Labels:       <none>
    Annotations:  <none>

    Type:  Opaque

    Data   ---> it doesnt show data, but config map shows
    ====
    postgres-password:  12 bytes