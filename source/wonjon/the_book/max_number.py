# 1.문자열로 있을경우 -> numbers 부터 시작
numbers = "17,92,18,33,58,7,33,42"
split_number_list = numbers.split(",")

# 2.리스트로 있을경우 split_number_list 부터 시작
#split_number_list = [17,92,18,33,58,7,33,42]

max_number = 0
first_number_index = 0
count = 0

for i in split_number_list:
    if first_number_index == 0:
        # 숫자가 전부 0보다 작을경우도 있을 수 있기때문에,
        # 초기화를 0으로 했어도 맨 처음값은 0과 비교가 아닌 해당값을 넣을 필요 있음
        max_number = int(i)
    elif max_number < int(i):
        max_number = int(i)
        count = first_number_index + 1

    first_number_index = first_number_index + 1

print("최댓값 = ",max_number)
print("몇번째 값 = ",count)
