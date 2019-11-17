def dummy(ind):
    total = 0
    for i in range(len(ind)):
        total += (len(ind) - i) * ind[i]
    return total