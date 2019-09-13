import math
import opt_functions 
from HillClimb import HillClimb
from ParallelHC import ParallelHC
from SimulatedAnnealing import SimulatedAnnealing

executions = 100
iterations = 1e+5
theads = 50

stop = lambda k, vector, function: k >= iterations
stopp = lambda k, vector, function: k >= iterations/theads

function = opt_functions.ackley
_min = -32
_max = 32
dim = 12

hc  = HillClimb(dim, function, stop)
hcp = ParallelHC(theads, dim, function, stopp)
st  = SimulatedAnnealing(dim, function, stop)

hc_candidates  = []
hcp_candidates = []
st_candidates  = []

for i in range(executions):
  hc_candidates.append(hc.execute(_min, _max))
  hcp_candidates.append(hcp.execute(_min, _max))
  st_candidates.append(st.execute(_min, _max))
  print((i+1)+'%')

hc_results  = [function(cand) for cand in hc_candidates]
hcp_results = [function(cand) for cand in hcp_candidates]
st_results  = [function(cand) for cand in st_candidates]

min_hc_index = hc_results.index(min(hc_results))
min_hcp_index = hcp_results.index(min(hcp_results))
min_st_index = st_results.index(min(st_results))

hc_av = sum(hc_results)/executions
hc_results.sort()
hc_med = hc_results[int(executions/2)]

hcp_av = sum(hcp_results)/executions
hcp_results.sort()
hcp_med = hcp_results[int(executions/2)]

st_av = sum(st_results)/executions
st_results.sort()
st_med = st_results[int(executions/2)]

name = function.__name__
file = open(name + '_results.txt', 'w+')

file.write('Params:\n\tFunction: {}\n\tDimension: {:.0f}\n\tIterations: {:.0f}\n\tExecutions: {:.0f}\n\n'.format(
  name, dim, iterations, executions
))

file.write('Algorithm    \t    Average    \t\t    Median    \t\t  Max\t\t  Min\t\tBest Individual\n')

file.write('Hill Climb   \t{:0.4f} ± {:0.4f}\t{:0.4f} ± {:0.4f}\t{:0.4f}\t{:0.4f}\t'.format(
  hc_av, math.sqrt(sum([(res - hc_av)**2 for res in hc_results])/executions),
  hc_results[int(executions/2)], math.sqrt(sum([(res - hc_med)**2 for res in hc_results])/executions),
  hc_results[-1], hc_results[0]
))
file.write(str(['{:0.4f}'.format(i) for i in hc_candidates[min_hc_index]]) + '\n')

file.write('Parallel HC  \t {:0.4f} ± {:0.4f} \t {:0.4f} ± {:0.4f} \t{:0.4f}\t{:0.4f}\t'.format(
  hcp_av, math.sqrt(sum([(res - hcp_av)**2 for res in hcp_results])/executions),
  hcp_results[int(executions/2)], math.sqrt(sum([(res - hcp_med)**2 for res in hcp_results])/executions),
  hcp_results[-1], hcp_results[0]
))
file.write(str(['{:0.4f}'.format(i) for i in hcp_candidates[min_hcp_index]]) + '\n')

file.write('Sim. Anneling\t{:0.4f} ± {:0.4f}\t{:0.4f} ± {:0.4f}\t{:0.4f}\t{:0.4f}\t'.format(
  st_av, math.sqrt(sum([(res - st_av)**2 for res in st_results])/executions),
  st_results[int(executions/2)], math.sqrt(sum([(res - st_med)**2 for res in st_results])/executions),
  st_results[-1], st_results[0]
))
file.write(str(['{:0.4f}'.format(i) for i in st_candidates[min_st_index]]) + '\n')
