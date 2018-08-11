import sys
import re

def     delete_comment(buffer):
    i = 0
    for x in buffer:
        res = x.find("#")
        if (res != -1):
            buffer[i] = x[:res]
        i += 1
    return (buffer)

def     delete_empty_elem(buffer):
    buffer = [x for x in buffer if x]
    return (buffer)

def     delete_space(buffer):
    i = 0
    for x in buffer:
        buffer[i] = x.split(" ")
        i += 1
    i = 0
    for x in buffer:
        buffer[i] = delete_empty_elem(x)
        i += 1
    return (buffer)

def     check_forbiden_char(buffer):
    for x in buffer:
        for n in x:
            match = re.search(r'[^ABCDEFGHIJKLMNOPQRSTUVWXYZ()!+|^=><=>?\']', n)
            if (match):
                print("Unknow symbol")
                sys.exit(-1)

def     minimal_len(buffer):
    min_len = 3

    if len(buffer) < 3:
        print("Too small file")
        sys.exit(-1)

def     count_unknow(buffer):
    count = 0
    for x in buffer:
        for n in x:
            res = n.find("?")
            if (res != -1):
                count += 1
    if (count != 1):
        print ("too big Unknow line")
        sys.exit(-1)
    if (count == 1):
        res = buffer[len(buffer) - 1][0]
        if (res.find("?")) != 0:
            print ("wrong position for unknow var")
            sys.exit(-1)
        if (len(res) == 1):
            print ("all variables known")
            sys.exit(-1)

def     validation(read_buffer):
    buffer = read_buffer.split('\n')
    buffer = delete_comment(buffer)
    buffer = delete_space(buffer)
    buffer = delete_empty_elem(buffer)

    minimal_len(buffer)
    check_forbiden_char(buffer)
    count_unknow(buffer)

    # [print(x) for x in buffer]
    sys.exit(1)
    return {'a' : 'b'}