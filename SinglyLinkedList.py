class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
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

    def pushFront(self, key, value = None):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key, value = None):
        new_node = Node(key, value)
        if(self.size == 0):
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):
        key = value = None
        if(len(self))>0:
            key = self.head.key
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
        return key, value

    def popBack(self):
        if (self.size == 0):
            return None, None
        else:
            previous, current = None, self.head
            while(current.next != None):
                previous, current = current, current.next
            key, value = tail.key, tail.value
            tail = current
            if(self.head == tail):
                self.head = None
            else:
                previous.next = tail.next
            self.size -= 1
            return key, value

    def search(self, key):
        for v in self:
            if (v.key == key):
                return v
        return None

    def remove(self, key):
        v = self.search(key)
        if (len(self) == 0 or v == None):
            return None
        elif(v == self.head):
            self.popFront(v)
        else:
            w = self.head
            while(w.next != None):
                if(w.next == v):
                    w.next = v.next
