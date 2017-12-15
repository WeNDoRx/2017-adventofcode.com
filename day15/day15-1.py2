#!/usr/bin/env python

lines = [line.rstrip('\n') for line in open('input')]

def generator_A(input):
	return input * 16807 % 2147483647

def generator_B(input):
	return input * 48271 % 2147483647

seed_a = int(lines[0].split("with ")[1])
seed_b = int(lines[1].split("with ")[1])

s = 0

for x in xrange(0,40000000):
	seed_a = generator_A(seed_a)
	seed_b = generator_B(seed_b)
	if bin(seed_a)[-16:] == bin(seed_b)[-16:]:
		s += 1

print s