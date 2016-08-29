import subprocess
fd = open("error.txt", "w")
output = subprocess.check_output('echo to stdout; echo to stderr 1>&2',shell=True,stderr=fd)
print type(output)
print subprocess.STDOUT
print 'Have %d bytes in output' % len(output)
print output
