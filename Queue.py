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
            x = self.items[self.front_index]
            self.front_index += 1
            return x
