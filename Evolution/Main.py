# pylint: disable=import-error, no-name-in-module
from helpers import make_experiment
from PoblationalSearch.Algorithms.TSPGA import TSPGA
from PoblationalSearch.Functions.Permutations import dummy

args = {
    #'function': dummy,
    #'ind_size': 29,
    'tsp_path': 'TSP/bays29.tsp',
    'generations': 100,
    'crossover_rate': 0.7
}

p_size = 100
executions = 10
ind, stats = make_experiment(TSPGA, args, p_size, executions)
print(min(ind))