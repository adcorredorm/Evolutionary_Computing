from random import random, sample

def uniform_selection(population):
    parents = []
    for _ in range(len(population)):
      parents.append(sample(population, 1))
    return parents

def tournament(population):
    parents = []
    for _ in range(len(population)):
        cand = sample(population, 4)
        while len(cand) > 1:
            part = sorted([cand[0], cand[1]])
            cand = cand[2:]
            if random() < 2/3: cand.append(part[0])
            else: cand.append(part[1])
        parents.append(cand[0])
    return parents

def elitist_tournament(population):
    parents = []
    for _ in range(len(population)):
      parents.append(min(sample(population, 4)))
    return parents