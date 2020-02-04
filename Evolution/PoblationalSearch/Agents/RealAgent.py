from random import random, gauss
from .Agent import Agent

class RealAgent(Agent):

	def init(self, size, _min=0, _max=1, exogenous=False, **kwargs):
		self.__dict__.update(kwargs)
		self.genome = [random()*(_max - _min) + _min for _ in range(size)]
		if exogenous:
			self.exogenous = self.init_exogenous()
		
	def init_exogenous(self):
		return [random() for _ in self.genome]

	def __str__(self):
		S = ''
		ft = '{:0.4f} '
		for value in self.genome:
			S += ft.format(value)
		return S + '| ' + ft.format(self.fitness)
