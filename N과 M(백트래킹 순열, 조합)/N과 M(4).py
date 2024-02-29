def all_permutation(data):
    permutation(data, [], 0)

def permutation(data, sol, level):
    if level == M:
        print(*sol)
        return

    for i in range(len(data)):
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
data = [i for i in range(1, N+1)]
all_permutation(data)