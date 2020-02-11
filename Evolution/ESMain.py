# pylint: disable=import-error, no-name-in-module
import math
from PoblationalSearch.Functions.Real import ackley, michalewicz, rastrigin
from PoblationalSearch.Agents.RealAgent import RealAgent
from PoblationalSearch.Algorithms.EvolutionStrategie import EvolutionStrategie
import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection
from helpers import make_experiment

function = ackley
ind_size = 20
p_size = 100
generations = 100
args = {
    '_min': -32.768,
    '_max': 32.768
}

evolution_strategy = {
    'function': function,
    'ind_size': ind_size,
    'p_size': p_size,
    'generations': generations,
    'selection_op': selection.random_selection(),
    'mutation_op': mutation.e_strategy_mutation(),
    'recombination_op': crossover.real_crossover(ind_size, 'exogenous'),
    'marriage_size': 2,
    'agent_args': args,
}

hc = {
    'function': function,
    'ind_size': ind_size,
    'agent': RealAgent,
    'p_size': p_size,
    'generations': generations,
    'mutation_op': mutation.real_mutation(),
    'agent_args': args,
}

binary_GA = {
    'function': function,
    'ind_size': ind_size,
    'p_size': p_size,
    'generations': generations,
    'agent': RealAgent,
    'agent_args': args,
    'selection_op': selection.tournament_selection(),
    'mutation_op': mutation.real_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.multipoint_crossover(1)
}

res = make_experiment('ESvsGA_ackley.txt',EvolutionStrategie, evolution_strategy, 30, binary_GA)
print(min(gen[-1] for gen in res[1]))