from random import random, sample
from .Algorithm import PoblationalAlgorithm

class MultiModal(PoblationalAlgorithm):

    def __init__(self, function, ind_size, p_size, generations, agent, selection_op, mutation_op,
                crossover_op, distance, radious, agent_args={}, **kwargs):
        self.ind_size = ind_size
        self.generations = generations
        self.distance = distance
        self.radious = radious
        self.agent = agent
        self.agent_args = agent_args
        super().__init__(function, p_size, **kwargs)

        #Operators
        self.select_parents = selection_op
        self.mutation_op = mutation_op
        self.crossover_op = crossover_op

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
        if len(parents) % 2 != 0:
            parents += sample(parents, 1)

        for i in range(len(parents)):
            p1, p2 = population[i], parents[i]
            h1, h2 = self.crossover_op.apply([p1, p2])
            h1 = self.mutation_op.apply([h1])[0]
            h2 = self.mutation_op.apply([h2])[0]
            if not self.stationary:
                self.evaluate([h1, h2])
            childs += [h1, h2]
        return childs

    #deterministic crowding
    def replace(self, population, parents, childs):
        #return childs
        pop = []
        for i in range(len(population)):
            p1 = population[i]
            h1, h2 = childs[2*i], childs[2*i + 1]
            d1, d2 = self.distance(p1.genome, h1.genome), self.distance(p1.genome, h2.genome)
            if d1 < d2:
                if d1 <= self.radious and h1 <= p1:
                    pop.append(h1)
                elif d2 <= self.radious and h2 <= p1:
                    pop.append(h2)
                else:
                    pop.append(p1)
            else:
                if d2 <= self.radious and h2 <= p1:
                    pop.append(h2)
                elif d1 <= self.radious and h1 <= p1:
                    pop.append(h1)
                else:
                    pop.append(p1)
        return pop

    def grow(self, population, k):
        parents = self.select_parents.apply(population)
        childs = self.descendant(population, parents)
        return self.replace(population, parents, childs)
    
    def hamming_distance(self, A, B):
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
        return count