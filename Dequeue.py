class deque:
    def __init__(self, s):
        self.items = []
        for i in range(len(s)):
            self.items.append(s[i])
    
    def append(self, val): #Right-append
        self.items.append(val)

    def appendleft(self, val): #Left-append
        self.items.append(0, val)

    def pop(self): #Right-pop
        return self.items.pop()

    def popleft(self): #Left-pop
        val = self.items[0]
        del self.items[0]
        return val

    def __len__(self):
        return len(self.items)
    
    def right(self):
        return self.items[-1]
    
    def left(self):
        return self.items[0]

def check_palindrome(s):
    dq = deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
    return palindrome

sentence = input()
print(check_palindrome(sentence))
        
