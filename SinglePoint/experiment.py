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

hc  = HillClimb(10, function, stop)
hcp = ParallelHC(theads, 10, function, stopp)
st  = SimulatedAnnealing(10, function, stop)

hc_candidates  = []
hcp_candidates = []
st_candidates  = []

for i in range(executions):
  hc_candidates.append(hc.execute(_min, _max))
  hcp_candidates.append(hcp.execute(_min, _max))
  st_candidates.append(st.execute(_min, _max))
  print(i)

hc_results  = [function(cand) for cand in hc_candidates]
hcp_results = [function(cand) for cand in hcp_candidates]
st_results  = [function(cand) for cand in st_candidates]

min_hc_index = hc_results.index(min(hc_results))
min_hcp_index = hcp_results.index(min(hcp_results))
min_st_index = st_results.index(min(st_results))


print("HC")
av = sum(hc_results)/executions
print("Av:", av)
print("DS:", math.sqrt(sum([(res - av)**2 for res in hc_results])/executions))
hc_results.sort()
med = hc_results[int(executions/2)]
print("Med:", med)
print("DS:", math.sqrt(sum([(res - med)**2 for res in hc_results])/executions))
print("Max:", hc_results[-1])
print("Min:", hc_results[0])
print(hc_candidates[min_hc_index])

print("HCP")
av = sum(hcp_results)/executions
print("Av:", av)
print("DS:", math.sqrt(sum([(res - av)**2 for res in hcp_results])/executions))
hcp_results.sort()
med = hcp_results[int(executions/2)]
print("Med:", med)
print("DS:", math.sqrt(sum([(res - med)**2 for res in hcp_results])/executions))
print("Max:", hcp_results[-1])
print("Min:", hcp_results[0])
print(hcp_candidates[min_hcp_index])

print("ST")
av = sum(st_results)/executions
print("Av:", av)
print("DS:", math.sqrt(sum([(res - av)**2 for res in st_results])/executions))
st_results.sort()
med = st_results[int(executions/2)]
print("Med:", med)
print("DS:", math.sqrt(sum([(res - med)**2 for res in st_results])/executions))
print("Max:", st_results[-1])
print("Min:", st_results[0])
print(st_candidates[min_st_index])