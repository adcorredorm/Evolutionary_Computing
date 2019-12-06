from abc import abstractmethod, ABCMeta
from .Agent import Agent

class HaEaAgent(Agent, metaclass=ABCMeta):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rates = []

    @abstractmethod
    def init_rates(self, ops):
        pass
