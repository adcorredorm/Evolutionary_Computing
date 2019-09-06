from random import random

def single_point(dim, function, descendant, replacement):
  i = 0
  vector = [random()] * dim
  while i < 1000000:
    candidate = descendant(vector, function)
    vector = replacement(vector, candidate, function)
    i += 1
  
  return vector