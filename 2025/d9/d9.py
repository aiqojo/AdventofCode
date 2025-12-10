import numpy as np
from tqdm import tqdm
import functools

with open('d9.txt', 'r') as file:
    data = file.read().split("\n")

d = []
for l in data:
    vals = l.split(",")
    vals = [int(val) for val in vals]
    d.append(vals)

min_x = min([v[0] for v in d])
max_x = max([v[0] for v in d])
min_y = min([v[1] for v in d])
max_y = max([v[1] for v in d])
# print(max_x)

boundary = set()
for i, p in enumerate(d):
    n_i = i + 1
    if i == len(d) - 1:
        n_i = 0

    # print()
    # print(d[i])
    # print(d[n_i])

    if p[0] == d[n_i][0]:
        if p[1] <= d[n_i][1]:
            line = range(p[1], d[n_i][1]+1)
        else:
            line = range(d[n_i][1], p[1]+1)
        for l in line:
            boundary.add((p[0], l))
    else:
        if p[0] <= d[n_i][0]:
            line = range(p[0], d[n_i][0]+1)
        else:
            line = range(d[n_i][0], p[0]+1)
        for l in line:
            boundary.add((l, p[1]))

# print(boundary)

p1_size = 0
p1_pair = ()
p2_size = 0
p2_pair = ()

