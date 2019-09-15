
# Step-1 - Install Spark on your Mac and Setup enviroment variables 


# Step-2 - Enable SSH login to localhost without password 

2.1 - Create SSH key pair on your local machine 

Apache Spark uses a set of Linux Shell Scripts to run a cluster of machines 


```ssh-keygen```

No passphrase is need 

run the following command 

```ssh localhost```

if you are able to login to your own mac via SSH then this step is setup. 


# Step-3 - run start-all.sh script 

You have added the spark sbin folder to your PATH variable so that you can run all of the scripts in that folder. 

run the following command. 

```start-all.sh``` 


You can use a webbrowser and open the following website to see the Spark GUI 

```http://localhost:8080```

This will run Spark Master and Spark worker on your machine 

To Stop the process you can use 


```stop-all.sh```  


# Step-4- You can submit your Spark code using the spark-submit 



```spark-submit  --master    spark://localhost:7077  YOUR-PYTHON.py INPUT OUTPUT```




