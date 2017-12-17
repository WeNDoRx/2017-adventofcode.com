#!/usr/bin/env python

f = open("input","r")

captcha = (f.readline())

s = 0

for x in xrange(0, len(captcha)):
	if captcha[x] == captcha[((x+len(captcha)/2))%len(captcha)]:
		s += int(captcha[x])

print s
