import numpy as np
from scipy.spatial import KDTree
import networkx as nx
from tqdm import tqdm

with open('d8-t.txt', 'r') as file:
    data = file.read().split("\n")

d_np = [] #np
d = [] #list
for l in data:
    ll = l.split(",")
    d_np.append(np.array(ll))
    d.append((ll[0], ll[1], ll[2]))

tree = KDTree(d_np)
g = nx.Graph()
for p in d:
    g.add_node(p)

n = 1000
itr = 0
seen = {}
# for i in tqdm(range(n)): # part 1
while not nx.is_connected(g): # part 2
    closest_conn = ()
    closest_dist = np.inf
    for j, p in enumerate(d_np): # looking out from each node
        k_val = 2
        searching = True
        while searching: # trying to find closest connection
            if (d[j], k_val) in seen:
                dist, idx = seen[(d[j], k_val)]
            else:
                dist, idx = tree.query(p, k=k_val)
                seen[(d[j], k_val)] = (dist, idx)
            if g.has_edge(d[j], d[idx[k_val-1]]):
                k_val += 1
                continue # already have, next k
            
            if dist[k_val-1] < closest_dist: # found new closest
                closest_conn = (j, idx[k_val-1])
                closest_dist = dist[k_val-1]
            searching = False # found at least something
            
    g.add_edge(d[closest_conn[0]], d[closest_conn[1]])
    # this print is pretty to watch
    # print([len(c) for c in sorted(nx.connected_components(g), key=len, reverse=True)])

# part 1
# comps = [len(c) for c in sorted(nx.connected_components(g), key=len, reverse=True)]
# print(comps[0] * comps[1] * comps[2])

# part 2
print(int(d[closest_conn[0]][0]) * int(d[closest_conn[1]][0]))