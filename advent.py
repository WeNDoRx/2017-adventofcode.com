#!/usr/bin/env python

import argparse
import sys
import os
import itertools

parser = argparse.ArgumentParser(description='2017 adventofcode.com solutions')
parser.add_argument('-d','--day', help='Run the solution for what day ? (1..25) | \'a\' for all', required=True)
parser.add_argument('-t','--task', help='First or second task ? (1 or 2)', required=False)
args = vars(parser.parse_args())

if args['day'] not in str(range(1,25)) and not 'a':
	print 'Day must be between 1 and 25 or a'
	sys.exit(-1)
if args['task'] not in ['1', '2', None]:
	print 'Task must be 1, 2 or parameter not used'
	sys.exit(-1)

torun = []

if args['day'] == 'a':
	torun = ['day%02d' % (x,) for x in xrange(1,26)]
else:
	torun = ['day%02d' % (int(args['day']),)]

if args['task'] == None:
	torun = list(itertools.chain.from_iterable([['./'+x+'/'+x+'-1.py', './'+x+'/'+x+'-2.py'] for x in torun]))
else:
	torun = list(itertools.chain.from_iterable([['./'+x+'/'+x+'-'+args['task']+'.py'] for x in torun]))

for file in torun:
	if not os.path.isfile(file):
		print 'File ' + file + ' does not exist.'
		sys.exit(-2)

for file in torun:
	os.chdir(file[2:7])
	execfile(file[8:])
	os.chdir('..')