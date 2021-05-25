class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def preorder(self, v):
        if (v != None):
            print(v.key)
            self.preorder(v.left)
            self.preorder(v.right)

    def find_loc(self, key):
        if (self.size == 0):
            return None
        p = None
        v = self.root
        while v:
            if (v.key == key):
                return v
            else:
                if (v.key < key):
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if (p and p.key == key):
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
            self.size += 1
            return v
        else:
            return None

    def deleteByMerging(self, x):
        a, b, pt = x.left, x.right, x.parent
        if (a == None):
            c = b
            s = pt
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m
            if (self.root == x):
                if c:
                    c.parent = None
                self.root = c
            else:
                if (pt.left == x):
                    pt.left = c
                else:
                    pt.right = c
            self.size -= 1
