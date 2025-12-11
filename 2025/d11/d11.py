import numpy as np
import networkx as nx
from tqdm import tqdm
import matplotlib.pylab as plt

with open('d11.txt', 'r') as file:
    data = file.read().split("\n")

you = None
G = nx.DiGraph()

for l in data:
    ll = l.split(":")
    end = ll[1].split(" ")[1:]
    for e in end:
        G.add_edge(ll[0], e)

print(G)
print(f"is dag: {nx.is_directed_acyclic_graph(G)}")
nx.draw_spring(G, with_labels=True)
# plt.show()

paths_1 = nx.all_simple_paths(G, "you", "out")
p1 = 0
for p in paths_1:
    p1 += 1
print(p1)

# sadly, I can't just use all_simple_paths for part 2, way too long lol

def node_check(state, node):
    # updates the state of the node
    # state meaning what specific nodes it has visited
    if node == "dac":
        if state == 0: # none to dac
            return 1
        if state == 2: # fft to dac
            return 3
        return state
    
    if node == "fft":
        if state == 0: # none to fft
            return 2
        if state == 1: # dac to fft
            return 3
        return state
    
    return state


topo = list(nx.topological_sort(G))
states = [0, 1, 2, 3]
# 0 is none, 1 is dac, 2 is fft, 3 is both

store = {node: {state: 0 for state in states} for node in G.nodes()}
store["svr"][0] = 1

for node in topo: # for each node, topologically
    for w in G.successors(node): # for each sucessor node below it
        for state in states: # for each state
            # we check the number of paths to this current node with this state
            paths = store[node][state]
            # we can quickly exit if there are no paths
            if paths == 0:
                continue
            # we find the next state
            next_state = node_check(state, node)
            # we add the number of paths to the successor node with the next state
            store[w][next_state] += paths

print(store["out"][3])