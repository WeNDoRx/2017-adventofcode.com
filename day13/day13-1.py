#!/usr/bin/env python

def stepPacket(position):
	position += 1
	global severity
	if firewall[position][1] == 0:
		severity += position * firewall[position][0]
		#print "FOUND"
	return position


def stepLayer(layer):
	firewall[layer] = (firewall[layer][0], firewall[layer][1] + firewall[layer][2], firewall[layer][2])
	if firewall[layer][1] == firewall[layer][0] -1:
	 	firewall[layer] = (firewall[layer][0], firewall[layer][1], -1)
	if firewall[layer][1] == 0:
 		firewall[layer] = (firewall[layer][0], firewall[layer][1], 1)

def performFirewallStep():
	for x in firewall:
		if firewall[x][1] != -1:
			stepLayer(x)

firewall = {}

lines = [line.rstrip('\n') for line in open('input')]

max_layer = 0
packet_position = -1
severity = 0

for line in lines:
	max_layer = max(max_layer, int(line.split(": ")[0]))

for x in xrange(0, max_layer):
	firewall[x] = (0, -1, 1)

for line in lines:
	firewall[int(line.split(": ")[0])] = int(line.split(": ")[1]), 0, 1

#print "initial:", firewall

for x in xrange(0, max_layer + 1):
	packet_position = stepPacket(packet_position)
	#print packet_position
	performFirewallStep()
	#print "at the end of picosecond", x, ":", firewall
print severity