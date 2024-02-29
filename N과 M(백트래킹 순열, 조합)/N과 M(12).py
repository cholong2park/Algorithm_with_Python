def all_permutation(data):
    permutation(data, [], 0)

def permutation(data, sol, level):
    if level == M:
        result.append(tuple(sol[:]))
        return

    for i in range(N):
        if level == 0:
            sol.append(data[i])
            permutation(data, sol, level+1)
            sol.pop()
        else:
            if data[i] >= sol[level-1]:
                sol.append(data[i])
                permutation(data, sol, level + 1)
                sol.pop()

N, M = map(int, input().split())
data = list(map(int, input().split()))
result = []
all_permutation(data)
result = list(set(result))
result.sort()
for i in result:
    print(*i)