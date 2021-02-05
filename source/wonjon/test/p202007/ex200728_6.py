# input "a,1,b,2,a,3"
from builtins import map

data = []
data2 = []

sales = "a,1,b,2,a,3"
sales2 = "d,4,g,5,j,7,b,5"

# list = ['a',1,'b',2,'a',3]
def make_frult_list(sales_string):
    list = sales_string.split(",")
    print(list)
    print("="*30)
    return list

# data = [['a',1],['b',2],['a',3]]
def make_frult_2list(sales_split_list):
    data = []
    length = len(sales_split_list)
    for i in range(length):
        # [[]]
        if i % 2 == 1:
            # print(i)
            data.append([sales_split_list[i-1],int(sales_split_list[i])])
    print(data)
    print("="*30)
    return data

# data2 = [['a',1],['b',2]]
def frult_list_distinct_plus(data):
    for j in data:
        is_dupl = False
        no_dupl = None
        for k in range(len(data2)):
            if data2[k][0] == j[0]:
                is_dupl = True
                no_dupl = k
        if is_dupl:
            data2[no_dupl][1] = j[1] + data2[no_dupl][1]
        else:
            data2.append(j)
    print(data2)
    print("="*30)
    return data2


frult_list_distinct_plus(make_frult_2list(make_frult_list(sales)))
frult_list_distinct_plus(make_frult_2list(make_frult_list(sales2)))

