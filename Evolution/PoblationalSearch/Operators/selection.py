from random import random, sample, shuffle
from .Operator import Operator

class random_selection(Operator):

    def apply(self, agents, size=-1):
        size = size if size >= 0 else len(agents)
        shuffle(agents)
        return agents[:size]

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

#Multimodal
class matting_restriction(Operator):

    def hamming_distance(self, A, B):
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
        return count
    
    def calculate_distances(self, agents):
        distances = [[0]*len(agents) for _ in range(len(agents))]
        for i in range(len(agents)):
            for j in range(i+1, len(agents)):
                d = self.distance(agents[i].genome, agents[j].genome)
                distances[i][j] = d
                distances[j][i] = d
        return distances

    def __init__(self, distance, radious, **kwargs):
        super().__init__(**kwargs)
        self.distance = distance
        self.radious = radious

    def apply(self, agents):
        distances = self.calculate_distances(agents)
        chosen = []
        for i in range(len(agents)):
            candidates = [j for j in range(len(agents))
                    if i != j and distances[i][j] <= self.radious]
            if len(candidates) > 0:
                chosen.append(agents[sample(candidates, 1)[0]])
            else:
                chosen.append(agents[i])
        return chosen
        