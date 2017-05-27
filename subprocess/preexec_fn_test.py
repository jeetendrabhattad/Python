#!/usr/bin/python
import subprocess

def foo():
    print("Executed.....")

subprocess.Popen(['echo', '"to stdout"'], preexec_fn = foo)

