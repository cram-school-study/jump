i = 0

f = open("d:\\2dan.txt", "w")

while i < 9:
    i = i + 1
    print("2 x", i, "=", 2*i)
    j = 2*1
##    data = "%d\n" % j
    data = "2 x %d = %d\n" % (i,j)
    f.write(data)

f.close()
