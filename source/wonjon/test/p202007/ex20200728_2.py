source = "a,1,b,1,c,1,a,1,d,1,f,1,c,1"
# data = [['a',1],['b',1],['c',1],['a',1],['d',1],['f',1],[c,1]]

temp = source.split(',')
# temp = ['a','1','b','1'...,'c','1']

data = []

for i in range(len(temp)):
    if i % 2 == 1:
        data.append([temp[i-1], int(temp[i])])
# 인덱스 번호를 i에 담는다,
print("data2 넣기 전")
print("data = ", data)

data2 = []

for j in range(len(data)):
    # 중복여부를 확인하고
    is_dupl = False
    no_dupl = None
    # 중복되는 인덱스 번호를 알아야 한다.
    for k in range(len(data2)):
        if data2[k][0] == data[j][0]:
            is_dupl = True
            no_dupl = k
    if is_dupl:
        sum = data2[no_dupl][1] + data[j][1]
        data2[no_dupl][1] = sum
        #data2[no_dupl] = [data2[no_dupl][0],sum]
        #바뀌는 부분만 주소값 새로 설정
    else:
        data2.append(data[j])
        #data2 = data2 + [[data[j][0],data[j][1]]]
        #새로 추가할때마다 주소값 새로 설정

print("\ndata2에 넣은 후")
print("data = ", data)
print("data2 = ", data2)

print("\ndata 비운 후")
data = []
print("data = ", data)
print("data2 = ", data2)