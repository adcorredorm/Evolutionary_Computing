# pylint: disable=import-error, no-name-in-module
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm

from PoblationalSearch.Agents.BinaryAgent import BinaryAgent
from PoblationalSearch.Agents.RealAgent import RealAgent
from PoblationalSearch.Agents.PermutationAgent import PermutationAgent

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
    'selection_op': selection.shuffle_selection(),
    'mutation_op': mutation.bin_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.simple_crossover(10)
}
bga = GeneticAlgorithm(**binary_GA).execute()
print(bga.best_ind[-1])

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
    'crossover_op': crossover.multipoint_crossover(10, 2)
}
rga = GeneticAlgorithm(**binary_GA).execute()
print(rga.best_ind[-1])

permutation_GA = {
    'function': dummy,
    'ind_size': 10,
    'p_size': p_size,
    'generations': generations,
    'agent': PermutationAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.perm_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.perm_crossover(10)
}
pga = GeneticAlgorithm(**permutation_GA).execute()
print(pga.best_ind[-1])