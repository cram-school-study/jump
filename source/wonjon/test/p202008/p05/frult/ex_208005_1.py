import os

if __name__ == "__main__":
    sales = []
    data2 = []

    with os.scandir('') as entries:
        for entry in entries:
            print(entry.name)

            with open("frult/{0}".format(entry.name), 'r', encoding='utf-8') as f:
                line1 = f.readline()
                line2 = f.readline()
                sales.append(line2)

    for sale in sales:
        split_sale = sale.split(",")
        data = []

        for i in range(int(len(split_sale)/2)):
            data.append([split_sale[i*2], int(split_sale[i*2+1])])

for i in data:

    for j in range(len(data2)):
        if data2[j][0] == i[0]:
            data2[j][1] = data2[j][1] + i[1]
        else :
            data2.append(i)



