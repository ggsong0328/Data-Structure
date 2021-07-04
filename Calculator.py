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

def get_token_list(expr):
    operator = '+-*/^()' #연산자와 괄호처리를 위한 문자열
    endNum = 0 #숫자 입력이 끝나는걸 알려주는 함수
    data = '' #한 자리 이상의 실수를 처리하기 위한 변수
    token_list = []
    for i in range(len(expr)):
        if expr[i] == ' ':
            continue
        if expr[i] not in operator:
            data = data + expr[i]
            endNum = 1
        else:
            if endNum == 1:
                token_list.append(data)
                data = ''
            endNum = 0
            token_list.append(expr[i])
    if endNum == 1:
        token_list.append(data)

    return token_list


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

def compute_postfix(token_list):
    solution = Stack()
    print(type(token_list))
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

expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)