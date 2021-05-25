import random, time

def unique_n(A):
	# code
	B = A[1:] #새로운 리스트 B를 선언해 A[1]부터 끝까지 저장
	for i in range(0, len(B)): #B[1] = A[0] 이므로 순차적 비교 가능
		if(A[i] == B[i]):
			print("NO")
			return
	print("YES")
	
def unique_nlogn(A):
	# code
	A.sort()
	for i in range(1, len(A)):
		if(A[i-1] == A[i]):
			print("NO")
			return
	print("YES")
	

def unique_n2(A):
	# code
	for i in range(0, len(A)):
		for j in range(i+1, len(A)):
			if(A[i] == A[j]):
				print("NO")
				return
	print("YES")

# input: 값의 개수 n
n = int(input())
# -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성
A = random.sample(range(-n, n+1), n)

# 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
s1 = time.process_time()
unique_n(A)
e1 = time.process_time()
print("unique_n 수행시간 =", round(e1-s1, 8))
print()
s2 = time.process_time()
unique_nlogn(A)
e2 = time.process_time()
print("unique_nlogn 수행시간 =", round(e2-s2, 8))
print()
s3 = time.process_time()
unique_n2(A)
e3 = time.process_time()
print("unique_n2 수행시간 =", round(e3-s3, 8))

# 당연히 모두 다르게 sample했으므로 YES가 세 번 연속 출력되어야 한다
# 동시에 각 함수의 실행 시간을 측정해본다
# 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다
