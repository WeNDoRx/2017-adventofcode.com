#!/usr/bin/env python

def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

mylist = list(xrange(256))

lines = [line.rstrip('\n') for line in open('input')]
lengths = map(int, lines[0].split(","))

i = 0
skipsize = 0
for length in lengths:
	# dirty hack for cyclic behaviour
	worklist = mylist + mylist
	# generate sublist and reversed sublist
	sublist = worklist[i : i+length]
	reversed_sublist = sublist[::-1]
	# modify work list with reversed sublist in place
	worklist = worklist[:i] + reversed_sublist + worklist[i+length:]
	# modify my list by shifting accordingly
	mylist = shift(worklist[i:i+len(mylist)], i)
	# change current position and inc skipsize
	i = (i + length + skipsize) % (len(mylist))
	skipsize += 1

print mylist[0] * mylist[1]