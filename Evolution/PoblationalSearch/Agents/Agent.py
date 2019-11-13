from abc import abstractmethod, ABCMeta

class Agent(metaclass=ABCMeta):

	@abstractmethod
	def init(self, size, **kwargs):
		pass

	def evaluate(self, function):
		if self.fitness is None:
			self.fitness = function(self.genome)

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

	def __le__(self, other): 
		return isinstance(other, self.__class__) and self.fitness <= other.fitness
	
	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.fitness == other.fitness

	def __ne__(self, other): 
		return isinstance(other, self.__class__) and self.fitness != other.fitness

	def __ge__(self, other): 
		return isinstance(other, self.__class__) and self.fitness >= other.fitness

	def __gt__(self, other): 
		return isinstance(other, self.__class__) and self.fitness > other.fitness
