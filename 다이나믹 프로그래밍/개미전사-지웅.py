# 8-3 전투개미
# [900, 1, 500, 1000, 499]같은 경우 1,4를 택해야 최선인데, 이러한 내용이 반영되도록 식을 짜보자
# case1 : 0번째 터는 경우, case2 : 1번째 터는 경우로 시작
# 터는 창고와 터는 창고 사이 털지 않는 창고의 수는 1, 2

N = 5 # 3이상 100이하
K = [900, 1, 500, 1000, 499] # 0이상1000이하

accum_list = [0]*100 # 창고 수만큼 리스트 생성
accum_list[0] = K[0] # 첫 창고(index = 0)만 털었을 경우
accum_list[1] = K[1] # 두번째 창고(index = 1)만 털었을 경우
accum_list[2] = K[0] + K[2] # 세번째 창고를 터는 경우 (index 0, 2)

for i in range(3,100): # 네번째 창고 (index = 3)부터 max를 사용하여 최대값들을 누적시켜야함
    accum_list[i] = max([(accum_list[i-2] + K[i]), accum_list[i-3] + K[i]])
    if i == N-1:
        break
    
# 이 수식 설명 (index를 기준으로 설명)
'''
3번의 창고의 경우 0번째 창고를 턴 후 보유한 식량의 양 혹은 1번째 창고를 턴 후 보유한 식량과
3번의 식량을 합한 값이 3번을 털었을 때 가지고 있을 수 있는 최대 식량 후보다.
max를 활용하여 최대값을 도출한다.

마찬가지로 5번의 경우 3번 창고를 털었을 때 보유한 식량의 양 혹은 2번 창고를 털었을 때 보유한 식량의 양과
5번의 식량을 합한 값이 가지고 있을 수 있는 최대 식량 후보다.
max를 활용하여 최대값을 도출한다.
'''

print(max(accum_list))