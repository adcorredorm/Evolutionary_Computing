from random import random

def single_point(dim, function, descendant, replacement, stop):
  i = 0
  vector = [random()] * dim
  while not stop(i, vector, function):
    candidate = descendant(vector, function)
    vector = replacement(vector, candidate, function)
    i += 1
  
  return vector