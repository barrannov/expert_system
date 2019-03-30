import sys

def read_file(name_file):
    try:
        f = open(name_file, 'r')
        res = f.read()
        f.close()
        return res
    except Exception as e:
        print (f"Read file error: {e}")
        sys.exit(1)