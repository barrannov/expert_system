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


def _solve_logic(a, b, operator, data):
    all_vars = data['vars']
    a = not all_vars[a[1]] if '!' in a else a
    b = not all_vars[b[1]] if '!' in b else b

    # if a is None or b is None:
    #     return None

    if operator == '^':
        return a != b
    elif operator == '+':
        return a and b
    elif operator == '|':
        return a or b
    elif operator == '=>':
        return not a or b
    elif operator == '<=>':
        return a == b


def _infixToPostfix(token_list):
    opStack = Stack()
    postfixList = []

    for token in token_list:
        if token.isalnum():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    # print(postfixList)
    return postfixList


def _solvePostfix(postfix_list):
    operand_stack = Stack()

    for token in postfix_list:
        if token.isalnum():
            operand_stack.push(token)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            # TODO solve conclusion here
            to_eval = operand1 + token + operand2
            result = str(eval(to_eval))

            operand_stack.push(result)
    return operand_stack.pop()


# def solve_condition():
#     try:
#         return solvePostfix(infixToPostfix(['-3']))
#     except(ZeroDivisionError):
#         print('You cannot divide by zero')
#
# solve_condition()


# print(infixToPostfix(['A', '|', 'B', '=>', 'C']))

def solve_condition(conditon, data):
    pass