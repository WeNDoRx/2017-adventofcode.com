#!/usr/bin/env python

lines = [line.rstrip('\n') for line in open('input')]
newlines = []

for line in lines:
	line = line.split(" ")
	newline = ""
	for element in line:
		newline += ''.join(sorted(element)) + " "
	newlines.append(newline)

print sum(len(x.split(" ")) == len(set(x.split(" "))) for x in newlines)