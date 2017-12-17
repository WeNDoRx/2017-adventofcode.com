#!/usr/bin/env python

lines = []
with open("input") as f:
	for line in f:
		split = map(int, line.rstrip().split("\t"))
		lines += [split]

s = 0

for line in lines:
	for x in xrange(0, len(line)):
		for y in xrange(0, len(line)):
			if line[x] % line[y] == 0 and x != y:
				s += line[x] / line[y]

print s