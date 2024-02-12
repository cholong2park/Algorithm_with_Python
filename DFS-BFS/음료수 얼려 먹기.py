def dfs(row, colum):
    if row < 0 or row >= N or colum < 0 or colum >= M:  # map 밖으로 넘어가면 False 반환하며 바로 종료
        return False
    if map_ice[row][colum] == 0:
        map_ice[row][colum] = 1   # 0인 곳에 방문하면 1로 바꾸어 방문했다는 것을 알림
        # 이후 상하좌우로 가서 다시 탐색 시작
        # 밑에서 진행하는 것은 첫 탐색에 결과값에 포함이 된다.
        dfs(row-1, colum)
        dfs(row, colum-1)
        dfs(row+1, colum)
        dfs(row, colum+1)
        return True
    return False

N, M = map(int, input().split())
map_ice = [list(map(int, input())) for _ in range(N)]

count = 0   # 만들 수 있는 얼음의 수
# 행 탐색을 진행한다.
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1

print(count)