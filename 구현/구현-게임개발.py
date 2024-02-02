"""
현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다. 캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이뤄진 N x M 크기의 직사각형으로,
각각의 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수 B는 서쪽으로부터 떨어진 칸의 개수이다.
캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.

캐릭터의 움직임 메뉴얼
    1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
    2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진하다. 왼쪽 방향에 가보지 않은
    칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
    3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때
    뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

입력조건
    - 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3 <= N, M <= 50)
    - 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 방향 d의 값으로는 다음과 같이
    4가지가 존재한다. 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
    - 셋째 줄부터 맵이 육지인지 바디인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽
    순서대로 주어진다. 맵의 외곽은 항상 바다로 되어 있다. 0: 육지, 1: 바다
    - 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
 
출력 조건
    - 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
"""
"""    
캐릭터 움직임
# 왼쪽으로 회전
    character[2] = (3 + int(character[2])) % 4 # 1(동)->0(북), 2(남)->1(동), 3(서)->2(남), 0(북)->3(서)

# 회전 후에 움직이기 
    # 동이면 1
        character[1] = int(character[1]) + 1
    # 서이면 3
        character[1] = int(character[1]) - 1
    # 남이면 2
        character[0] = int(character[0]) + 1
    # 북이면 0
        character[0] = int(character[0]) - 1

"""
def move(arr, direction):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    arr[0] += dx[direction]
    arr[1] += dy[direction]

N, M = map(int, input().split())
*point, direction = list(map(int, input().split()))
map_in = [list(map(int, input().split())) for _ in range(N)]

count = 0   # 움직였다는건 새로운 곳을 방문했다는 것! 움직일때마다 count += 1
map_in[point[0]][point[1]] -= 1 # 방문할때마다 map_in에 새겨진 값들을 하나씩 뺄 것임

while 0 < point[0] < N-1 and 0 < point[1] < M-1:
    if map_in[point[0]-1][point[1]] == 0:
        direction = 0
        move(point, direction)
        count += 1
        map_in[point[0]][point[1]] -= 1
    elif map_in[point[0]][point[1]+1] == 0:
        direction = 1
        move(point, direction)
        count += 1
        map_in[point[0]][point[1]] -= 1
    elif map_in[point[0]+1][point[1]] == 0:
        direction = 2
        move(point, direction)
        count += 1
        map_in[point[0]][point[1]] -= 1
    elif map_in[point[0]][point[1]-1] == 0:
        direction = 3
        move(point, direction)
        count += 1
        map_in[point[0]][point[1]] -= 1
    else:
        direction = (direction + 2) % 4
        while 0 < point[0] < N-1 and 0 < point[1] < M-1:
            move(point, direction)
            count += 1
print(count-1)  # 1을 빼주는 이유는 마지막으로 바다로 뛰어드는 횟수는 차감