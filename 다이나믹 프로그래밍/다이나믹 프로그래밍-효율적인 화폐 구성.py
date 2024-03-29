"""
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다. 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한
화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다. 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한으
화폐 개수이다.
- 입력 조건
    - 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10000)
    - 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10000보다 작거나 같은 자연수이다.
- 출력 조건
    - 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
    - 불가능할 때는 -1을 출력한다.
"""
"""
15 (2, 3, 7) 15 - [7] = 8, 8 - 7 = 1 < arr[0], 8 - [3] = 5, 5 - [3] = 2, 2 - 3 = -1 < arr[0],  2 - [2] = 0
만들 화폐랑 쓴 화폐 갯수 => 1 x / 2 1 / 3 1 / 4 2 / 5 2 / 6 2 / 7 1 / 

"""
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

d = [0] * (M+1)
num = M # 원본 M이 훼손되지 않게 M 값을 복사해서 넣어줌
i = len(arr) - 1
while True: # 큰 수 부터 하나씩 빼 나가자
    if num - arr[i] == 0:
        print(d[M]+1)
        break
    if (num-arr[i]) < arr[0]:
        i -= 1
    if (num-arr[i]) >= arr[0]:
        num -= arr[i]
        d[M] += 1
    if i == 0 and ((num-arr[i]) < arr[0]):
        print(-1)
        break
# 많은 중복 연산이 있다.... 심지어 값을 저장해놓고 그걸 이용하지도 않잖아...

"""
한번 메모이제이션 생각해보자
d = [0] * (M+1)
num = M # 원본 M이 훼손되지 않게 M 값을 복사해서 넣어줌
i = len(arr) - 1
for i in range(arr[len(arr)-1]):
    if num - arr[i] == 0:
        print(d[M]+1)
        break
    if (num-arr[i]) < arr[0]:
        i -= 1
    if (num-arr[i]) >= arr[0]:
        num -= arr[i]
        d[M] += 1
    if i == 0 and ((num-arr[i]) < arr[0]):
        print(-1)
        break
d[M] = d[M-arr[len(arr)-1]] + 1
"""