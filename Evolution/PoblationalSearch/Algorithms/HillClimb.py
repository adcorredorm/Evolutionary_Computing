from copy import deepcopy
from random import random, sample
from .Algorithm import PoblationalAlgorithm

class HillClimb(PoblationalAlgorithm):

    def __init__(self, function, ind_size, p_size, generations, agent,  mutation_op,
                agent_args={}, **kwargs):
        self.ind_size = ind_size
        self.generations = generations
        self.agent = agent
        self.agent_args = agent_args
        self.mutation_op = mutation_op
        super().__init__(function, p_size, **kwargs)
    
    def init_population(self, p_size):
        population = []
        for _ in range(p_size):
            ind = self.agent()
            ind.init(self.ind_size, **self.agent_args)
            population.append(ind)
        return population

    def stop(self, population, k):
        return self.generations <= k

    def descendant(self, population, parents):
        childs = []
        for ind in population:
            copy = deepcopy(ind)
            child = self.mutation_op.apply([copy])
            if not self.stationary:
                self.evaluate(child)
            childs.extend(child)
        return childs
    
    def replace(self, population, parents, childs):
        pop = []
        for i in range(len(population)):
            if childs[i] <= population[i]: 
                pop.append(childs[i])
            else: pop.append(population[i])
        return pop
    
    def grow(self, population, k):
        childs = self.descendant(population, None)
        return self.replace(population, None, childs)