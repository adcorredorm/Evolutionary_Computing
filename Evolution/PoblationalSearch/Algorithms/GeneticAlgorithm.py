from random import random, sample
from .Algorithm import PoblationalAlgorithm

class GeneticAlgorithm(PoblationalAlgorithm):

    def __init__(self, function, ind_size, p_size, generations, agent, selection_op, mutation_op,
                crossover_rate, crossover_op, agent_args={}, **kwargs):
        self.ind_size = ind_size
        self.generations = generations
        self.crossover_rate = crossover_rate
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
            ind.fitness = self.function(ind.genome)
            population.append(ind)
        return population
  
    def stop(self, population, k):
        return self.generations <= k

    def descendant(self, population, parents):
        childs = []
        if len(parents) % 2 != 0:
            parents += sample(parents, 1)

        for i in range(0, len(parents), 2):
            p1, p2 = parents[i], parents[i+1]
            if random() < self.crossover_rate:
                h1, h2 = self.crossover_op.apply([p1, p2])
                h1 = self.mutation_op.apply([h1])[0]
                h2 = self.mutation_op.apply([h2])[0]
                h1.fitness = self.function(h1.genome)
                h2.fitness = self.function(h2.genome)
                childs += [h1, h2]
            else:
                childs += [p1, p2]
        return childs

    def replace(self, population, parents, childs):
        pop = []
        for i in range(len(parents)):
            if childs[i] <= parents[i]: pop.append(childs[i])
            else: pop.append(parents[i])
        return pop

    def grow(self, population, k):
        parents = self.select_parents.apply(population)
        childs = self.descendant(population, parents)
        return self.replace(population, parents, childs)
  