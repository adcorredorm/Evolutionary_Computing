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

  def select(self, population):
    return min(population)

  def __init__(self, function, **kwargs):
    self.function = function
    self.__dict__.update(kwargs)

  def execute(self, p_size):
    k = 0
    stats = []
    population = self.init_population(p_size)
    while not self.stop(population, k):
      population = self.grow(population, k)
      stats.append(self.select(population).fitness)
      k += 1
    return (self.select(population), stats)
