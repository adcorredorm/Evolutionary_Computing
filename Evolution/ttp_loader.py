import os
import math

class ttp_loader():

    def __init__(self, path):
        abs_path = os.path.dirname(os.path.abspath(__file__)) + '/'
        file = open(abs_path + path)
        
        self.name = file.readline().strip().split('\t')[1]
        self.kp_type = file.readline().strip().split(':')[1].split(',')
        self.dimension = int(file.readline().strip().split('\t')[1])
        self.n_items = int(file.readline().strip().split('\t')[1])
        self.capacity = int(file.readline().strip().split('\t')[1])
        self.min_speed = float(file.readline().strip().split('\t')[1])
        self.max_speed = float(file.readline().strip().split('\t')[1])
        self.renting_ratio = float(file.readline().strip().split('\t')[1])
        self.edge_w_type = file.readline().strip().split('\t')[1]
        file.readline()

        self.nodes = []
        for _ in range(self.dimension):
            _, x, y = file.readline().strip().split('\t')
            self.nodes.append({
                'coordinates': (float(x), float(y)),
                'items': []
                })
        file.readline()
        self.items = []
        for _ in range(self.n_items):
            i, profit, weight, node = file.readline().strip().split('\t')
            self.nodes[int(node)-1]['items'].append(int(i)-1)
            self.items.append((int(profit), int(weight)))

        file.close()
    
    def get_distance(self, a, b):
        n_a = self.nodes[a]['coordinates']
        n_b = self.nodes[b]['coordinates']
        total = sum([(n_a[c] - n_b[c])**2 for c in range(len(n_a))])
        return math.sqrt(total)
    