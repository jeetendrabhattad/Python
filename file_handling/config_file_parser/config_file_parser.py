#!/usr/bin/python

import ConfigParser as CFP

def parseConfigFile(cfg_file_name):
    parser = CFP.ConfigParser()
    parser.read(cfg_file_name)
    print parser.sections()
    print parser.options("First")
    print parser.get("First", "ip")

def main():
    cfg_file_name = input("Enter Configuration File Name:")
    parsed_configurations = parseConfigFile(cfg_file_name)

if __name__ == "__main__":
    main()
