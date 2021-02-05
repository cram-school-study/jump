import os

report_data = []

# 5.
def make_csv():
    with open("202007.csv", "w", encoding="utf-8") as f:
        for i in report_data:
            f.write("{0},{1}\n".format(i[0],i[1]))
#---------------------------------------------------------------------------------
# 4.
def check_dupl(item_list):
    # 중복여부, 인덱스
    for i in range(int(len(report_data))):
        if report_data[i][0] == item_list[0]:
            return True, i
    return False, None

# 3.
def make_report(param_list):
    for i in param_list:
        is_dupl, idx_dupl = check_dupl(i)
        if is_dupl:
            report_data[idx_dupl][1] = i[1] + report_data[idx_dupl][1]
        else:
            report_data.append(i)

# ----------------------------------------------------------------------------------
# 2.
def transform_data(file):
    with open(file, 'r', encoding='UTF-8') as f :
        line1 = f.readline()
        line2 = f.readline()

        new_list = []
        temp_list = line2.split(",")

        temp_length_half = int(len(temp_list)/2)
        for i in range(temp_length_half):
            new_list.append([temp_list[i*2],int(temp_list[i*2+1])])

        return new_list
#-------------------------------------------------------------------------------------
# 1.
def dir_list(param_string) :
    with os.scandir(param_string) as entries:
        for entry in entries:

            data_list = transform_data("{0}{1}".format(param_string,entry.name))
            #transform_data(entry.path)
            make_report(data_list)


if __name__ == "__main__":
    param_string = 'p202007/'
    dir_list(param_string)
    make_csv()
