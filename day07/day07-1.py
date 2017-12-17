#!/usr/bin/env python

lines = [line.rstrip('\n') for line in open('input')]

all_nodes = []
for line in lines:
	node = line.split(" ")[0]
	all_nodes += [node]
	if len(line.split(" ")) > 2:
		for node in line.split("->")[1].strip().split(", "):
			all_nodes += [node]

print list(set([i for i in all_nodes if all_nodes.count(i) == 1]))[0]