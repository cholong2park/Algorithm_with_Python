"""
메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져 있다. 각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를
선택적으로 약탈하여 식량을 빼앗을 예정이다. 이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.
따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소 한 칸 이상 떨어진 식량창고를 약탈해야 한다. 예를 들어 식량창고 4개가 다음과 같이
존재한다고 가정하자.
{1, 3, 1, 5}
이때 개미 전사는 두 번째 식량창고와 네 번째 식량창고를 선택했을 때 최댓값인 총 8개의 식량을 빼앗을 수 있다. 개미 전사는 식량창고가 이렇게 일직선상일 때 최대한
많은 식량을 얻기를 원한다.
개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.
- 입력 조건
    - 첫째 줄에 식량창고의 개수 N이 주어진다. (3 <= N <= 100)
    - 둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다. (0 <=  K <= 1000)
- 출력 조건
    - 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.
"""
"""
앞의 2개를 선택하면 뒤의 수는 정해질 수 있다.
i=0 max(arr[0]+arr[2], arr[0]+arr[3])
i=1 max(arr[1]+arr[3], arr[1]+arr[4])
i=2 max(arr[2]+arr[4], arr[2]+arr[5])
i=3 max(arr[3]+arr[5], arr[3]+arr[6])
......
i=n-2 max(arr[n-2]+arr[n], arr[n]+arr[n+3])
i=n-1 max(arr[n-1]+arr[n+1], arr[n-1]+arr[n+2])
i=n max(arr[n]+arr[n+2], arr[n]+arr[n+3])
"""
def max_num(arr, i, N):
    if len(arr[i:N]) == 1:
        arr1 = arr[i:N]
        return arr1[0]
    elif len(arr[i:N]) == 2:
        arr2 = arr[i:N]
        return max(arr2[0], arr2[1])
    elif len(arr[i:N]) == 3:
        arr3 = arr[i:N]
        return max(arr3[0]+arr3[2], arr3[1])
    else:
        return max(arr[i]+max_num(arr, i+2, N), arr[i]+max_num(arr, i+3, N))
    
N = int(input())
arr = list(map(int, input().split()))
if max_num(arr, 0, N) < max_num(arr, 1, N):
    print(max_num(arr, 1, N))
else:
    print(max_num(arr, 0, N))