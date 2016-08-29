import subprocess
#subprocess.call(['cp'], shell=False)
#subprocess.check_call(['cp'])
output = None
try:
    #global output
    output = subprocess.check_output(['ls'], shell=True, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    #global output
    print "In exception:"
    print e.__str__()
    print e.returncode
    #print output
'''
output = subprocess.check_output(['cp'], shell=False, stderr=subprocess.STDOUT)
print 'Have %d bytes in output' % len(output)
print output
'''
