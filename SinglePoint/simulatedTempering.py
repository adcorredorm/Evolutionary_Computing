from random import random
from hillClimb import descendant
from gereralAlg import single_point

def cool_scheme():
    return random()

def replacement(x, y, function):
  if function(x) <= function(y) or random() <= cool_scheme():
    return x
  return y

def tempering(n, function, stop):
  return single_point(n, function, descendant, replacement, stop)

function = lambda x : 3*(x[0]**2) - 2*x[0] - 10
stop = lambda i, vector, function: i >= 100000
x = tempering(1, function, stop)
print(x)
print(function(x))
