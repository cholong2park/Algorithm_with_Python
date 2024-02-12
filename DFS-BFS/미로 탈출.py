"""
# 코딩테스트를 준비하며 반드시 알아야 하는 라이브러리 6가지!
    1. 내장 함수: 기본 내장 라이브러리
    2. itertools: 순열과 조합
    3. heapq: 힙(Heap) 기능 제공, 우선순위 큐 기능 구현
    4. bisect: 이진 탐색(Binary Search) 기능 제공
    5. collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조 포함
    6. math: 필수적인 수학적 기능 제공(팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수들과 파이같은 상수 포함)

# Queue
queue 의 기본인 FIFO(First In First Out)

Queue는 멀티 태스킹을 위한 프로세스 스케줄링 방식을 구현하기 위해 많이 사용된다 (운영체제)
    - Enqueue : 큐에 데이터를 넣는 기능
    - Dequeue : 큐에서 데이터를 꺼내는 기능

queue 라이브러리에는 Queue(), LifoQueue(), PriorityQueue() 를 제공한다.
    - Queue() : 일반적인 큐 자료구조
    - LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조 (like stack)
    - PriorityQueue() : 우선순위 큐 -> 데이터마다 우선순위를 넣어서, 우선수위가 높은 순으로 데이터 출력

# List
    >>> queue = [1, 2, 3]
    >>> queue.append(4)
    >>> queue.append(5)
    >>> print(queue)
    [1, 2, 3, 4, 5]
    >>> queue.pop(0)
    1
    >>> queue.pop(0)
    2
    >>> print(queue)
    [3, 4, 5]
list 자료 구조의 .append(n) 함수를 사용하면 뒤에 데이터를 추가 할 수 있고, .pop(0) 함수를 이용하면 맨 앞의 데이터를 제거할 수 있기 때문에 
큐 자료구조를 사용하는 효과가 난다. 그러나 성능적으로 문제가 있는데, 파이썬의 list 자료 구조는 무작위 접근에 최적화된 자료 구조이기 때문이다.
pop(0) 연산의 시간 복잡도는 O(N) 이어서 N이 커질 수록 연산이 매우 느려진다. 그래서 큐 자료구조를 사용하려고 한다면 list 자료 구조는 별로이다.

# deque
double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료구조이다.
popleft() 라는 메서드를 사용하면 list의 pop(0) 메서드와 같은 효과를 가진다!
    >>> from collections import deque
    >>> queue = deque([1, 2, 3])
    >>> queue.append(4)
    >>> queue
    deque[1, 2, 3, 4]
    >>> queue.popleft()
    1
    >>> queue.popleft()
    2
    >>> queue
    deque[3, 4]
deque는 Queue와 다르게 appendleft(x) 라는 메서드가 있는데, 이 메서드를 사용하면 데이터를 맨 앞에서 삽입할수 있다고 한다.
deque의 popleft()와 appendleft(x) 메서드는 모두 O(1)의 시간 복잡도를 가지기 때문에, list 자료 구조보다 성능이 훨씬 뛰어나다
그러나 단점도 있는데, 무작위 접근의 시간 복잡도가 O(N)이고, 내부적으로 linked list를 사용하고 있기 때문에 N번째 데이터에 접근하려면 N번 순회가 필요하다.

# Queue
deque와 달리 방향성이 없기 때문에 데이터 추가와 삭제가 하나의 메서드로 처리된다!
데이터를 추가 할 때 : put(x) 메서드를 사용
데이터 삭제 : get() 메서드 사용
    >>> from queue import Queue
    >>> que = Queue()
    >>> que.put(1)
    >>> que.put(2)
    >>> que.put(3)
    >>> que.get()
    1
    >>> que.get()
    2
    Queue의 성능은 deque와 똑같다. 데이터 추가/삭제는 O(1), 데이터 접근은 O(N)의 시간 복잡도를 가진다.
"""
from collections import deque

def bfs(row, colum):
    d_row = [-1, 1, 0, 0]
    d_colum = [0, 0, -1, 1]
    queue = deque() # deque를 사용하여 queue 구현
    queue.append((row, colum))
    while queue:    # queue가 들어있으면 True, 비어있으면 False
        row, colum = queue.popleft()
        for i in range(4):
            n_row = row + d_row[i]
            n_colum = colum + d_colum[i]
            if n_row < 0 or n_row >= N or n_colum < 0 or n_colum >= M:  # 미로를 벗어나면 다시 진행
                continue
            if miro_map[n_row][n_colum] == 0:   # 벽에 도달해도 그냥 진행
                continue
            if miro_map[n_row][n_colum] == 1:
                miro_map[n_row][n_colum] = miro_map[row][colum] + 1
                queue.append((n_row, n_colum))
    return miro_map[N-1][M-1]

N, M = map(int, input().split())
miro_map = [list(map(int, input())) for _ in range(N)]

print(bfs(0, 0))