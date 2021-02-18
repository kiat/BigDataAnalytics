# How to run Jupyter Notebook on Google Cloud Dataproc  


# Create a Dataproc Cluster and Enable access to Web Interfaces 

1. Enable Component Gateway 

**Component gateway** 

 Enable access to the web interfaces of default and selected optional components on the cluster. Learn more


![Create a Cluster and Enable Access to Web Interfaces ](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/gc-webinterface-1.png)

This is well documented here 

https://cloud.google.com/dataproc/docs/concepts/accessing/dataproc-gateways?hl=en_US



2. Add Jupyter notebook 


Then you need to click on **Advanced options** 

and select  **Optional components**  

Install optional open source components on the cluster. Learn more

 


![Create a Cluster and Enable Access to Web Interfaces ](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/gc-webinterface-2.png)


The Jupyter Web UI is available on port 8123 on the cluster's first master node. Python and PySpark kernels are available.



# Access the Web interfaces (Jupyter and Spark History)
After your cluster is provisioned and running, click on the cluster and go to Web Interfaces 




![Create a Cluster and Enable Access to Web Interfaces ](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/gc-webinterface-3.png)



You can find all of the Web Interfaces here, Jupyter and Spark History

**You can click on the given Links and Access them** 
No further setups is needed. 


![Create a Cluster and Enable Access to Web Interfaces ](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/gc-webinterface-4.png)


