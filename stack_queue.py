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

S = Stack()
S.push(10)
S.push(2)
print(S.top())
print(S.pop())
print(len(S))
print(S.isEmpty())

# stack_queue.py 에 저장
class Queue:
	def __init__(self):
		self.items = []		# 데이터 저장을 위한 리스트 준비
		self.front_index = 0	# 다음 dequeue될 값의 인덱스 저장
		
	def enqueue(self, val):
		self.items.append(val)
		
	def dequeue(self):
		if len(self.items) == 0 or self.front_index == len(self.items):
			print("Queue is empty")
		else:
			x = self.items[self.front_index]
			self.front_index += 1
			return x

	def front(self):
		if len(self.items) == 0 or self.front_index == len(self.items):
			print("Queue is empty")
		else:
			return self.items[self.front_index]

	def __len__(self):	# len()로 호출하면 stack의 item 수 반환
 		return len(self.items)-self.front_index # why?
	
	def isEmpty(self):
		return len(self)
	
Q = Queue()
Q.enqueue(10)
Q.enqueue(4)
print(Q.dequeue())
print(Q.front())
print(Q.dequeue())
print(Q.front())