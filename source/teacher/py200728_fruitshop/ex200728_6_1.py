# str = 'a,1,b,1,a,1'
# temp = ['a','1','b','1','a','1']
# list = [['a','1'],['b','1'],['a','1']]


def transform_data(param):
    list = []
    temp = param.split(",")
    # temp = ['a','1','b','1','a','1']
    # len(temp)/2 ==> 3.0
    # int(len(temp)/2) ==> 3
    # range(int(len(temp)/2))
    # for i in temp:
    for i in range(int(len(temp) / 2)):
        # ['a',int('1')] => ['a',1]
        list.append([temp[i * 2], int(temp[i * 2 + 1])])
    return list


if __name__ == "__main__":
    str = 'a,1,b,1,a,1'
    list = transform_data(str)
    print(list)
