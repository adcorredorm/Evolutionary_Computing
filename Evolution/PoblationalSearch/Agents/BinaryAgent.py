from random import random
from .Agent import Agent

class BinaryAgent(Agent):

	def init(self, size, **kwargs):
		self.__dict__.update(kwargs)
		self.genome = [random() < 0.5 for _ in range(size)]

	def __str__(self):
		S = ''
		for value in self.genome:
			S += '1' if value else '0'
		return S + ' ' + str(self.fitness)
