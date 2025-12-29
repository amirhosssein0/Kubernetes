Resource Management: Requests and Limits

Our cluster is made up of multiple servers (nodes), and each node runs multiple Pods.

First challenge:
These Pods need resources like memory and CPU, and their usage changes under different loads. The first problem is that one Pod might consume so much CPU that it interferes with other Pods, causing them to not get enough resources (starvation).

We can define an upper bound for a Pod’s CPU and memory consumption using limits.

A limit is the maximum amount of resources a Pod is allowed to use. If it exceeds that—especially for memory—Kubernetes may restart it, and for CPU it will throttle it to prevent overuse.

This way, we make sure other Pods don’t get starved of resources.

Second challenge:
Limits are the maximum allowed resource usage for Pods. But normally, Pods don’t constantly use that much CPU and memory.

So another important job Kubernetes does is scheduling: if we have, for example, three nodes and each node has different CPU and memory capacity, Kubernetes needs to decide which Pods should run on which node based on their resource needs.

For example, maybe a node could fit 5 Pods in practice, but if we schedule strictly based on their limits, we might only be able to place 2 Pods on that node. That’s why we need to define a Pod’s typical/expected resource usage, so Kubernetes can make better scheduling decisions about where each Pod should run—based on the amount of CPU and memory it requests.

That value is called the request, which is defined alongside limits under the resources section.

So scheduling is based on requests, not limits—because limits represent the absolute maximum, while requests represent the normal/typical usage.

That’s because at any given moment, Pods usually aren’t using their maximum resources.

1) kubectl apply -f random-number/

2) kubectl top pod --> monitor

3) kubectl top node