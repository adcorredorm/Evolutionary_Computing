import math
from HillClimb import HillClimb
from ParallelHC import ParallelHC
from SimulatedTempering import SimulatedTempering

executions = 100
iterations = 1e+5
theads = 50

function = lambda x: 4*(x[0]**4) - 10*x[0] - 2
stop = lambda k, vector, function: k >= iterations
stopp = lambda k, vector, function: k >= iterations/theads

hc  = HillClimb(1, function, stop)
hcp = ParallelHC(theads, 1, function, stopp)
st  = SimulatedTempering(1, function, stop)

hc_candidates  = []
hcp_candidates = []
st_candidates  = []

for _ in range(executions):
  hc_candidates.append(hc.execute())
  hcp_candidates.append(hcp.execute())
  st_candidates.append(st.execute())

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