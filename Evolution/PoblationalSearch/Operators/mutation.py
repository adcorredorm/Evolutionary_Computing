from random import random, gauss, randint
from .Operator import Operator
from .fix import *

class bin_mutation(Operator):

    def apply(self, agents, rate=-1):
        agent = agents[0]
        rate = rate if rate >= 0 else 1/len(agent.genome)
        for i in range(len(agent.genome)):
            if random() < rate:
                agent.genome[i] = not agent.genome[i]
        agent.fitness = None
        return [agent]

class real_mutation(Operator):

    def apply(self, agents, rate=-1, sigma=0.1):
        agent = agents[0]
        rate = rate if rate >= 0 else 1/len(agent.genome)
        for i in range(len(agent.genome)):
            if random() < rate:
                agent.genome[i] = gauss(agent.genome[i], sigma)
        agent.fitness = None
        return [agent]

class perm_mutation(Operator):

    def apply(self, agents, rate=-1):
        agent = agents[0]
        rate = rate if rate >= 0 else 1/len(agent.genome)
        agent = agents[0]
        size = len(agent.genome)
        for i in range(size):
            if random() < rate:
                while True:
                    p = randint(0, size - 1)
                    if p != i:
                        break
                aux = agent.genome[i]
                agent.genome[i] = agent.genome[p]
                agent.genome[p] = aux
                agent.fitness = None
        return [agent]
    
class flip_mutation(Operator):

    def apply(self, agents):
        agent = agents[0]
        size = len(agent.genome)
        p1, p2 = randint(0, size - 1), randint(0, size - 1)
        p1, p2 = sorted([p1, p2])
        n_gen = agent.genome[:p1]
        n_gen += reversed(agent.genome[p1:p2])
        n_gen += agent.genome[p2:]
        agent.genome = n_gen
        agent.fitness = None
        return [agent]

class e_strategy_mutation(Operator):

    def apply(self, agents):
        agent = agents[0]
        agent.exogenous = [gauss(e, e) for e in agent.exogenous]
        for i in range(len(agent.genome)):
            agent.genome[i] = gauss(agent.genome[i], agent.exogenous[i])
        agent.fitness = None
        return [agent]

class kp_mutation(Operator):

    def __init__(self, W, item_w, mutation, **kwargs):
        super().__init__(**kwargs)
        self.mutation = mutation
        self.fix = kp_fix(W, item_w)
    
    def apply(self, agents):
        a = self.mutation.apply(agents)
        return self.fix.apply(a)

class tsp_mutation(Operator):

    def __init__(self, mutation_op, **kwargs):
        super().__init__(**kwargs)
        self.mutation_op = mutation_op

    def apply(self, agents, rate=-1):
        agents = self.mutation_op.apply(agents)
        agent = agents[0]
        rate = rate if rate >= 0 else 1/len(agent.genome)
        for i in range(len(agent.friends)):
            if random() < rate:
                agent.friends[i] = randint(0, agent.pop_sizes[i] - 1)
        return [agent]
