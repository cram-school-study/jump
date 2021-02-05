f = open("d://mession 2.txt","w")
a = ""

for i in [1,2,3,4,5,6,7,8,9] :
    for j in [2,3,4] :
        if j*i < 10 :
            a = a + "%d * %d = %d\t\t" % (j,i,j*i)
        if j*i >= 10 :
            a = a + "%d * %d = %d\t" % (j, i, j * i)
    f.write(a+"\n")
    a = ""

f.write("\n")

for i in [1,2,3,4,5,6,7,8,9] :
    for j in [5,6,7] :
        if j*i < 10 :
            a = a + "%d * %d = %d\t\t" % (j,i,j*i)
        if j*i >= 10 :
            a = a + "%d * %d = %d\t" % (j, i, j * i)
    f.write(a+"\n")
    a = ""

f.write("\n")

for i in [1,2,3,4,5,6,7,8,9] :
    for j in [8,9] :
        if j*i < 10 :
            a = a + "%d * %d = %d\t\t" % (j,i,j*i)
        if j*i >= 10 :
            a = a + "%d * %d = %d\t" % (j, i, j * i)
    f.write(a+"\n")
    a = ""

f.write("\n")

f.close()