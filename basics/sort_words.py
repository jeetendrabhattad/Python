#!/usr/bin/python

def SortAcceptedWords():
	words = raw_input("Enter Words")
	print(words)
	items = words.split(',')
	items.sort()
	print(','.join(items))

if __name__ == '__main__':
	SortAcceptedWords()
