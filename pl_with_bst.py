class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None
		self.height = 0  # 높이 정보도 유지함에 유의!!

	def __str__(self):
		return str(self.key)
	
	def is_left(self):
		if (self.left == None):
			return False
		else:
			return True
		
	def is_right(self):
		if (self.right == None):
			return False
		else:
			return True
		
	def get_height(self):
		if (self.left == None and self.right == None):
			self.height = 0
		elif (not self.is_left()):
			self.height = self.right.height + 1
		elif (not self.is_right()):
			self.height = self.left.height + 1
		else:
			if (self.left.height > self.right.height):
				self.height = self.left.height + 1
			else:
				self.height = self.right.height + 1
				
class BST:
	def __init__(self):
		self.root = None
		self.size = 0
	def __len__(self):
		return self.size

	def preorder(self, v):
		if v != None:
			print(v.key, end=' ')
			self.preorder(v.left)
			self.preorder(v.right)

	def inorder(self, v):
		if(v != None):
			self.inorder(v.left)
			print(v.key, end = ' ')
			self.inorder(v.right)

	def postorder(self, v):
		if(v != None):
			self.postorder(v.left)
			self.postorder(v.right)
			print(v.key, end = ' ')

	def find_loc(self, key):
		if(self.size == 0):
			return None
		p = None
		v = self.root
		while v:
			if(v.key == key): return v
			elif(v.key < key):
				p = v
				v = v.right
			else:
				p = v
				v = v.left
		return p

	def search(self, key):
		p = self.find_loc(key)
		if(p and p.key == key):
			return p
		else:
			return None

	def insert(self, key):
		# 노드들의 height 정보 update 필요
		p = self.find_loc(key)
		if(p != None and p.key == key):
			return
		if(p == None or p.key != key):
			v = Node(key)
			if(p == None):
				self.root = v
			else:
				v.parent = p
				if(p.key >= key):
					p.left = v
				else:
					p.right = v
				while p:
					p.get_height()
					p = p.parent
			self.size += 1
			return v
		else:
			return None

	def deleteByMerging(self, x):
		# 노드들의 height 정보 update 필요
		if (x == None): return
		a, b, pt = x.left, x.right, x.parent
		if(a == None):
			c = b
		else:
			c = m = a
			
			while m.right:
				m = m.right
			m.right = b
			if b: 
				b.parent = m
				while m:
					m.get_height()
					m = m.parent
				
		if (self.root == x):
			if c: c.parent = None
			self.root = c
		else:
			if (pt.left == x):
				pt.left = c
				pt.get_height()
			else:
				pt.right = c
				pt.get_height()
			if c: c.parent = pt
		self.size -= 1
		
		
	def deleteByCopying(self, x):
		# 노드들의 height 정보 update 필요
		if (x == None): return
		a, b, pt = x.left, x.right, x.parent
		if a:
			y = a
			while y.right:
				y = y.right
			x.key = y.key
			y_p = y.parent
			
			if y.left:
				y.left.parent = y.parent
				y.left.parent.get_height()
			if y.parent.left is y:
				y.parent.left = y.left
				y.parent.get_height()
			else:
				y.parent.right = y.left
				y.parent.get_height()	
			del y
			while y_p:
				y_p.get_height()
				y_p = y_p.parent

		elif not a and b:
			y = b
			while y.left:
				y = y.left
			x.key = y.key
			y_p = y.parent
			if y.right:
				y.right.parent = y.parent
				y.parent.get_height()
			if y.parent.left is y:
				y.parent.left = y.right
				y.parent.get_height()
			else:
				y.parent.right = y.right
				y.parent.get_height()
			del y
			while y_p:
				y_p.get_height()
				y_p = y_p.parent
	
		else:
			if(pt == None):
				self.root = None
			else:
				if(pt.left is x):
					pt.left = None
				else:
					pt.right = None
			del x
			while pt:
				pt.get_height()
				pt = pt.parent

	def height(self, x): # 노드 x의 height 값을 리턴
		if x == None: return -1
		else: return x.height

	def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
		# x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
		if(x == None): return None
		if(x.right != None):
			temp = x.right
			while(temp.left):
				temp = temp.left
			return temp
		pt = x.parent
		while (pt != None and x == pt.right):
			x = pt
			pt = pt.parent
		return pt
		
	def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
		# x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
		if(x == None): return None
		if(x.left != None):
			temp = x.left
			while(temp.right):
				temp = temp.right
			return temp
		pt = x.parent
		while (pt != None and x == pt.left):
			x = pt
			pt = pt.parent
		return pt
	
	def rotateLeft(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		if not z: return
		x = z.right
		if(x == None): return
		b = x.left
		x.parent = z.parent
		if z.parent:
			if(z.parent.left == z):
				z.parent.left = x
			else:
				z.parent.right = x
		if x: 
			x.left = z
		z.parent = x
		z.right = b
		z.get_height()
		x.get_height()
		if b: 
			b.parent = z
			z.right = b
			z.get_height()
			x.get_height()
		if(z == self.root and z != None):
			self.root = x
			self.root.get_height()

	def rotateRight(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		if not z: return
		x = z.left
		if (x == None): return
		b = x.right
		x.parent = z.parent
		if z.parent:
			if (z.parent.left == z):
				z.parent.left = x
			else:
				z.parent.right = x
		if x: 
			x.right = z
		z.parent = x
		z.left = b
		z.get_height()
		x.get_height()
		if b: 
			b.parent = z
			z.left = b
			z.get_height()
			x.get_height()	
		if(z == self.root and z!= None):
			self.root = x
			self.root.get_height()