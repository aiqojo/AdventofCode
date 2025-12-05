with open('d5.txt', 'r') as file:
    data = file.read().split("\n")

fresh = set()
p1 = 0
for d in data:
    if d.count("-") == 1:
        ranges = d.split("-")
        fresh.add((int(ranges[0]), int(ranges[1])))
    elif d == "":
        continue
    else:
        for f in fresh:
            if int(d) >= int(f[0]) and int(d) <= int(f[1]):
                p1 += 1
                break

def overlapped(f1, f2):
    if (f1[0] <= f2[0]) and (f1[1] >= f2[0]) and (f1[1] <= f2[0]):
        return True, (f1[0], f2[1])
    elif (f1[0] >= f2[0]) and (f1[1] >= f2[1]) and (f1[0] <= f2[1]):
        return True, (f2[0], f1[1])
    elif (f2[0] <= f1[0] <= f2[1]) and (f2[0] <= f1[1] <= f2[1]):
        return True, (f2[0], f2[1])
    elif (f1[0] <= f2[0] <= f1[1]) and (f1[0] <= f2[1] <= f1[1]):
        return True, (f1[0], f1[1])

    return False, ()

p2 = 0
adjusted = False
while True:
    adjusted = False
    cur_fresh = set()
    for f in fresh:
        added = False
        for ff in fresh:
            if f == ff:
                continue
            ret = overlapped(f, ff)
            if ret[0] == False:
                continue
            else:
                cur_fresh.add(ret[1])
                adjusted = True
                added = True
        if added == False:
            cur_fresh.add(f)
    fresh = cur_fresh
    if adjusted == False:
        break

for f in fresh:
    p2 += (int(f[1]) - int(f[0])) + 1

print(p1)
print(p2)