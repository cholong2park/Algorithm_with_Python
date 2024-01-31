"""
N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을
출력하는 프로그램을 작성하시오.
- 입력 조건
    - 첫 번째 줄에 N, K가 공백으로 구분되어 입력된다. (1 <= N <= 100,000, 0 <= K <= N)
    - 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000 보다 작은 자연수이다.
    - 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000 보다 작은 자연수입니다.
- 출력 조건
    - 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.
"""
list_num, count = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(list_num-1, 0, -1):  # A는 작은 수부터 정렬!
    for j in range(0, i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

for i in range(list_num-1, 0, -1):  # B는 큰 수부터 정렬!
    for j in range(0, i):
        if B[j] < B[j+1]:
            B[j], B[j+1] = B[j+1], B[j]

for i in range(count):
    if A[i] < B[i]:
        A[i] = B[i]
    elif A[i] == B[i]:
        pass

result = 0
for x in A:
    result += x

print(result)