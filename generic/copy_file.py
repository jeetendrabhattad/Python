import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sourcefile", help="Source File Path")
    parser.add_argument("--destinationfile", help="Destination File Path")

    args = parser.parse_args()
    print args.sourcefile, args.destinationfile
