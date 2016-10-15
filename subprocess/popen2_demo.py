import subprocess

print '\npopen2:'

proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
print proc.poll(), " child term"
stdout_value = proc.communicate('through stdin to stdout')[0]
print '\tpass through:', repr(stdout_value)
