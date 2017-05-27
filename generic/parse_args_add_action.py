import argparse
'''
def test():
    print "test"
class Square(argparse.Action):
    def __init__(self, **kwargs):
        print("constructor")
        self.type = "count"
'''
parser = argparse.ArgumentParser()
parser.add_argument("-x", type=int, help="the base")
parser.add_argument("-y", type=int, help="the exponent")
#nswer = args.x**args.y
#parser.add_argument("-v", "--verbosity", action=Square)
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
print args
answer = args.x**args.y
print args.verbosity
if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
if args.verbosity >= 1:
        print("{}^{} == ".format(args.x, args.y))
        print(answer)
