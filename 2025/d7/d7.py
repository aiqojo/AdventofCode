import numpy as np

with open('d7.txt', 'r') as file:
    data = file.read().split("\n")

data = np.array([np.array(row, str) for row in data])
res = []

def add_bars(row, row_n, prev_row, res):
    loc_s = np.where(row == "S")
    loc_bar = np.where(row == "|")
    if prev_row is not None:
        loc_bar_prev = np.where(np.array(prev_row) == "|")
    else:
        loc_bar_prev = [[]]
    loc_caret = np.where(row == "^")
    
    for loc in loc_s[0]:
        row_n[loc] = "|"
    for loc in loc_bar[0]:
        row_n[loc] = "|"
    for loc in loc_bar_prev[0]:
        if row_n[loc] != "^":
            row_n[loc] = "|"
    for loc in loc_caret[0]:
        try:
            if row_n[loc-1] != "|":
                if len(res) > 0:
                    res[-1][loc-1] = "|"
                row_n[loc-1] = "|"
        except:
            pass
        try:
            if row_n[loc+1] != "|":
                if len(res) > 0:
                    res[-1][loc+1] = "|"
                row_n[loc+1] = "|"
        except:
            pass

p1 = 0

for i, r in enumerate(data):
    row = np.array(list(r))
    loc_caret = np.where(row == "^")

    if i+1 == len(data):
        continue

    row_n = list(data[i+1].copy())
    if i > 0 and len(res) > 0:
        prev_row = res[-1]
    else:
        prev_row = None
    add_bars(row, row_n, prev_row, res)
    
    for loc in loc_caret[0]:
        if i > 0 and len(res) > 0:
            if res[-2][loc] == "|":
                p1 += 1

    res.append(row_n)

print(p1)

p2 = 0
paths = {} # set()

def dfs(row, col, res):
    char = res[row][col]
    t = 0

    if row == len(res) - 1:
        return 1 # got to end
    if (row, col) in paths: # pull from paths
        return paths[(row, col)]

    if char == "|": # move down
        t += dfs(row + 1, col, res)
    elif char == "^": # move down and to side
        t += dfs(row + 1, col - 1, res)
        t += dfs(row + 1, col + 1, res)
    paths[(row, col)] = t
    return t

print(dfs(0, data[0].find("S"), res))