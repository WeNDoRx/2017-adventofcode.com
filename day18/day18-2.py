#!/usr/bin/env python

from collections import deque

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def initiateRegisters(lines, reg, x):
	for line in lines:
		if not RepresentsInt(line.split(" ")[1]):
			reg[line.split(" ")[1]] = 0
		if line.split(" ")[1] == "p":
			reg[line.split(" ")[1]] = x

def execute(instruction, reg, pc, deq_in, deq_out, machineid):
	global sndcount

	instruction = instruction.split(" ")

	# snd instruction
	if instruction[0] == "snd":
		if RepresentsInt(instruction[1]):
			deq_out.append(int(instruction[1]))
		else:
			deq_out.append(reg[instruction[1]])
		if machineid == 1:
			sndcount += 1

	# set instruciton
	if instruction[0] == "set":
		if RepresentsInt(instruction[2]):
			reg[instruction[1]] = int(instruction[2])
		else:
			reg[instruction[1]] = reg[instruction[2]]

	# add instruction
	if instruction[0] == "add":
		if RepresentsInt(instruction[2]):
			reg[instruction[1]] += int(instruction[2])
		else:
			reg[instruction[1]] += reg[instruction[2]]

	# mul instruction
	if instruction[0] == "mul":
		if RepresentsInt(instruction[2]):
			reg[instruction[1]] *= int(instruction[2])
		else:
			reg[instruction[1]] *= reg[instruction[2]]

	# mod instruction
	if instruction[0] == "mod":
		if RepresentsInt(instruction[2]):
			reg[instruction[1]] = reg[instruction[1]] % int(instruction[2])
		else:
			reg[instruction[1]] = reg[instruction[1]] % reg[instruction[2]]

	# rcv instruction
	if instruction[0] == "rcv":
		reg[instruction[1]] = deq_in.popleft()

	# jgz instruction
	if instruction[0] == "jgz":
		# cmp
		if RepresentsInt(instruction[1]):
			cmpv = int(instruction[1])
		else:
			cmpv = reg[instruction[1]]
		# cmpt
		if RepresentsInt(instruction[2]):
			val = int(instruction[2])
		else:
			val = reg[instruction[2]]

		if cmpv > 0:
			pc += val - 1
	pc += 1
	return reg, pc, deq_in, deq_out

lines = [line.rstrip('\n') for line in open('input')]

sndcount = 0

reg0, reg1 = {}, {}
pc0, pc1 = 0, 0
deq0, deq1 = deque(), deque()

initiateRegisters(lines, reg0, 0)
initiateRegisters(lines, reg1, 1)

while not(lines[pc0].split(" ")[0] == "rcv" and len(deq0) == 0 and lines[pc1].split(" ")[0] == "rcv" and len(deq1) == 0):
	
	while not(lines[pc0].split(" ")[0] == "rcv" and len(deq0) == 0):
		reg0, pc0, deq0, deq1 = execute(lines[pc0], reg0, pc0, deq0, deq1, 0)

	while not(lines[pc1].split(" ")[0] == "rcv" and len(deq1) == 0):
		reg1, pc1, deq1, deq0 = execute(lines[pc1], reg1, pc1, deq1, deq0, 1)

print sndcount