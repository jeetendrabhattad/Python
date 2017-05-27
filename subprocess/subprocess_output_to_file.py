#!/usr/bin/python
import subprocess

fd=open("a.txt", "w")
proc = subprocess.Popen(['echo', '"to stdout"'], stdout=fd)
fd.close()
