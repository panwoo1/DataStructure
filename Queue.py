class Queue:
    def __init__(self):
        self.itmes = []
        self.front_index = 0
    
    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty")
            return None
        else:
        x = self.items[self.front_index]
        self.front_index += 1
        return x
    
    def front(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("Queue is empty")
        else:
            return self.items[self.front_index]

    def __len__(self):
        return len(self.items) - self.front_index

    def isEmpty(self):
        return len(self)