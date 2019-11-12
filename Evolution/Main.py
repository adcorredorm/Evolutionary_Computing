# pylint: disable=import-error, no-name-in-module
from helpers import make_experiment
from PoblationalSearch.Algorithms.PermutationGA import PermutationGA
from PoblationalSearch.Functions.Permutations import dummy
from TSP.tsp_loader import eval_tsp

args = {
    'function': eval_tsp,
    'ind_size': 29,
    'generations': 100,
    'crossover_rate': 0.7
}

p_size = 100
executions = 10
ind, stats = make_experiment(PermutationGA, args, p_size, executions)
print(min(ind))