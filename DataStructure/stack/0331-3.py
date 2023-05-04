from LinkedStack import *

def checkString(s):
    stack = LinkedStack()
    i = 0
    
    while s[i] != '$':
        stack.push(s[i])
        i += 1
    i += 1
    while i < len(s):
        if stack.pop() != s[i]:
            return False
        else:
            i += 1
    return True

print(checkString("abc$cba"))