import os

def txt_2line_read(path):
    with open(path, "r", encoding = "utf-8" ) as f:
        line1 = f.readline()
        line2 = f.readline()
    return line2



if __name__ == "__main__":
    str_list = []
    result_list = []

    with os.scandir('') as files:
        for i in files:
            temp_str = txt_2line_read(i.path).split(",")

            for j in range(int(len(temp_str)/2)):
                str_list.append( [temp_str[j*2], int(temp_str[j*2+1])] )

    for k in str_list:
        flag = False
        result_idx = None

        for n in range(len(result_list)):
            if result_list[n][0] == k[0]:
                flag = True
                result_idx = n

        if flag :
            result_list[result_idx][1] = result_list[result_idx][1] + k[1]
        else :
            result_list.append(k)

print(result_list)
