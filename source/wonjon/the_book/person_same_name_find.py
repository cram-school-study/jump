person_list = ["Tom", "Jerry", "Mike", "Tom"]
person_not_same_name = set(person_list)
person_same_name = set()




if len(person_list) != len(person_not_same_name):
    for i in person_not_same_name:
        count = 0
        for j in person_list:
            if j == i:
                count = count + 1

            if count == 2:
                person_same_name.add(j)
                count = 0

print(person_same_name)