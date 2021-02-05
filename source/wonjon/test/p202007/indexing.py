#a = "Life is too short, You need Python"
#print(a[3])

#count = 0
#for i in a:
#    if i == "o":
#        print(i)
#        count = count + 1
#print(count)

for i in ["20010331Rainy","179Rai354ny","21r354yn76"]:
    count = 0
    for j in i:
        if j == "R":
            print(i[:count])
            print(i[count:])
        count = count + 1

