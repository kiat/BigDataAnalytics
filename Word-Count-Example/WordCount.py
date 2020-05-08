from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <file> <output> ", file=sys.stderr)
        exit(-1)
        
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1])
    
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    
    counts.saveAsTextFile(sys.argv[2])
    
    sc.stop()
