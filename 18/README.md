PersistentVolumeClaim, PersistentVolume, and StorageClass

This section is about volumes and storing data at the cluster level.

Kubernetes has an interesting idea: to use storage at the cluster level, it creates an abstraction layer so we don’t need to deal with the infrastructure details of a specific cluster.

For example, if a DevOps engineer wants to deploy an application on Kubernetes, there’s no need for them to know the details of AWS storage services. Instead, we want that engineer to simply describe what kind of storage they need, and the cloud platform provides it.

That’s why Kubernetes has an object called a PVC (PersistentVolumeClaim). A PVC is a description of the user’s storage request. For example: “I need 1GB of storage that my Pod can read and write to, but other Pods shouldn’t be able to do that”—for example using ReadWriteOncePod.

So a PVC is basically a request describing the required storage.

Now consider another person: an administrator. This person is a cloud/storage expert for the platform where the product runs. The admin creates the actual storage resource, which is called a PV (PersistentVolume). A PV is a Kubernetes object that represents real storage (an abstraction over a real disk, like an AWS disk).

The admin creates a PV, and then Kubernetes sees that a PVC request exists (e.g., “I need 1GB”). Kubernetes checks whether there is a matching PV available. If a suitable PV exists, Kubernetes claims it for that PVC. When the request is satisfied, we say the PVC is claimed.

There is a one-to-one relationship between a PV and a PVC: they get bound to each other.

In addition, there are different access modes:

ReadWriteOnce (RWO): one node can read and write

ReadOnlyMany (ROX): many Pods/nodes can read, but cannot write

ReadWriteMany (RWX): many Pods can read and write, even across different nodes

ReadWriteOncePod (RWOP): only one Pod can read and write

When a request is made, the “claim” (binding) can happen in two ways:

1) Static provisioning:
The admin manually creates and configures the storage (the PV) using commands and configuration.

2) Dynamic provisioning:
Nowadays, when we create a request (PVC), the cloud provider can automatically create the storage for us, but with default settings.
If we want to customize the behavior and settings of that storage, the admin does it dynamically using an object called a StorageClass.

In a StorageClass, we describe how storage should be created dynamically—meaning we override the cloud provider’s default settings with our own requirements.

So the StorageClass describes the storage that should be created. “Dynamic” means we define what features and behavior our cloud-provided storage should have, and whenever a user submits a storage request, Kubernetes looks at the StorageClass and automatically creates a matching PV based on it, and then the PVC claims it.

Summary:

PVC: the user’s request specifying how much storage is needed

PV: the actual storage resource that gets created; if it matches the PVC requirements (size, permissions/access mode, etc.), it is assigned to the PVC (they become bound/claimed)