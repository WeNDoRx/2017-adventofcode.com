#!/usr/bin/env python

groups = [[0]]

def updateGroups(connected):
	global groups
	# temporary list of groups
	tmp = []
	# for each group
	for group in groups:
		# for each element in the connected elements list
		for element in connected:
			# if the element is found in the current group
			if element in group:
				# add the group to the temporary list of groups
				tmp += [group]
	# for each group in the temporary groups
	for delete in tmp:
		# if it is possible
		if delete in groups:
			# delete the group from the global groups list
			groups.remove(delete)
	# add the new group, that is a flattened list of elements in the old groups and elements in the new connected ones
	groups += [list(set(sum(tmp, []) + connected))]

lines = [line.rstrip('\n') for line in open('input')]

for line in lines:
	# one input source
	src = int(line.split("<->")[0])
	# multiple output destinations 
	dst = map(int, line.split("<->")[1].split(","))
	# connected ends
	connected = list(set([src] + dst))

	updateGroups(connected)

for x in groups:
	if 0 in x:
		print len(x)