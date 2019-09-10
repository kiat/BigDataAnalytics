
# Step-1 

Install java JDK on your machine 


java -version

java version "1.8.0_211"
Java(TM) SE Runtime Environment (build 1.8.0_211-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.211-b12, mixed mode)


and setup 

JAVA_HOME variable to the main folder where you have installed your java 

```export JAVA_HOME=`/usr/libexec/java_home -v 1.8` ``


# Download Apache Spark 


```/Users/kiat/spark-2.3.0-bin-hadoop2.7```


http://spark.apache.org/downloads.html


Direct link is for example following 

http://apache.osuosl.org/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz


Run on the command line the following command to download: 

```wget http://apache.osuosl.org/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz```


Uncompress it 

```tar xvfz spark-2.4.4-bin-hadoop2.7.tgz```

I have my spark on the following folder 

```/Users/kiat/spark-2.3.0-bin-hadoop2.7```

# Setup Enviroment Variables. 

Edit the bash_profile file and set some Environment variables 

```nano .bash_profile```



```export SPARK_HOME=/Users/kiat/spark-2.3.0-bin-hadoop2.7```
```export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH```

Set it to the path where you have your python3 

```export PYSPARK_PYTHON=/Users/kiat/anaconda3/bin/python3```

Add Spark bin and sbin folder to the PATH 

```export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin```



If you want to use the jupyter notebook on your mac set the following two variables as well. 

**Note:** Note that you can only use pyspark ipython shell or jupyter notebooks, one of them only 
You can comment or uncomment the following variables to use one of them  

```export PYSPARK_DRIVER_PYTHON="jupyter"```
```export PYSPARK_DRIVER_PYTHON_OPTS="notebook"```


To activate the current variables you can restart your mac or type 

```source .bash_profile```

