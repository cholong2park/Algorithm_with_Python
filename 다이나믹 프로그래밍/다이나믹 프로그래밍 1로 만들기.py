"""
정수 X가 주어질 때 사용할 수 있는 연산은 다음과 같이 4가지이다.
    a. X가 5로 나누어떨어지면, 5로 나눈다.
    b. X가 3으로 나누어 떨어지면, 3으로 나눈다.
    c. X가 2로 나누어 떨어지면, 2로 나눈다.
    d. X에서 1을 뺀다.
정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
- 입력 조건
    - 첫째 줄에 정수 X가 주어진다. (1 <= X <= 30,000)
- 출력 조건
    - 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""
def makeone(num):
    d = [0] * 30001 # 주어진 X가 30000까지
    for i in range(2, num + 1):
        d[i] += d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5]+1)
    return d[num]

N = int(input())
count = makeone(N)
print(count)