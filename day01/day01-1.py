#!/usr/bin/env python

f = open("day01.input","r")

captcha = (f.readline())

s = 0

for x in xrange(0, len(captcha) - 1):
	if captcha[x] == captcha[x+1]:
		s += int(captcha[x])
if captcha[len(captcha)-1] == captcha[0]:
	s += int(captcha[0])

print s