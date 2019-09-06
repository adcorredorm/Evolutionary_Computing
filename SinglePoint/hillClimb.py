from random import random
from gereralAlg import single_point

def descendant(vector, function):
  return [component + (random()*2) - 1 for component in vector]

def replacement(x, y, function):
  if function(x) <= function(y):
    return x
  return y

def hillClimb(n, function):
  return single_point(n, function, descendant, replacement)

function = lambda x : 3*(x[0]**2) - 2*x[0] - 10
x = hillClimb(1, function)
print(x)
print(function(x))
