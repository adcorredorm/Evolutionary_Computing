# pylint: disable=import-error, no-name-in-module
import tsplib95
import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm
from PoblationalSearch.Agents.PermutationAgent import PermutationAgent
from helpers import make_experiment

tsp_path = 'TSP/eil51.tsp'
tsp_problem = tsplib95.load_problem(tsp_path)
def tsp(genome):
    count = 0
    for i in range(len(genome) - 1):
        count += tsp_problem.wfunc(genome[i]+1, genome[i + 1]+1)
    return count + tsp_problem.wfunc(genome[-1]+1, genome[0]+1)

tsp_GA = {
    'function': tsp,
    'ind_size': 51,
    'p_size': 100,
    'generations': 100,
    'agent': PermutationAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.flip_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.perm_crossover(51)
}

res = make_experiment(GeneticAlgorithm, tsp_GA, 10)
print(min(gen[-1] for gen in res[1]))