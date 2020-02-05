import math
from PoblationalSearch.Agents.CoAgent import TSPCoAgent, KPCoAgent
from ttp_loader import ttp_loader

problem = ttp_loader('TTP/eil51_n50_uncorr_01.ttp')

#f
def total_time(agents):
    tsp_id = 0 if agents[0].__class__ == TSPCoAgent else 1
    tsp_agent = agents[tsp_id].genome
    kp_agent = agents[1 - tsp_id].genome

    w_c = 0
    v_c = problem.max_speed
    f = 0
    for i in range(problem.dimension):
        d = problem.get_distance(tsp_agent[i], tsp_agent[(i+1)%problem.dimension])
        for it in problem.nodes[i]['items']:
            if kp_agent[it]:
                w_c += problem.items[it][1]
        v_c = problem.max_speed - w_c*(problem.max_speed-problem.min_speed)/problem.capacity
        f += d / v_c
    return f

#g
def utility(agents):
    tsp_id = 0 if agents[0].__class__ == TSPCoAgent else 1
    tsp_agent = agents[tsp_id].genome
    kp_agent = agents[1 - tsp_id].genome

    times = [-1 for _ in range(problem.dimension)]
    w_c = 0
    v_c = problem.max_speed
    f = 0
    for i in range(problem.dimension):
        d = problem.get_distance(tsp_agent[i], tsp_agent[(i+1)%problem.dimension])
        for it in problem.nodes[i]['items']:
            if kp_agent[it]:
                times[it] = v_c
                w_c += problem.items[it][1]
        v_c = problem.max_speed - w_c*(problem.max_speed-problem.min_speed)/problem.capacity
        f += d / v_c
    
    utils = 0
    for i in range(problem.n_items):
        if kp_agent[i]:
            utils += problem.items[i][0] * (0.9 ** math.floor((f - times[i])/10))
    return - utils