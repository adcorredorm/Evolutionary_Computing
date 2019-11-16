from copy import deepcopy
from numpy.random import dirichlet
from numpy import zeros, ones
from random import randint, sample
from .Operator import Operator

class multipoint_crossover(Operator):

    def __init__(self, ind_size, k_points, **kwargs):
        super().__init__(**kwargs)
        assert k_points < ind_size, "Cut points must be lower than individual's size"
        self.ind_size = ind_size
        self.k_points = k_points
    
    def apply(self, agents):
        genomes = [[] for _ in range(len(agents))]
        points = sample(range(1, self.ind_size), self.k_points)
        points = sorted([0] + points + [self.ind_size])
        for i in range(len(points) - 1):
            for j in range(len(agents)):
                cut = agents[(i+j)%len(agents)].genome[points[i]:points[i+1]]
                genomes[j] += cut
        
        children = deepcopy(agents)
        for i in range(len(agents)):
            children[i].genome = genomes[i]
            children[i].fitness = None
        return children


class simple_crossover(multipoint_crossover):

    def __init__(self, ind_size, **kwargs):
        super().__init__(ind_size, 1, **kwargs)

class real_crossover(Operator):

    def __init__(self, ind_size, *params, **kwargs):
        super().__init__(**kwargs)
        self.ind_size = ind_size
        self.params = ('genome',) + params

    @staticmethod
    def recombinate(alpha, values):
        vector = zeros(len(values))
        for i in range(len(vector)):
            vector[i] = sum(alpha[j] * values[j] for j in range(len(values)))
        return vector
    
    def apply(self, agents):
        alpha = dirichlet(ones(len(agents)))
        values = {}
        for param in self.params:
            aux = [agent.__dict__[param] for agent in agents]
            values[param] = real_crossover.recombinate(alpha, aux)
        
        _cls = agents[0].__cls__
        return [_cls(**values)]

class perm_crossover(Operator):

    def __init__(self, ind_size, *params, **kwargs):
        super().__init__(**kwargs)
        self.ind_size = ind_size

    def cross_parents(self, p1, p2, point):
        gen = p1.genome[:point]
        while len(gen < self.ind_size):
            point = (point + 1)%self.ind_size
            if p2.genome[point] not in gen:
                gen.append(p2.genome[point])
        return gen

    def apply(self, agents):
        cross_point = randint(1, self.ind_size - 3)
        genomes = []
        for i in range(len(agents)):
            p1, p2 = agents[i], agents[(i+1)%len(agents)]
            genomes.append(self.cross_parents(p1, p2, cross_point))
        
        children = []
        for i in range(len(agents)):
            aux = deepcopy(agents[i])
            aux.genome = genomes[i]
            aux.fitness = None
            children.append(aux)
        return children
        