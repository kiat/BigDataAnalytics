# CS777 - Setup Programming Environment - Windows 10
***
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
You should see something  like the following:
```
java version "1.8.0_241"
Java(TM) SE Runtime Environment (build 1.8.0_241-b07)
Java HotSpot(TM) 64-Bit Server VM (build 25.241-b07, mixed mode)
```

If instead of the java version you see the following error, then we need to setup the system environment so that windows can find java
```
'java' is not recognized as an internal or external command,
operable program or batch file.
```

Add the following system environment variable (Be careful to replace jdk1.8.0_241 with the path of your java installation in Program Files):
```
JAVA_HOME C:\Program Files\Java\jdk1.8.0_241
```

## Step 2: Python(Anaconda distro) Installation

Anaconda is an awesome python distro which contains most of the libraries we will need for this course. Please download and install the latest python ditro form here:
https://www.anaconda.com/distribution/#download-section

During the installation, please remember to set the following Advanced Installation Options to true:
 * Add Anaconda to my PATH environment variable
 * Register Anaconda as my default Python
Anaconda will also ask if you want to install VS Code. This is an excellent IDE, so I recommend that you install it but it's totally optional. 

A great installation guide for Anaconda is available here: https://www.datacamp.com/community/tutorials/installing-anaconda-windows

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
* Choose a package type: Pre-built for Hadoop 2.7

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

Download winutils.exe corresponding to your hadoop versionFrom the hadoop binaries repo:
https://github.com/steveloughran/winutils
In our case we need to get the winutils.exe from here:
https://github.com/steveloughran/winutils/tree/master/hadoop-2.7.1/bin
Save winutils.exe in the following directory:
```
C:\ProgramData\spark\spark-2.4.4-bin-hadoop2.7\bin
```
Now, create the an emoty folder 'hive' in the following location:
```
C:\tmp
```
Finally, add pysark to Anaconda. To do this, fire up a command prompt in administrator mode and type in the following command:
```
conda install pyspark
```

## Step 4: Install & Configure PyCharm(Community Edition)

Before installing PyCharm, please make sure that you have completed steps 1 to 3 successfully. You can download and install the community edition of PyCharm from here:
https://www.jetbrains.com/pycharm/download/#section=windows

## Step 5: Configure Jupyter Notebook for PySpark

Setting up jupyter notebook for pyspark is quite simple. Just add the following system environment variables:
```PYSPARK_DRIVER_PYTHON``` set to ```jupyter```<br/>
```PYSPARK_DRIVER_PYTHON_OPTS``` set to ```notebook```
