def all_permutation(data):
    bUsed = [0] * len(data)
    permutation(data, [], 0, bUsed)

def permutation(data, sol, level, bUsed):
    if level == M:
        print(*sol)
        return

    for i in range(len(data)):
        if not bUsed[i]:
            sol.append(data[i])
            bUsed[i] = True
            permutation(data, sol, level+1, bUsed)
            sol.pop()
            bUsed[i] = False

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
all_permutation(data)