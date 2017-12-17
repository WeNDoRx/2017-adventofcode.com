#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt

lines = [line.rstrip('\n') for line in open('input')]

G=nx.DiGraph()

for line in lines:
	node = line.split(" ")[0]
	#print "adding node", node
	G.add_node(node, weight = int(line.split(" ")[1][1:-1] ))
	if len(line.split(" ")) > 2:
		for child in line.split("->")[1].strip().split(", "):
			#print "adding edge", node, "->", child
			G.add_edge(node, child)

root = nx.topological_sort(G)[0]

children = list(reversed(list(nx.topological_sort(G))))

# add attribute total_weight = 0
nx.set_node_attributes(G, 0, "total_weight")

for x in children:
	G.node[x]["total_weight"] = G.node[x]["weight"]

for x in children:
	for child in G.neighbors(x):
		G.node[x]["total_weight"] += G.node[child]["total_weight"]

previous_problem = None
problem = root
while problem != None:
	previous_problem = problem
	weights = []
	for child in G.neighbors(problem):
		weights.append(G.node[child]["total_weight"])
	#print weights
	for child in G.neighbors(problem):
		problem = None
		if weights.count(G.node[child]["total_weight"]) == 1:
			problem = child
			break

for node in G:
	if previous_problem in G.neighbors(node):
		weights = []
		for child in G.neighbors(node):
			weights.append(G.node[child]["total_weight"])

weights = list(set(weights))
weights.remove(G.node[previous_problem]["total_weight"])

print G.node[previous_problem]["weight"] - G.node[previous_problem]["total_weight"] + weights[0]

	#if weights.count(G.node[child]["total_weight"]) != 1:
	#	print G.node[child]["total_weight"]
	#	break

#nx.draw(G, with_labels = True)
#plt.show()
