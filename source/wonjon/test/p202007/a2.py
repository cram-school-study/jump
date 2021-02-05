i = 0

f = open("d:\\test\\a\\a3\\aaa.txt", "w")

while i < 9:
    i = i + 1
    print("2 x", i, "=", 2*i)
    j = 2*i
    data = "%d\t%d\n" % (i,j)
    f.write(data)


f.close()