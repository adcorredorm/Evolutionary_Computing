from HillClimb import HillClimb
from ParallelHC import ParallelHC
from SimulatedTempering import SimulatedTempering

iterations = 100
theads = 10

function = lambda x: 4*(x[0]**4) - 10*x[0] - 2
stop = lambda k, vector, function: k >= iterations
stopp = lambda k, vector, function: k >= iterations/theads

hc  = HillClimb(1, function, stop)
hcp = ParallelHC(theads, 1, function, stopp)
st  = SimulatedTempering(1, function, stop)

exe = [(m.__class__, m.execute()) for m in [hc, hcp, st]]

for c, r in exe:
  print(c)
  print(r)
  print(function(r))