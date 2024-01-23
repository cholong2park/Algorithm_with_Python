"""
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""

n = int(input())
k = list(input().split())   # 내가 가지고 있는 동전의 종류

count = 0   # 몇 개의 동전이 필요한지 횟수 저장할 변수

for i in k:
    count += n // int(i)
    n %= int(i)

print(count)