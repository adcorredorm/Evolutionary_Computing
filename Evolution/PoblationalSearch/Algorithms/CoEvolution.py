class CoEvolution():

    def __init__(self, function, generations, algorithms, alg_args, **kwargs):
        self.function = function
        self.generations = generations
        
        self.p_sizes = [arg['p_size'] for arg in alg_args]
        self.algorithms = []
        #evaluate = lambda x: None
        for i in range(len(algorithms)):
            arg = alg_args[i]
            arg['function'] = self.function
            arg['stationary'] = True
            #arg['evaluate'] = evaluate
            pop_sizes = self.p_sizes[:i] + self.p_sizes[i+1:]
            if 'agent_args' in arg:
                arg['agent_args'].update({'pop_sizes': pop_sizes})
            else:
                arg['agent_args'] = {'pop_sizes': pop_sizes}

            pop = algorithms[i](**arg)
            self.algorithms.append(pop)

        #for alg in self.algorithms:
        #    alg.__dict__['evaluate'] = self.evaluate

        self.evaluate_all()

        self.tracer = CoTracer()
        self.tracer.add(self.algorithms)
    
    def evaluate(self, agents):
        populations = [alg.population for alg in self.algorithms]
        for agent in agents:
            proper = 0
            for i in range(len(populations)):
                if agent in populations[i]:
                    proper = i
                    break
            pops = populations[:proper] + populations[proper+1:]
            friends = agent.get_friends(pops)
            agent.fitness = self.function(friends)
    
    def evaluate_all(self):
        populations = [alg.population for alg in self.algorithms]
        for i in range(len(populations)):
            pops = populations[:i] + populations[i+1:]
            for j in range(len(populations[i])):
                agent = populations[i][j]
                friends = agent.get_friends(pops)
                agent.fitness = self.function(friends)

    def stop(self, populations, k):
        return self.generations <= k
    
    def execute(self):
        k = 0
        while not self.stop(self.algorithms, k):
            all_parents = []
            all_childs = []
            for alg in self.algorithms:
                parents = alg.select_parents.apply(alg.population)
                childs = alg.descendant(alg.population, parents)
                all_parents.append(parents)
                all_childs.append(childs)
                #alg.population = alg.grow(alg.population, k)

            current_pops = [alg.population for alg in self.algorithms]
            for i in range(len(all_childs)):
                pops = current_pops[:i] + current_pops[i+1:]
                for j in range(len(all_childs[i])):
                    agent = all_childs[i][j]
                    friends = agent.get_friends(pops)
                    agent.fitness = self.function(friends)
            
            for i in range(len(self.algorithms)):
                alg = self.algorithms[i]
                new_p = alg.replace(alg.population, all_parents[i], all_childs[i])
                alg.population = new_p

            self.evaluate_all()
            self.tracer.add(self.algorithms)
            k += 1 
        return self.tracer

class CoTracer():
    
    def __init__(self):
        self.best_ind = []
        self.best_fit = []
        self.best_pop = 0
        self.last_generations = None
    
    def add(self, algorithms):
        populations = [alg.population for alg in algorithms]
        self.last_generations = populations
        best = self.find_best(populations)
        self.best_ind.append(best[0])
        self.best_fit.append(best[0].fitness)
        self.best_pop = best[1]

    def find_best(self, poulations):
        best = self.last_generations[0][0]
        pop = 0
        for i in range(len(self.last_generations)):
            bp = sorted(self.last_generations[i])[0]
            if bp < best:
                best = bp
                pop = i
        return (best, pop)
            
    def get_best(self):
        pops = self.last_generations[:self.best_pop] + self.last_generations[self.best_pop + 1:]
        return self.best_ind[-1].get_friends(pops)
