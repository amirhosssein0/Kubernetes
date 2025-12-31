StatefulSets

Stateless applications do not keep information about previous interactions with a user. What does that mean?

Imagine a user sends a request. Everything needed to generate the response is contained in that request. The application does not store any prior information related to that user or that request.

The advantage is that if we scale up and run 10 instances of the application behind a load balancer, it doesn’t matter whether the request goes to instance 1 or instance 5, because none of them assume any stored user state—so they are interchangeable.

But some applications are stateful, meaning they keep information from previous requests. For example, we can consider databases as stateful because they store data.


This section is about applications that are stateful and manage a large volume of data, and how we can scale them on Kubernetes.

A good example is databases. When you want to scale a database, there are special requirements, especially because they are data-intensive.

For example, if you want to scale a database across multiple nodes, each node may store a portion of the data or a replica of the main data. Often, one database server has read and write capabilities, while other servers only have read access because they hold replicas or backups. When data is written to the primary server, it must somehow be propagated to the other servers so they can read it.

Message queues (like Kafka) and caches (like Redis) are also examples of stateful systems.

We learned that with a Deployment we can create multiple replicas of our application and scale it. But there’s an important point:

In a Deployment, replicas are identical and interchangeable. That means Deployments are suitable for scaling stateless applications, not stateful ones—because for stateful apps, the data itself also needs to be scaled and managed.

In a Deployment, we can’t differentiate between Pods. All Pods are exactly the same, and we can’t say that only one Pod should have read/write access while others are different. Since all Pods are identical, Kubernetes introduced another object called a StatefulSet. A StatefulSet is a controller responsible for managing Pods for stateful workloads.

A StatefulSet assigns each Pod a stable, unique, and reusable identity, which allows us to communicate with each Pod individually—even when we scale the StatefulSet. This is done using DNS.

Another difference is startup behavior: with StatefulSets, Pods can be started in order, whereas Deployments usually create replicas in parallel.

For example, suppose we have a StatefulSet with three Postgres replicas. Each Pod has a unique name:

postgres-0

postgres-1

postgres-2


Each of these Pods can have its own dedicated volume, specific to that Pod.

In contrast, if we defined replicas using a Deployment with a volume, that volume would be shared among all replicas.