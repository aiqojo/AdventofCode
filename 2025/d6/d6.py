import numpy as np

with open('d6.txt', 'r') as file:
    data = file.read().split("\n")

nums = []
symb = []
for l in data:
    ll = l.split()
    if ll[0] in ["+", "*"]:
        symb = ll.copy()
        continue
    nums.append(ll)
    
nums = np.array([np.array(row, int) for row in nums])

p1 = 0

for i, val in enumerate(symb):
    if val == "+":
        p1 += np.sum(nums[:, i])
    else:
        p1 += np.prod(nums[:, i])

print(p1)

d = []
for l in data:
    ll = d.append(list(l))

d = np.array([np.array(row, str) for row in d])

p2 = 0
cur_symb = ""
stockpile = []
for i, val in enumerate(d.T):
    if val[-1] != " ":
        if len(stockpile) > 0:
            if cur_symb == "+":
                p2 += np.sum(stockpile)
            else:
                p2 += np.prod(stockpile)
            stockpile = []

        cur_symb = val[-1]
    nums = np.delete(val[:-1], np.where(val[:-1] == " "))
    if len(nums) == 0:
        continue
    stockpile.append(int(''.join(nums)))

if cur_symb == "+":
    p2 += np.sum(stockpile)
else:
    p2 += np.prod(stockpile)

print(p2)