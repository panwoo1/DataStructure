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

def compute_postfix(postfix):
	
	stack = Stack()
	token_list = postfix.split(' ')
	
	for token in token_list:
		
		if token == '+':
			t1 = stack.pop()
			t2 = stack.pop()
			stack.push(float(t2) + float(t1))
			
		elif token == '-':
			t1 = stack.pop()
			t2 = stack.pop()
			stack.push(float(t2) - float(t1))	
	
		elif token == '*':
			t1 = stack.pop()
			t2 = stack.pop()
			stack.push(float(t2) * float(t1))
			
		elif token == '/':
			t1 = stack.pop()
			t2 = stack.pop()
			stack.push(float(t2) / float(t1))
			
		elif token == '^':
			t1 = stack.pop()
			t2 = stack.pop()
			stack.push(float(t2) ** float(t1))
		
		else:
			stack.push(token)
	
	return stack.pop()
	

postfix = input()
result = compute_postfix(postfix)
print("%.4f" %result)