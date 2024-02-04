"""
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
- 입력 조건
    - 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
    - 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다
    작거나 같은 양의 정수 또는 0이다.
- 출력 조건
    - 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
"""
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x >= pivot]
    right_side = [x for x in tail if x < pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr = quick_sort(arr)

for num in range(arr[0], -1, -1):   # arr에서 가장 긴 길이의 떡부터 잘라가보자잇
    sum_num = 0
    for x in arr:
        if x > num:
            sum_num += (x - num)
    if sum_num == M:
        print(num)
        break