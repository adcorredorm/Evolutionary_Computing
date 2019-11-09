def dummy(ind):
    total = 0
    for i in range(len(ind)):
        total += i * ind[i]
    return total