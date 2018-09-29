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
from pyspark.sql.functions import udf
from pyspark.sql.functions import *
from pyspark.sql.functions import array



# if __name__ == "__main__":
    # create spark configuration
#     conf = SparkConf(appName="TPCH-Example")
    # create spark context with the above configuration
#    sc = SparkContext(conf=conf)



# lineitems = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(sys.arg[1])
path="file:////home/kia/GIT/MET-CS777/data/tpch_tables_scale_0.1/"
# path is where you have the folder. It can be a distributed path like S3, gc or hdfs

customer = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(path+"customer.tbl")
orders = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(path+"orders.tbl")
lineitems = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(path+"lineitem.tbl")
part = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(path+"part.tbl")
supplier = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(path+"supplier.tbl")
partsupp = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(path+"partsupp.tbl")
region = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(path+"region.tbl")
nation = sqlContext.read.format('csv').options(header='true', inferSchema='true',  sep ="|").load(path+"nation.tbl")


# You can convert all to RDDs if you want. 
# customerRDD=customer.rdd
# ordersRDD=orders.rdd
# lineitemsRDD=lineitems.rdd
# partRDD=part.rdd
# supplierRDD=supplier.rdd
# partsuppRDD=partsupp.rdd
# regionRDD=region.rdd
# nationRDD=nation.rdd



# Question 1
# Implement a pyspark code that can find out the top-10 sold products. 

lines = lineitems.select("ORDERKEY", "PARTKEY")\
		 .withColumn("COUNT", lit(1))\
		 .groupBy("PARTKEY").agg(func.sum("COUNT"))

result_1 = lines.orderBy("sum(COUNT)", ascending=False).limit(10).show()
result_1.saveAsTextFile(sys.arg[2])



# ---------------------------------------------------------------------------
# Question 2

# Find the top-10 customers based on the number of products ordered.


order_parts = lineitems.select("ORDERKEY", "PARTKEY")

customer_orders = orders.select("ORDERKEY", "CUSTKEY")


# Here we get the a table of all customers and their ordered parts. 
customer_parts = customer_orders.join(order_parts, customer_orders.ORDERKEY == order_parts.ORDERKEY , 'full' ).drop('ORDERKEY')


# After we have a table of (CUSTKEY, ORDERKEY), we can just count up the number of times that we see the customer key in the table for each customer 
# And this is a the number of times that the customer ordered parts. 
customer_parts.withColumn("COUNT", lit(1)).groupBy("CUSTKEY").agg(func.sum("COUNT")).orderBy("sum(COUNT)", ascending=False).limit(10).show()

# +-------+----------+                                                            
# |CUSTKEY|sum(COUNT)|
# +-------+----------+
# |   8362|       155|
# |    346|       153|
# |  14707|       149|
# |  11998|       148|
# |   9454|       148|
# |  14398|       147|
# |     85|       142|
# |  10354|       142|
# |   3709|       141|
# |    547|       141|
# +-------+----------+



# ---------------------------------------------------------------------------

# Question 3
# Find the top-10 customers that have ordered products from the same supplier. 


partsupp_keys=partsupp.select("PARTKEY", "SUPPKEY")

custpmer_supplier=customer_parts.join(partsupp_keys, customer_parts.PARTKEY == partsupp.PARTKEY , 'full'  ).drop('PARTKEY')

custpmer_supplier.withColumn("COUNT", lit(1)).groupBy("CUSTKEY", "SUPPKEY").agg(func.sum("COUNT")).orderBy("sum(COUNT)", ascending=False).limit(10).show()

# +-------+-------+----------+                                                    
# |CUSTKEY|SUPPKEY|sum(COUNT)|
# +-------+-------+----------+
# |   4567|    844|         7|
# |   4792|    592|         6|
# |  11809|     17|         6|
# |  14767|      8|         6|
# |   2173|    572|         6|
# |   6139|    233|         6|
# |    874|    430|         6|
# |    154|    380|         5|
# |   6889|    729|         5|
# |   8794|    545|         5|
# +-------+-------+----------+




# ---------------------------------------------------------------------------
# Question 4 and 5
# Find the customers who have not ordered products from their own country and have ordered only foreign products. 


# Solution: 
# We get from custpmer_supplier CUSTKEY and SUPPKEY
# custpmer_supplier.show()
# +-------+-------+                                                               
# |CUSTKEY|SUPPKEY|
# +-------+-------+
# |   9733|    149|
# |   9733|    399|
# |   9733|    649|
# ... 



# We need to just check if the customer has ordered something from his own country.


custpmer_supplier.show()


customer_nationKey = customer.select("CUSTKEY", "NATIONKEY")
supplier_nationKey = supplier.select("SUPPKEY", "NATIONKEY")



custpmer_supplier_custNation = custpmer_supplier.join(customer_nationKey, "CUSTKEY", 'full')
custpmer_supplier_supNation = custpmer_supplier.join(supplier_nationKey, "SUPPKEY", 'full')



from pyspark.sql import functions as F
from pyspark.sql.functions import udf

custpmer_supplier_custNation_agg = custpmer_supplier_custNation.groupBy("CUSTKEY").agg(F.collect_set("NATIONKEY").alias('agg_nation'))

cSN_agg_withSupp = custpmer_supplier_custNation.join(custpmer_supplier_custNation_agg, "CUSTKEY" , 'full')

# We need to cast the NationKey to IntegerType
cSN_agg_withSupp = cSN_agg_withSupp.withColumn("NATIONKEY", cSN_agg_withSupp["NATIONKEY"].cast(IntegerType()))

# Check Schema 
cSN_agg_withSupp.printSchema()



# Define a UDF to check if the nation of the customer is in the list of his orders_products_nations

isIn_udf = udf(lambda element, mlist: True if element in  mlist else False, BooleanType())

from_own = cSN_agg_withSupp.withColumn("from_own", isIn_udf(cSN_agg_withSupp.NATIONKEY, cSN_agg_withSupp.agg_nation))

# Should return none after filter because we have no customer that have not ordered products from his own country. 
from_own.filter(from_own.from_own==False).show()

# from_own.show()
# +-------+-------+---------+----------+--------+                                 
# |CUSTKEY|SUPPKEY|NATIONKEY|agg_nation|from_own|
# +-------+-------+---------+----------+--------+
# +-------+-------+---------+----------+--------+






# ---------------------------------------------------------------------------
# Question 6
# Find the top-10 similar customers based of their orders. (Jaccard Similarity)
# First of all we collect all of the products that each customer ordered. 



custoemr_partset=customer_parts.groupBy("CUSTKEY").agg(F.collect_set("PARTKEY").alias('product_list'))

# Do the cross join and rename fields 

customers_parts_combi = custoemr_partset.crossJoin(custoemr_partset ).toDF("C1", "L1", "C2" , "L2").filter("C1 not like C2")

# then we can drop duplicates which might take longer time. 
customers_parts_combi = customers_parts_combi.dropDuplicates(['C1','C2'])

# Define a user defined function for calculation of Jaccard similarity distance
# Return type is Float and it should defined. 
jaccard = udf(lambda a, b:  float(float( len(set(a) & set(b)))  / len( set(a) | set(b) )) , FloatType())

customer_jaccard = customers_parts_combi.withColumn("jaccard", jaccard(customers_parts_combi.L1, customers_parts_combi.L2))

# The following line will cause large number of computation tasks. 
customer_jaccard.orderBy("jaccard", ascending=False).limit(10).show()

# On TPCH scale 0.1 you can get the following results 

# +-----+--------------------+-----+--------------------+----------+              
# |   C1|                  L1|   C2|                  L2|   jaccard|
# +-----+--------------------+-----+--------------------+----------+
# |10376|[13032, 18343, 15...| 8456|[15747, 18343, 41...|0.09090909|
# | 8456|[15747, 18343, 41...|10376|[13032, 18343, 15...|0.09090909|
# | 4808|[17169, 19122, 33...|10901|[10142, 9529, 124...|0.06666667|
# |10901|[10142, 9529, 124...| 4808|[17169, 19122, 33...|0.06666667|
# | 7532|[15572, 2151, 174...| 5390|[5452, 16969, 755...|0.06451613|
# | 5390|[5452, 16969, 755...| 7532|[15572, 2151, 174...|0.06451613|
# | 2489|[6418, 7101, 7102...| 4283|[13060, 12044, 12...|0.06349207|
# | 4283|[13060, 12044, 12...| 2489|[6418, 7101, 7102...|0.06349207|
# | 7739|[9743, 16030, 489...| 5462|[6890, 7231, 1737...|    0.0625|
# | 4385|[1648, 7100, 1122...| 2768|[19866, 1648, 123...|    0.0625|
# +-----+--------------------+-----+--------------------+----------+

# The most similar customers are 10376 and 8456


# ---------------------------------------------------------------------------
# Question 7
# Find the top-10 product pairs that are ordered mostly together. 



# RDD solution 
# Easier to do it in RDD

lineitemsRDD = sqlContext.read.format('csv').options(header='true', inferSchema='false',  sep ="|").load(path+"lineitem.tbl").rdd
orderPartsRDD = lineitemsRDD.map(lambda x: (x[0], x[1]))


order_PartList_RDD = orderPartsRDD.combineByKey(lambda x: [x], lambda u, v: u + [v], lambda u1,u2: u1+u2).map(lambda x:(x[0], list(x[1]))).filter(lambda x: len(x[1])>1)

from itertools import combinations

order_PartPermutList_RDD=  order_PartList_RDD .flatMap(lambda x:  combinations(x[1], 2) ).map(lambda x: ((x[0], x[1] ), 1))
order_PartPermutList_RDD.reduceByKey(lambda a, b:a+b).top(10, lambda x: x[1])







# Dataframe
from pyspark.sql import functions as F
order_parts = lineitems.select("ORDERKEY", "PARTKEY")

partLists= order_parts.groupBy("ORDERKEY").agg(F.collect_set("PARTKEY").alias('listParts'))


# Process only pairs of products - remove orders that include only one single product. 

partLists= partLists.where(size(col("listParts")) >  1)

# Define a function to create all pair combinations. 
# You can also use itertools 
# import itertools
# from itertools import permutations

# I define here the following permutation function. 
def permut(x):
	a=list()        
	for i in range(len(x)):
		for j in range(i, len(x)):
			if(i != j):
				a.append(str(x[i])+"-"+str(x[j]))
	return a 


# ... 

