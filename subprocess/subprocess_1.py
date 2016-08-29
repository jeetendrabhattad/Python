import subprocess

# Simple command
subprocess.call(['python loop.py', '-l'], shell=True)
#subprocess.call(['python loop.py', '-l'], shell=False)
subprocess.call(['ls', '-l'], shell=False)
subprocess.call(['ls', '-l'], shell=True)

'''
The return value from call() is the exit code of the program. The caller is responsible for interpreting it to detect errors. The check_call() function works like call() except that the exit code is checked, and if it indicates an error happened then a CalledProcessError exception is raised.
'''
#subprocess.check_call(['cp', '-l'], shell=True)
subprocess.check_call(['cp out1.txt out3.txt'], shell=True)

#Capturing output
output = subprocess.check_output(['ls', '-l'])
print 'Have %d bytes in output' % len(output)
print output

#Working with Pipes Directly

#To run a process and read all of its output, set the stdout value to PIPE and call communicate().
print '\nread:'
proc = subprocess.Popen(['echo', '"to stdout"'], 
                                stdout=subprocess.PIPE )
stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)

#set up a pipe to allow the calling program to write data to it, set stdin to PIPE.
print '\nwrite:'
proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE)
proc.communicate('\tJay Jay Ram-krishna Hari to stdin\n')

#setup to do read & write as part of one subprocess
print '\npopen2:'

proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout_value = proc.communicate('through stdin to stdout')[0]
print '\tpass through:', repr(stdout_value)
