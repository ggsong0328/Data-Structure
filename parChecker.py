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

def parChecker(parSeq):
    S = Stack()
    for p in parSeq:
        if p == "(" :
            S.push(p)
        else:
            if S.isEmpty():
                return False
            else:
                S.pop()
    if S.isEmpty():
        return True
    else:
        return False

parSeq = input()
print(parChecker(parSeq))