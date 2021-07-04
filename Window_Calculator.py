from tkinter import Tk, Label, Button, Entry, StringVar
from functools import partial

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self) == 0

def compute_postfix(token_list):
    solution = Stack()
    for i in range(len(token_list)):
        if token_list[i] not in '+-*/^':
            token_list[i] = float(token_list[i])
    for token in token_list:
        a = solution.pop()
        b = solution.pop()
        if type(token) is float:
            solution.push(token)
        elif token == '+':
            a = solution.pop()
            b = solution.pop()
            solution.push(b + a)
        elif token == '-':
            a = solution.pop()
            b = solution.pop()
            solution.push(b - a)
        elif token == '*':
            a = solution.pop()
            b = solution.pop()
            solution.push(b * a)
        elif token == '/':
            a = solution.pop()
            b = solution.pop()
            solution.push(b / a)
        elif token == '^':
            a = solution.pop()
            b = solution.pop()
            solution.push(b ** a)

    return solution.pop()

def infix_to_postfix(token_list):
    opstack = Stack()
    operator = '+-/*^'
    outstack = []
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == "(":
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
        elif token in operator:
            if opstack.isEmpty() == True:
                opstack.push(token)
            elif prec[token] > prec[opstack.top()]:
                opstack.push(token)
            else:
                while prec[opstack.top()] >= prec[token]:
                    outstack.append(opstack.pop())
                    if opstack.isEmpty() == True: break
                opstack.push(token)
        else:
            outstack.append(token)
    while opstack.isEmpty() == False:
        outstack.append(opstack.pop())
    return outstack


def do_something():
    value = compute_postfix(infix_to_postfix(expr.get()))
    total.set("{0:.4f}".format(value))
    return

root = Tk()
root.title("My Calculator")
expr = StringVar()
title_label = Label(root, text="My Calcualtor").grid(row=0, columnspan=2)
input_exam = Label(root, text="Space between terms: ( 3 + 2 ) * 8").grid(row=1, columnspan=2)
exp_entry = Entry(root, textvariable=expr).grid(row=2, column=0)
total_label = Label(root, text="TOTAL").grid(row=3, column=0)
total = StringVar()
total.set('0')
value_label = Label(root, textvariable=total, width=20).grid(row=3, column=1)
equal_btn = Button(root, text=' = ', width=20, command=do_something).grid(row=2, column=1)
root.mainloop()
root.destroy()