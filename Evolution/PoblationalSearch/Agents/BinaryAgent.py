from random import random
from .Agent import Agent

class BinaryAgent(Agent):

	def init(self, size, **kwargs):
		self.genome = [random() < 0.5 for _ in range(size)]

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
