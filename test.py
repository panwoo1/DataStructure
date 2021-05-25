import time
from random import randrange

def findMin(alist):
    minsofar = alist[0]
    for i in alist: # O(n) alist의 길이만큼 반복, loop 중첩 없음   
        if i < minsofar:
            minsofar = i
    return minsofar

# 확인
print(findMin([5,2,1,0]))
print(findMin([0,2,3,4]))

# 연산시간 (O(n))
for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for _ in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print("size: {}, time: {}".format(listSize, end-start))