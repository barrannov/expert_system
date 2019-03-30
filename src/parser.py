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

prec["^"] = 2
prec["+"] = 4
prec["|"] = 3

prec["!"] = 1
prec["<=>"] = 1
prec["=>"] = 1
prec["("] = 1
prec[")"] = 1


def _solve_logic(a, b, operator):
    if not a or not b:
        return None

    res = 'False'

    if a == 'True' or a == 'False':
        a = eval(a)

    if b == 'True' or b == 'False':
        b = eval(b)

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

    neg = False
    for token in token_list:
        if token not in prec.keys():
            if neg:
                token = 'False' if token == 'True' else 'True'
            postfix_list.append(token)
            neg = False
        elif token == '!':
            neg = True
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


def _validate_condition_operands(a, b, operator):
    if not a or not b:
        if operator == '|':
            if a == 'True' or b == 'True':
                a = 'True'
                b = 'True'
    return a, b


def _validate_conclusion_operands(a, b, operator):
    if not a or not b:
        if operator == '+':
            if a == 'True' or b == 'True':
                a = 'True'
                b = 'True'
    return a, b


def _solve_postfix(postfix_list, condition=False, conclusion=False):
    operand_stack = Stack()

    for token in postfix_list:
        if token not in prec.keys():
            operand_stack.push(token)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            if condition is True:
                operand1, operand2 = _validate_condition_operands(operand1, operand2, token)
            elif conclusion is True:
                operand1, operand2 = _validate_conclusion_operands(operand1, operand2, token)

            result = _solve_logic(operand1, operand2, token)
            operand_stack.push(result)

    final_value = operand_stack.pop()
    return final_value


def solve_expression(expression, condition=False, conclusion=False):
    if condition is True and conclusion is True:
        print('True should be only one condition or conclusion.')

    exp_res = str(_solve_postfix(_infix_to_postfix(expression), condition, conclusion))
    return None if exp_res == 'None' else exp_res
