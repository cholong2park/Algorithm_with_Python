"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
    - 00시 00분 03초
    - 00시 13분 30초
반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다.
    - 00시 02분 55초
    - 01시 27분 45초

입력 조건:
    - 첫째 줄에 정수 N이 입력된다. (0 <= N <= 23)
출력 조건:
    - 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.
"""
N = int(input()) # N을 입력받았다.

Time = []
Time_hour = []
Time_minute = []
Time_second = []

for hour in range(N + 1):
    Time_hour.append(hour) # [0, 1, 2, .. N]라는 '시'의 list 완성
Time.append(Time_hour)  # Time이라는 큰 list에 삽입
for minute in range(60):
    Time_minute.append(minute)  # [0, 1, 2, 3, ..... 57, 58, 59]라는 '분'의 list 완성
Time.append(Time_minute)  # Time이라는 큰 list에 삽입
for second in range(60):
    Time_second.append(second)  # [0, 1, 2, 3, ..... 57, 58, 59]라는 '분'의 list 완성
Time.append(Time_second)  # Time이라는 큰 list에 삽입

# Time은 [[시], [분], [초]]라는 구조의 리스트로 탄생함

number_in_3 = {3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53}   # 0 ~ 60 사이에 3이 들어가는 숫자들의 set

count_3 = 0 # 3이 들어갈때마다 +1이 될 변수

for hour in Time[0]:
    for minute in Time[1]:
        for second in Time[2]:  # 시, 분, 초를 순회하는 3중 for문
            if (hour in number_in_3) or (minute in number_in_3) or (second in number_in_3):
                count_3 += 1
            else:
                pass

print(count_3)