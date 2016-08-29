import subprocess
fd = open("popen_demo.py","r")
print fd
fd1 = open("out1.txt","w")
print fd1
fd2 = open("out2.txt","w")
print fd2
print '\nread:'
proc = subprocess.Popen(['wc'],stdin=fd, stdout=fd1, stderr=fd2)
fd.close()
#stdout_value = proc.communicate()[0]
#print '\tstdout:', repr(stdout_value)
