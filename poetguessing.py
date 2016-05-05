#!/usr/bin/python3

import sys
import fileinput, re, operator

from collections import defaultdict
from math import log

import os


words = defaultdict(lambda: defaultdict(int))
pattern = re.compile(r'[a-zA-Z]+', re.I)
count = 0
logsum = 0

if (len(sys.argv)>1):
	search = sys.argv[1]

seen = set()

for filename in os.listdir('poetry'):
	count = 0
	name = filename.lower().rstrip(".txt")
	f = open('poetry/%s' % filename, 'r')
	for line in f:
		for (word) in re.findall(pattern,line):
			# print filename.lower().rstrip(".txt")
			words[name][word.lower()]+=1
			count += 1

# 	# print " ".join(( filename, str(count), str(words[search]), str(float(float(words[search])/float(count))) ))
# 	# print '{:>4}/{:>6} = {:.12} {}'.format(str(words[search]),str(count),str(float(float(words[search])/float(count))), filename.rstrip(".txt"))
	# print 'log(({}+1)/{:>6}) = {:8.4f} {}'.format(str(words[search]), str(count), log((words[name][search]+1.0)/count),filename)

print ">>>{}".format(words['john_keats']['and'])

logsums = defaultdict(int)

for filename in os.listdir('tests'):
	logsums.clear()
	f = open('tests/%s' % filename, 'r')
	for line in f:
		for (word) in re.findall(pattern,line):
			if word not in seen:
				for poet in words:
					seen.add(word)
					logsums[poet] += log((words[poet][word]+1.0)/count)
			


	tmp = max(logsums.iteritems(), key=operator.itemgetter(1))
	print "{} most resembles the work of {} (log-probability={}".format(filename,tmp[0],tmp[1])
	# print logsums
