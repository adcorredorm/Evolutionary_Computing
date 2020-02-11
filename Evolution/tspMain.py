# pylint: disable=import-error, no-name-in-module
import os
import tsplib95
import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm
from PoblationalSearch.Agents.PermutationAgent import PermutationAgent
from helpers import make_experiment

tsp_path = os.path.dirname(os.path.abspath(__file__)) + '/TSP/fl1400.tsp'
tsp_problem = tsplib95.load_problem(tsp_path)
def tsp(genome):
    count = 0
    for i in range(len(genome) - 1):
        count += tsp_problem.wfunc(genome[i]+1, genome[i + 1]+1)
    return count + tsp_problem.wfunc(genome[-1]+1, genome[0]+1)

p_size = 100
generations = 100

tsp_GA = {
    'function': tsp,
    'ind_size': tsp_problem.dimension,
    'p_size': p_size,
    'generations': generations,
    'agent': PermutationAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.flip_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.perm_crossover(tsp_problem.dimension)
}

hc = {
    'function': tsp,
    'ind_size': tsp_problem.dimension,
    'p_size': p_size,
    'generations': generations,
    'agent': PermutationAgent,
    'mutation_op': mutation.flip_mutation(),
}

res = make_experiment('TSP_fl1400.txt',GeneticAlgorithm, tsp_GA, 30, hc)
print(min(gen[-1] for gen in res[1]))