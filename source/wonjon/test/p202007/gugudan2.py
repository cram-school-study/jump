'''
i = 0
data = ""

f = open("d://2dan1.txt","w")

while i < 9 :
    i = i + 1
    print("2 x %d = %d" % (i,i*2))
    data = "%s2 x %d = %d\n" % (data,i,i*2)


f.write(data)
f.close()
구구단 2단 출력
'''

'''
i = 0
j = 0
data = ""

f = open("d://gugudan1.txt","w")

while i < 9 :
    i = i + 1
    j = 0
    while j < 9 :
        j = j + 1
        print("%d x %d = %d" % (i,j,i*j))
        data = "%s%d x %d = %d\n" % (data,i,j,i*j)

f.write(data)
f.close()

구구단 1~9단 출력(while문)
'''

list1 = [0,1,2,3,4,5,6,7,8]
list2 = [0,1,2,3,4,5,6,7,8]
data = ""

f = open("d://gugudan2.txt","w")

for i in list1 :
    i = i + 1
    j = 0
    for j in list2 :
        j = j + 1
        print("%d x %d = %d" % (i,j,i*j))
        data = "%s%d x %d = %d\n" % (data,i,j,i*j)

f.write(data)
f.close()

