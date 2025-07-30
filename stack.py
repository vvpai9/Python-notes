from math import fmod

class Stack:
    def __init__(self):
        self.s = []
        self.top = -1
    def push (self, data = 0.0):
        self.top = self.top + 1
        self.s.append (data)
    def pop (self):
        data = self.s.pop(self.top)
        self.top = self.top - 1
        return data
    def StackEmpty (self):
        if self.top == -1:
            return 1
        return 0
    def StackTop (self):
        return self.s[self.top]
    def display(self):
        print (self.s)

def associativeLtoR(op):
    if op == '+' or op == '-' or op == '*' or op == '/' or op == '//':
        return 1
    elif op == '$' or op == '^' or op == '**':
        return 0

def precedence (op):
    if op == '+' or '-':
        return 1
    elif op == '*' or op == '/' or op == '//':
        return 2
    elif op == '$' or op == '^':
        return 3

def convert (infix, postfix):
    stk = Stack()
    for ip in infix:
        if ip.isalpha() or ip.isdigit():
            postfix.append(ip)
        elif ip == ')':
            while stk.StackTop() != '(':
                postfix.append (stk.pop())
            stk.pop ()
        else:
            while True:
                if stk.StackEmpty() or ip == '(' or stk.StackTop() == '(' or (associativeLtoR(ip) and precedence(ip) > precedence(stk.StackTop())) or (not (associativeLtoR(ip)) and precedence(ip) >= precedence(stk.StackTop())):
                    break
                postfix.append(stk.pop())
            stk.push(ip)
    while not stk.StackEmpty():
        postfix.append(stk.pop())

def evalPostfix(infix, postfix):
    convert (infix, postfix)
    stk = Stack()
    for ip in postfix:
        if ip.isalpha():
            print ("Enter the value of", ip, ":")
            res = float (input())
            stk.push(res)
        elif (ip.isdigit ()):
            stk.push (float(ip))
        else:
            op2 = stk.pop()
            op1 = stk.pop()
            if ip == '+':
                res = op1 + op2
            elif ip == '-':
                res = op1 - op2
            elif ip == '*':
                res = op1 * op2
            elif ip == '/':
                res = op1 / op2
            elif ip == '//':
                res = op1 // op2
            elif ip == '%':
                res = fmod (op1, op2)
            elif ip == '$' or '^':
                res = op1 ** op2
            stk.push (res)
    res = stk.pop()
    return res

if __name__ == '__main__':
    print ("(Use '$' or '^' for exponentiation.)")
    infix = input ("Enter infix expression: ")
    postfix = []
    res = evalPostfix(infix, postfix)
    print ("Result: ", res)
