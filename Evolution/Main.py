# pylint: disable=import-error, no-name-in-module
from helpers import make_experiment
from PoblationalSearch.Algorithms.PermutationGA import PermutationGA
from PoblationalSearch.Functions.Permutations import dummy

args = {
    'function': dummy,
    'ind_size': 30,
    'generations': 100,
    'crossover_rate': 0.7
}

p_size = 100
executions = 10
make_experiment(PermutationGA, args, p_size, executions)
