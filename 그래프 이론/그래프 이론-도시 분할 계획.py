'''
마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있는 편리한 길이다.
그리고 길마다 길을 유지하는데 드는 유지비가 있따.
마을의 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다. 마을이 너무 커서 혼자서는 관리할 수 없기 때문이다.
마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다. 각 분리된 마을 안에 있는 임의의 두 집 사이에
경로가 항상 존재해야 한다는 뜻이다. 마을에는 집이 하나 이상 있어야 한다.
그렇게 마을의 이장은 계획을 세우다가 마을 안에 길이 너무 많다는 생각을 하게 되었다. 일단 분리된 두 마을 사이에 있는 길들은
필요가 없으므로 없앨 수 있다. 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨
수 있다. 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.
이것을 구하는 프로그램을 작성하시오.
'''
# 힌트 : 2개의 최소 신장 트리 구현. 최소 신장 트리를 찾은 뒤에 최소 신장 트리를 구성
# 하는 간선 중에서 가장 비용이 큰 간선을 제거하는 것이다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [[0] for i in range(N+1)]
for i in range(N+1): #  처음에는 자기 자신을 자식으로 가지는 부모 리스트 생성
    parent[i] = i

lines = []   # 간선에 대한 정보를 담을 리스트
result = 0  # 유지비를 담을 변수

for _ in range(M):
    a, b, cost = map(int, input().split())
    lines.append([cost, a, b])   # cost를 오름차순으로 정렬하기 위해서 첫번째 원소를 cost로 지정

lines.sort()
last = 0 # 마지막에 가장 큰 cost를 저장할 변수

for line in lines:
    cost, a, b = line
    if find_parent(parent, a) != find_parent(parent, b):    # 같은 부모를 가지지 않는다는 것은 사이클이 안된다는 것
        union_parent(parent, a, b)
        result += cost
        last = cost # 가장 마지막에 남는 cost가 가장 큰 유지비가 드는 간선

print(result - last)    # N개 노드가 있으면 신장 트리의 간선 N-1 여기서 -1이 가장 큰 cost
