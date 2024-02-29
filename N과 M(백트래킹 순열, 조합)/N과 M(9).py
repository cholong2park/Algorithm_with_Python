def all_permutation(data):
    bUsed = [0] * N
    permutation(data, [], 0, bUsed)

def permutation(data, sol, level, bUsed):
    if level == M:
        result.append(tuple(sol[:]))
        return

    for i in range(N):
        if not bUsed[i]:
            sol.append(data[i])
            bUsed[i] = True
            permutation(data, sol, level+1, bUsed)
            sol.pop()
            bUsed[i] = False

N, M = map(int, input().split())
result = []
data = list(map(int, input().split()))
all_permutation(data)
result = list(set(result))
result.sort()
for i in result:
    print(*i)