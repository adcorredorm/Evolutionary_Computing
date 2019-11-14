from abc import abstractmethod, ABCMeta

class Operator(metaclass=ABCMeta):

    @abstractmethod
    def apply(self, agents, **kwargs):
        return [agents]