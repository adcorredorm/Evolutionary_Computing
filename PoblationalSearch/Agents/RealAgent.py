from random import random, gauss
from Agents.Agent import Agent

class RealAgent(Agent):

	def init(self, size, _min=0, _max=1):
		self.genome = [random()*(_max - _min) + _min for _ in range(size)]

	def evaluate(self, function):
		if self.fitness is None:
			self.fitness = function(self.genome)

	def mutate(self, sigma=0.1, rate=-1):
		rate = rate if rate >= 0 else 1/len(self.genome)
		for i in range(len(self.genome)):
			if random() < rate:
				self.genome[i] = gauss(self.genome[i], sigma)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def __str__(self):
		S = ''
		ft = '{:0.4f} '
		for value in self.genome:
			S += ft.format(value)
		return S + '| ' + ft.format(self.fitness)
