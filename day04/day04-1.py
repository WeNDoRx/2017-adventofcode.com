#!/usr/bin/env python

lines = [line.rstrip('\n') for line in open('input')]

print sum(len(x.split(" ")) == len(set(x.split(" "))) for x in lines)