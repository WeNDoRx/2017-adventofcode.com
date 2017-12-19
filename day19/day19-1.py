#!/usr/bin/env python

import numpy as np

def getStart(matrix):
	return (0, matrix[0].index("|"))

def follow(start):
	d = 0
	x, y = start
	while matrix[x][y] != " ":
		# follow line
		if matrix[x][y] != "+":
			if matrix[x][y].isupper():
				colected.append(matrix[x][y])
			# down
			if d == 0:
				x += 1
			# right
			if d == 1:
				y += 1
			# up
			if d == 2:
				x -= 1
			# left
			if d == 3:
				y -= 1

		# else means +
		else:
			# vertical to horizontal
			if d == 0 or d == 2:
				# if there is something at the right
				if matrix[x][y+1] != " ":
					y += 1
					d = 1
					continue
				if matrix[x][y-1] != " ":
					y += -1
					d = 3
					continue
			# horizontal to vertical
			if d == 1 or d == 3:
				# if there is something above
				if matrix[x-1][y] != " ":
					x += -1
					d = 2
					continue
				# if there is something below
				if matrix[x+1][y] != " ":
					x += 1
					d = 0
					continue

lines = [line.rstrip('\n') for line in open('input')]

matrix = []
colected = []

for line in lines:
	matrix += [list(line)]

start = getStart(matrix)
follow(start)
print "".join(colected)