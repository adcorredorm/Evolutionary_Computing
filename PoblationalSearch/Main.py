from helpers import plot_poblation
from BinaryGA import BinaryGA
from RealGA import RealGA
from Functions.Binary import max_one
from Functions.Real import ackley, rastrigin, michalewicz

kwargs = {}

alg = RealGA(ackley, 10, 100, 0.7, -32.768, 32.768, **kwargs)
pop = []
executions = 10
for _ in range(executions):
    pop.append(alg.execute(100)[1])
plot_poblation(pop)