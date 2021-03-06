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
        if(key in self.A):
            return None
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


n = int(input())
m = int(input())
direct_g = [[] for i in range(n)]
source_node = 0
distance = [float("inf") for i in range(n)]
distance[0] = 0

for i in range(m):
    u, v, w = map(int, input().split())
    direct_g[u].append([v, w])

H = AdaptedHeap()
H.insert(distance[0])
while H:
    u = H.delete_min()
    for i in direct_g[u]:
        if(distance[u] + i[1] < distance[i[0]]):
            old = distance[i[0]]
            distance[i[0]] = distance[u] + i[1]
            H.insert(i[0])

for n in distance:
    print(n, end=' ')
