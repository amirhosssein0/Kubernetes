How to Scale Out with Replicas?

If we have only one Pod for a Service and, for any reason, that Pod fails, the Service cannot provide service during the time it takes to replace the Pod.

But if we have multiple Pods—for example, two—and one of them fails, the other one can still handle requests. When traffic is sent to a Deployment, for each request, one of the Pods is selected and the request is forwarded to that Pod.

Note:
When our cluster has dozens of nodes, these replica Pods can run on different nodes, enabling horizontal scalability.


1) kubectl apply -f random-number/

2) kubectl get pods
NAME                                               READY   STATUS    RESTARTS        AGE
random-number-api-deployment-7d894bf754-kfx5k      1/1     Running   0               43s
random-number-api-deployment-7d894bf754-ttnx5      1/1     Running   0               43s
random-number-client-deployment-7dcb8b75bc-2657m   1/1     Running   0               42s
random-number-client-deployment-7dcb8b75bc-jfrm4   1/1     Running   0               42s
random-number-client-deployment-7dcb8b75bc-npvq5   1/1     Running   0               42s


We previously said that a Deployment is responsible for managing Pods.

Here, when we create replicas, the Deployment actually manages a ReplicaSet, and the ReplicaSet manages the Pods.

We usually don’t create ReplicaSets directly; instead, we work with Deployments.
And a Deployment doesn’t only manage ReplicaSets—it also manages other things, such as rollout and update behavior for those Pods.



3) kubectl get rs
NAME                                         DESIRED   CURRENT   READY   AGE
random-number-api-deployment-7d894bf754      2         2         2       8m49s
random-number-client-deployment-7dcb8b75bc   3         3         3       8m48s