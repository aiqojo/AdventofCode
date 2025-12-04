from tqdm import tqdm

with open('d3.txt', 'r') as file:
    data = file.read().split("\n")

p1 = 0
for bank in data:
    val = ""
    first_idx = None
    # find first digit
    for i in reversed(range(10)):
        idx = bank.find(str(i))
        if idx == -1 or idx == len(bank) - 1:
            continue
        else:
            val += bank[idx]
            first_idx = idx
            break
    # find second digit
    for i in reversed(range(10)):
        new_bank = bank[first_idx + 1:]
        idx = new_bank.find(str(i))
        if idx == -1:
            continue
        else:
            val += new_bank[idx]
            break

    p1 += int(val)

print(p1)

p2 = 0
vals = []

for bank in tqdm(data):
    print("\n\n\n\n")
    val = ""
    total_digits = 0
    left = 0
    remaining = 12 - len(val)
    right = len(bank) - remaining + 1
    test_iter = 0
    while len(val) < 12:
        print("\n\n")
        remaining = 12 - len(val)
        right = len(bank) - remaining + 1

        for i in reversed(range(10)):
            idx = bank[left:right].find(str(i))
            if idx == -1:
                continue
            else:
                val += bank[left:right][idx]
                left += idx + 1
                right += 1
                break

    print(f"{val} | {len(val)}")
    p2 += int(val)
    vals.append(val)

print(p2)