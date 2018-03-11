# l_1 and l_infinity regression using cvxpy
import numpy as np
import cvxpy as cvx
import matplotlib as mp

# generate a synthetic dataset

# actual parameter values
a_act = 2
b_act = 5

# Number of points in dataset
N = 100

# Noise magnitude
mag = 30

# datapoints
x = np.arange(0,N)
y = a_act * x + b_act + np.random.normal(0,mag,N)

# Scatter plot of data
mp.pyplot.scatter(x,y)

