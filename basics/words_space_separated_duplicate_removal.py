#!/usr/bin/python

def AcceptSpaceSeparatedWordsRemoveDuplicateAndSort():
	'''	Accept Space Separated List of Words,
		Remove Duplicate Words,
		Display sorted list of words
	'''
	x = raw_input("Enter space separated list of words:")
	l1 = set(x.split(' '))
	print sorted(l1)

if __name__ == '__main__':
	AcceptSpaceSeparatedWordsRemoveDuplicateAndSort()
