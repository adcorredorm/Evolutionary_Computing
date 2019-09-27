from random import random, randint, shuffle
from Algorithm import GeneticAlgorithm

class BinaryGA(GeneticAlgorithm):
  
  def __init__(self, p_size, function, ind_size, generations, select_parents, crossover_rate):
    super().__init__(p_size, function, ind_size, generations)
    #self.select_parents = select_parents
    self.crossover_rate = crossover_rate

  def init_population(self, p_size):
    population = []
    for _ in range(p_size):
      population.append([random() > 0.5 for _ in range(self.ind_size)])
    return population

  def select_parents(self, population, function):
    shuffle(population) #TODO:
    return population

  @classmethod
  def mutate(cls, ind):
    for value in ind:
      if random() < 1/len(ind): 
        value = not value 
    return ind

  def descendant(self, population, parents, function):
    childs = []
    for i in range(0, len(parents), 2):
      p1, p2 = parents[i], parents[i+1]
      if random() < self.crossover_rate:
        cut_point = randint(1, len(p1))
        h1 = self.mutate(p1[:cut_point] + p2[cut_point:])
        h2 = self.mutate(p2[:cut_point] + p1[cut_point:])
        childs += [h1, h2]
      else:
        childs += [p1, p2]
    return childs

  def replace(self, population, parents, childs, function):
    pop = []
    for i in range(len(parents)):
      if function(parents[i]) < function(childs[i]): pop.append(parents[i])
      else: pop.append(childs[i])
    return pop
  
def max_one(ind):
  count = 0
  for value in ind:
    if value: count += 1
  return len(ind) - count

best = BinaryGA(20, max_one, 60, 100, '', 1).execute()
for v in best:
  if v: print(1, end=' ')
  else: print(0, end=' ')
print()
print(max_one(best))