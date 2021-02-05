from .frult import Frult


class File():
    def __init__(self, file_name):
        file_name_split = file_name.split("_")
        self.shop_name = file_name_split[0]
        self.day = file_name_split[1]
        self.frults = []
        self.frult_count_read()

    def frult_count_read(self):
        with open("txt/{0}_{1}_1.txt".format(self.shop_name, self.day), 'r', encoding='utf-8') as f:
            line1 = f.readline()
            line2 = f.readline()
        frult_list_split = line2.split(",")

        for i in range(int(len(frult_list_split)/2)):
            self.frults.append( Frult(frult_list_split[i*2], int(frult_list_split[i*2+1])) )
