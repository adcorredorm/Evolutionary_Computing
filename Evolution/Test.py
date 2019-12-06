import tsplib95

# pylint: disable=import-error, no-name-in-module
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm
from PoblationalSearch.Algorithms.EvolutionStrategie import EvolutionStrategie
from PoblationalSearch.Algorithms.CoEvolution import CoEvolution

from PoblationalSearch.Agents.BinaryAgent import BinaryAgent
from PoblationalSearch.Agents.RealAgent import RealAgent
from PoblationalSearch.Agents.PermutationAgent import PermutationAgent, HPerAgent
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
    'crossover_op': crossover.multipoint_crossover(2)
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
    'mutation_op': mutation.flip_mutation(),
    'crossover_rate': 0.7,
    'crossover_op': crossover.perm_crossover(10)
}
pga = GeneticAlgorithm(**permutation_GA).execute()
print(pga.best_ind[-1])

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
es = EvolutionStrategie(**evolution_strategy).execute()
print(es.best_ind[-1])


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

tspga = GeneticAlgorithm(**tsp_GA).execute()
print(tspga.best_ind[-1])

tsp_HaEa = {
    'function': tsp,
    'ind_size': 29,
    'p_size': p_size,
    'generations': generations,
    'agent': HPerAgent
}

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

coe = CoEvolution(**Co_Evolution).execute()
print(*coe.get_best(), sep=' | ')