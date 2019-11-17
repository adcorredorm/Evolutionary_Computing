from .Algorithm import PoblationalAlgorithm
from ..Agents.RealAgent import RealAgent

class EvolutionStrategie(PoblationalAlgorithm):

    def __init__(self, function, ind_size, p_size, generations, selection_op, 
            mutation_op, recombination_op, marriage_size=2, agent_args={}, **kwargs):
        self.ind_size = ind_size
        self.generations = generations
        self.marriage_size = marriage_size
        self.agent_args = agent_args
        super().__init__(function, p_size, **kwargs)

        #Operators
        self.selection_op = selection_op
        self.mutation_op = mutation_op
        self.recombination_op = recombination_op

    def init_population(self, p_size):
        population = []
        for _ in range(p_size):
            ind = RealAgent()
            ind.init(self.ind_size, exogenous=True, **self.agent_args)
            ind.fitness = self.function(ind.genome)
            population.append(ind)
        return population

    def stop(self, population, k):
        return self.generations <= k

    def replace(self, population, children):
        total = population + children
        total.sort()
        return total[:len(population)]

    def grow(self, population, k):
        children = []
        for _ in range(len(population)):
            parents = self.selection_op.apply(population, size=self.marriage_size)
            ind = self.recombination_op.apply(parents)
            ind = self.mutation_op.apply(ind)[0]
            ind.fitness = self.function(ind.genome)
            children.append(ind)
        return self.replace(population, children)
    