class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None
		self.height = 0  # 높이 정보도 유지함에 유의!!

	def __str__(self):
		return str(self.key)


class BST:
	def __init__(self):
		self.root = None
		self.size = 0
	def __len__(self):
		return self.size
	
	def update_height(self, v): #높이 정보 업데이트
		while v != None: #root node 까지
			l , r = -1, -1
			if v.left != None:
				l = v.left.height
			if v.right != None:
				r = v.right.height
			v.height = max(l, r) + 1
			v = v.parent

	def preorder(self, v):
		if v != None:
			print(v.key, end=' ')
			self.preorder(v.left)
			self.preorder(v.right)

	def inorder(self, v):
		if v != None:
			self.inorder(v.left)
			print(v.key, end=' ')
			self.inorder(v.right)	

	def postorder(self, v):
		if v != None:
			self.postorder(v.left)
			self.postorder(v.right)
			print(v.key, end=' ')

	def find_loc(self, key):
		if self.size == 0: return None
		p = None
		v = self.root
		while v != None:
			if v.key == key: return v
			elif v.key < key:
				p = v
				v = v.right
			else:
				p = v
				v = v.left
		return p

	def search(self, key):
		p = self.find_loc(key)
		if p and p.key == key:
			return p
		else:
			return None

	def insert(self, key):
		# 노드들의 height 정보 update 필요
		p = self.find_loc(key)
		#p.height = 0
		if p == None or p.key != key:
			v = Node(key)
			if p == None:
				self.root = v
			else:
				v.parent = p
				if p.key >= key:
					p.left = v
				else:
					p.right = v
			self.update_height(v) #높이 업데이트
			self.size = self.size + 1
			return v
		else:
			print("key is already in the tree!")
			return p

	def deleteByMerging(self, x):
		# 노드들의 height 정보 update 필요
		if x == None: return None
		a, b, pt = x.left, x.right, x.parent
		if a == None:
			c = b
			s = pt
		else:
			c = m = a
			while m.right: m = m.right
			m.right = b
			if b:
				b.parent = m
			s = m
		if self.root == x:
			if c: c.parent = None
			self.root = c
		else:
			if pt.left == x: pt.left = c
			else: pt.right = c
			if c: c.parent = pt
		self.size = self.size - 1
		self.update_height(s)
		return s

	def deleteByCopying(self, x):
		# 노드들의 height 정보 update 필요
		if x == None :
			return None
		a = x.left
		if a == None:
			b, pt = x.right, x.parent
			if pt == None:
				self.root = b
			else:
				if pt.left == x:
					pt.left = b
				else:
					pt.right = b
			if b != None:
				b.parent = pt
			del x
		else:
			m = a
			while m.right:
				m = m.right
			x.key = m.key
			l, pt = m.left, m.parent
			if pt.left == m:
				pt.left = l
			else:
				pt.right = l
			if l != None:
				l.parent = pt
			del m
		self.size = self.size - 1
		self.update_height(pt)
		return pt


	def height(self, x): # 노드 x의 height 값을 리턴
		if x == None: return -1
		else: return x.height

	def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
		# x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
		if x == None: return None
		succ = None
		s = self.root
		if x.right != None: #case 1: x가 오른쪽 subtree가 존재한다면 오른쪽 subtree에서 가장 작은 노드를 찾는다
			succ = x.right
			while succ.left != None:
				succ = succ.left
		elif x.right == None:  #case 2: x의 오른쪽 subtree가 존재하지 않는다면 root 노드에서부터 찾는다
			while s.key != x.key:
				if x.key <= s.key:
					succ = s
					s = s.left
				else:
					s = s.right
		else: return None
		return succ
		

	def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
		# x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
		if x == None: return None
		pred = None
		s = self.root
		if x.left != None: #case 1: x의 왼쪽 subtree가 존재한다면 왼쪽 subtree에서 가장 큰 노드를 찾는다
			pred = x.left
			while pred.right != None:
				pred = pred.right
		elif x.left == None: #case 2: x의 왼쪽 subtree가 존재하지 않는다면 root 노드에서부터 찾는다
			while x.key != s.key:
				if x.key > s.key:
					pred = s
					s = s.right
				else:
					s = s.left
		else:
			return None
		return pred

	def rotateLeft(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		y = x.right
		if y == None: return
		b = y.left
		y.parent = x.parent
		if x.parent:
			if x.parent:
				if x.parent.left == x:
					x.parent.left = y
				if x.parent.right == x:
					x.parent.right = y	
		if y != None:
			y.left = x
		x.parent = y
		x.right = b
		if b != None:
			b.parent = y
		if self.root == x and y != None:
			self.root = y
		self.update_height(x)
	

	def rotateRight(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		y = x.left
		if y == None: return
		b = y.right
		y.parent = x.parent
		if x.parent != None:
			if x.parent.left == x:
				x.parent.left = y
			if x.parent.right == x:
				x.parent.right = y
		if y != None:
			y.right = x
		x.parent = y
		x.left = b
		if b != None:
			b.parent = x
		if self.root == x and y != None:
			self.root = y
		self.update_height(x)

	# 정의 필요

class AVL(BST):
	def __init__(self):
		self.root = None
		self.size = 0

	def rebalance(self, x, y, z):
		# assure that x, y, z != None
		# return the new 'top' node after rotations
		# z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음
		if z.left == y: #z의 왼쪽 노드가 y고
			if y.left != x: #y의 왼쪽 노드가 x가 아니면, 즉 
				self.rotateLeft(y)
			self.rotateRight(z)
		else:
			if y.left == x:
				self.rotateRight(y)
			self.rotateLeft(z)
		return z.parent

		
	def BalanceFactor(self, x): #rebalance를 위한 Balance Factor
		#BF = 왼쪽 서브트리 높이 - 오른쪽 서브트리 높이 (empty == -1)
		if x == None:
			return None
		if x.right == None:
			if x.left == None:
				return 0 #x가 왼쪽, 오른쪽 노드가 없다면 0 리턴
			else:
				return (self.height(x.left) + 1) * -1 #아니면 x의 왼쪽 노드의 높이에서 1을 더한후 음수를 취한다
		else:
			if x.left == None:
				return self.height(x.right) + 1 #오른쪽 노드만 존재할 경우 오른쪽 노드의 높이에서 1을 더한다
			else:
				return self.height(x.right) - self.height(x.left) #오른쪽, 왼쪽 노드 둘 다 존재할 경우 오른쪽 노드의 높이에서 왼쪽 노드의 높이를 뺀다

	def insert(self, key):
		# BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면 
		# super(class_name, instance_name).method()으로 호출
		# 새로운 삽입된 노드가 리턴됨
		v = super(AVL, self).insert(key)
		#if v == None: 
		# x, y, z를 찾아 rebalance(x, y, z)를 호출
		# x, y ,z 찾기
		a = v
		while a.parent != None: #헤드 노드까지
			if self.BalanceFactor(a.parent) < -1 or self.BalanceFactor(a.parent) > 1: #v의 Balance Factor가 -2 또는 2인 parent 노드가 발생한다면, 즉 balanced 하지 않았다면
				z = a.parent #z는 a의 parent 노드
				if self.BalanceFactor(z) <= 0: #z의 Balance Factor가  0 이하면, 즉 z의 왼쪽 노드의 높이가 오른쪽 노드의 높이 보다 크거나 같으면
					y = z.left #y는 z의 왼쪽 노드가 된다
				else: # 1 이상이면, 즉 z의 왼쪽 노드의 높이가 오른쪽 노드의 높이 보다 작으면
					y = z.right #y는 z의 오른쪽 노드가 된다
				y.parent = z #z는 y의 parent 노드
				if self.BalanceFactor(y) <= 0: #y의 Balance Factor 가 0 이하면, 즉 y의 왼쪽 노드의 높이가 오른쪽 노드의 높이 보다 크거나 같으면 
					x = y.left #x는 y의 왼쪽 노드가 된고
				else: # 1 이상이면, 즉 y의 왼쪽 노드의 높이가 오른쪽 노드의 높이 보다 작으면
					x = y.right #x는 y의 오른쪽 노드가 된다
				x.parent = y #y는 x의 parent 노드
				if x != None and y != None and z != None: #x, y, z를 찾고, 이들이 모두 None이 아니면
					w= self.rebalance(x,y,z) #rebalance
					if w.parent == None:
						self.root = w
				break
			a = a.parent
		return v

	def delete(self, u): # delete the node u
		v = self.deleteByCopying(u) # 또는 self.deleteByMerging을 호출. 이 과제에서는 채점을 위해 deleteByCopying을 호출한다
		#삭제 함수를 호출후, insert와 같이 rebalance 통한 rotation 실행
		if v == None:
			return
		a = None
		# height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장
		while v != None:
				# v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
				# z - y - x를 정한 후, rebalance(x, y, z)을 호출
			if self.BalanceFactor(v) < -1 or self.BalanceFactor(v) > 1:  #v가 balance가 되어 있지 않다면 rebalance 시켜준다
				z = v
				if self.BalanceFactor(z) <= 0: #z의 왼쪽 노드의 높이가 오른쪽 노드의 높이 보다 크거나 같으면
					y = z.left
				else: #z의 왼쪽 노드의 높이가 오른쪽 노드의 높이 보다 작으면
					y = z.right
				y.parent = z
				if self.BalanceFactor(y) <= 0: #y의 왼쪽 노드의 높이가 오른쪽 노드의 높이 보다 크거나 같으면 
					x = y.left
				else: #y의 왼쪽 노드의 높이가 오른쪽 노드의 높이 보다 작으면
					x = y.right
				x.parent = y
				if x != None and y!= None and z != None:
					v = self.rebalance(x, y, z)
			a = v
			v = v.parent
		if a != None:
			self.root = a


T = AVL()
while True:
	cmd = input().split()
	if cmd[0] == 'insert':
		v = T.insert(int(cmd[1]))
		print("+ {0} is inserted".format(v.key))
	elif cmd[0] == 'delete':
		v = T.search(int(cmd[1]))
		T.delete(v)
		print("- {0} is deleted".format(int(cmd[1])))
	elif cmd[0] == 'search':
		v = T.search(int(cmd[1]))
		if v == None:
			print("* {0} is not found!".format(cmd[1]))
		else:
			print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'height':
		h = T.height(T.search(int(cmd[1])))
		if h == -1:
			print("= {0} is not found!".format(cmd[1]))
		else:
			print("= {0} has height of {1}".format(cmd[1], h))
	elif cmd[0] == 'succ':
		v = T.succ(T.search(int(cmd[1])))
		if v == None:
			print("> {0} is not found or has no successor".format(cmd[1]))
		else:
			print("> {0}'s successor is {1}".format(cmd[1], v.key))
	elif cmd[0] == 'pred':
		v = T.pred(T.search(int(cmd[1])))
		if v == None:
			print("< {0} is not found or has no predecssor".format(cmd[1]))
		else:
			print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
	elif cmd[0] == 'preorder':
		T.preorder(T.root)
		print()
	elif cmd[0] == 'postorder':
		T.postorder(T.root)
		print()
	elif cmd[0] == 'inorder':
		T.inorder(T.root)
		print()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")