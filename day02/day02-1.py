#!/usr/bin/env python

lines = []
with open("input") as f:
	for line in f:
		split = map(int, line.rstrip().split("\t"))
		lines += [split]

s = 0

for line in lines:
	s += max(line) - min(line)

print s