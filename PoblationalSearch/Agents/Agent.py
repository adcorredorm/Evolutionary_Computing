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
		return isinstance(other, self.__class__) and self.fitness < other.fitness

	def __le__(self, other): return self < other or self == other
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.fitness == other.fitness

	def __ne__(self, other): return not self == other

	def __ge__(self, other): return not self < other

	def __gt__(self, other): return not self <= other
