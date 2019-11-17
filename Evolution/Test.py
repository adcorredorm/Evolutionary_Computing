# pylint: disable=import-error, no-name-in-module
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm
from PoblationalSearch.Agents.BinaryAgent import BinaryAgent
from PoblationalSearch.Functions.Binary import max_one

import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection

p_size = 10
generations = 20

binary_GA = {
    'function': max_one,
    'ind_size': 10,
    'p_size': p_size,
    'generations': generations,
    'agent': BinaryAgent,
    'selection_op': selection.shuffle_selection(),
    'mutation_op': mutation.bin_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.simple_crossover(100)
}
bga = GeneticAlgorithm(**binary_GA).execute()
print(bga.best_ind[-1])