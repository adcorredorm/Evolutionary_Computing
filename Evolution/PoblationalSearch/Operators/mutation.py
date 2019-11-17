from random import random, gauss, randint
from .Operator import Operator

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

    def apply(self, agents):
        agent = agents[0]
        size = len(agent.genome)
        p1, p2 = randint(0, size - 1), randint(0, size - 1)
        aux = agent.genome[p1]
        agent.genome[p1] = agent.genome[p2]
        agent.genome[p2] = aux
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
