from tqdm import tqdm

with open('d2.txt', 'r') as file:
    data = file.read()

inps = data.split(",")
print(inps)

def invalid_id(inp):
    tot = 0
    start = int(inp.split('-')[0])
    end = int(inp.split('-')[1])
    print(start, end)
    for i in range(start, end+1):
        i_list = list(str(i))
        if len(set(i_list)) == len(i_list):
            continue # if all unique numbers skip
        if len(i_list) % 2 != 0:
            continue
        half_len = int(len(i_list) / 2)
        if i_list[half_len:] == i_list[:half_len]:
            tot += i

    return tot

def invalid_id_2(inp):
    tot = 0
    start = int(inp.split('-')[0])
    end = int(inp.split('-')[1])
    for i in range(start, end+1):
        i_str = str(i)
        i_list = list(str(i))
        if len(set(i_list)) == len(i_list):
            continue # if all unique numbers skip
        half_len = int(len(i_list) / 2)
        for length in range(1, half_len+1):
            subs = [i_str[b:b+length] for b in range(0, len(i_str), length)]
            subs = [int(sub) for sub in subs]

            if len(set(subs)) == 1:
                tot += i
                break
    return tot


p1 = 0
for inp in inps:
    p1 += invalid_id(inp)

print(f"p1: {p1}")

p2 = 0
for inp in tqdm(inps):
    p2 += invalid_id_2(inp)

print(f"p2: {p2}")