number1 = 1532
number2 = 6542

number1_divisor_list = []
number2_divisor_list = []
number_same = []


# 두 수의  찾기

for i in range(1, number1+1):
    if number1 % i == 0:
        number1_divisor_list.append(i)

for i in range(1, number2+1):
    if number2 % i == 0:
        number2_divisor_list.append(i)

# 두수의 약수 중 같은것 찾기
for i in number1_divisor_list:
    for j in number2_divisor_list:
        if i == j:
            number_same.append(j)
            print(j)

# 그 값중 최대인것 찾기
number_same.sort()
print(number_same[len(number_same)-1])

