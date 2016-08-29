#!/usr/bin/python

def GenerateMatrix(rows, cols):
	row = []
	matrix = []
	for i in range(rows):
		for j in range(cols):
			row.append(i*j)
		matrix.append(row)
		row = []
	return matrix

if __name__ == '__main__':
	rows = input("Enter Number of Rows:")
	cols = input("Enter Number of Columns i.e elements per row:")
	print(GenerateMatrix(rows, cols))
