from multiprocessing import Process
from random import random
from gereralAlg import single_point

def descendant(vector, function):
  return [component + (random()*2) - 1 for component in vector]

def replacement(x, y, function):
  if function(x) <= function(y):
    return x
  return y

def hillClimb(n, function, stop):
  return single_point(n, function, descendant, replacement, stop)

def parallelHC(n, function, stop, threads):
    th = []
    for _ in range(threads):
        t = Process(target=hillClimb, args=(n, function, stop))
        th.append(t)
        t.start()
    [t.join() for t in th]

function = lambda x : 3*(x[0]**2) - 2*x[0] - 10
stop = lambda i, vector, function: i >= 100000
x = hillClimb(1, function, stop)
print(x)
print(function(x))
