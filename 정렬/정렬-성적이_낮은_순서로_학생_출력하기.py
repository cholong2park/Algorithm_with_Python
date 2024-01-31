"""
- 입력 조건
    - 첫 번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
    - 두 번째 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
    문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.
- 출력 조건
    - 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
"""
num = int(input())
student = {}
grade_list = [0] * num
for i in range(num):
    name, grade = input().split()
    student[int(grade)] = name
    grade_list[i] += int(grade) # grade_list += student.values()
# print(student) = {'name': grade, ....}

"""
def CountingSort(diction, k):
    counts = [0] * 101  # 점수가 1부터 100까지이니 0~100까지의 빈 배열을 생성
    temp = [0] * k
    for i in diction:
        counts[diction[i]] += 1
    for i in range(101):
        counts[i] != counts[i-1]
    for i in range(100, -1, -1):
        counts[i] -= 1
        temp[counts[diction.get(i)]]
이거 카운팅정렬로 가능함? 뭔가 0~9까지를 정렬하는거 아니면 힘들어 보임.... 심지어 리스트가 아니라 딕션....?
"""   
for i in range(num-1, 0, -1):
    for j in range(0, i):
        if grade_list[j] > grade_list[j+1]:
            grade_list[j], grade_list[j+1] = grade_list[j+1], grade_list[j]

name_list = []
for i in grade_list:
    name_list += [student[i]]

print(*name_list)
