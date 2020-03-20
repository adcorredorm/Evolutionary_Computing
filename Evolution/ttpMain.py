# pylint: disable=import-error
import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection

from PoblationalSearch.Agents.CoAgent import TSPCoAgent, KPCoAgent
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm
from PoblationalSearch.Algorithms.CoEvolution import CoEvolution

from ttp_loader import ttp_loader
from helpers import make_experiment

import sys

filename = sys.argv[1]

problem = ttp_loader('TTP/{}.ttp'.format(filename))

def ttp1(agents):
    tsp_id = 0 if agents[0].__class__ == TSPCoAgent else 1
    tsp_agent = agents[tsp_id].genome
    kp_agent = agents[1 - tsp_id].genome

    g = 0
    for i in range(problem.n_items):
        if kp_agent[i]:
            g += problem.items[i][0]
    
    w_c = 0
    v_c = problem.max_speed
    f = 0
    for i in range(problem.dimension):
        d = problem.get_distance(tsp_agent[i], tsp_agent[(i+1)%problem.dimension])
        for it in problem.nodes[i]['items']:
            if kp_agent[it]:
                w_c += problem.items[it][1]
        v_c = problem.max_speed - w_c*(problem.max_speed-problem.min_speed)/problem.capacity
        f += d / v_c
    
    R = problem.renting_ratio
    return R*f - g # Converted into minimization problem

tsp = {
    'ind_size': problem.dimension,
    'p_size': 64,
    'generations': 0,
    'agent': TSPCoAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.tsp_mutation(mutation.perm_mutation()),
    'crossover_rate': 0.7,
    'crossover_op': crossover.perm_crossover(problem.dimension)
}

W = problem.capacity
item_w = [it[1] for it in problem.items]

kp = {
    'ind_size': problem.n_items,
    'p_size': 64,
    'generations': 0,
    'agent': KPCoAgent,
    'selection_op': selection.elitist_tournament(),
    'mutation_op': mutation.kp_mutation(W, item_w, mutation.bin_mutation()),
    'crossover_rate': 0.7,
    'crossover_op': crossover.kp_crossover(W, item_w, crossover.simple_crossover())
}

ttp = {
    'function': ttp1,
    'generations': 1000,
    'algorithms': [GeneticAlgorithm, GeneticAlgorithm],
    'alg_args': [tsp, kp]
}

#coe = CoEvolution(**ttp).execute()
#print(*coe.get_best(), sep='\n')

res = make_experiment(filename, CoEvolution, ttp, 30)
#print(min(gen[-1] for gen in res[1]))