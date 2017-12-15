#!/usr/bin/env python

lines = [line.rstrip('\n') for line in open('input')]

vals_a = []
vals_b = []

def generator_A(input):
	global vals_a
	val = input * 16807 % 2147483647
	if val % 4 == 0:
		vals_a.append(val)
	return val

def generator_B(input):
	global vals_b
	val = input * 48271 % 2147483647
	if val % 8 == 0:
		vals_b.append(val)
	return val

seed_a = int(lines[0].split("with ")[1])
seed_b = int(lines[1].split("with ")[1])

s = 0

while True:
	if len(vals_a) < 5000000:
		seed_a = generator_A(seed_a)
	if len(vals_b) < 5000000:
		seed_b = generator_B(seed_b)
	if len(vals_b) == 5000000 and len(vals_a) == 5000000:
		break

for x in xrange(0, 5000000):
	if bin(vals_a[x])[-16:] == bin(vals_b[x])[-16:]:
		s += 1

print s