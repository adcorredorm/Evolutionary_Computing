from random import sample
from .Operator import Operator

class kp_fix():

    def __init__(self, W, item_w, **kwargs):
        super().__init__(**kwargs)
        self.W = W
        self.item_w = item_w
    
    def calculate_w(self, agent):
        w = 0
        for i in range(len(self.item_w)):
            if agent.genome[i]:
                w += self.item_w[i]
            if w > self.W:
                break
        return w

    def apply(self, agents):
        for agent in agents:
            w = self.calculate_w(agent)
            if w > self.W:
                bag = []
                for i in range(len(self.item_w)):
                    if agent.genome[i]: 
                        bag.append(i)
                while w > self.W:
                    index = sample(bag, 1)[0]
                    bag.remove(index)
                    agent.genome[index] = False
                    w = self.calculate_w(agent)
        return agents
    