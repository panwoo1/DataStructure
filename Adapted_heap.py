class AdaptedHeap:  # min_heap으로 정의함!
    def __init__(self):
        self.A = []
        self.D = {}  # dictionary D[key] = index

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def insert(self, key):
        # code here
        # key 값이 최종 저장된 index를 리턴한다!

        index = len(self.A)
        self.D[key] = index
        self.A.append(key)
        self.heapify_up(self.D[key])
        return self.D[key]

    def heapify_up(self, k):
        # code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
        p = (k-1) // 2
        if p >= 0 and self.A[p] > self.A[k]:
            self.A[k], self.A[p] = self.A[p], self.A[k]
            self.D[self.A[k]], self.D[self.A[p]
                                      ] = self.D[self.A[p]], self.D[self.A[k]]
            self.heapify_up(p)

    def heapify_down(self, k):
        # code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
        L, R = 2*k + 1, 2*k + 2
        s_value_index = k
        if(L <= len(self.A) - 1 and self.A[k] > self.A[L]):
            s_value_index = L
        if(R <= len(self.A) - 1 and self.A[k] > self.A[R] and self.A[L] > self.A[R]):
            s_value_index = R
        if (s_value_index != k):
            self.A[k], self.A[s_value_index] = self.A[s_value_index], self.A[k]
            self.D[self.A[k]], self.D[self.A[s_value_index]
                                      ] = self.D[self.A[s_value_index]], self.D[self.A[k]]
            self.heapify_down(s_value_index)

    def find_min(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 리턴
        # code here
        if (len(self.A) == 0):
            return None
        else:
            return self.A[0]

    def delete_min(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
        # code here
        if (len(self.A) == 0):
            return None
        else:
            k = self.D[self.find_min()]
            print(k)
            self.A[k], self.A[-1] = self.A[-1], self.A[k]
            self.D[self.A[k]], self.D[self.A[-1]
                                      ] = self.D[self.A[-1]], self.D[self.A[k]]
            x = self.A.pop()
            self.D.pop(x)
            self.heapify_down(k)
            return x

    def update_key(self, old_key, new_key):
        # old_key가 힙에 없으면 None 리턴
        # 아니면, new_key 값이 최종 저장된 index 리턴
        # code here
        if old_key not in self.D:
            return None
        old_key_index = self.D[old_key]
        if old_key > new_key:
            self.A[old_key_index] = new_key
            self.D.pop(old_key)
            self.D.update({self.A[old_key_index]: old_key_index})
            self.heapify_up(old_key_index)
        if old_key < new_key:
            self.A[old_key_index] = new_key
            self.D.update({self.A[old_key_index]: old_key_index})
            self.D.pop(old_key)
            self.heapify_down(old_key_index)
        return self.D[new_key]


# 아래 명령 처리 부분은 수정하지 말 것!
H = AdaptedHeap()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        key = int(cmd[1])
        loc = H.insert(key)
        print(f"+ {int(cmd[1])} is inserted")
    elif cmd[0] == 'find_min':
        m_key = H.find_min()
        if m_key != None:
            print(f"* {m_key} is the minimum")
        else:
            print(f"* heap is empty")
    elif cmd[0] == 'delete_min':
        m_key = H.delete_min()
        if m_key != None:
            print(f"* {m_key} is the minimum, then deleted")
        else:
            print(f"* heap is empty")
    elif cmd[0] == 'update':
        old_key, new_key = int(cmd[1]), int(cmd[2])
        idx = H.update_key(old_key, new_key)
        if idx == None:
            print(f"* {old_key} is not in heap")
        else:
            print(f"~ {old_key} is updated to {new_key}")
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
