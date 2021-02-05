'''
1. str1, str2등 문자열의 형태로 목록을 1개가 아닌 여러개를 받을 수 있다.
2. 받는 값을 결과적으로 list 2차 형태로 표현한다. 중복시 한군데로 더하여 통합 ex) [[a,1],[b,2]]
3. 함수안의 함수를 만들어 표시해본다.
4. if조건문으로 메인을 불러본다. -안해봤으니
'''

str = "a,1,b,2,c,3,d,4,e,5,a,1"
str1 = "a,6,g,9,c,2"

def make_split_list(str):
    list = []
    list2 = []
    list = str.split(",")
    for i in range(int(len(list)/2)):
        list2.append([list[i*2],list[i*2+1]])
    return list2

def distinct_chk(chk_list_1, insert_list):
    falg = False
    chk_number = None
    for j in range(len(result_list)):
        if result_list[j][0] == chk_list_1[0][0]:
            falg = True
            chk_number = j
    return falg, chk_number



if __name__ == "__main__":
    split_list = []
    split_list = make_split_list(str)

    result_list = []
    for i in split_list:
        distinct_falg = False
        chk_idx = None

        distinct_falg, chk_idx = distinct_chk(i, result_list)

        if distinct_falg == True:
            result_list[chk_idx][1] = result_list[chk_idx][1] + i[1]
        else: result_list.append(i)

print(result_list)



