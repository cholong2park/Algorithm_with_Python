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

map_xy = list(map(int, list(input().split(' ')))) # [int형(열), int형(행)]
character = list(map(int, list(input().split(' '))))   # [int형(행), int형(열), int형(방향)]

real_map = []
for _ in range(map_xy[1]):
    map_row = list(map(int, list(input().split(' '))))
    real_map.append(map_row)
# print(real_map) real_map은 map[0]개의 요소를 가진 list를 map[1]개 가지고 있는 바둑판이다.

"""    
캐릭터 움직임
# 왼쪽으로 회전
    character[2] = (3 + int(character[2])) % 4 # 1(동)->0(북), 2(남)->1(동), 3(서)->2(남), 0(북)->3(서)

# 회전 후에 움직이기 
    # 동이면
        character[1] = int(character[1]) + 1
    # 서이면
        character[1] = int(character[1]) - 1
    # 남이면
        character[0] = int(character[0]) + 1
    # 북이면
        character[0] = int(character[0]) - 1
"""

character_map_list = [] # 캐릭터가 중복된 위치로 안가게 방지하기 위해 캐릭터가 있었던 위치들을 저장할 리스트
character_map_list.append(character[0:1])   # character에서 방향 요소를 빼고 처음 위치 요소만 저장

# 정해진 반복 횟수가 없기에 while문을 조건으로는 외곽으로 가면 종료(외곽은 온통 1이다)

while (0 < character[0] and character[0] < map_xy[1]) and (0 < character[1] and character[1] < map_xy[0]):
    # 일단 4 방향 탐색 시작
    if real_map[character[0] - 1][character[1]] == 1 or ([(character[0] - 1), character[1]] in character_map_list):
        if real_map[character[0] + 1][character[1]] == 1 or ([(character[0] + 1), character[1]] in character_map_list):
            if real_map[character[0]][character[1] - 1] == 1 or ([(character[0]), (character[1] - 1)] in character_map_list):
                if real_map[character[0]][character[1] + 1] == 1 or ([character[0], (character[1] + 1)] in character_map_list):
                    if character[2] == 0: # 방향이 북이면 
                        character[0] += 1
                        continue
                    elif character[2] == 1: # 방향이 동이면
                        character[1] -= 1
                        continue
                    elif character[2] == 2: # 방향이 남이면
                        character[0] -= 1
                        continue
                    else:   # 방향이 서이면
                        character[1] += 1
                        continue
                else:   # 4방향 중에 나아갈 길이 있다면 아래 코드 실행
                    pass
            else:
                pass
        else:
            pass
    else:
        pass

    character[2] = (3 + character[2]) % 4  # 일단 보는 방향에서 왼쪽 방향을 보게 만들자
    if character[2] == 0:   # 회전 후 보는 방향이 북이면
        if real_map[character[0] - 1][character[1]] != 1: # 이동한 곳이 바다가 아니라면
            if [(character[0] - 1), character[1]] not in character_map_list: # 이동한 곳이 갔었던 곳도 아니라면
                character[0] = character[0] - 1    # 이동하고
                character_map_list.append(character[0:1]) # 위치 저장!
            else:   # 이동한 곳이 갔었던 곳이라면 다시 처음(방향 전환)부터
                continue
        else:   # 이동한 곳이 바다라면 다시 처음(방향 전환)부터
            continue
            

    elif character[2] == 1: # 회전 후 보는 방향이 동이면 
        if real_map[character[0]][character[1] + 1] != 1: # 이동한 곳이 바다가 아니라면
            if [character[0], (character[1] + 1)] not in character_map_list: # 이동한 곳이 갔었던 곳도 아니라면
                character[1] = character[1] + 1    # 이동하고
                character_map_list.append(character[0:1]) # 위치 저장!
            else:   # 이동한 곳이 갔었던 곳이라면 다시 처음(방향 전환)부터
                continue
        else:   # 이동한 곳이 바다라면 다시 처음(방향 전환)부터
            continue

    elif character[2] == 2:   # 회전 후 보는 방향이 남이면 
        if real_map[character[0] + 1][character[1]] != 1: # 이동한 곳이 바다가 아니라면
            if [(character[0] + 1), character[1]] not in character_map_list: # 이동한 곳이 갔었던 곳도 아니라면
                character[0] = character[0] + 1    # 이동하고
                character_map_list.append(character[0:1]) # 위치 저장!
            else:   # 이동한 곳이 갔었던 곳이라면 다시 처음(방향 전환)부터
                continue
        else:   # 이동한 곳이 바다라면 다시 처음(방향 전환)부터
            continue
    
    else:   # 회전 후 보는 방향이 서이면
        if real_map[character[0]][character[1] - 1] != 1: # 이동한 곳이 바다가 아니라면
            if [character[0], (character[1] - 1)] not in character_map_list: # 이동한 곳이 갔었던 곳도 아니라면
                character[1] = character[1] - 1    # 이동하고
                character_map_list.append(character[0:1]) # 위치 저장!
            else:   # 이동한 곳이 갔었던 곳이라면 다시 처음(방향 전환)부터
                continue
        else:   # 이동한 곳이 바다라면 다시 처음(방향 전환)부터
            continue

print(len(character_map_list[1:]))  # 첫번째 위치 요소는 빼고 방문한 갯수 출력