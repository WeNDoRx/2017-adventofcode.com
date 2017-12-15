#!/usr/bin/env python

import binascii

def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

def one_round(mylist, curr_pos, skip_size, lengths_list):
	i = curr_pos
	skip_size = skip_size
	for length in lengths_list:
		worklist = mylist + mylist
		sublist = worklist[i : i+length]
		reversed_sublist = sublist[::-1]
		worklist = worklist[:i] + reversed_sublist + worklist[i+length:]
		mylist = shift(worklist[i:i+len(mylist)], i)
		i = (i + length + skip_size) % (len(mylist))
		skip_size += 1
	return mylist, i, skip_size

def n_rounds(mylist, n, lengths_list):
	curr_pos, skip_size = 0, 0
	for _ in xrange(0, n):
		mylist, curr_pos, skip_size = one_round(mylist, curr_pos, skip_size, lengths_list)
	return mylist

def densify(sparse_hash):
	dense = []
	# for 16 groups
	for x in xrange(0, 16):
		r = 0
		# of 16 elements
		for y in xrange (0, 16):
			# xor them all
			r = r ^ sparse_hash[x * 16 + y]
		dense += [r]
	# generate string
	return "".join(['%.2x' % x for x in dense])

def knot(index):
	# my list, 0 .. 255
	mylist = list(xrange(256))

	lines = [line.rstrip('\n') for line in open('input')]

	# generate the lengths_list by converting each element from the input to it's ord and adding the default sufix
	lengths_list = map(str, lines[0] + "-" + str(index))
	lengths_list = list((ord(i) for i in lengths_list)) + [17, 31, 73, 47, 23]

	# calculate the sparse hash by running one round 64 times
	sparse_hash = n_rounds(mylist, 64, lengths_list)
	# calculate dense hash from sparse hash
	dense_hash = densify(sparse_hash)

	return dense_hash

def binify(string):
	final = ""
	for x in string:
		if x == "0":
			final += "0000"
			continue
		if x == "1":
			final += "0001"
			continue
		if x == "2":
			final += "0010"
			continue
		if x == "3":
			final += "0011"
			continue
		if x == "4":
			final += "0100"
			continue
		if x == "5":
			final += "0101"
			continue
		if x == "6":
			final += "0110"
			continue
		if x == "7":
			final += "0111"
			continue
		if x == "8":
			final += "1000"
			continue
		if x == "9":
			final += "1001"
			continue
		if x == "a":
			final += "1010"
			continue
		if x == "b":
			final += "1011"
			continue
		if x == "c":
			final += "1100"
			continue
		if x == "d":
			final += "1101"
			continue
		if x == "e":
			final += "1110"
			continue
		if x == "f":
			final += "1111"
			continue
	return final

s = 0

for x in xrange(0,128):
	s += binify(knot(x)).count("1")

print s