#!/usr/bin/env python 

lines = map(int, [line.rstrip('\n') for line in open('input')])

index = 0
c = 0

while index >=0 and index < len(lines):
	lines[index] += 1
	#print lines, "-", index
	index += lines[index] - 1

	#print lines, "-", index
	c += 1
print c
