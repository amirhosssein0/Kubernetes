Rollout Strategy for Deployment 

In this strategy, we assume our application has multiple instances running on the nodes. For example, we have 5 instances of our app and version 1 is serving users. A new version has been released—version 2—and we want to replace the current version with the new one using a deployment strategy.

There are different strategies like blue-green, canary, and rollout. A rollout works like this: suppose we have several instances of version 1, for example 3 Pods. Version 2 is ready, so we replace one of the Pods with the new version while the other two Pods are still running the old version. Then we update the second Pod to version 2 while one old Pod is still running. Finally, we update the last remaining old Pod to the new version.

So the replacement happens step by step.

The advantage is that there is no downtime—at any moment, the application keeps serving users through the available Pods.

The disadvantage is that the versions must be able to coexist. For example, while one Pod is running version 2 and others are still running version 1, they need to be compatible; if they conflict, the system can break.

So rollout gradually replaces Pods with the new version. By default, Kubernetes uses a rollout approach to deploy a new version.

In this section’s example, we have the Redis StatefulSet, and we want to change the Redis version from 7.4 to a newer version.

* before changes: 

1) kubectl apply -f redis/

2) kubectl get statefulset -o wide
NAME    READY   AGE   CONTAINERS        IMAGES
redis   bash3/3     64s   redis-container   redis:7.4

* after changes

3) kubectl apply -f redis/
configmap/redis-role-config unchanged
service/redis-svc unchanged
statefulset.apps/redis configured

4) kubectl get statefulset -o wide
NAME    READY   AGE     CONTAINERS        IMAGES
redis   2/3     6m28s   redis-container   redis:7.4-alpine
        |
        2pods are changed

5) kubectl rollout status statefulset/redis
partitioned roll out complete: 3 new pods have been updated...

6) kubectl get statefulset -o wide
NAME    READY   AGE     CONTAINERS        IMAGES
redis   3/3     9m24s   redis-container   redis:7.4-alpine

If you want to undo your changes:
Kubernetes always saves 2 last versions of our deployment and we can rollback easily

7) kubectl rollout undo statefulset/redis
statefulset.apps/redis rolled back

8) kubectl rollout status statefulset/redis
Waiting for 1 pods to be ready...
partitioned roll out complete: 3 new pods have been updated...

9) kubectl get statefulset -o wide
NAME    READY   AGE   CONTAINERS        IMAGES
redis   3/3     13m   redis-container   redis:7.4


First, redis-0 (the leader) comes up, then redis-1, then redis-2.
When we do a rollout update, Kubernetes replaces them from the end:
it updates redis-2 first, then redis-1, and finally redis-0.
