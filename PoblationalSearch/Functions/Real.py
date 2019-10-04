import math

def ackley(x, a=20, b=0.2, c=2*math.pi):
    p1 = -a*math.exp(-b*math.sqrt(sum([i**2 for i in x])/len(x)))
    p2 = -math.exp(sum([math.cos(c*i) for i in x])/len(x))
    return p1 + p2 + a + math.exp(1)

def rastrigin(x):
  return 10*len(x) + sum([i**2 - 10*math.cos(2*math.pi*i) for i in x])

def michalewicz(x, m=10):
  res = 0
  for i in range(len(x)):
    res += math.sin(x[i]) * (math.sin((i*x[i]**2)/math.pi))**(2*m)
  return - res