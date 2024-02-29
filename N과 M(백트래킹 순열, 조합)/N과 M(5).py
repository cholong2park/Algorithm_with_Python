def all_permutation(data):
    bUsed = [0] * N
    permutation(data, [], 0, bUsed)

def permutation(data, sol, level, bUsed):
    if level == M:
        print(*sol)
        return

    for i in range(N):
        if not bUsed[i]:
            sol.append(data[i])
            bUsed[i] = True
            permutation(data, sol, level+1, bUsed)
            sol.pop()
            bUsed[i] = False

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
all_permutation(data)