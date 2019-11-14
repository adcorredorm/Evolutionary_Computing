from random import random, gauss, randint
from .Operator import Operator

class bin_mutation(Operator):

    def apply(self, agents, rate=-1, **kwargs):
        agent = agents[0]
        rate = rate if rate >= 0 else 1/len(agent.genome)
        for i in range(len(agent.genome)):
            if random() < rate:
                agent.genome[i] = not agent.genome[i]
        return [agents]

class real_mutation(Operator):

    def apply(self, agents, rate=-1, sigma=0.1, **kwargs):
        agent = agents[0]
        rate = rate if rate >= 0 else 1/len(agent.genome)
        for i in range(len(agent.genome)):
            if random() < rate:
                agent.genome[i] = gauss(agent.genome[i], sigma)
        return [agent]

class perm_mutation(Operator):

    def apply(self, agents, **kwargs):
        agent = agents[0]
        size = len(agent.genome)
        p1, p2 = randint(0, size - 1), randint(0, size - 1)
        aux = agent.genome[p1]
        agent.genome[p1] = agent.genome[p2]
        agent.genome[p2] = aux
        return [agent]