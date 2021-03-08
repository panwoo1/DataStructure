'''
    Code by Chan-Su Shin (신찬수, 한국외대, 컴전학부)
    자료구조및실습 수업용 코드
    - hash table + linear probing + resize 환경에서 
    - set, remove, search 랜덤 생성해서 simulation
    - 결과를 hash.csv 파일에 append 모드로 기록함
    2020-05-07
'''

import random
import csv
import time

class HashOpenAddr:
    def __init__(self, size=8, ratio=0.5):
        self.size = size # number of slots
        self.items = 0   # number of items in hash table!
        self.when_resize = ratio # the empty slot ratio for resize
        self.keys = [None]*self.size
        self.values = [None]*self.size
        self.operations = 0     # number of operations
        self.collisions = 0     # number of collsions at find_slot calls
        self.comparisons = 0    # number of comparisons at set, search, remove operations
        self.succ_comp = self.fail_comp = 0     # number of comparisons for (un)successful searches
        self.succ_search = self.fail_search = 0 # number of (un)successful searches
        self.resize = 0

        # for testing
        self.keys_in_H = {0}

    def __str__(self):
        return str(self.keys)

    def __len__(self): # number of (keys, values) in hash table
        return self.items

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i

        # updating the numbers for stats
        self.operations += 1
        collision = 0
        comparison = 1
        # counting collisiion
        if self.keys[i] != None and self.keys[i] != key: # collision occurs
            collision = 1

        # counting comparision and finding slot 
        while self.keys[i] != None and self.keys[i] != key:
            i = (i+1) % self.size
            comparison += 1
            if i == start: # table is full, but not happen
                return None, collision, comparison
        return i, collision, comparison

    def move(self): # move keys in old table into new table
        old_size, old_keys, old_values = self.size, self.keys, self.values
        self.size = self.size * 2 # doubling the size
        self.items = 0 # reset the number of items of larger H
        self.keys = [None] * self.size
        self.values = [None] * self.size
        for i in range(old_size):
            if old_keys[i] != None:
                self.set(old_keys[i], old_values[i])
        del old_keys
        del old_values
        self.resize += 1

    def set(self, key, value=None):
        # resize when empty slots are less than half
        if len(self) > self.size*self.when_resize: 
            self.move() # doubling the number of slots
            print("resize({} -> {})".format(self.size//2, self.size), end=" ")

        i, coll, comp = self.find_slot(key)
        if i == None:
            print("H is FULL! <--- MUST NOT HAPPEN")
            return None

        if self.keys[i] != None:  # key is already in H
            self.values[i] = value
        else:   # new item, so insert it
            self.keys[i] = key
            self.values[i] = value
            self.items += 1
            # add keys to keys_in_H
            self.keys_in_H.add(key)
        
        self.collisions += coll  # total collisions
        self.comparisons += comp # total comparisons
        return key

    def remove(self, key):
        i, coll, comp = self.find_slot(key)

        if i == None:
            print("NEVER HAPPEN in remove!!")
            return None

        if self.keys[i] == None: # no key in H
            return None

        # update total collisions and comparisons
        self.collisions += coll
        self.comparisons += comp

        self.keys_in_H.remove(key)

        j = i
        while True:
            self.keys[i] = None  # mark H[i] as unoccupied
            while True:
                j = (j + 1) % self.size
                if self.keys[j] == None:  # done, so return
                    self.items -= 1
                    return key

                self.comparisons += 1 # additional comparison
                k = self.hash_function(self.keys[j])
                if not (i < k <= j or j < i < k or k <= j < i):
                    break
            self.keys[i] = self.keys[j]
            self.values[i] = self.keys[j]
            i = j

    def search(self, key):
        i, coll, comp = self.find_slot(key)

        self.collisions += coll
        self.comparisons += comp

        if i != None and self.keys[i] != None:
            # success
            self.succ_search += 1
            self.succ_comp += comp
            return self.values[i]
        else:
            self.fail_search += 1
            self.fail_comp += comp
            return None

    def hash_function(self, key):
       return key % self.size

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)


m = int(input("Hash table size m = "))
r = float(input("Load factor for resize (0 < r < 1) = "))
H = HashOpenAddr(m, r)

fieldnames = ['operations', 'collisions', 'comparisons', 'succ_search', 'succ_comp', 'fail_search', 'fail_comp']
with open('hash.csv', 'w') as f_csv:
    csv_writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('hash.csv', 'a') as f_csv:
        print(H.operations, end=": ")
        op = random.randint(1,5)
        if op == 1 or op == 2: # set
            key = random.randint(1, 2*H.size)
            result = H.set(key, 'v'+str(key))
            print(f"set({key}) - ", end="")
            if result == None:
                print("FULL - NEVER HAPPEN!")
                break
            else:
                print("done.")
        elif op == 3: # remove
            key = random.randint(1, 2*H.size)
            result = H.remove(key)
            print(f"remove({key}) - ", end="")
            if result == None:
                print("failed.")
            else:
                print("done.")
        else: # op == 4, 5 search
            if op == 4: # successful search
                key = random.choice(tuple(H.keys_in_H))
            if (op == 4 and key == None) or op == 5: # unsuccessful search
                while True:
                    key = random.randint(1, 3*H.size)
                    if key not in H.keys_in_H:
                        break
            result = H.search(key)
            print(f"search({key}) - ", end="")
            if result == None:
                print("failed.")
            else:
                print("done.")
        
        csv_writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        info = {
            'operations': H.operations,
            'collisions': H.collisions,
            'comparisons': H.comparisons,
            'succ_search': H.succ_search,
            'succ_comp': H.succ_comp,
            'fail_search': H.fail_search,
            'fail_comp': H.fail_comp
        }
        csv_writer.writerow(info)
    time.sleep(0.2) # sleep for 0.2 seconds