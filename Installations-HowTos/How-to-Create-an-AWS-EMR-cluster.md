# How to Create a Spark Cluster on AWS EMR 

In this tutotrial you will learn how to create a AWS EMR (ElasticMapReduce) cluster and run a python spark job on it. 

You will learn: 

1. Create a Key Pair on EC2 

2. Create an AWS EMR cluster

3. Upload a PySpark program to S3 

4. Run a Spark job (Computation Steps)

5. Check out the results on S3 Storage. 

6. Login to Master Node and run spark on Command Line

7. Run pyspark code on Apache Zeppelin 



# AWS Console

![AWS Educate First Page](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-1.png "AWS Educate First Page")

Click on the AWS console and open it. 

This is the main AWS console page. 



![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-2.png "AWS")


<span style="color:red">**IMPORTANT NOTE:**</span>
Check if you are in **N. Virginia** Amazon Data center. This is the top right menu, the second one close to **Support**. 
If you are not in **N. Virginia**, use the drop down menu and change it to **N. Virginia** and stay there for the whole class. 


## Start Up a EMR Cluster


![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-2.png "AWS")


# AWS EC2 

Amaozn AWS EC2 (Elastic Computing) 

The first step is to go to EC2 and create a key pair. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-3.png "AWS")

You can skip the following step if you have already generated a key pair. 

# How to Create your Key Pair on AWS EC2 

To connect to the cluster you will create later, you need a Key Pair as an identity.

1. Go to Amazon AWS website (aws.amazon.com).
2. Sign in with your user name and password. Go to EC2 (you can reach EC2 from the AWS services search text box).
3. Click "key pairs".
4. Click "Create Key Pair".
5. Pick a key pair name that is likely unique to you. Type it in, and click ``Create''.
6. This should create a ".pem" file that you can download. 
You will subsequently use this .pem file to connect securely to a machine over the internet. 




![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-4.png "AWS")

Download and store the key file **.pem** file. 

It would make your commands simple if you store this key file in your HOME folder. 
HOME folder is the main user folder, for example on my Mac it is /Users/kiat/ (note that my account name on my Mac is kiat)


![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-5.png "AWS")

<span style="color:red">**IMPORTANT NOTE:**</span>
Never share your prive key .pem file with anyone (be carefull to not push it to github)



<span style="color:blue">**NOTE:**</span>
You can click on the AWS log on top left to go back to main AWS console page. 

#  AWS EMR 

Now go back to AWS EMR. 


![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-6.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-7.png "AWS")

1. Select Spark here to have Apache Spark installed on your cluster machines. 
2. Select your keypair from the EC2 key pair 


<span style="color:red">**IMPORTANT NOTE:**
It is important that you select your Pair Key. 
Otherwise you can not login to your master machine using SSH connection. 
</span>

You can also select the number of machines that you want to have or the type of machines. 

AWS makes here a suggestion of 1 master node and 2 worker node with EC instance type of **m5.xlarge** 

Each machine of type **m5.xlarge** (M5 General Purpose Extra Large)	

has 16.0 GiB	and 4 vCPUs	, 10 Gigabit	

Costs in N.Virigina data center approximaty $0.192 per Hour



You can check the pricing here 
https://aws.amazon.com/ec2/pricing/on-demand/ 

So this cluster will cust 3 * 0.192 = 0.576 

And because we are using EMR to make the spark installation more easier, amazon will charge more. 
It will be approximatly an addional 20% 

Approximate cost per hour =  0.576 × 1.2  = 0.6912 USD 

There will be additional costs for data transfers. For example when you transfer data between Amazon data centers or between your own servers/laptops and AWS. 

AWS charges hourly, so it does not matter if you start and stop the cluster immadiatly you will pay the cost for 
a complete hour of computation. Also when you run a cluster for 65 min, you will be charged for 2 hours and not for 1 hour and 5 min. 



![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-8.png "AWS")


It can take up to some minutes until your cluster of machines are provisioned, running and ready for use. 

The provisioning time depends on number of machines, type of machines and how busy is AWS in that time/date. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-9.png "AWS")

If you see that your machined have received their IP addresses, your cluster is ready for use. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-10.png "AWS")

Click on **Steps** tab and if you see the instakktion task as complete then your cluster is ready to use. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-11.png "AWS")

AWS EMR consider all of the installation and computations as processing steps. They developed some scripts to install spark on EC2 machines. EMR is a a very easy to use way to start machines, install spark and hadoop and run computations on it. 

You can start adding your computation task as a next processing task. 

Click on **Add step** button 

The steps to run Spark Jobs on EMR is documented well here 

[https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-submit-step.html](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-submit-step.html)

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-12.png "AWS")

Change the menu to **Spark Application** because we will run our pyspark script. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-13.png "AWS")


You will to have your python script stored in a S3 bucket and accessable publicly. 

AWS S3 (Amazon Simple Storage Service) is a service offered by AWS that provides object storage to store very large files. 

We need to go to S3 and store our Python Script there. 

# Amazon Storage S3 

Go to the main AWS Console and go to AWS S3 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-14.png "AWS")

First create a bucket in S3. 

**A S3 Bucket** is like a folder on your laptop. However, S3 buckets are unique names because all of the files in the folder will be accessable via S3 intervaces. It should be 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-15.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-16.png "AWS")

We create bucket and allow public access to the folder. We just want to store here tiny script files and allow AWS EMR to access these files. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-18.png "AWS")

I created here a bucket with my name. You need to search for a unique bucket name and create it. 


![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-19.png "AWS")


# Go back to EMR to set up a data processing step 

Now lets go back to EMR and set up our processing step. 

In EMR it is called a **A step** which is a processing step. 

We need to set up 3 things

1. What is our python script that we want to run (an address on S3)
2. What is our input data file or folder on S3 
3. What is our result output folder on S3 

So we need to have 3 different address. 

Output folder on S3 should not exist. 
This folder will be created when your result output is generated. 
You will get an error if the output folder exist on S3. If you have created it before you can remove it before or change the folder name. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-20.png "AWS")


My python script location is : 
```s3://kiateymourian/sparkfiles/WordCount.py```

In your prgoram arguments you should add your input and output filders, like my input file and output folder:  
```s3://metcs777/WikipediaPagesOneDocPerLine1000LinesSmall.txt  s3://kiateymourian/output```

Input file locations are given to you on your assignments. 

**It is important to have at least one space between input and output locations.**


**Your script should read the input and output files from the command line arguments.**

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-21.png "AWS")

If your processing step is failing under 20 seconds, it is probably faild and you have some where in your program or your setup an error. 

You can read the log files and check again. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-22.png "AWS")


# Enabling SSH Connection if you want to see GUIs 

If you want to see the Spark GUI spark History UI then you need to use an SSH connection and set up a SOCKS proxy. 

Read the documentations on EMR 

You need to install FoxyProxy plugin for chrome or firefox to setup the proxy connection. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-23.png "AWS")



# Running Steps 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-24.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-25.png "AWS")

After your Processing step is completed you can go to output folder on S3 and check the results 

You can also see the log files for informations and potential errors. 

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-26.png "AWS")


# Computation results output on S3 
![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-27.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-28.png "AWS")


# Do not forget to terminate the EMR Cluster

![AWS](https://raw.githubusercontent.com/kiat/BigDataAnalytics/master/Installations-HowTos/sceenshots/AWS-fig-29.png "AWS")


**Do not forget to terminate your EMR. **

Reember that for the 3 machines in your cluster you are paying about .7 cents per hours. It seems to be cheap but it sums up fast when you forget it for some days. 




# Connect to the Master Node using SSH 

# How to connect to AWS EC2 machines from Mac/Linux.

The following assumes that your .pem fle is called MyFirstKeyPair.pem and that it is
located in your working directory; replace this with the actual name and location of your fle,
assuming that you called your key pair something else. 
Type:

```chmod 500 MyFirstKeyPair.pem```

Now, you can connect to your master machine **(replace “54.172.82.0” with the IP address of
your own master machine):**

ssh -i "MyFirstKeyPair.pem" ubuntu@54.172.82.0

This will give you a Linux prompt; you are connected to your master node.
Important: Never share your .pem fle. 



