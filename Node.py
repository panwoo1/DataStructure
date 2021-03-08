class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key)