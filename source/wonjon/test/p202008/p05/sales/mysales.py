class Mysales:
    def __init__(self, source):
        self.source = "a,1"
        self.sale_list = []
        self.transform_data()

    def transform_data(self):

        with open(self.source, 'r', encoding='utf-8') as f:
            line1 = f.readlines()
            line2 = f.readlines()
            print(line2)

            temp_list = line2.split(",")
            for i in range(int(len(temp_list)/2)):
                self.sale_list.append( temp_list[i*2], temp_list[i*2-1] )

