'''
money = 10
card = True

if money >= 3500 or card == True:
    print("택시를 타고가라")
elif money >=1600:
    print("버스를 타고가라")
else:
    print("걸어가라")
'''
from itertools import count

'''
a = [1,2,3]
b = 1

if b in a:
    print("T")
else:
    print("F")


if b not in a:
    print("F")
else:
    print("T")
'''

'''
coffee = 10

while True:
    money = int(input("돈을 넣어주세요"))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d 입니다." % coffee )
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''







