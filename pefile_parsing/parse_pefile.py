import pefile

def ParsePEFile(file_name):
    pe = pefile.PE(file_name)
    for section in pe.sections:
        print section.Name, hex(section.VirtualAddress)

#    print pe.dump_info()
    ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    print ep
    data = pe.get_memory_mapped_image()[ep:ep+200]
    print data
if __name__ == '__main__':
    file_name = raw_input("Enter Exe File Name:")
    ParsePEFile(file_name)
