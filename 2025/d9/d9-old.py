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

seen = {}

vertical_edges = []
for i in range(len(d)):
    p1 = d[i]
    n_i = i + 1
    if i == len(d) - 1:
        n_i = 0
    p2 = d[n_i]

    # skip vertical lines
    if p1[0] == p2[0]:
        continue

    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    vertical_edges.append({
        'x1': p1[0], 'y1': p1[1],
        'x2': p2[0], 'y2': p2[1],
        'min_x': min_x, 'max_x': max_x
    })

# sorting to break early inside in_bounds()
vertical_edges.sort(key=lambda e: e['min_x'])

@functools.lru_cache(maxsize=100000000)
def in_bounds(c):
    # c is point (cx, cy)
    # Returns True if inside, False if outside
    
    count = 0  # # of crossings
    cx, cy = c

    for edge in vertical_edges:
        # since we're sorted, once we're over, we can break
        if edge["min_x"] > cy:
            break
        # doesn't contain, skip
        if cy > edge["max_x"]:
            continue
        # if edge is to the right, at this point, we cross it
        if edge["y1"] > cy:
            count += 1
        
    return count % 2 == 1

@functools.lru_cache(maxsize=100000000)
def is_valid_p(p):
    if p in boundary:
        return True
    return in_bounds(p)

for c1 in tqdm(d):
    for c2 in d:
        if c1 == c2:
            continue
        c1_t = tuple(c1)
        c2_t = tuple(c2)
        if (c1_t, c2_t) in seen or (c2_t, c1_t) in seen:
            continue

        s0 = abs(c1[0] - c2[0]) + 1
        s1 = abs(c1[1] - c2[1]) + 1
        size = s0 * s1
        seen[(c1_t, c2_t)] = size
        if size > p1_size:
            p1_size = size
            p1_pair = (c1_t, c2_t)

        # if the size is less than our current p2 size, we can skip
        if size <= p2_size:
            continue

        # have to check all points
        min_x, max_x = min(c1[0], c2[0]), max(c1[0], c2[0])
        min_y, max_y = min(c1[1], c2[1]), max(c1[1], c2[1])
        
        all_valid = True
        
        # Check corners first - most invalid rectangles fail here
        corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
        for corner in corners:
            if not is_valid_p(corner):
                all_valid = False
                break
        
        if not all_valid:
            continue  # Skip perimeter checking
        
        # top & bottom edges
        for x in range(min_x, max_x + 1):
            for y in [min_y, max_y]:
                p = (x, y)
                if not is_valid_p(p):
                    all_valid = False
                    break
            if not all_valid:
                break
        
        if all_valid: # skip if we failed above
            for y in range(min_y + 1, max_y):
                for x in [min_x, max_x]:
                    p = (x, y)
                    if not is_valid_p(p):
                        all_valid = False
                        break
                if not all_valid:
                    break

        if all_valid:
            if size > p2_size:
                p2_size = size
                p2_pair = (c1_t, c2_t)

print(p1_size)
print(p2_size)
print(p2_pair)