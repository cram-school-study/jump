string = "a,4,b,6,d,8,a,8,b,4,c,7,g,9,h,1,a,6,b,3,h,5"
##string = "a,1,b,2"

count_number_string = 0

temp_string=""
temp_number=""

str = ""
for i in string :
    if count_number_string % 2 == 0:
        temp_string = temp_string + i
    if count_number_string % 2 == 1:
        temp_number = temp_number + i

    if i == ",":
        if count_number_string % 2 == 0:
            temp_string = temp_string
        if count_number_string % 2 == 1:
            temp_number = temp_number

        count_number_string = count_number_string + 1

temp_c = temp_string.count(",")
##11
count = 0
result = ""

'''
for i in temp_string :
    if count == temp_string.find(",") :
        ## 1
        result = result + temp_string[]

    count = count + 1
'''