from abc import abstractmethod, ABCMeta
from .Tracer import Tracer

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

    def select(self, population):
        return sorted(population)[0]

    def __init__(self, function, p_size, **kwargs):
        self.function = function
        self.__dict__.update(kwargs)
        self.tracer = Tracer()

        self.population = self.init_population(p_size)
        self.tracer.add(self.population)

    def execute(self):
        k = 0
        while not self.stop(self.population, k):
            self.population = self.grow(self.population, k)
            self.tracer.add(self.population)
            k += 1
        return self.tracer
