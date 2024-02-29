def all_permutation(data):
    permutation2(data, [], 0)

def permutation2(data, sol, level):
    if level == M:
        print(*sol)
        return

    for i in range(len(data)):
        sol.append(data[i])
        permutation2(data, sol, level+1)
        sol.pop()

N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
all_permutation(data)