import tsplib95
import math

# pylint: disable=import-error, no-name-in-module
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm
from PoblationalSearch.Algorithms.EvolutionStrategie import EvolutionStrategie
from PoblationalSearch.Algorithms.CoEvolution import CoEvolution
from PoblationalSearch.Algorithms.MultiModal import MultiModal

from PoblationalSearch.Agents.BinaryAgent import BinaryAgent
from PoblationalSearch.Agents.RealAgent import RealAgent
from PoblationalSearch.Agents.PermutationAgent import PermutationAgent
from PoblationalSearch.Agents.CoAgent import KPCoAgent

from PoblationalSearch.Functions.Binary import max_one
from PoblationalSearch.Functions.Real import ackley, michalewicz, rastrigin
from PoblationalSearch.Functions.Permutations import dummy

import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection

p_size = 100
generations = 100

binary_GA = {
    'function': max_one,
    'ind_size': 10,
    'p_size': p_size,
    'generations': generations,
    'agent': BinaryAgent,
    'selection_op': selection.uniform_selection(),
    'mutation_op': mutation.bin_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.simple_crossover()
}
#bga = GeneticAlgorithm(**binary_GA).execute()
#print(bga.best_ind[-1])

binary_GA = {
    'function': ackley,
    'ind_size': 5,
    'p_size': p_size,
    'generations': generations,
    'agent': RealAgent,
    'agent_args': {
        '_min': -32.768,
        '_max': 32.768
    },
    'selection_op': selection.tournament_selection(),
    'mutation_op': mutation.real_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.multipoint_crossover(2)
}
#rga = GeneticAlgorithm(**binary_GA).execute()
#print(rga.best_ind[-1])

permutation_GA = {
    'function': dummy,
    'ind_size': 10,
    'p_size': p_size,
    'generations': generations,
    'agent': PermutationAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.flip_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.perm_crossover(10)
}
#pga = GeneticAlgorithm(**permutation_GA).execute()
#print(pga.best_ind[-1])

evolution_strategy = {
    'function': ackley,
    'ind_size': 5,
    'p_size': p_size,
    'generations': generations,
    'selection_op': selection.random_selection(),
    'mutation_op': mutation.e_strategy_mutation(),
    'recombination_op': crossover.real_crossover(5, 'exogenous'),
    'marriage_size': 2,
    'agent_args': {
        '_min': -32.768,
        '_max': 32.768
    },
}
#es = EvolutionStrategie(**evolution_strategy).execute()
#print(es.best_ind[-1])


def tsp(genome):
    tsp_path = 'TSP/bays29.tsp'
    tsp_problem = tsplib95.load_problem(tsp_path)

    count = 0
    for i in range(len(genome) - 1):
        count += tsp_problem.wfunc(genome[i]+1, genome[i + 1]+1)
    return count + tsp_problem.wfunc(genome[-1]+1, genome[0]+1)

tsp_GA = {
    'function': tsp,
    'ind_size': 29,
    'p_size': p_size,
    'generations': generations,
    'agent': PermutationAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.perm_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.perm_crossover(29)
}

#tspga = GeneticAlgorithm(**tsp_GA).execute()
#print(tspga.best_ind[-1])

def coFunction(agents):
    total = 0
    for agent in agents:
        total += max_one(agent.genome[:agent.size])
    return total

test_co = {
    'ind_size': 10,
    'p_size': 16,
    'generations': generations,
    'agent': KPCoAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.bin_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.simple_crossover()
}

test_co2 = {
    'ind_size': 15,
    'p_size': 16,
    'generations': generations,
    'agent': KPCoAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.bin_mutation(),
    'crossover_rate': 0.9,
    'crossover_op': crossover.simple_crossover()
}

Co_Evolution = {
    'function': coFunction,
    'generations': generations,
    'algorithms': [GeneticAlgorithm, GeneticAlgorithm],
    'alg_args': [test_co, test_co2]
}

#coe = CoEvolution(**Co_Evolution).execute()
#print(*coe.get_best(), sep=' | ')

def euclidean(A, B):
    s = 0
    for i in range(len(A)):
        s += (A[i] - B[i])**2
    return math.sqrt(s)

mm = {
    'function': rastrigin,
    'ind_size': 2,
    'p_size': 20,
    'generations': 20,
    'agent': RealAgent,
    'selection_op': selection.matting_restriction(euclidean, 1),
    'mutation_op': mutation.real_mutation(),
    'crossover_op': crossover.simple_crossover(),
    'distance': euclidean,
    'radious': 1,
    'agent_args': {
        '_min': -5.12,
        '_max': 5.12
    }
}

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

mm = MultiModal(**mm).execute()

x = [v.genome[0] for v in mm.last_generation]
y = [v.genome[1] for v in mm.last_generation]
z = [v.fitness for v in mm.last_generation]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z, 'gray')
plt.show()
