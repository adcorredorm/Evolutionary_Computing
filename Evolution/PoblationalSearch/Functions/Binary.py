def max_one(ind):
  count = 0
  for value in ind:
    if value: count += 1
  return len(ind) - count