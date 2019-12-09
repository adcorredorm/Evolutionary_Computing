# pylint: disable=import-error, no-name-in-module
import csv
import numpy as np
from random import shuffle

import PoblationalSearch.Operators.crossover as crossover
import PoblationalSearch.Operators.mutation as mutation
import PoblationalSearch.Operators.selection as selection
from PoblationalSearch.Algorithms.EvolutionStrategie import EvolutionStrategie

class NNProblem():

    def __init__(self, data_path, label_path, layer_sizes, validation=0.3):
        self.layer_sizes = list(layer_sizes)
        self.data = {}
        self.input_size = 0
        self.validation_data = []
        self.train_data = []

        self.load_data(data_path, label_path, validation)

    def load_data(self, data_path, label_path, validation):
        self.data = {}
        with open(data_path) as file:
            headers = file.readline().strip()
            self.input_size = len(headers.split(',')) - 2
            for row in file:
                row_data = row.strip().split(',')
                self.data[row_data[1]] = {
                    'features': [float(v) for v in row_data[2:]],
                    'label': 0
                }
        self.normalize_features()
        
        with open(label_path) as file:
                file.readline()
                for row in file:
                    _id, label = row.strip().split(',')
                    value = 1 if label == 'True' else 0
                    self.data[_id]['label'] = value
        
        keys = list(self.data.keys())
        shuffle(keys)
        cut = int(len(keys) * validation)
        self.validation_data = keys[:cut]
        self.train_data = keys[cut:]
    
    def normalize_features(self):
        max_values = [0]*self.input_size
        for key in self.data:
            features = self.data[key]['features']
            for i in range(self.input_size):
                max_values[i] = max(max_values[i], features[i])
        
        for key in self.data:
            features = self.data[key]['features']
            for i in range(self.input_size):
                features[i] /= max_values[i]

    def evaluate(self, genome, data='train'):
        if data == 'train':
            data = self.train_data
        elif data == 'validation':
            data = self.validation_data
        else:
            data = self.data.keys()
        
        layers = self.make_network(genome)
        error = 0
        for key in data:
            current = np.array(self.data[key]['features'] + [1])
            for layer in layers:
                current = self.sigmoid(current @ layer)
                current = np.append(current, 1)
            calculated = current[0]
            error += abs(self.data[key]['label'] - calculated)
        return error
    
    def sigmoid(self, array):
        result = []
        for value in array:
            result.append(1/(1 + np.exp(-value)))
        return np.array(result)

    
    def make_network(self, genome):
        layers = []
        current_size = self.input_size + 1
        index = 0
        for size in self.layer_sizes + [1]:
            layer = []
            for _ in range(current_size):
                layer.append(genome[index:index + size])
                index += size
            layers.append(np.array(layer))
            current_size = size + 1
        return layers

    def total_conections(self):
        count = 0
        layer = self.input_size
        for value in self.layer_sizes:
            count += (layer + 1) * value
            layer = value
        count += self.layer_sizes[-1] + 1
        return count

    def make_validation(self, genome, data='train'):
        if data == 'train':
            data = self.train_data
        elif data == 'validation':
            data = self.validation_data
        else:
            data = self.data.keys()
        
        layers = self.make_network(genome)
        accuracy = 0
        for key in data:
            current = np.array(self.data[key]['features'] + [1])
            for layer in layers:
                current = self.sigmoid(current @ layer)
                current = np.append(current, 1)
            calculated = 0 if current[0] < 0.5 else 1
            if calculated == self.data[key]['label']:
                accuracy += 1
        return accuracy/len(data)

problem_args = {
    'data_path': 'NN/features_30m.csv',
    'label_path': 'NN/data_train_label.csv',
    'layer_sizes': (6, 3),
    'validation': 0.3,
}

problem = NNProblem(**problem_args)

evolution_strategy = {
    'function': problem.evaluate,
    'ind_size': problem.total_conections(),
    'p_size': 30,
    'generations': 100,
    'selection_op': selection.random_selection(),
    'mutation_op': mutation.e_strategy_mutation(),
    'recombination_op': crossover.real_crossover(5, 'exogenous'),
    'marriage_size': 2,
    'agent_args': {
        
    },
}

es = EvolutionStrategie(**evolution_strategy).execute()
best = es.best_ind[-1]

print('Train Data')
print(problem.evaluate(best.genome, 'train'))
print(problem.make_validation(best.genome, 'train'))

print('Validation Data')
print(problem.evaluate(best.genome, 'validation'))
print(problem.make_validation(best.genome, 'validation'))

print('Total Data')
print(problem.evaluate(best.genome, 'all'))
print(problem.make_validation(best.genome, 'all'))
