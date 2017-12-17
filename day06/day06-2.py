#!/usr/bin/env python

import hashlib

lines = [line.rstrip('\n') for line in open('input')]
blocks = map(int, ' '.join(lines).split('\t'))
configurations = [hashlib.md5(''.join(map(str, blocks[:]))).hexdigest()]

while True:
	m = max(blocks)
	i = blocks.index(max(blocks))
	blocks[i] = 0

	for x in xrange(0, m):
		i += 1
		if i >= len(blocks):
			i = 0
		blocks[i] += 1

	if (hashlib.md5(' '.join(map(str, blocks[:]))).hexdigest()) in configurations:
		print len(configurations) - configurations.index(hashlib.md5(' '.join(map(str, blocks[:]))).hexdigest())
		break

	configurations.append(hashlib.md5(' '.join(map(str, blocks[:]))).hexdigest())