#!/usr/bin/python

import arithmatic_operations

basic = input("Enter Basic Salary:-")
salary = arithmatic_operations.Add(basic, basic/2)
tax = arithmatic_operations.Div(salary,10)
salary = arithmatic_operations.Sub(salary,tax)
print("salary is %d"%salary)
