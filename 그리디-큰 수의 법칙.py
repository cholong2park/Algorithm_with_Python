"""
N: 배열의 크기, M: 숫자가 더해지는 횟수, K: 숫자가 연속가능한 횟수
- 입력조건
    1. 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
    3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.
- 출력 조건
    1. 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
- 입력 예시
    5 8 3
    2 4 5 4 6
- 출력 예시
    46
"""
n, m, k = map(int, input().split(' '))  # map 함수로 각각에 인자에 int 적용 / .split('구분자')를 통해 input()로 넣은 것들을 띄어쓰기로 짤라서 n, m, k에 넣어줌
number = input().split(' ')  # n 갯수의 자연수를 입력하고 list에 넣고 number에 할당

number.sort()   # sort()를 통하여 오름차순 정렬

big_2 = int(number[n - 2])
big = int(number[n - 1])

count = 0
result = 0
while count < m:
    for i in range(k):
        result += big
        count += 1
    result += big_2
    count += 1

print(result)    