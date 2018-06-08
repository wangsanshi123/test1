from operator import add, sub, mul, truediv
import ast
from functools import reduce

def calc(expr):
    # TODO: Your awesome code here
    ls = expr.split(" ")
    dicts = {"+": add, '-': sub, '*': mul, '/': truediv}
    while not "".join(ls).replace('.', '', 1).isdigit() and len(ls) > 1:
        for i, item in enumerate(ls):
            if not item.replace('.', '', 1).isdigit():
                ls[i - 2] = str(reduce(dicts[item], [int(ls[i - 2]), int(ls[i - 1])]))
                ls.remove(ls[i])
                ls.remove(ls[i - 1])
                break
            pass
    if len(ls) > 1:
        temp = ls[-1]
        return ast.literal_eval(temp)
    return ast.literal_eval(ls[0]) if ls[0] else 0
    pass

def calc2(expr):
    OPERATORS = {"+": add, '-': sub, '*': mul, '/': truediv}

    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()


def solution(string, markers):
    # your code here



    pass




if __name__ == '__main__':
    expr = "5 1 2 + 4 * + 3 -"
    expr = ""
    expr = "1 2 3"
    # expr = "1 2 3.5"
    # print(calc(expr))
    print(calc2(expr))
