from abc import abstractmethod, ABCMeta

class Operator(metaclass=ABCMeta):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @abstractmethod
    def apply(self, agents):
        return agents