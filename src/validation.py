import sys
import re


def delete_comment(buffer):
    i = 0
    for x in buffer:
        res = x.find("#")
        if (res != -1):
            buffer[i] = x[:res]
        i += 1
    return (buffer)


def delete_empty_elem(buffer):
    buffer = [x for x in buffer if x]
    return (buffer)


def delete_space(buffer):
    i = 0
    for x in buffer:
        buffer[i] = x.split(" ")
        i += 1
    i = 0
    for x in buffer:
        buffer[i] = delete_empty_elem(x)
        i += 1
    return (buffer)


def check_forbiden_char(buffer):
    for x in buffer:
        for n in x:
            match = re.search(r'[^A-Z()!+|^><=?\']', n)
            if (match):
                print("Unknow symbol")
                sys.exit(-1)


def minimal_len(buffer):
    min_len = 3

    if len(buffer) < 3:
        print("Too small file")
        sys.exit(-1)


def count_unknow(buffer):
    count = 0
    for x in buffer:
        for n in x:
            res = n.find("?")
            if (res != -1):
                count += 1
    if (count != 1):
        print("Please one line with ?\nExample:\n?ABC")
        sys.exit(-1)
    if (count == 1):
        res = buffer[len(buffer) - 1][0]
        if (res.find("?")) != 0:
            print("wrong position for unknow var")
            sys.exit(-1)
        if (len(res) == 1):
            print("all variables known")
            sys.exit(-1)
    res = buffer[len(buffer) - 2]
    if (len(res) != 1):
        print ("wrong position for known var")
        sys.exit(-1)


def append_in_dic_conditions(buffer, d):
    list_a = list()
    [list_a.append(x) for x in buffer if
     (x != buffer[len(buffer) - 1]) and (x != buffer[len(buffer) - 2])]
    d['conditions'] = list_a
    return (d)

def     validation_only_one_implies(d):
    for x in d['conditions']:
        count = 0
        for n in x:
            if n == "=>":
                count += 1
            if (count == 2):
                print("Need only one implies in 1 line")
                sys.exit(-1)

def     validation_only_one_if_and_only_if(d):
    for x in d['conditions']:
        count = 0
        for n in x:
            if n == "<=>":
                count += 1
            if (count == 2):
                print("Need only one if and only if in 1 line")
                sys.exit(-1)

def     validation_brackets(d):
    for x in d['conditions']:
        count = 0
        for n in x:
            if (n == "("):
                count += 1
            if (n == ")"):
                count -= 1
            if (n == "<=>" or n == "=>"):
                if (count != 0):
                    print("Error in brackets")
                    sys.exit(-1)
                count = 0
        if (count != 0):
            print("Error in brackets")
            sys.exit(-1)



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

def     error(y, x, n):
    print("line " + str(y), "error in", x, "number ", n)
    sys.exit(-1)

def     validation_operator(d):
    y = 0
    for x in d['conditions']:
        old = '0'
        now = '0'
        # oldt = '0'
        j = 0
        e = 0
        for n in x:
            if (re.search(r'[A-Z\']', n)):
                now = 'v'
            elif (re.search(r'[!+|^\']', n)):
                now = 'o'
            elif (re.search(r'[<=>]', n)):
                now = "e"
                e += 1
            else:
                now = n

            if ((len(n) == 2 and n != ("=>")) or (len(n) == 3 and n != "<=>")):
                error(y, x, 1)
            elif ((now == "v" and old == "v") or (now == "o" and old == "o" and n != "!")):
                error(y, x, 2)
            elif now == "o" and ((old == "(" or old == "0") and n != "!"):
                error(y, x, 3)
            elif (now == 'v' and old == ")"):
                error(y, x, 4)
            elif now == ")" and old == "(":
                error(y, x, 5)
            elif (now == ")" and (old == "o" or old == '0')):
                error(y, x, 6)
            elif (now == "e" and (old == "o" or old == "0")):
                error(y, x, 7)
            elif (n == "!" and ((old == "v" or old == ")") and old != "0")): # !A => A
                error(y, x, 8)
            # elif (now == "(" and oldt == "!"):
            #     error(y, x, 9)
            old = now
            # oldt = n
            j += 1
            if (j == len(x)) and (now != "v" and now != ")"):
                print ("line " + str(y), 'error end in', x)
                sys.exit(-1)
        if (e != 1):
            print ("line " + str(y), "error implies or if and only if operator")
            sys.exit(-1)
        y += 1
    # double_char(d)
    print ("valid")
    # print (d)
    # sys.exit(-1)

# def     double_char(d):
#     for x in d['conditions']:
#         s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         for n in x:
#             if (n.isalpha()):
#                 res = s.find(n)
#                 if (res == -1):
#                     print ("double_char char")
#                     sys.exit(-1)
#                 else:
#                     s = s.replace(n, n.lower())

def     validation(read_buffer):
    try:
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
        validation_only_one_implies(d)
        validation_only_one_if_and_only_if(d)
        validation_brackets(d)
        validation_operator(d)

        # print (d)
        # for x in d['conditions']:
        #     print (x)
        # sys.exit(-1)
        return d
    except:
        print ("Error")
        sys.exit(-1)