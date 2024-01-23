"""
- 입력 조건
    1. 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 <= N, M <= 100)
    2. 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.
- 출력 조건
    1. 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
- 입력 예시 1   출력 예시 1             - 입력 예시 2   출력 예시 2
  3 3           2                        2 4           3
  3 1 2                                  7 3 1 8
  4 1 4                                  3 3 4 4
  2 2 2
"""

n, k = map(int, input().split(' '))
number = []

for i in range(n):
    number.append(input().split(' '))
# 해당 for문을 통해서 number는 list를 인자로 가지는 list 구조가 되었다. (행과 열을 가진 바둑판과 같은 형태)

count = [] # row(행)들을 돌면서 가장 작은 수들을 넣어 줄 새 list 생성

for row in number:  # row를 순회
    row.sort()
    count.append(row[0])

count.sort(reverse=True)    # 큰 수가 index 0로 위치하도록 정렬
print(count[0])