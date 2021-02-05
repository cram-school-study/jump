# 버전 1
'''
if __name__ == "__main__":
    input_Point = input("지점명을 입력하시오\n")

    with open(input_Point + ".txt", "w", encoding="utf-8") as f:
        while True:
            input_frult = input("과일명을 입력하시오\n")
            input_conut = input("갯수를 입력하시오\n")

            f.write(input_frult + "," + input_conut + ",")

            input_next = input("추가할 과일이 있나요? (Y/N)\n")
            if input_next == "N":
                break
'''

# 해당 버전을 연/월/일 폴더로 나누어져 저장하며,
# 지점명_1 등으로 파일명으로 지점을 구분하며,
# 같은날 1번째 파일일 경우 _1, 2번째 파일일 경우 _2로 저장함.
# 해당 데이터는 판매데이터이고 예시적으로 명시하는것이라 데이터는 처음에 입력값으로 받음.
# 데이터 예 ) aaa_1.txt -> a,3,b,4
# 버전 2
import datetime, os

# 디렉토리에 연,월,일 폴더 있는지 여부 확인
# 깊이와 경로를 파라미터로 받음 ( ex) 깊이 1 = 연, 깊이 2 = 월, 깊이 3 = 일 )
# 해당 디렉토리가 없으면 추가
def dir_Flag(level, path):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    if level == 0: dir = str(year)
    elif level == 1: dir = str(month)
    elif level == 2: dir = str(day)

    path = path + "\\" + dir

# 해당 디렉토리가 없으면 폴더 추가
    if os.path.isdir(path) is not True:
        os.makedirs(path)
# 경로와 깊이 반환
    return path, level + 1

if __name__ == "__main__":
# 최초 실행시 확인도 안했으므로 깊이 0부터 차례대로 확인을 위하여 깊이 0
    level = 0
    path = "D:\jeongwj\PycharmProjects\jump\source\wonjon\\test\p202008\p17"
    file_flag = False

# 입력 받아야 하는 값은 따로 분리
    point = "buchon"
    str_line = "a,3,b,6,c,7,d,3,a,5"

# 연, 월, 일 깊이 3으로 있는지 여부 확인 없으면 디렉토리 폴더 생성
    while level < 3:
        path, level = dir_Flag(level, path)

# 디렉토리 폴더는 다 완성되었으므로, 해당 경로에 지점 및 번호 있는지 여부 확인
    with os.scandir(path) as entries :
        count = 0
        for entry in entries:
            filename = entry.name
            filename_split = filename.split('_')
# 해당 지점명으로 된 폴더가 있으면 파일을 일단 만들어야하므로 해당 flag값 변경
            if filename_split[0] == point:
                file_flag = True

# 지점명이 들어가 있는 파일이 있을경우 해당 번호+1 값으로 파일 생성
    if file_flag is True:
        with open(path + '\\' + point + '_' + str(int(filename_split[1]) + 1), 'w', encoding='utf-8') as f:
            f.write(str_line)
# 지점명이 들어가 있는 파일이 없을경우 해당 번호를 0으로 해서 파일 생성
    else:
        with open(path + '\\' + point + '_0', 'w', encoding='utf-8') as f:
            f.write(str_line)
















