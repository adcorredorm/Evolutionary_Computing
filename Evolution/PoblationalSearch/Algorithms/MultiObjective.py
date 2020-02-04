from random import random, sample
from .CoEvolution import CoEvolution

class CoMultiObjective(CoEvolution):

    def __init__(self, functions, generations, algorithms, alg_args, **kwargs):
        self.functions = functions
        for args in alg_args:
            if 'agent_args' in args:
                args['agent_args']['objectives'] = [0 for _ in range(len(functions))]
            else:
                args['agent_args'] = {'objectives' : [0 for _ in range(len(functions))]}
        super().__init__(self.no_dominance, generations, algorithms, alg_args, **kwargs)

    def no_dominance(self, agent, population):
        counter = 0
        for ind in population:
            better_or_equal = True
            better = False
            for i in range(len(self.functions)):
                better_or_equal &= ind.objectives[i] <= agent.objectives[i]
                better |= ind.objectives[i] < agent.objectives[i]
            if better_or_equal and better:
                counter += 1
        #It's negative to transforms into minimiation problem
        return counter - len(population)

    
    def evaluate_all(self):
        populations = [alg.population for alg in self.algorithms]
        for i in range(len(populations)):
            pops = populations[:i] + populations[i+1:]
            for j in range(len(populations[i])):
                agent = populations[i][j]
                friends = agent.get_friends(pops)
                for k in range(len(self.functions)):
                    agent.objectives[k] = self.functions[k](friends)
        
        for pop in populations:
            for ind in pop:
                ind.fitness = self.no_dominance(ind, pop)
    
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
        
            current_pops = [alg.population for alg in self.algorithms]
            for i in range(len(all_childs)):
                pops = current_pops[:i] + current_pops[i+1:]
                for j in range(len(all_childs[i])):
                    agent = all_childs[i][j]
                    friends = agent.get_friends(pops)
                    for w in range(len(self.functions)):
                        agent.objectives[w] = self.functions[w](friends)
            for i in range(len(current_pops)):
                for ind in all_childs[i]:
                    ind.fitness = self.no_dominance(ind, current_pops[i])
            
            for i in range(len(self.algorithms)):
                alg = self.algorithms[i]
                new_p = alg.replace(alg.population, all_parents[i], all_childs[i])
                alg.population = new_p

            self.evaluate_all()
            self.tracer.add(self.algorithms)
            k += 1
        return self.tracer
