"""
str() 메소드는 객체의 클래스 이름과 객체의 메모리 주소로 구성된 객체에 대한 설명을 문자열로 반환한다.
"""

class People():
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def __str__(self):
        return "info -- name " + self.__name + " age : " + str(self.__age)

'''
    def __str__(self):
        return super().__str__()
'''

p1 = People(29, "Lee")
print(p1.__str__())