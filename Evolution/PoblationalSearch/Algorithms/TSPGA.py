import tsplib95
from random import shuffle
from ..Agents.PermutationAgent import PermutationAgent
from .GeneticAlgorithm import GeneticAlgorithm

class TSPAgent(PermutationAgent):
    
    def init(self, size):
        self.genome = [i+2 for i in range(size)]
        shuffle(self.genome)

    def __str__(self):
        S = '[1,'
        for value in self.genome:
            S += str(value) + ','
        return S[:-1] + '] ' + '{:0.2f}'.format(self.fitness)


class TSPGA(GeneticAlgorithm):

    def evaluate(self, genome):
        fenotipe = [1] + genome
        count = 0
        for i in range(self.ind_size):
            count += self.problem.wfunc(fenotipe[i], fenotipe[(i+1)%self.ind_size])
        return count
    
    def cross_parents(self, p1, p2, point):
        child = p1.genome[:point]
        while len(child) < len(p1):
            point = (point + 1)%len(p1)
            if p2.genome[point] not in child:
                child.append(p2.genome[point])
        return child

    def __init__(self, tsp_path, generations, crossover_rate, **kwargs):
        self.problem = tsplib95.load_problem(tsp_path)
        super().__init__(
            self.evaluate, self.problem.dimension - 1, generations, crossover_rate,
            TSPAgent, **kwargs)