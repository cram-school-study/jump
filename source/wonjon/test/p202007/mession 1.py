from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

result = ["","","","",""]
j = 0

f = open("d://mession 1.txt","w")

def drawing(number) :
    if number == 0 :
        number0()
    if number == 1 :
        number1()
    if number == 2 :
        number2()
    if number == 3 :
        number3()
    if number == 4 :
        number4()
    if number == 5 :
        number5()
    if number == 6 :
        number6()
    if number == 7 :
        number7()
    if number == 8 :
        number8()
    if number == 9 :
        number9()
    if number == "/" :
        number10()

def number0() :
    list0 = ["*****","*   *","*   *","*   *","*****"]
    for i in list0 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        #i = i + "\n"
        #f.write(i)
    j = 0
def number1() :
    list1 = ["  *  ","  *  ","  *  ","  *  ","  *  "]
    for i in list1 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number2() :
    list2 = ["*****","    *","*****","*    ","*****"]
    for i in list2 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number3() :
    list3 = ["*****","    *","*****","    *","*****"]
    for i in list3 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number4() :
    list4 = ["  *  "," **  ","*****","  *  ","  *  "]
    for i in list4 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number5() :
    list5 = ["*****","*    ","*****","    *","*****"]
    for i in list5 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number6() :
    list6 = ["*****","*    ","*****","*   *","*****"]
    for i in list6 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number7() :
    list7 = ["*****","*   *","*   *","    *","    *"]
    for i in list7 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number8() :
    list8 = ["*****","*   *","*****","*   *","*****"]
    for i in list8 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number9() :
    list9 = ["*****","*   *","*****","    *","    *"]
    for i in list9 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
        # i = i + "\n"
        # f.write(i)
    j = 0
def number10() :
    list10 = ["    *","   * ","  *  "," *    ","*    "]
    for i in list10 :
        global result,j
        result[j] = result[j] + i + "\t"
        j = j + 1
    j = 0


drawing(year//1000)
drawing(year%1000//100)
drawing(year%100//10)
drawing(year%10//1)

drawing("/")

drawing(int(month%100/10))
drawing(month%10//1)

drawing("/")

drawing(int(day%100/10))
drawing(day%10)

drawing("/")

drawing(int(hour%100/10))
drawing(hour%10)

drawing("/")

drawing(int(minute%100/10))
drawing(minute%10)

f.write(result[0] + "\n")
f.write(result[1] + "\n")
f.write(result[2] + "\n")
f.write(result[3] + "\n")
f.write(result[4] + "\n")
f.close();

