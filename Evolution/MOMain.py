# pylint: disable=import-error, no-name-in-module
import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits import mplot3d

from PoblationalSearch.Algorithms.MultiModal import MultiModal
from PoblationalSearch.Agents.CoAgent import TSPCoAgent, KPCoAgent
from PoblationalSearch.Algorithms.MultiObjective import CoMultiObjective

from MOfunctions import *
from helpers import hamming_distance
from ttp_loader import ttp_loader

import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection

problem = ttp_loader('TTP/eil51_n50_uncorr_01.ttp')

tsp = {
    'ind_size': problem.dimension,
    'p_size': 64,
    'generations': 0,
    'agent': TSPCoAgent,
    'selection_op': selection.matting_restriction(hamming_distance, 2),
    'mutation_op': mutation.tsp_mutation(mutation.perm_mutation()),
    'crossover_op': crossover.perm_crossover(problem.dimension),
    'distance': hamming_distance,
    'radious': 2
}

W = problem.capacity
item_w = [it[1] for it in problem.items]

kp = {
    'ind_size': problem.n_items,
    'p_size': 64,
    'generations': 0,
    'agent': KPCoAgent,
    'selection_op': selection.matting_restriction(hamming_distance, 2),
    'mutation_op': mutation.kp_mutation(W, item_w, mutation.bin_mutation()),
    'crossover_op': crossover.kp_crossover(W, item_w, crossover.simple_crossover()),
    'distance': hamming_distance,
    'radious': 2
}

MultiObj = {
    'functions': [total_time, utility],
    'generations': 30,
    'algorithms': [MultiModal, MultiModal],
    'alg_args': [tsp, kp]
}

mo = CoMultiObjective(**MultiObj).execute()
x = [v.objectives[0] for v in mo.last_generations[0]]
y = [v.objectives[1] for v in mo.last_generations[0]]
x.extend([v.objectives[0] for v in mo.last_generations[1]])
y.extend([v.objectives[1] for v in mo.last_generations[1]])
for i in range(len(x)):
    plt.plot(x[i], y[i], 'bo')
plt.show()