from ListStack import *

def paren_balance(string) -> bool:
    s = ListStack()
    for index in range(len(string)):
        if string[index] == '(':
            s.push('(')
        elif string[index] == ')':
            if s.isEmpty():
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False