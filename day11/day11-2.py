#!/usr/bin/env python

def getCoordinates(path):
	return path.count("nw") - path.count("se"), path.count("n") - path.count("s"), path.count("ne") - path.count("sw")

def getMinWayBack((nw, n, ne)):
	return max(abs(nw - n), abs(n - ne), abs(ne - nw))

lines = [line.rstrip('\n') for line in open('input')]
path = lines[0].split(",")

maxi = 0
for x in xrange(1, len(path)):
	if getMinWayBack(getCoordinates(path[:x])) > maxi:
	 	maxi = getMinWayBack(getCoordinates(path[:x]))

print maxi