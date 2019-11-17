from random import random, sample, shuffle
from .Operator import Operator

class shuffle_selection(Operator):

    def apply(self, agents):
        shuffle(agents)
        return agents

class uniform_selection(Operator):

    def apply(self, agents, size=-1):
        size = size if size >= 0 else len(agents)
        selected = []
        for _ in range(size):
            selected += sample(agents, 1)
        return selected

class tournament_selection(Operator):

    def __init__(self, t_size=4, pick_method=uniform_selection, advantage=2/3, **kwargs):
        super().__init__(**kwargs)
        self.t_size = t_size
        self.pick_method = pick_method()
        self.advantage = advantage
    
    def make_tournament(self, candidates):
        while len(candidates) > 1:
            duel = sorted(candidates[:2])
            winner = duel[0] if random() < self.advantage else duel[1]
            candidates = candidates[2:]
            candidates.append(winner)
        return candidates[0]

    def apply(self, agents, size=-1):
        size = size if size >= 0 else len(agents)
        selected = []
        for _ in range(size):
            candidates = self.pick_method.apply(agents, self.t_size)
            selected.append(self.make_tournament(candidates))
        return selected

class elitist_tournament(tournament_selection):

    def __init__(self, t_size=4, **kwargs):
        super().__init__(t_size, advantage=1, **kwargs)
    
    def make_tournament(self, candidates):
        return sorted(candidates)[0]
