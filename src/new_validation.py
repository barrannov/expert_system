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

def validate_syntax(buffer):
    count = 0
    for x in buffer:
        for n in x:
            res = n.find("?")
            if (res != -1):
                count += 1

    if (count != 1):
        raise Exception('Invalid file syntax: no line with ?')

    if (count == 1):
        res = buffer[len(buffer) - 1][0]
        if (res.find("?")) != 0:
            raise Exception('Invalid file syntax: wrong position for ?')

        if (len(res) == 1):
            raise Exception('Invalid file syntax: no unknown variables')

    res = buffer[len(buffer) - 2]
    if (len(res) != 1):
        raise Exception('Invalid file syntax: wrong position for known vars')


def validation (buffer) :
    if len(buffer) < 5 :
        raise Exception('Empty file')

    separated_buf = buffer.split('\n')
    separated_buf = delete_comments(separated_buf)
    separated_buf = delete_spacing(separated_buf)
    separated_buf = check_invalid_char(separated_buf)

    if len(separated_buf) < 3 :
        raise Exception('Not enough data')

    validate_syntax(separated_buf)
