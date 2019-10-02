from random import random
from abc import abstractmethod, ABCMeta

class Agent(metaclass=ABCMeta):

	@abstractmethod
	def init(self, size):
		pass

	@abstractmethod
	def evaluate(self, function):
		pass

	def __init__(self, **kwargs):
		self.genome = []
		self.fitness = None
		self.__dict__.update(kwargs)

	def __str__(self):
		return str(self.genome)
	
	def __len__(self):
		return len(self.genome)
	
	def __iter__(self):
		return iter(self.genome)

	def __next__(self):
		return next(self.genome)

	def __lt__(self, other):
		return isinstance(other, BinaryAgent) and self.fitness < other.fitness

	def __le__(self, other): return self < other or self == other
	
	def __eq__(self, other):
		return isinstance(other, BinaryAgent) and self.fitness == other.fitness

	def __ne__(self, other): return not self == other

	def __ge__(self, other): return not self < other

	def __gt__(self, other): return not self <= other

class BinaryAgent(Agent):

	def init(self, size):
		self.genome = [random() < 0.5 for _ in range(size)]

	def evaluate(self, function):
		if self.fitness is None:
			self.fitness = function(self.genome)

	def mutate(self, rate=-1):
		rate = rate if rate >= 0 else 1/len(self.genome)
		for i in range(len(self.genome)):
			if random() < rate:
				self.genome[i] = not self.genome[i]

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def __str__(self):
		S = ''
		for value in self.genome:
			S += '1' if value else '0'
		return S + ' ' + str(self.fitness)
