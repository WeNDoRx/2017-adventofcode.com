#!/usr/bin/env python

def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

def one_round(mylist, curr_pos, skip_size):
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

def n_rounds(mylist, n):
	curr_pos, skip_size = 0, 0
	for _ in xrange(0, n):
		mylist, curr_pos, skip_size = one_round(mylist, curr_pos, skip_size)
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

# my list, 0 .. 255
mylist = list(xrange(256))

lines = [line.rstrip('\n') for line in open('input')]

# generate the lengths_list by converting each element from the input to it's ord and adding the default sufix
lengths_list = map(str, lines[0])
lengths_list = list((ord(i) for i in lengths_list)) + [17, 31, 73, 47, 23]

# calculate the sparse hash by running one round 64 times
sparse_hash = n_rounds(mylist, 64)
# calculate dense hash from sparse hash
dense_hash = densify(sparse_hash)

print dense_hash