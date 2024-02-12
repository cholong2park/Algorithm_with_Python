from collections import deque

def bfs(start):
    visited = [-1] * (N + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:    # 큐가 다 비어 있을 때까지
        now = queue.popleft()
        for next in arr[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1    # 시작한 숫자로 부터 얼만큼 떨어져있는지 확인
                queue.append(next)
    total = sum(visited)
    return total

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for i in range(M):
    person1, person2 = map(int, input().split())
    arr[person1].append(person2)
    arr[person2].append(person1)

min_total = 999999
result = 0  # 가장 적은 사람의 숫자가 들어갈 곳
for i in range(1, N+1):
    total = bfs(i)
    if total < min_total:
        min_total = total
        result = i

print(result)