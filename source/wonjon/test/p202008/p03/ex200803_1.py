myfriends = {'a':'가,나','b':'다,라,마','c':'가,다,바'}

# myfriends -> 총 values 목록 만들기
# 각 values 마다 key의 목록 만들기

text = ""
my_friend_set = set()

for i in myfriends.values():
    my_list = i.split(",")
    my_set = set(my_list)
    my_friend_set = my_friend_set | my_set

for k in my_friend_set:
    temp = ""
    for j in myfriends.keys():
        if k in myfriends[j]:
            temp = temp + ',' + j
    text = text + "{} = {}\n".format(k, temp)

print(text)
