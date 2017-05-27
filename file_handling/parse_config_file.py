#!/usr/bin/python

def Open(config_file_name):
    fd = open(config_file_name)
    # validate configuration file if any
    return fd
def ParseConfig(config_file_handle):
    result = {}
    line = " "
    if config_file_handle != None:
        print line
        while line != "":
            line = config_file_handle.readline()
            if line.startswith('['):
                break
            if not line.startswith("#") and "=" in line:
                config_option = line.split("=")
                #print config_option
                if "#" in config_option[1]:
                    config_option[1] = config_option[1].split("#")[0]
                result[config_option[0]] = config_option[1][0:-1]
    print result, line
    return result, line

def ParseSections(config_file_handle):
    result = {}
    key = ''
    if config_file_handle != None:
        line = " "
        while line != "":
            #print line
            if line.startswith('['):
                key = line[1:line.index(']')]
                #print key
                dic, line = ParseConfig(config_file_handle)
                result[key] = dic
                #print result
                continue    
            line = config_file_handle.readline()
    return result                    
def main():
    config_file_name = input("Enter Name of Configuration File:")
    config_file_handle = Open(config_file_name)
    configurations = ParseSections(config_file_handle)
    for key in configurations:
        print key,"=", configurations[key]
    config_file_handle.close()
if __name__ == "__main__":
    main()
