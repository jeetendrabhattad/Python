#!/usr/bin/python
import sys

def TestDivision(numerator, denominator):
    try:
        result = numerator/denominator
        #x += 10
        print result
    except ZeroDivisionError as e:
        print "ZeroDivisionError:", e 
        sys.exit(0)
    except ArithmeticError as e:
        print "ArithmeticError:", e 
        sys.exit(0)
    except BaseException as e:
        print("Exception caught", e)
    else:
        print "No Exception Occured Hence Executing"
    finally:
        print "Executing in any case"
    '''
    except Exception as e:
        print "Exception:", e
    print "Executing Always"
    '''
if __name__ == "__main__":
    TestDivision(10, 20)
    TestDivision(10, 0)
