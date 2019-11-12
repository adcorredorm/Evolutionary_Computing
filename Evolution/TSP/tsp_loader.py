import tsplib95
import os
import random

# bays29 solution 2020

problem = tsplib95.load_problem('TSP/bays29.tsp')

def eval_tsp(ind):
    count = 0
    for i in range(29):
        count += problem.wfunc(ind[i] + 1, ind[(i+1)%29] + 1)
    return count