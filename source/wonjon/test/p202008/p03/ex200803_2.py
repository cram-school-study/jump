myfriends = {'a':'가,나','b':'다,라,마','c':'가,다,바'}

# myfriends -> 총 values 목록 만들기
# {가,나,다,라,마,바}
# 각 values 마다 key의 목록 만들기
# {가 : a,c}, {나 : a}...

main_set = set()

for i in myfriends.values():
    str_list = i.split(",")
    main_set = main_set.union(set(str_list))

print(main_set)
