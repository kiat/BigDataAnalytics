from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
import sys
import requests
from operator import add

from pyspark.sql.types import *
from pyspark.sql import functions as func
from pyspark.sql.functions import lit




if __name__ == "__main__":
    

    # create spark configuration
    conf = SparkConf(appName="TPCH-Example")

    # create spark context with the above configuration
    sc = SparkContext(conf=conf)


    # lineitems = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load("file:////Users/kiat/git/MET-CS777/data/tpch_tables_scale_0.1/lineitem.tbl")

    lineitems = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(sys.arg[1])



    




# Question 1
# Implement a pyspark code that can find out the top-10 sold products. 

    lines = lineitems.select("ORDERKEY", "PARTKEY")\
    .withColumn("COUNT", lit(1))
    .groupBy("PARTKEY").agg(func.sum("COUNT"))\

    result_1 = lines.orderBy("sum(COUNT)", ascending=False).limit(10).show()
    result_1.saveAsTextFile(sys.arg[2])



# Something like this with RDD... 
# orders.map(lambda p: (p[0], p[2]*p[3]) ).reduceByKey(lambda (a,b): a+b).top(10, lambda x: x[1])





# ---------------------------------------------------------------------------
# Question 2

# Find the top-10 customers based on the number of products ordered.





# ---------------------------------------------------------------------------

# Question 3
# Find the top-10 customers that have ordered products from the same supplier. 





# ---------------------------------------------------------------------------
# Question 4 and 5
# Find the customers who have not ordered
# products from their own country and have ordered only foreign products. 

# Get customer and Orderd countries from product table 





# ---------------------------------------------------------------------------
# Question 6
# Find the top-10 similar customers based of their orders. (Jaccard Similarity)
# First of all we collect all of the products that each customer ordered. 




# ---------------------------------------------------------------------------
# Question 7
# Implement a pyspark code that can find the top-10 products pairs that are ordered mostly together. 














    
    sc.stop()
