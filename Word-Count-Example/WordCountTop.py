from __future__ import print_function
import sys
from operator import add
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <file> <output> ", file=sys.stderr)
        exit(-1)

    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1])

    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    
    # We get the top 20 of this list sorting by number of counts 
    topWords = counts.top(20, lambda x: x[1])
    
    # now we want to store this result in a single file on the cluster. 
    dataToASingleFile = sc.parallelize(topWords).coalesce(1)

    dataToASingleFile.saveAsTextFile(sys.argv[2])

    sc.stop()
