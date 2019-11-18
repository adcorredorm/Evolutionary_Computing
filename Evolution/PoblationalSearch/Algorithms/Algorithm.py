from abc import abstractmethod, ABCMeta

class PoblationalAlgorithm(metaclass=ABCMeta):

    @abstractmethod
    def init_population(self, p_size):
        pass

    @abstractmethod
    def stop(self, population, k):
        pass

    @abstractmethod
    def grow(self, population, k):
        pass

    def evaluate(self, agents):
        for agent in agents:
            agent.fitness = self.function(agent.genome)

    def select(self, population):
        return sorted(population)[0]

    def __init__(self, function, p_size, tracer=True, **kwargs):
        self.function = function
        self.__dict__.update(kwargs)
        self.population = self.init_population(p_size)
        
        self.tracer_on = tracer
        if tracer:
            self.tracer = Tracer()
            self.tracer.add(self.population)

    def execute(self):
        k = 0
        while not self.stop(self.population, k):
            self.population = self.grow(self.population, k)
            if self.tracer_on:
                self.tracer.add(self.population)
            k += 1
        return self.tracer


class Tracer():

    def __init__(self):
        self.best_ind = []
        self.best_fit = []
        self.last_generation = None

    def add(self, population):
        best = sorted(population)[0]
        self.best_ind.append(best)
        self.best_fit.append(best.fitness)
        self.last_generation = population