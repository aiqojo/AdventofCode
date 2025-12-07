inp = []

with open("d1/d1.txt", "r") as f:
    for line in f:
        inp.append(line.strip())

loc = 50
count = 0
count_2 = 0
d = 100

for i in inp:
    loc_b = loc
    move = int(i[1:])
    if i[0] == 'R':
        loc = (loc + move) % d
        count_2 += (move + loc_b % d) // d
    else:
        loc = (loc - move) % d
        count_2 += (move + -1*loc_b % d) // d

    if loc == 0:
        count += 1

print(count)
print(count_2)