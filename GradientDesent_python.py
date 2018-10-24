from __future__ import print_function

import sys

import numpy as np
from numpy import *
from scipy import stats

# This is an implementation of Gradient Descent in python and numpy
# Data set of this example


def isfloat(value):
	try:
		float(value)
		return True
	except:
        	return False



def readData(fileName, lowFilter, highFilter):

	x=[]
	y=[]
	with open(fileName) as f:
		for i in f:
			a=i.split(",")
			if(len(a)==17):
				if(isfloat(a[5]) and isfloat(a[11])):
					if(float(a[5])!=0 and float(a[11])!=0):
						if(float(a[11])> lowFilter and float(a[11]) < highFilter):
							x.append(float(a[5]))
							y.append(float(a[11]))

	ax=np.array(x)
	ay=np.array(y)
	return np.vstack((ax, ay))



def gradient_descent_run(points, m_current, b_current, learningRate, num_iteration, precision):
	# m is the beta1
	# b is the beta 0 or Y-Intercept
	X=points[0]
	Y=points[1]
	previous_step_size=1

	N = float(len(Y))
	iters=0
	cost = 9999999999999999

	while (previous_step_size > precision and iters < num_iteration):
		y_current = (m_current * X) + b_current
		m_prev = m_current

		m_gradient = -(2/N) * sum(X * (Y - y_current))
		b_gradient = -(2/N) * sum(Y - y_current)
		new_learingRate = learningRate
# in 1100 iteration
# but more costly due to cost funtion calculation
#
#		old_cost = cost
#		cost = sum([data**2 for data in (Y - y_current)]) / N
#		if(cost<old_cost):
#			new_learingRate=learningRate*1.05
#
#		if(cost>old_cost):
#			new_learingRate=learningRate*0.5


		m_current = m_current - (new_learingRate * m_gradient)
		b_current = b_current - (new_learingRate * b_gradient)

		previous_step_size = abs(m_current - m_prev)
		iters = iters+1
		if(iters%100==0):
			print("Iteration: ", iters," Beta0 :  ",  "{0:.10f}".format(b_current) , " Beta1 : ", "{0:.10f}".format(m_current) )


	return m_current, b_current







def run(fileName):

	points = readData(fileName, 5., 100.)
# numerical Solution
	slope, intercept, r_value, p_value, std_err = stats.linregress(points[0],points[1])
	print("slope: ", slope)
	print("intercept: ", intercept)


# Gradient Descent
	starting_b=0
	starting_m=0

	learningRate=0.00001
	num_iteration=10000000
	precision = 0.00000001

	[m, b] = gradient_descent_run(points, starting_b, starting_m, learningRate, num_iteration, precision)

	print("======== Final Results ==============")
	print("Data after filter: ", points.shape)
	print("Beta0: ", b)
	print("Beta1: ", m)


if __name__ == "__main__":
	run(sys.argv[1])



# learning Rate = 0.01
# Iteration:  1200  Beta0 :   4.3509580481  Beta1 :  2.6376461370
# ======== Final Results ==============
# Data after filter:  (2, 1718496)
# Beta0:  4.350962228020886
# Beta1:  2.6376455350280423



# # learning Rate = 0.001
# Iteration:  10300  Beta0 :   4.3509000498  Beta1 :  2.6376544897
# ======== Final Results ==============
# Data after filter:  (2, 1718496)
# Beta0:  4.350903391574003
# Beta1:  2.6376540084537377


# Doing the same linear Regression with R
# R Results
# taxi <- read.csv("/home/kia/Desktop/taxi-data-sorted-small.csv" , header = F)
# taxi <-taxi[ which(taxi$V6 != 0 & taxi$V12 != 0 & taxi$V12 > 5 & taxi$V12 < 100), ]
# lm(taxi$V12~taxi$V6)

# Coefficients:
# (Intercept)      taxi$V6
#       4.351        2.638
