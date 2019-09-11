#!/bin/bash

## declare an array variable
#  mkdir tpch_scale_1 
# ./dbgen -s 1
#  mv *.tbl tpch_scale_1  


declare -a arr=("customer" "part" "lineitem" "nation" "orders" "partsupp" "region" "supplier")

## now loop through the above array
for i in "${arr[@]}"
do
   echo "$i"

   cat "tpch_scale_0.1/${i}_header.txt"  > tmp

   cat "tpch_scale_$1/$i.tbl" >> tmp

   mv tmp "tpch_scale_$1/$i.tbl"

done







