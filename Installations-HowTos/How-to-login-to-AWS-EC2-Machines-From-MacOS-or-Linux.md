
# How to connect to AWS EC2 machines from Mac/Linux.

The following assumes that your .pem fle is called MyFirstKeyPair.pem and that it is
located in your working directory; replace this with the actual name and location of your fle,
assuming that you called your key pair something else. 
Type:

```chmod 500 MyFirstKeyPair.pem```

Now, you can connect to your master machine (replace “54.172.82.0” with the IP address of
your own master machine):

ssh -i "MyFirstKeyPair.pem" ubuntu@54.172.82.0

This will give you a Linux prompt; you are connected to your master node.
Important: Never share your .pem fle. 
