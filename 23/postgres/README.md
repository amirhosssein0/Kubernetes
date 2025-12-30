In the previous section, we learned about multi-container Pods.
This section is about another type of multi-container setup called an init container.

An init container is one or more containers inside a Pod that run before the Pod’s main container starts. Kubernetes runs the init containers first, and if they don’t fail, then after they finish successfully, the main container is started.

Use cases:
We know containers inside a Pod can share volumes. For example, if we have a database and we want to seed it with some initial data, and we don’t want that logic inside the main container, we can do it using an init container. In this session, the init container runs some scripts to generate or load initial data and stores it in a shared volume for Postgres. If the init container completes successfully, Kubernetes starts Postgres, and Postgres uses that volume.

Another example: sometimes our main container needs some files or data that aren’t in our repository, and we don’t want to install Git inside the main container and clone a repo (because it would complicate the container). Instead, we create an init container to do that work, and then share the downloaded data with the main container through a volume.

1) kubectl apply -f postgres/

2) kubectl get pods --> running after successful init

3) kubectl logs postgres-deployment-78c78c6754-w786c

4)  kubectl exec -it deploy/postgres-deployment -c postgres -- psql -U postgres

    postgres=# \c customers
    You are now connected to database "customers" as user "postgres".
    customers=# \dt
                List of relations
    Schema |   Name   | Type  |  Owner   
    --------+----------+-------+----------
    public | profiles | table | postgres
    (1 row)
    customers=# SELECT * FROM profiles;
    id | name  
    ----+-------
    1 | AMIR0
    (1 row)
