"""
다형성(Pylymorphism)
"""
class Korean():
    def greeting(self):
        print("안녕하세요.")

class American():
    def greeting(self):
        print("Hello")

def sayhello(people):
    people.greeting()


kim = Korean()
john = American()
sayhello(kim)
sayhello(john)

