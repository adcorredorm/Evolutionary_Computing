from random import random
from .Algorithm import PoblationalAlgorithm

class HaEa(PoblationalAlgorithm):

    def __init__(self, function, p_size, generations, 
                    agent, ind_size, agent_args, operators, parents_op, **kwargs):
        super().__init__(function, p_size, **kwargs)
        self.generations = generations
        self.agent = agent
        self.ind_size = ind_size
        self.agent_args = agent_args
        self.operators = operators
        self.parents_op = parents_op

    def init_population(self, p_size):
        population = []
        for _ in range(p_size):
            ind = self.agent()
            ind.init(self.ind_size, len(self.operators), **self.agent_args)
            population.append(ind)
        self.evaluate(population)
        return population
    
    def stop(self, population, k):
        return k <= self.generations

    def select_op(self, rates):
        rand = random()
        index, acc = 0, 0
        for rate in rates:
            acc += rate
            if acc > rand:
                break
            index += 1
        return index

    def select_parents(self, arity):
        return self.parents_op.apply(self.population, arity)

    def best(self, descendant, agent):
        best = agent
        for ind in descendant:
            if ind <= best:
                best = ind 
        return best

    def normalize_rates(self, rates):
        total = sum(rates)
        return [rate/total for rate in rates]

    def grow(self, population, k):
        n_population = []
        for agent in self.population:
            rates = agent.rates
            learning = random()
            op_id = self.select_op(rates)
            op = self.operators[op_id]
            parents = self.select_parents(op.arity - 1)
            descendant = op.apply(agent, parents)
            child = self.best(descendant, agent)
            if child < agent:
                rates[op_id] *= (1 + learning)
            else:
                rates[op_id] *= (1 - learning)
            rates = self.normalize_rates(rates)
            child.rates = rates
            n_population.append(child)
        return n_population
