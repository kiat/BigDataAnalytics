# How to Create a Spark Cluster on AWS EMR 

In this tutotrial you will learn how to create a AWS EMR (ElasticMapReduce) cluster and run a python spark job on it. 

You will learn: 

1. Create an AWS EMR cluster

2. Upload a PySpark program onto the cluster

3. Run a Spark job

4. Check out the results on S3 Storage. 



# AWS Console

![AWS Educate First Page](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-1.png "AWS Educate First Page")

Click on the AWS console and open it. 

This is the main AWS console page. 


![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-2.png "AWS")




## Start Up a EMR Cluster



![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-2.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-2.png "AWS")


# AWS EC2 

Amaozn AWS EC2 (Elastic Computing) 


![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-3.png "AWS")



# How to Create your Key Pair on AWS EC2 

To connect to the cluster you will create later, you need a Key Pair as an identity.

1. Go to Amazon AWS website (aws.amazon.com).
2. Sign in with your user name and password. Go to EC2 (you can reach EC2 from the AWS services search text box).
3. Click "key pairs".
4. Click "Create Key Pair".
5. Pick a key pair name that is likely unique to you. Type it in, and click ``Create''.
6. This should create a ".pem" file that you can download. 
You will subsequently use this .pem file to connect securely to a machine over the internet. 

**IMPORTANT NOTE:** Never share your prive key .pem file with anyone (be carefull to not push it to github)


![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-4.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-5.png "AWS")


#  AWS EMR 

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-6.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-7.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-8.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-9.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-10.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-11.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-12.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-13.png "AWS")


# Amazon Storage S3 

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-14.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-15.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-16.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-18.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-19.png "AWS")


# Back to Amazon EMR to run a Job on it. 

In EMR it is called a **A step** which is a processing step. 


![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-20.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-21.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-22.png "AWS")


# Enabling SSH Connection if you want to see GUIs 

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-23.png "AWS")

# Running Steps 

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-24.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-25.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-26.png "AWS")


# Computation results output on S3 
![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-27.png "AWS")

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-28.png "AWS")

# Do not forget to terminate the EMR Cluster

![AWS](https://raw.githubusercontent.com/kiat/MET-CS777/master/HowTos/sceenshots/AWS-fig-29.png "AWS")




