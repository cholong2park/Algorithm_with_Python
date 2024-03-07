dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
check_x0 = [0, 0, -1, 1, 1, -1, 2, -2, -1, 1]
check_y0 = [-1, -2, -1, -1, 0, 0, 0, 0, 1, 1]
check_x1 = [1, 2, 1, 1, 0, 0, 0, 0, -1, -1]
check_y1 = [0, 0, 1, 1, -1, 1, -2, 2, -1, 1]
def tornado(point, direction):
    global out
    if direction == 0:
        for i in range(10):
            nx = point[0] + check_x0[i]
            ny = point[1] + check_y0[i]
            if i == 0:
                more = 55*graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 1:
                more = 5 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 2 or i == 3:
                more = 10 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 4 or i == 5:
                more = 7 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 6 or i == 7:
                more = 2 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            else:
                more = 1 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
    elif direction == 1:
        for i in range(10):
            nx = point[0] + check_x1[i]
            ny = point[1] + check_y1[i]
            if i == 0:
                more = 55*graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 1:
                more = 5 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 2 or i == 3:
                more = 10 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 4 or i == 5:
                more = 7 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 6 or i == 7:
                more = 2 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            else:
                more = 1 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
    elif direction == 2:
        for i in range(10):
            nx = point[0] - check_x0[i]
            ny = point[1] - check_y0[i]
            if i == 0:
                more = 55*graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 1:
                more = 5 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 2 or i == 3:
                more = 10 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 4 or i == 5:
                more = 7 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 6 or i == 7:
                more = 2 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            else:
                more = 1 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
    else:
        for i in range(10):
            nx = point[0] - check_x1[i]
            ny = point[1] - check_y1[i]
            if i == 0:
                more = 55*graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 1:
                more = 5 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 2 or i == 3:
                more = 10 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 4 or i == 5:
                more = 7 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            elif i == 6 or i == 7:
                more = 2 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more
            else:
                more = 1 * graph[point[0]][point[1]]//100
                if 0 <= nx < N and 0 <= ny < N:
                    graph[nx][ny] += more
                else:
                    out += more



def next(point, count_num, move, direction):
    global num
    if point[0] != 0 or point[1] != 0:
        tornado(point, direction)
        if count_num != move:
            point = [point[0] + dx[direction], point[1] + dy[direction]]
            next(point, count_num + 1, move, direction)
        else:
            point = [point[0] + dx[direction], point[1] + dy[direction]]
            num += 1
            next(point, 0, num//2, (direction + 1) % 4)
    elif point

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
start = [N//2, N//2]
out = 0
num = 0
next(start, 0, 0, 0)
print(out)