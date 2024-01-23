"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은
N이 K로 나누어떨어질 때만 선택할 수 있다.
    1. N에서 1을 뺀다.
    2. N을 K로 나눈다.
- 입력 조건
    1. 첫째 줄에 N(2 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
- 출력 조건
    1. 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
- 입력 예시     - 출력 예시
25 5             2
"""

n, k = map(int, input().split(' '))

count = 0   # 횟수를 저장할 변수

while n != 1:   # n이 1이 아니면 계속 반복! (1이 되는 순간 종료)
    if n % k != 0: # n을 k로 나눴을 때 나머지가 0이 아니면
        n -= 1  # n에서 1 빼고 
        count += 1  # 횟수 1 추가!
    else:
        n /= k  # n을 k로 나누고 그 값을 다시 넣어줌
        count += 1  # 횟수 1 추가!

print(count)
