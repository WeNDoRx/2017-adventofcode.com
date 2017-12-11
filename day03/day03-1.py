#!/usr/bin/env python

def A(n):
	return 4*n**2 - 10*n + 7

def B(n):
	return 4*n**2 - 8*n + 5

def C(n):
	return 4*n**2 - 6*n + 3

def D(n):
	return 4*n**2 - 4*n + 1

def find_supperior_swipe(n):
	# for exponents
	for x in xrange(1, n):
		# for direction
		for d in xrange(0, 4):
			if d == 0:
				if A(x) > n:
					return(x, d)
				
			if d == 1:
				if B(x) > n:
					return(x, d)
				
			if d == 2:
				if C(x) > n:
					return(x, d)
				
			if d == 3:
				if D(x) > n:
					return(x, d)

def find_distance(x, l, n):
	sup, inf = 0,0
	if l == 0:
		sup, inf = A(x), D(x-1) + 1

	if l == 1:
		sup, inf = B(x), A(x)

	if l == 2:
		sup, inf = C(x), B(x)

	if l == 3:
		sup, inf = D(x), C(x)

	if sup - n == abs(inf - n):
		return x-1

	middle = (sup + inf)/2
	
	return abs(n - middle) + x - 1


n = int(open("input").readline().rstrip())

print find_distance(find_supperior_swipe(n)[0], find_supperior_swipe(n)[1], n)