#!/usr/bin/env python

registers = {}

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def initiateRegisters(lines):
	global registers
	for line in lines:
		registers[line.split(" ")[1]] = 0

def execute(instruction):
	global registers, pc, snd
	instruction = instruction.split(" ")

	# snd instruction
	if instruction[0] == "snd":
		snd = registers[instruction[1]]
		#print "set snd to", snd

	# set instruciton
	if instruction[0] == "set":
		if RepresentsInt(instruction[2]):
			registers[instruction[1]] = int(instruction[2])
		else:
			registers[instruction[1]] = registers[instruction[2]]

	# add instruction
	if instruction[0] == "add":
		if RepresentsInt(instruction[2]):
			registers[instruction[1]] += int(instruction[2])
		else:
			registers[instruction[1]] += registers[instruction[2]]

	# mul instruction
	if instruction[0] == "mul":
		if RepresentsInt(instruction[2]):
			registers[instruction[1]] *= int(instruction[2])
		else:
			registers[instruction[1]] *= registers[instruction[2]]

	# mod instruction
	if instruction[0] == "mod":
		if RepresentsInt(instruction[2]):
			registers[instruction[1]] = registers[instruction[1]] % int(instruction[2])
		else:
			registers[instruction[1]] = registers[instruction[1]] % registers[instruction[2]]

	# rcv instruction
	if instruction[0] == "rcv" and registers[instruction[1]] != 0:
		print snd
		pc = -100
		snd = registers[instruction[1]]

	# rcv instruction
	if instruction[0] == "jgz" and registers[instruction[1]] > 0:
		pc += int(instruction[2]) - 1

	pc += 1
	#print registers, pc

lines = [line.rstrip('\n') for line in open('input')]

initiateRegisters(lines)

pc = 0
snd = 0

while pc < len(lines) and pc > -1:
	#print lines[pc]
	execute(lines[pc])
	#raw_input()

