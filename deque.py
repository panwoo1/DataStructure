class deque:
	def __init__(self, s):
		self.items = []
		for c in s:
			self.items.append(c)
		
	def append(self, c):
		self.items.append(c)
		
	def appendleft(self, c):
		self.items.insert(0, c)
		
	def pop(self):
		if len(self.items) == 0:
			print("Deque is empty")
		else:
			return self.items.pop()
		
	def popleft(self):
		if len(self.items) == 0:
			print("Deque is empty")
		else:
			return self.items.pop(0)
			
	def __len__(self):
		return len(self.items)
	
	def right(self):
		if len(self.items) == 0:
			print("Deque is empty")
		return self.items[len(self.items)-1]

	def left(self):
		if len(self.items) == 0:
			print("Deque is empty")
		return self.items[0]
		
def check_palindrome(s):
	dq = deque(s)
	palindrome = True
	while len(dq) > 1:
		if dq.popleft() != dq.pop():
			palindrome = False
	return palindrome


palindrome = input()
print(check_palindrome(palindrome))