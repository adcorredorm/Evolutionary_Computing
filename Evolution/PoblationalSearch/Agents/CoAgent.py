from abc import abstractmethod, ABCMeta
from random import randint
from .Agent import Agent
from .PermutationAgent import TSPAgent

class CoAgent(metaclass=ABCMeta):

	@abstractmethod
	def get_friends(self):
		pass

class TSPCoAgent(TSPAgent, CoAgent):

	def init(self, size, pop_sizes, **kwargs):
		super().init(size, kwargs)
		self.pop_sizes = pop_sizes
		self.friends = [randint(0, p_size - 1) for p_size in pop_sizes]

	def get_friends(self):
		return self.friends
	
	def mutate(self):
		super().mutate()
		selected = randint(0, len(self.friends))
		self.friends[selected] = randint(0, self.pop_sizes[selected] - 1)
