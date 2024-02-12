def dfs(start):
    visited[start] = 1
    next = arr[start]
    if visited[next] == 0:
        dfs(next)

Test = int(input())
for _ in range(Test):
    result = 0
    N = int(input())
    visited = [0] * (N + 1)
    arr = [0] + list(map(int, input().split()))
    for i in range(1, N + 1):
        if visited[i] == 0:
            dfs(i)
            result += 1
    print(result)