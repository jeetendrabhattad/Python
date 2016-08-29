#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   opts,args = getopt.getopt(argv,"i:o:")
   print type(opts)
   print args
   print opts
   if opts.__eq__(list()):
      print 'empty'
      sys.exit(1)
   for opt, arg in opts:
      if opt in ("-i"):
         inputfile = arg
         print 'Input file is "', inputfile
      elif opt in ("-o"):
         outputfile = arg
         print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])
