class Tracer():

    def __init__(self):
        self.best_ind = []
        self.best_fit = []
        self.last_generation = None

    def add(self, population):
        best = sorted(population)[0]
        self.best_ind.append(best)
        self.best_fit.append(best.fitness)
        self.last_generation = population
