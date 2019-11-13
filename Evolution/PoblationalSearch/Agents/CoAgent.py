from abc import abstractmethod, ABCMeta
from random import randint
from .Agent import Agent
from.BinaryAgent import BinaryAgent
from .PermutationAgent import TSPAgent

class CoAgent(metaclass=ABCMeta):

	@abstractmethod
	def get_friends(self):
		return []

class TSPCoAgent(TSPAgent, CoAgent):

	def init(self, size, pop_sizes, **kwargs):
		super().init(size, **kwargs)
		self.pop_sizes = pop_sizes
		self.friends = [randint(0, p_size - 1) for p_size in pop_sizes]

	def get_friends(self):
		return self.friends
	
	def mutate(self):
		super().mutate()
		selected = randint(0, len(self.friends) - 1)
		self.friends[selected] = randint(0, self.pop_sizes[selected] - 1)

class KPCoAgent(BinaryAgent, CoAgent):

	@staticmethod
	def number_to_bin(num, bits):
		formater = '{' + '0:0{}b'.format(bits) + '}'
		number = formater.format(num)
		return [b == '1' for b in list(number)]
	
	@staticmethod
	def bool_to_number(bool_a):
		b_number = ['1' if b else '0' for b in bool_a]
		return int(''.join(b_number), 2)

	def calculate_bits(self):
		return max(len(bin(p_size - 1)) for p_size in self.pop_sizes) - 2

	def get_friends(self):
		friends = []
		acumulate = self.size
		for _ in self.pop_sizes:
			code = self.genome[acumulate : acumulate + self.bits]
			friends.append(KPCoAgent.bool_to_number(code))
			acumulate += self.bits
		return friends

	def init(self, size, pop_sizes, **kwargs):
		super().init(size, **kwargs)
		self.size = size
		self.pop_sizes = pop_sizes
		self.bits = self.calculate_bits()
		for p_size in pop_sizes:
			friend = randint(0, p_size - 1)
			self.genome += KPCoAgent.number_to_bin(friend, self.bits)