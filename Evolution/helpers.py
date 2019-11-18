import matplotlib.pyplot as plt
import numpy as np

def plot_stats(data):
    _min = []
    _max = []
    avg = []
    median = []

    pop = np.transpose(data)
    for gen in pop:
        _min.append(min(gen))
        _max.append(max(gen))
        avg.append(np.average(gen))
        median.append(np.median(gen))

    plt.plot(_min)
    plt.plot(_max)
    plt.plot(avg)
    plt.plot(median)
    plt.grid(True, linestyle='dotted', linewidth=1)

    plt.legend(['min', 'max', 'average', 'median'])
    plt.ylabel('fitness')
    plt.xlabel('generations')

    plt.show()

def make_experiment(algorithm_class, algorithm_args, executions):
    stats = []
    solutions = []
    for _ in range(executions):
        algorithm = algorithm_class(**algorithm_args)
        tracer = algorithm.execute()
        solutions.append(tracer.best_ind)
        stats.append(tracer.best_fit)
    plot_stats(stats)
    return (solutions, stats)