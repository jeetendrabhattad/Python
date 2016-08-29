def notdivisibleby(x):
    return x%2 !=0 and x%3!=0

print (filter(notdivisibleby, range(2, 25)))
print (map(notdivisibleby, range(2, 25)))
