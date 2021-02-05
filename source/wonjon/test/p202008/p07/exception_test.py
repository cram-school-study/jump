'''
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
'''

a = []
for i in range(17):
    a.append("")

print(a)
print(len(a))