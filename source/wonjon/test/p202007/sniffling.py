"""
해당 문자열의 숫자들을 정렬 후
홀수일경우 가운데 값을 출력
짝수일경우 가운데 값 2개의 평균을 출력
"""

str = "1,2,3,4,5,6,7,8,9,10"

# 문자열 리스트 형태로 분리
str_list = str.split(",")
int_list = []

# 문자열 리스트 형태 -> 숫자 리스트 형태
for i in str_list:
    int_list.append(int(i))

# 숫자형 리스트 형태 오름차순 정렬
int_list.sort()

# 홀수의 경우, 가운데 값을 출력
# 짝수의 경우, 가운데 값 2개의 평균을 출력
length = len(int_list)

result = None
# 짝수
if length % 2 == 0:
    sum = int_list[int(length/2)-1] + int_list[int(length/2)]
    avg = sum / 2
    result = avg
# 홀수
elif length % 1 == 0:
    result = int_list[int(length/2)]

print(result)


