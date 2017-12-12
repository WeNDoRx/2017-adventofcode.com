#!/usr/bin/env python

groups = [[0]]

def addtToGroups(connected):
	global groups
	tmp = []
	for group in groups:
		for element in connected:
			if element in group:
				tmp += [group]
			
	for delete in tmp:
		if delete in groups:
			groups.remove(delete)

	groups += [list(set(sum(tmp, []) + connected))]

lines = [line.rstrip('\n') for line in open('input')]

for line in lines:
	
	src = int(line.split("<->")[0])
	dst = map(int, line.split("<->")[1].split(","))
	# connected ends
	connected = list(set([src] + dst))
	addtToGroups(connected)

print len(groups)