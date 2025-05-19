# Given an algebraic expression as a string s containing operands (letters), + and - operators, and parentheses,
#  simplify the expression by removing all parentheses and correctly applying the operators. Return the simplified expression
#   without parentheses.


def remove_parenthesis(string):
    result = ''
    sign_stack = [1]
    for i in range(len(string)):
        if string[i] == '(':
            if i > 0 and string[i-1] == '-':
                sign_stack.append(-sign_stack[-1])
            else:
                sign_stack.append(sign_stack[-1])
        elif string[i] == ')':
            sign_stack.pop()
        elif string[i] == '+':
            if sign_stack[-1] == 1:
                result += '+'
            else:
                result += '-'
        elif string[i] == '-':
            if sign_stack[-1] == 1:
                result += '-'
            else:
                result += '+'
        else:
            result += string[i]
    return result
                

