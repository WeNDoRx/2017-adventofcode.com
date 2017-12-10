#!/usr/bin/env python

regs = {}

glob_max = 0

lines = [line.rstrip('\n') for line in open('input')]

def operate(dst, op, amm, cond_src, cond, cond_amm):
	global glob_max
	cond_status = eval(str(regs[cond_src]) + cond + cond_amm)
	if cond_status:
		if op == "inc":
			regs[dst] += int(amm)
		if op == "dec":
			regs[dst] -= int(amm)
	glob_max = max(glob_max, regs[dst])
	

for line in lines:
	split = line.split(" ")
	
	dst = split[0]
	opp = split[1]
	amm = split[2]
	cond_src = split[4]
	cond = split[5]
	cond_amm = split[6]

	if dst not in regs:
		regs[dst] = 0
	if cond_src not in regs:
		regs[cond_src] = 0

	operate(dst, opp, amm, cond_src, cond, cond_amm)

print glob_max