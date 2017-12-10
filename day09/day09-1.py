#!/usr/bin/env python

def removeIgnored(line):
	new_line = ""
	i = 0
	while i != len(line):
		if line[i] == "!":
			i += 2
			continue
		new_line += line[i]
		i += 1
	return new_line

def removeGarbage(line):
	new_line = ""
	i = 0
	while i != len(line):
		if line[i] == "<":
			i = line.find(">", i) + 1
			continue
		new_line += line[i]
		i += 1
	return new_line

def calculateScore(line):
	score = 0
	level = 0
	i = 0
	while i != len(line):
		if line[i] == "{":
			level += 1
			i += 1
			continue
		if line[i] == "}":
			score += level
			level -= 1
		i += 1
	return score

lines = [line.rstrip('\n') for line in open('input')]

for line in lines:
	line = removeIgnored(line)
	line =  removeGarbage(line)
	print calculateScore(line)