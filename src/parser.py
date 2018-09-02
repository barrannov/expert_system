class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


prec = dict()

prec["^"] = 3
prec["!"] = 3
prec["+"] = 3
prec["|"] = 3
prec["<=>"] = 2
prec["=>"] = 2
prec["("] = 1
prec[")"] = 1


def _solve_logic(a, b, operator, all_vars):

    if a == 'True' or a == 'False':
        a = eval(a)
    elif b == 'True' or b == 'False':
        b = eval(b)
    else:
        a = not all_vars[a[1]] if '!' in a else all_vars[a]
        b = not all_vars[b[1]] if '!' in b else all_vars[b]

    # if a is None or b is None:
    #     return None

    if operator == '^':
        res = a != b
    elif operator == '+':
        res = a and b
    elif operator == '|':
        res = a or b
    elif operator == '=>':
        res = not a or b
    elif operator == '<=>':
        res = a == b
    return str(res)


def _infix_to_postfix(token_list):
    op_stack = Stack()
    postfix_list = []

    for token in token_list:
        if token not in prec.keys():
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and \
                    (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())

    return postfix_list


def _solve_postfix(postfix_list, all_vars):
    operand_stack = Stack()

    for token in postfix_list:
        if token not in prec.keys():
            operand_stack.push(token)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            if operand1 is None:
                return operand1

            if operand2 is None:
                return operand2

            result = _solve_logic(operand1, operand2, token, all_vars)
            # if result is None:
            #     return None

            operand_stack.push(result)
    final_value = operand_stack.pop()
    if final_value != 'False' and final_value != 'True':
        return all_vars[final_value]
    else:
        return final_value


def _prepare_condition(condition):
    for i, token in enumerate(condition):
        if token in list(prec):
            continue
        condition[i] = (
            '!' if token['neg'] else ''
        ) + token['var']
    return condition


def solve_condition(condition, all_vars):
    solve_condition = _prepare_condition(condition)
    return _solve_postfix(_infix_to_postfix(solve_condition), all_vars)
