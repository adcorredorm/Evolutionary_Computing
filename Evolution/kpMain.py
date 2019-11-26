# pylint: disable=import-error, no-name-in-module
import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm
from PoblationalSearch.Agents.BinaryAgent import BinaryAgent
from helpers import make_experiment

def load_problem(path):
    with open(path) as file:
        dim, W = file.readline().strip().split(' ')
        values = []
        weigths = []
        for line in file.readlines():
            v, w = line.strip().split(' ')
            values.append(float(v))
            weigths.append(float(w))
    return int(dim), float(W), values, weigths

dim, W, values, weigths = load_problem('KP/kp20.kp')

def kp_function(agent):
    plan = agent
    total = 0
    for i in range(len(plan)):
        if plan[i]:
            total += values[i]
    return - total

kp = {
    'function': kp_function,
    'ind_size': dim,
    'p_size': 100,
    'generations': 100,
    'agent': BinaryAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.kp_mutation(W, weigths, mutation.bin_mutation()),
    'crossover_rate': 1,
    'crossover_op': crossover.kp_crossover(W, weigths, crossover.simple_crossover())
}

res = make_experiment(GeneticAlgorithm, kp, 10)
print(min(gen[-1] for gen in res[1]))