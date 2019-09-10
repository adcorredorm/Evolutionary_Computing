from multiprocessing.pool import ThreadPool
from HillClimb import HillClimb

class ParallelHC:

  def __init__(self, threads, dim, function, stop):
    self.threads = threads
    self.function = function
    self.obj = HillClimb(dim, function, stop)
    self.pool = ThreadPool(processes = threads)

  def execute(self):
    execution = [self.pool.apply_async(self.obj.execute) for i in range(self.threads)]
    results = [res.get() for res in execution]
    return ParallelHC.find_min(results, self.function)

  @staticmethod
  def find_min(results, function):
    opt = results[0]
    value = function(opt)
    for res in results[1:]:
      aux = function(res)
      if aux < value:
        opt = res
        value = aux
    return opt
    