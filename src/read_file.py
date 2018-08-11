import sys

def read_file(name_file):
    try:
        f = open(name_file, 'r')
        res = f.read()
        return res
    except:
        print ("Read file error.")
        sys.exit(1)