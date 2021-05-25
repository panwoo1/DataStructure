# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None

	def __str__(self):
		return str(self.key)


class Tree:
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def preorder(self, v):
		if (v != None):
			print(v.key, end = " ")
			self.preorder(v.left)
			self.preorder(v.right)
						
	def inorder(self, v):
		if (v != None):
			self.inorder(v.left)
			print(v.key, end = " ")
			self.inorder(v.right)
						
	def postorder(self, v):
		if (v != None):
			self.postorder(v.left)
			self.postorder(v.right)
			print(v.key, end = " ")
					
	def find_loc(self, key):
		if (self.size == 0):
			return None
		p = None
		v = self.root
		while v:
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
		if(p and p.key == key):
			return p
		else:
			return None
		
	def insert(self, key):
		p = self.find_loc(key)
		if (p == None or p.key != key):
			v = Node(key)
			if (p == None):
				self.root = v
			else:
				v.parent = p
				if (p.key >= key):
					p.left = v
				else:
					p.right = v
			self.size = self.size + 1
			return v
		else:
			return None

	def deleteByMerging(self, x):
		# assume that x is not None
		a, b, pt = x.left, x.right, x.parent

		if a == None:
			c = b
		else:
			c = m = a

			while m.right:
				m = m.right
			m.right = b
			if b: b.parent = m

		if self.root == x:  
			if c: c.parent = None
			self.root = c
		else:  
			if pt.left == x:
				pt.left = c
			else:
				pt.right = c
			if c: c.parent = pt
		self.size -= 1

	def deleteByCopying(self, x):
		a, b, pt = x.left, x.right, x.parent
		if a:
			y = a
			while y.right:
				y = y.right
			x.key = y.key
			
			if y.left:
				y.left.parent = y.parent
			if y.parent.left is y:
				y.parent.left = y.left
			else:
				y.parent.right = y.left
			del y
			self.size -= 1
			
		elif not a and b:
			y = b
			while y.left:
				y = y.left
			x.key = y.key
			if y.right:
				y.right.parent = y.parent
			if y.parent.left is y:
				y.parent.left = y.right
			else:
				y.parent.right = y.right
			del y
			self.size -= 1
			
		else:
			if pt == None and x.left == None and x.right == None:
				self.root = None
			else:
				if(pt.left is x):
					pt.left = None
				else:
					pt.right = None
			del x
			self.size -= 1

T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
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


T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
       	print("* {0} is not found!".format(cmd[1]))
        else:
       	print(" * {0} is found!".format(cmd[1]))
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
