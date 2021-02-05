data = "apple,1,banana,2,apple,4,kiwi,4,apple,6,banana,3123,fgsdffsdfsd,31231,dr,6,a,5,c,7"
split_data = data.split(",")
index = 0 # split_data i 값 변수
t_f = 0 # 상품 중복 물품시 구분 True, False 여부 변수
old_str = "" # 상품 중복 물품 이름 임시 저장 변수
name = []
sums = []


for a in split_data:
    if index % 2 == 0:
        old_str = a
        if name.count(a) == 0:
            name.append(a)
        elif not name.count(a) == 0:
            t_f = 1

    elif index % 2 == 1:
        index_index = 0

        if t_f == 0:
            sums.append(a)
        elif not t_f == 0:
            for b in name :
                if b == old_str :
                    if t_f == 1:
                        sums[index_index] = int(sums[index_index]) + int(a)
                index_index = index_index + 1

        t_f = 0
    index = index + 1

print(name)
print(sums)

