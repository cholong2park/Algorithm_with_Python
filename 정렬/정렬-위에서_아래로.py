"""
- 입력조건
    - 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1 <= N <= 500)
    - 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1이상 100,000 이하의 자연수이다.
- 출력조건
    - 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는
    자유롭게 출력해도 괜찮다.
"""
num = int(input())
num_list = [0]*num

for i in range(num):
    num_list[i] = int(input())

for i in range(num-1, 0, -1):
    for j in range(0, i): 
        if num_list[j] < num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

print(*num_list)