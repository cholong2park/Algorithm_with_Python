"""
학교에서 학새들에게 0번부터 N번까지의 번호를 부여했다. 처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N+1개의 팀이 존재한다.
이때 선생님은 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있다.

    1. '팀 합치기' 연산은 두 팀을 합치는 연산이다.
    2. '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.

선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.
"""
N, M = map(int, input().split())

num_list = [[] for _ in range(N+1)]

for _ in range(M):
    yeonsan, a, b = map(int, input().split())

    if yeonsan == 0:
        num_list[a].append(b)
        num_list[b].append(a)
    
    if yeonsan == 1:
        if b in num_list[a]:
            print('YES')
        else:
            print('NO')