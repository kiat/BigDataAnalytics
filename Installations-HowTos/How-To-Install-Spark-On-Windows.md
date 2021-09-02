# CS777 - Setup Programming Environment - Windows 10

We will need the following software components to setup the programming environment for this course on a Windows machine:

1. Java
2. Anaconda Python Distribution
3. winutils
4. Spark
5. PyCharm (IDE for Python Development)

Following are step-by-step instructions for putting together all the components:

## Step 1: Java Installation

If you do not already have Java installed on your machine, then you can download it from here: https://www.java.com/en/download/win10.jsp

Once the installation is complete, we need to verify the installation. Fire up windows command prompt and type in the following command:
```
java -version
```
You should see the version of java printed out on the command prompt:
```
java version "1.8.0_241"
Java(TM) SE Runtime Environment (build 1.8.0_241-b07)
Java HotSpot(TM) 64-Bit Server VM (build 25.241-b07, mixed mode)
```
*Note the actual versions will differ based on the version of java installed on your computer*

If instead of the java version you see the following error, then we need to setup the system environment so that windows can find java
```
'java' is not recognized as an internal or external command,
operable program or batch file.
```

Add the following **system** environment variable (Be careful to replace jdk1.8.0_241 with the path of your java installation in Program Files):<br/>
```JAVA_HOME``` set to ```C:\Program Files\Java\jdk1.8.0_241```

## Step 2: Python(Anaconda distro) Installation

Anaconda is an awesome python distribution which contains most of the libraries we will need for this course. Please download and install the latest anaconda python ditro form here:
https://www.anaconda.com/distribution/#download-section

During the installation, please remember to set the following Advanced Installation Options to true:
 * Add Anaconda to my PATH environment variable<br/>
 * **Register Anaconda as my default Python** (This is important)<br/>
Anaconda will also ask if you want to install VS Code. This is an excellent IDE, so I recommend that you install it, but it is totally optional. 

A rather detailed installation guide for Anaconda is available here, just in case you need some additional help:
https://www.datacamp.com/community/tutorials/installing-anaconda-windows

Now it's time to verify our conda and python installations. Fire up a command propmt and type in the following:
```
conda --version
python --version
```
You should get the versions as output (Note: the actual versions may be different):
```
conda 4.8.0
Python 3.7.3
```

## Step 3: Spark Installation

Download the last stable version of Apache Spark from the following url:
http://spark.apache.org/downloads.html

You can use the following options:
* Choose a Spark release: 2.4.4 (Aug 30 2019)<br/>
* Choose a package type: Pre-built for Hadoop 2.7<br/>
*Please note that Spark and Hadoop are regularly updated & therefore the actual versions will differ*

Create a folder 'spark' in 'C:\ProgramData' and move 'spark-2.4.4-bin-hadoop2.7.tgz' from your downloads folder to this directory.
Now uncompress the file using 7zip, so that you have the following directory structure:
```
 Directory of C:\ProgramData\spark\spark-2.4.4-bin-hadoop2.7

09/15/2019  03:07 PM    <DIR>          .
09/15/2019  03:07 PM    <DIR>          ..
09/15/2019  03:08 PM    <DIR>          bin
09/15/2019  01:28 PM    <DIR>          conf
08/27/2019  04:30 PM    <DIR>          data
08/27/2019  04:30 PM    <DIR>          examples
09/15/2019  03:07 PM    <DIR>          hadoop
08/27/2019  04:30 PM    <DIR>          jars
08/27/2019  04:30 PM    <DIR>          kubernetes
08/27/2019  04:30 PM            21,316 LICENSE
08/27/2019  04:30 PM    <DIR>          licenses
08/27/2019  04:30 PM            42,919 NOTICE
08/27/2019  04:30 PM    <DIR>          python
08/27/2019  04:30 PM    <DIR>          R
08/27/2019  04:30 PM             3,952 README.md
08/27/2019  04:30 PM               164 RELEASE
08/27/2019  04:30 PM    <DIR>          sbin
08/27/2019  04:30 PM    <DIR>          yarn
```

Create system environment variables for spark
```
SPARK_HOME = C:\ProgramData\spark\spark-2.4.4-bin-hadoop2.7
HADOOP_HOME = C:\ProgramData\spark\spark-2.4.4-bin-hadoop2.7
```
Append the following path to your system environment variable Path
```
C:\ProgramData\spark\spark-2.4.4-bin-hadoop2.7\bin
```

Download winutils.exe corresponding to your hadoop versionFrom the hadoop binaries repo:<br/>
https://github.com/steveloughran/winutils<br/>
In our case we need to get the winutils.exe from here:<br/>
https://github.com/steveloughran/winutils/tree/master/hadoop-2.7.1/bin
Save winutils.exe in the ```C:\ProgramData\spark\spark-2.4.4-bin-hadoop2.7\bin``` directory:

Now, create the an empty folder ```hive``` in the ```C:\tmp``` directory

Finally, we need to install pysark bindings for Anaconda. To do this, fire up **Anaconda Propmpt** in administrator mode and type in the following command:
```
conda install pyspark
```
This concludes the setup procedure for pyspark. Now let's check if our spark installation actually works.
Fire up the **Anaconda Propmpt** and type in the following command<br/>
```
pyspark
```
This should fire up the spark server on your computer. The output would look something like this:
![windows_install_01](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_01.PNG)
Enter Ctrl+Z to close the spark session.

So, our installation is good, now let's create PySpark script in python and see how we can execute it on spark.
  * First, let us create a simple python script ```TestPySpark.py``` that will just print some details about the spark instance. You can save this file at a path of your choice. For this example, I have the file stored at ```C:\Users\Subrat\Documents\CS777```<br/>
  ```python
  import sys
  from pyspark import SparkContext

  # Print the script name
  print("PySpark Script: ", sys.argv[0])

  # Create a spark context and print some information about the context object
  sc = SparkContext()
  print(sc.version)
  print(sc.pythonVer)
  print(sc.master)

  # Free the spark context object
  sc.stop()
  print("end")
  ```
  * Next, run the python script using the following commands (*using appropriate path on your computer*) in the **Anaconda Prompt**:
  ```
  cd C:\Users\Subrat\Documents\CS777
  spark-submit TestPySpark.py
  ```
  If there are no problems, you should see the following output:
  ![windows_install_02](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_02.PNG)
  As you can see, spark generated tons of messages which end up obfuscating the output that we are really interested in. To fix this, let us update the logging properties for spark. Here's how:
   * Navigate to the conf folder in your spark installation directory. For example:
     ```
     C:\ProgramData\spark\spark-2.4.4-bin-hadoop2.7\conf
     ```
   * If you do not have a file ```log4j.properties``` here, then copy the file ```log4j.properties.template``` and rename it to ```log4j.properties```
   
**NOTE:**
   * Just in case that you do not want to see many info log outputs, you can open (This is very **optional step**) the ```log4j.properties``` and change the following two lines from:
        ```
        # Set everything to be logged to the console
        log4j.rootCategory=INFO, console
        ```
       to 
        ```
        # Set only warnings to be logged to the console
        log4j.rootCategory=WARN, console
        ```
   * Save the ```log4j.properties``` and re-run ```TestPySpark.py``` Now you should see only relevant output:
   ![windows_install_08](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_08.PNG)



## Step 4: Configure Jupyter Notebook for PySpark

Setting up jupyter notebook for pyspark is quite simple. Just add the following system environment variables:
```PYSPARK_DRIVER_PYTHON``` set to ```jupyter```<br/>
```PYSPARK_DRIVER_PYTHON_OPTS``` set to ```notebook```<br/>
To check that we can use spark with jupyter notebook, let's create a simple notebook ```TestPySparkJupyterNotebook``` in the folder ```C:\Users\Subrat\Documents\CS777```. Update the following code in this notebook
![windows_install_03](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_03.PNG)

Now execute all cells **except** the last one with sc.stop()
![windows_install_04](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_04.PNG)

In the **Out[3]** click the link **Spark UI**. This will launch the SparkUI. You will learn how to use the Spark UI later in the course.
![windows_install_05](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_05.PNG)

Finally, run the cell with sc.stop() to close the spark session
![windows_install_06](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_06.PNG)


**NOTE:** If you enabled pyspark with Jupyter Notebook, you will not be able to use **spark-submit**. If you need to use **spark-submit** again, then you need to comment out the two enviroment variables (PYSPARK_DRIVER_PYTHON and  PYSPARK_DRIVER_PYTHON_OPTS )so that you can use spark-submit 


## Step 5: Install & Configure PyCharm(Community Edition)

Before installing PyCharm, please make sure that you have completed steps 1 to 3 successfully. You can download and install the community edition of PyCharm from here:
https://www.jetbrains.com/pycharm/download/#section=windows

Once you have installed PyCharm, create a new project and add the python script ```TestPySpark.py``` we created earlier in Step3. Run the script and you should see the following:
![windows_install_07](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_07.PNG)

***
## Troubleshooting

1. I get the following error when I run the jupyter notebook in Step 4. What do I do?
   ```python
   ValueError: Cannot run multiple SparkContexts at once; existing SparkContext(app=PySparkShell, master=local[*]) created by <module> at C:\ProgramData\Anaconda3\lib\site-packages\IPython\utils\py3compat.py:188
   ```
   Solution 1: Close all other spark sessions and try again.<br/>
   Solution 2: Another alternative is to use the SparkSession object. Example below:<br/>
   ```python
   # import for spark session handle
   from pyspark.sql import SparkSession
   spark = SparkSession.builder.appName('cs777-Application1').getOrCreate()
   ```
  
2. Do I need ***findspark** ?
   No, this library is not required anymore with pysaprk bindings for Anaconda, we installed in Step3
   
3. When I run ```spark-submit TestPySpark.py``` why do I get error like this?
   ![windows_install_err_01](https://github.com/kiat/BigDataAnalytics/blob/master/Installations-HowTos/sceenshots/windows_install_err_01.PNG)
   Solution: You get this error because, in Step 4, we setup the system environment variables ```PYSPARK_DRIVER_PYTHON``` and ```PYSPARK_DRIVER_PYTHON_OPTS``` to run pyspark on a Jupyter notebook. To avoid this problem, you can either use PyCharm or temporarily disable these two environment variables
   
