'''
동빈이는 총 N개의 강의를 듣고자 한다. 모든 강의는 1번부터 N번까지의 번호를 가진다. 또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다. 예를 들어 N=3일 때, 3번 강의의 선수 강의로
1번과 2번 강의가 있고, 1번과 2번 강의는 선수 강의가 없다고 가정하자. 그리고 각 강의에 대하여 강의 시간이 다음과 같다고 가정하자.
    - 1번 강의 : 30시간
    - 2번 강의 : 20시간
    - 3번 강의 : 40시간
이 경우 1번 강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지의 최소 시간은 20시간, 3번 강의를 수강하기까지의 최소 시간은 70시간이다.

동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램을 작성하시오.
'''

# 위상 정렬 알고리즘의 응용문제이다.
import copy

N = int(input())

# 진입차수
in_line = [0] * (N+1)
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)

for i in range(1, N+1):
    data = list(map(int, input().split()))  # data의 첫 정보는 걸리는 시간, 두번째는 그 강의를 듣기 위한 선행 강의
    time[i] = data[0]
    for x in data[1:-1]:    # data = [1, 2, 3, 4, 5]일 때 data[1:-1]이면 [2, 3, 4] / data = [1, 2]일 떼 data[1:-1]이면 []
        in_line[i] += 1
        graph[x].append(i)  # x가 선행 강의이며 그 선행 강의 list에 하위 강의 i를 넣어준다.

result = copy.deepcopy(time)    # time을 훼손하지 않으면서 알고리즘을 진행하면서 바뀌는 값들을 넣어줄 곳 => 리스트의 값을 복사할때는 deepcopy 사용하자
q= []

for i in range(1, N+1):
    if in_line[i] == 0:
        q.append(i)

while q:
    now = q.pop(0)
    for i in graph[now]:
        result[i] = max(result[i], result[now]+time[i])
        in_line -= 1
        if in_line[i] == 0:
            q.append(i)

for i in range(1, N+1):
    print(result[i])