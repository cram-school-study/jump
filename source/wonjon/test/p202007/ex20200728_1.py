source = "1,2,3,4"
#chk_dupl라는 파라미터 2개(문자열,체크 해야할 숫자)가 들어가는 함수를 만들고, 문자열에 체크해야할 숫자가 있는지 여부를 True, False 반환

def chk_dupl(source , chk_num):
    split_sorce = source
    for i in split_sorce:
        if int(i) == chk_num:
            return True
        else:
            return False


result = chk_dupl(source, 7)
print(result)

result = chk_dupl(source, 1)
print(result)