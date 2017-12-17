#!/usr/bin/env python

spin = [line.rstrip('\n') for line in open('input')]
spin = int(spin[0])

buff = [0]
pos = 0

for x in xrange(1,2018):
	ins = (pos + spin) % len(buff)
	buff = buff[:ins+1] + [x] + buff[ins+1:]
	pos = ins + 1
print buff[buff.index(2017)+1]