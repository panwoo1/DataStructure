class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = self.prev = self
    
    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __iter__(self):
        v = self.head
        while (v!= None):
            yield v
            v = v.next

    def __str__(self):
        s = ""
        v = self.head
        while (v):
            s += str(v.key) + " -> "
            v = v.next
        s += "None"
        return s
    def __len__(self):
        return self.size

    def isEmpty(self):
        v = self.head
        if(v.next == self.head):
            return True
        else:
            return False

    def search(self, key):
        v = self.head
        while(v.next != self.head):
            if(v.key == key):
                return v
            v = v.next
        return None

    def splice(a, b, x):
        if(a == None or b == None or x == None):
            return

        ap = a.prev
        bn = b.next

        ap.next = bn
        bn.prev = ap

        xn = x.next
        xn.prev = b
        a.prev = x
        x.next = a

    def moveAfter(self, a, x):
        self.splice(a, a, x)

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)
    
    def insertBefore(self, x, key):
        self.moveAfter(Node(key), x)

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def remove(self, x):
        if(x == None or x == self.head):
            return
        x.prev.next = x.next
        x.next.prev = x.prev

    def popFront(self):
        if (self.isEmpty()):
            return None
        key = self.head.next.key
        self.remove(head.next)
        return key

    def popBack(self):
        if (self.isEmpty()):
            return None
        key = self.head.prev.key
        self.remove(head.prev)
        return key

    def first(self):
        if (self.isEmpty()):
            return None
        else:
            return self.head.next

    def last(self):
        if (self.isEmpty()):
            return None
        else:
            return self.head.prev

    def join(self, list):
        self.splice(list.head.next, list.head.prev, self.head.prev)

    def split(self, x):
        new_list = DoublyLinkedList()
        self.splice(x, self.head.prev, list.self.next)
        return new_list
    
    def printList(self):
		v = self.head.next
		print("h -> " , end='')
		while(v != self.head):
			if(v.next != self.head):
				print(v.key, "->", end=" ")
			else:
				print(v.key, end="")
			v = v.next
		print(" -> h")