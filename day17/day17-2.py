#!/usr/bin/env python

spin = [line.rstrip('\n') for line in open('input')]
spin = int(line)

# since 0 is always at the first place, we only care when we insert a value after 0
# that's why we can only track when a value is inserted after 0 and pretend we inserted
# something but actually insert nothing but increase the virutal length of the buffer
buff = [0]
pos = 0
len_buff = 1

for x in xrange(1,50000001):
	ins = (pos + spin) % len_buff
	if ins == 0:
		buff = [0, x] + buff[1:]
	pos = ins + 1
	len_buff += 1
print buff[1]