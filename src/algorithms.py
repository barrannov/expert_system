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


def _solve_logic(a, b, operator, data):
    all_vars = data['vars']

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


def _solve_postfix(postfix_list, data):
    operand_stack = Stack()

    for token in postfix_list:
        if token not in prec.keys():
            operand_stack.push(token)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            result = _solve_logic(operand1, operand2, token, data)
            if result is None:
                return None

            operand_stack.push(result)
    final_value = operand_stack.pop()
    if final_value != 'False' and final_value != 'True':
        return data['vars'][final_value]
    else:
        return final_value


# def solve_condition():
#     try:
#         return solvePostfix(infixToPostfix(['-3']))
#     except(ZeroDivisionError):
#         print('You cannot divide by zero')
#
# solve_condition()


# print(infixToPostfix(['A', '|', 'B', '=>', 'C']))

def solve_condition(conditon, data):
    return _solve_postfix(_infix_to_postfix(conditon), data)
