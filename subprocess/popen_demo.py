import subprocess
def LineWordCharCount(input_file, output_file, error_file):
    fd_in = open(input_file,"r")
    print fd_in
    fd_out = open(output_file,"w")
    print fd_out
    fd_error = open(error_file,"w")
    print fd_error
    print '\nread:'
    proc = subprocess.Popen(['wc'],stdin=fd_in, stdout=fd_out, stderr=fd_error)
    fd_in.close()
    fd_out.close()
    fd_error.close()

def main():
    input_file = input("Enter input file name:")
    output_file = input("Enter output file name:")
    error_file = input("Enter output error name:")
    LineWordCharCount(input_file, output_file, error_file)

if __name__ == "__main__":
    main()
#stdout_value = proc.communicate()[0]
#print '\tstdout:', repr(stdout_value)
