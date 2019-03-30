import re

def delete_comments(buffer):
    i = 0
    for x in buffer:
        res = x.find("#")
        if (res != -1):
            buffer[i] = x[:res]
        i += 1
    return (buffer)

def delete_spacing(buffer):
    i = 0
    for x in buffer:
        buffer[i] = x.split(" ")
        i += 1
    i = 0

    for x in buffer:
        buffer[i] = [f for f in x if f]
        i += 1

    buffer = [f for f in buffer if f]
    return (buffer)

def check_invalid_char(buffer):
    for x in buffer:
        for n in x:
            match = re.search(r'[^A-Z()!+|^><=?\']', n)
            if (match):
                raise Exception('Invalid char: '+n)

def validate_syntax_unknow_variables(buffer):
    count = 0
    for x in buffer:
        for n in x:
            if (n.find("?") != -1):
                count += len([q for q in n if q=="?"])

    if (count < 1):
        raise Exception('Invalid file syntax: no line with ?')
    elif (count > 1):
        raise Exception('Invalid file syntax: too many ?')

    res = buffer[len(buffer) - 1][0]
    if (res.find("?")) != 0:
        raise Exception('Invalid file syntax: wrong position for ?')

    if (len(res) == 1):
        raise Exception('Invalid file syntax: no unknown variables')

    res = buffer[len(buffer) - 2]
    if (len(res) != 1):
        raise Exception('Invalid file syntax: wrong position for known vars')



def validate_syntax_facts(buffer):
    count = 0
    for x in buffer:
        for n in x:
            if (n.find("=") == 0 and n.find("=>") == -1 and n.find("<=") == -1):
                count += len([q for q in n if q=="="])
    if (count < 1):
        raise Exception('Invalid file syntax: no line with =')
    elif (count > 1):
        raise Exception('Invalid file syntax: too many =')

    res = buffer[len(buffer) - 2][0]
    if (res.find("=")) != 0:
        raise Exception('Invalid file syntax: wrong position for =')



def make_dictionary_conditions(buffer):
    list_vars = {"conditions" : [], "vars" : []}

    list_a = list()
    [list_a.append(x) for x in buffer if
     (x != buffer[len(buffer) - 1]) and (x != buffer[len(buffer) - 2])]
    list_vars['conditions'] = list_a

    return (list_vars)



def init_bool_vars(buffer, vals):
    tmp_list = list()

    for x in buffer:
        for n in x:
            if (n.isalpha()) == True:
                tmp_list.append(n)

    tmp_list = list(set(tmp_list))
    d_tmp = {}

    for x in tmp_list:
        d_tmp[x] = 'False'
    x_none = buffer[len(buffer) - 1][0].replace("?", "")

    for x in x_none:
        d_tmp[x] = None
    x_true = buffer[len(buffer) - 2][0].replace("=", "")

    for x in x_true:
        d_tmp[x] = 'True'
    vals['vars'] = d_tmp
    vals['unknown_vars'] = [x for x in x_none]

    return vals



def validation_implies(d):
    for x in d['conditions']:
        count = 0
        for n in x:
            if n == "=>":
                count += 1
            if (count > 1):
                raise Exception('Invalid file syntax: allowed only one implies per 1 line')


def validation_if_per_line(d):
    for x in d['conditions']:
        count = 0
        for n in x:
            if n == "<=>":
                count += 1
            if (count > 1):
                raise Exception('Invalid file syntax: allowed only one "if" per 1 line')


def validation_brackets(d):
    for x in d['conditions']:
        count = 0
        for n in x:
            if (n == "("):
                count += 1
            if (n == ")"):
                count -= 1
            if (n == "<=>" or n == "=>"):
                if (count != 0):
                    raise Exception('Invalid file syntax: Error in brackets')
                count = 0
            if (count < 0):
                    raise Exception('Invalid file syntax: No opening bracket')    
        if (count != 0):
            raise Exception('Invalid file syntax: Error in brackets')



def error(y, x, n):
    raise Exception("Invalid file syntax: line " + str(y), "error in", x, "number ", n)

def check_valid_char(x):
    print(x)

def validation_operators(d):
    y = 0
    for x in d['conditions']:
        old = '0'
        now = '0'
        old_n = ''
        j = 0
        for n in x:
            # check_valid_char(x)
            if (re.search(r'[A-Z\']', n)):
                now = 'v'
            elif (re.search(r'[!+|^\']', n)):
                now = 'o'
            elif (re.search(r'<=>', n) or re.search(r'=>', n)):
                now = "e"
            elif (re.search(r'[\(\)]', n)):
                now = "b"
            else:
                raise Exception("Invalid file syntax: invalid operator ", n,  ", error end in ", x)

            if ((len(n) == 2 or len(n) == 3) and now != "e"):
                error(y, x, 1)
            elif ((now == "v" and old == "v") or (now == "o" and old == "o" and n != "!")): # C C => E  |OR|  C <=> <=> E
                error(y, x, 2)
            elif now == "o" and ((old_n == "(" or old == "0" or old_n == "=>" or old == "e") and n != "!"):
                error(y, x, 3)
            elif (now == 'v' and old_n == ")"):
                error(y, x, 4)
            elif n == ")" and old_n == "(":
                error(y, x, 5)
            elif (now == ")" and (old == "o" or old == '0')):
                error(y, x, 6)
            elif (now == "e" and (old == "o" or old == "0")):
                error(y, x, 7)
            elif (n == "!" and (((old == "v" or old_n == ")") and old != "0") or old_n == "!")): # !A => A  |OR|  !!A => B
                error(y, x, 8)
            old = now
            old_n = n
            j += 1
            if (j == len(x)) and (now != "v" and n != ")"):
                raise Exception("Invalid file syntax: line " + str(y), "error end in ", x)
        y += 1

def set_spacing(buf):
    buffer = buf.replace("(", " ( ").replace(")", " ) ")
    buffer = buffer.replace("!", " ! ")
    buffer = buffer.replace("+", " + ").replace("|", " | ").replace("^", " ^ ")
    buffer = buffer.replace("<=>", " <=> ")
    buffer = re.sub(r"(.*[^<])=>(.+)", r"\1 => \2", buffer)

    return buffer



def validation (buffer) :
    if len(buffer) < 5 :
        raise Exception('Empty file')

    buffer = set_spacing(buffer) 

    buf = buffer.split('\n')
    buf = delete_comments(buf)
    buf = delete_spacing(buf)

    check_invalid_char(buf)

    if len(buf) < 3 :
        raise Exception('Not enough data')

    validate_syntax_unknow_variables(buf)
    validate_syntax_facts(buf)

    vals = make_dictionary_conditions(buf)
    vals = init_bool_vars(buf, vals)
    validation_implies(vals)
    validation_if_per_line(vals)
    #print(vals)
    validation_brackets(vals)
    validation_operators(vals)

    return vals
