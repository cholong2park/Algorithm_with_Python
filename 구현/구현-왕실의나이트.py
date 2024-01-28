"""
행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면이다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서
다음과 같은 2가지 경우로 이동할 수 있다.
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
이때 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.

입력 조건
    - 첫째 줄에 8 x 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.
출력 조건
    - 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
"""

# 문제를 풀기 전 좀 더 쉽게 풀기 위해서 파이썬의 아스키코드에 대해서 알아보자!!!!!
# 문자 A ~ Z는 65 ~ 90의 아스키 값을 갖게 되고, 문자 a ~ z는 97 ~ 122라는 아스키 값을 갖는다.
# ard() 함수를 사용하면 문자를 아스키 값으로, chr()함수를 사용하면 아스키 값을 문자로 표현할 수있다.
# 예시) print(ard('A')) => 65 , print(chr(65)) => A


knight_colum_row = input()
knight_colum_row_list = [knight_colum_row[0], knight_colum_row[1]]
# 이번에는 붙어있는 문자열이었기에 split 함수를 사용할 수 없었고 슬라이싱 하여 나이트의 위치를 list화 하였다. 해당 list[0]은 열을 list[1]은 행을 의미한다.
# a1을 input 하면 ['a', '1']이라는 리스트가 만들어진다.


kingdom_garden = []
for _ in range(8):
    kingdom_garden.append(['a', 'b', 'c', 'd', 'e', 'f', 'g',' h'])

# kingdom_garden은 열[a(0) ~ h(7) 8개 요소를 갖는 리스트]을 8개(0 ~ 7)인 list이다.
# a1을 입력하면 list[0][0]을 나타내게 된다는 것을 명심하자!!!!!

kinght_in_garden_row =  int(knight_colum_row_list[1]) - 1   # 1을 빼준 이유는 문제상에서는 1이지만 실제 컴퓨터 상에서는 0이기 때문
kingdom_in_garden_colum = kingdom_garden[0].index(knight_colum_row_list[0])    # garden에서 'a'의 인덱스 값은 0, 'b'는 1 etc
# 위의 작업을 통해서 우리는 knight의 위치를 컴퓨터 상의 list 바둑판 좌표에 옮길 수 있었다.

count_move = 0  # 경우의 수를 저장해둘 값이다!

# 총 최대 8가지 경우의 수가 좌,우로 2번 움직이고 위,아래 1번[4가지] / 위, 아래로 2번 움직이고 좌, 우 1번[4가지]
# 1
kinght_in_garden_row += 2
kingdom_in_garden_colum += 1
if (0 <= kinght_in_garden_row and kinght_in_garden_row <= 7) and (0 <= kingdom_in_garden_colum and kingdom_in_garden_colum <= 7):
    count_move += 1
else:
    pass
# 제자리로 돌려 놓자!
kinght_in_garden_row -= 2
kingdom_in_garden_colum -= 1

# 2
kinght_in_garden_row += 2
kingdom_in_garden_colum -= 1
if (0 <= kinght_in_garden_row and kinght_in_garden_row <= 7) and (0 <= kingdom_in_garden_colum and kingdom_in_garden_colum <= 7):
        count_move += 1
else:
    pass
kinght_in_garden_row -= 2
kingdom_in_garden_colum += 1

# 3
kinght_in_garden_row -= 2
kingdom_in_garden_colum += 1
if (0 <= kinght_in_garden_row and kinght_in_garden_row <= 7) and (0 <= kingdom_in_garden_colum and kingdom_in_garden_colum <= 7):
    count_move += 1
else:
    pass
kinght_in_garden_row += 2
kingdom_in_garden_colum -= 1

# 4
kinght_in_garden_row -= 2
kingdom_in_garden_colum -= 1
if (0 <= kinght_in_garden_row and kinght_in_garden_row <= 7) and (0 <= kingdom_in_garden_colum and kingdom_in_garden_colum <= 7):
    count_move += 1
else:
    pass  
kinght_in_garden_row += 2
kingdom_in_garden_colum += 1

# 5
kinght_in_garden_row += 1
kingdom_in_garden_colum += 2
if (0 <= kinght_in_garden_row and kinght_in_garden_row <= 7) and (0 <= kingdom_in_garden_colum and kingdom_in_garden_colum <= 7):
    count_move += 1
else:
    pass
kinght_in_garden_row -= 1
kingdom_in_garden_colum -= 2

# 6
kinght_in_garden_row += 1
kingdom_in_garden_colum -= 2
if (0 <= kinght_in_garden_row and kinght_in_garden_row <= 7) and (0 <= kingdom_in_garden_colum and kingdom_in_garden_colum <= 7):
    count_move += 1
else:
    pass
kinght_in_garden_row -= 1
kingdom_in_garden_colum += 2

# 7
kinght_in_garden_row -= 1
kingdom_in_garden_colum += 2
if (0 <= kinght_in_garden_row and kinght_in_garden_row <= 7) and (0 <= kingdom_in_garden_colum and kingdom_in_garden_colum <= 7):
    count_move += 1
else:
    pass
kinght_in_garden_row += 1
kingdom_in_garden_colum -= 2

# 8
kinght_in_garden_row -= 1
kingdom_in_garden_colum -= 2
if (0 <= kinght_in_garden_row and kinght_in_garden_row <= 7) and (0 <= kingdom_in_garden_colum and kingdom_in_garden_colum <= 7):
    count_move += 1
else:
    pass
kinght_in_garden_row += 1
kingdom_in_garden_colum += 2

print(count_move)