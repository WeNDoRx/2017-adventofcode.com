#!/usr/bin/env python

progs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
#progs = ["a","b","c","d","e"]

def executeInstruction(instruction):
	global progs
	if instruction[0] == "s":
		spin = int(instruction.split("s")[1])
		progs = progs[-spin:] + progs[:-spin]
		return

	if instruction[0] == "x":
		swap = map(int, instruction.split("x")[1].split("/"))
		progs[swap[0]], progs[swap[1]] = progs[swap[1]], progs[swap[0]]
		return

	if instruction[0] == "p":
		swap = instruction[1:].split("/")
		a, b = progs.index(swap[0]), progs.index(swap[1])
		progs[a], progs[b] = swap[1], swap[0]
		return

lines = [line.rstrip('\n') for line in open('input')]

instructions = lines[0].split(",")

# the idea is simple: we look for repeating chunks and modulo 1 billion with it ...
confs = {}
i = 0
confs["".join(progs)] = i

while True:
	for instruction in instructions:
		executeInstruction(instruction)
	if "".join(progs) not in confs:
		confs["".join(progs)] = i
		i += 1
	else:
		break

for _ in xrange(0, 1000000000 % (i + 1)):
	for instruction in instructions:
		executeInstruction(instruction)

print "".join(progs)