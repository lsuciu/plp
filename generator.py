data = set([1, 2, 3])

from itertools import combinations

print [set(el) for r in range(len(data) + 1) for el in combinations(data, r)]
