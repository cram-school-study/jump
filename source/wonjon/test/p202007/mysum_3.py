source = "a,1,b,2,c,3,a,1,d,2,c,3"
temp = source.split(",")
data = []
data2 = []

for i in range(len(temp)):
    sub_list = []
    if i%2 == 1:
        sub_list.append(temp[i-1])
        sub_list.append(int(temp[i]))
        data.append(sub_list)
'''
for i in data:
    index = False
    for j in data2:
        if j[0] == i[0]:
           j[1] = j[1] + i[1]
           index = True

    if index == False:
        data2.appen(i)
'''


for i in range(len(data)):
    is_dupl = False
    for j in range(len(data2)):
        if data2[j][0] == data[i][0]:
            sum = data2[j][1] + data[i][1]
            data2[j][1] = sum
            is_dupl = True
    if is_dupl:
        pass
    else:
        data2.append(data[i])

data = []

print(data)
print(data2)




