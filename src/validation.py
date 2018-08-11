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

def     append_in_dic_conditions(buffer, d):
    list_a = list()
    [list_a.append(x) for x in buffer if (x != buffer[len(buffer) - 1]) and (x != buffer[len(buffer) - 2])]
    d['conditions'] = list_a
    return (d)

def      init_true_or_false_var(buffer, d):
    tmp_list = list()
    for x in buffer:
        for n in x:
            if (n.isalpha()) == True:
                tmp_list.append(n)
    tmp_list = list(set(tmp_list))
    d_tmp = {}
    for x in tmp_list:
        d_tmp[x] = False
    x_none = buffer[len(buffer) - 1][0].replace("?", "")
    for x in x_none:
        d_tmp[x] = None
    x_true = buffer[len(buffer) - 2][0].replace("=", "")
    for x in x_true:
        d_tmp[x] = True
    d['vars'] = d_tmp
    return (d)

def     validation(read_buffer):
    read_buffer = read_buffer.replace("!", " ! ")
    read_buffer = read_buffer.replace("(", " ( ")
    read_buffer = read_buffer.replace(")", " ) ")

    buffer = read_buffer.split('\n')
    buffer = delete_comment(buffer)
    buffer = delete_space(buffer)
    buffer = delete_empty_elem(buffer)

    minimal_len(buffer)
    check_forbiden_char(buffer)
    count_unknow(buffer)
    d = {"conditions" : [], "vars" : []}
    d = append_in_dic_conditions(buffer, d)
    d = init_true_or_false_var(buffer, d)
    print (d['vars'])
    sys.exit(1)
    return d