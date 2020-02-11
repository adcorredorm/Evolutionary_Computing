import os
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
# pylint: disable=import-error
from PoblationalSearch.Algorithms.HillClimb import HillClimb
from PoblationalSearch.Algorithms.GeneticAlgorithm import GeneticAlgorithm

def plot_stats(data, comparative=None):
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

    plt.plot(_min, label='min')
    plt.plot(_max, label='max')
    plt.plot(avg, label ='average')
    plt.plot(median, label='median')
    plt.grid(True, linestyle='dotted', linewidth=1)

    plt.ylabel('fitness')
    plt.xlabel('generations')

    if comparative is not None:
        comparative = np.transpose(comparative)
        comp = []
        for gen in comparative:
            comp.append(min(gen))
        plt.plot(comp, label='Hill Climb', linestyle='--')

    plt.legend()
    plt.show()

def make_experiment(filename, algorithm_class, algorithm_args, executions, hc_args=None):
    stats = []
    solutions = []
    for _ in range(executions):
        algorithm = algorithm_class(**algorithm_args)
        tracer = algorithm.execute()
        solutions.append(tracer.best_ind)
        stats.append(tracer.best_fit)
    if hc_args is not None:
        comparative = []
        for _ in range(executions):
            tracer = HillClimb(**hc_args).execute()
            comparative.append(tracer.best_fit)
        make_resume(filename, algorithm_args, solutions, stats, comparative)
        plot_stats(stats, comparative)
    else:
        make_resume(filename, algorithm_args, solutions, stats)
        plot_stats(stats)
    return (solutions, stats)

def make_resume(filename, args, solutions, data, comparative=None):
    with open(os.path.dirname(os.path.abspath(__file__)) + '/results/' + filename, 'w+') as f:
        f.write('generations: {}\n'.format(args['generations']))
        if 'ind_size' in args:
            f.write('population size: {}\n'.format(args['ind_size']))
        
        best = sorted(solutions[-1])[0]
        for gen in solutions:
            b_gen = sorted(gen)[0]
            if b_gen < best:
                best = b_gen
        f.write('Best solution:\n')
        f.write(str(best)+'\n')
        f.write(str(best.fitness) +'\n')
        if 'functions' in args:
            f.write('Objectives:\n')
            for obj in solutions[-1].objectives:
                f.write(obj + '\n')
        last_gen = np.transpose(data)[-1]
        avg = np.average(last_gen)
        med = np.median(last_gen)
        std_avg = np.sqrt(sum([(x_i - avg)**2 for x_i in last_gen]) / (len(last_gen) - 1))
        std_med = np.sqrt(sum([(x_i - med)**2 for x_i in last_gen]) / (len(last_gen) - 1))
        f.write('Average: {:0.4f}\tStd Deviation: {:0.4f}\n'.format(avg, std_avg))
        f.write('Median: {:0.4f}\tStd Deviation: {:0.4f}\n'.format(med, std_med))

        if comparative is not None:
            last_gen_hc = np.transpose(comparative)[-1]
            avg_hc = np.average(last_gen_hc)
            med_hc = np.median(last_gen_hc)
            std_avg_hc = np.sqrt(sum([(x_i - avg_hc)**2 for x_i in last_gen_hc]) / (len(last_gen_hc) - 1))
            std_med_hc = np.sqrt(sum([(x_i - med_hc)**2 for x_i in last_gen_hc]) / (len(last_gen_hc) - 1))
            f.write('Hill Climb\n')
            f.write('Average: {:0.4f}\tStd Deviation: {:0.4f}\n'.format(avg_hc, std_avg_hc))
            f.write('Median: {:0.4f}\tStd Deviation: {:0.4f}\n'.format(med_hc, std_med_hc))

            z_test_avg = (avg - avg_hc) / np.sqrt(std_avg**2/len(last_gen) + std_avg_hc**2/len(last_gen_hc))
            z_test_med = (med - med_hc) / np.sqrt(std_med**2/len(last_gen) + std_med_hc**2/len(last_gen_hc))
            
            f.write('Algorithm {}pass z test with 95% significance using average.\n'.format(
                '' if z_test_avg < -1.96 else 'not '))
            f.write('Algorithm {}pass z test with 95% significance using median.'.format(
                '' if z_test_med < -1.96 else 'not '))


def hamming_distance(A, B):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    return count
