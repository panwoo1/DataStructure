'''
Infix to postfix
'''


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
        return self.__len__() == 0

def infix_to_postfix(infix):
    
	opstack = Stack()
	outstack = []
	token_list = infix.split(' ')
		
		# 연산자의 우선순위 설정
	prec = {}
	prec['('] = 0
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	prec['^'] = 3
	
	for token in token_list:
		if token == '(':
			opstack.push(token)
		elif token == ')':
			while opstack.top() != '(':
				outstack.append(opstack.pop())
			opstack.pop()
		elif token in '+-/*^':
			if opstack.isEmpty():
				opstack.push(token)
			else:
				while len(opstack) > 0:
					if prec[opstack.top()] >= prec[token]:
						outstack.append(opstack.pop())
					else:
						break
				opstack.push(token)
		else: # operand일 때
			outstack.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
		# ... ... ...
	while not opstack.isEmpty():
		outstack.append(opstack.pop())
	
	return " ".join(outstack)

	
infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)