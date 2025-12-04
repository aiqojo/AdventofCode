from tqdm import tqdm

with open('d4.txt', 'r') as file:
    data = file.read().split("\n")

def check_adjacent(data, x, y):
    dirs = [(-1,0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    adj = 0
    for d in dirs:
        try:
            if x+d[0] < 0 or y+d[1] < 0:
                continue
            if data[x+d[0]][y+d[1]] == "@":
                adj += 1
        except:
            pass
        if adj >= 4:
            break
    return adj

p1 = 0
p2 = 0

to_remove = []
changed = True
first = True # for p1
while changed:
    changed = False
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                adj = check_adjacent(data, i, j)
                if adj < 4:
                    changed = True
                    to_remove.append((i,j))
                    if first:
                        p1 += 1
                    p2 += 1

    for r in to_remove:
        row = list(data[r[0]])
        row[r[1]] = "."
        ''.join(row)
        data[r[0]] = row
    
    first = False

print(p1)
print(p2)