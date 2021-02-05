class Animal:
    def __init__(self):
        self.type = "동물"
    def eat(self):
        pass
    def get_type(self):
        print(self.type_Str)


class Tiger(Animal):
    def __init__(self):
        pass
    def bark(self):
        print("으르렁")


class Cat(Tiger):
    def __init__(self):
        pass
    #Tiger클래스의 bark메서드 오버라이딩
    def bark(self):
        print("야옹")


class Lion(Animal):
    def __init__(self):
        pass
    def bark(self):
        print("어흥")


animal = Animal()
animal.get_type()

tiger = Tiger()
tiger.bark()

cat = Cat()
cat.bark()

lion = Lion()
lion.bark()


class Manager():
    def __init__(self):
        self.animals = []
    def insert_animal(self, animal):
        self.animals.append(animal)
    def bark_animal(self):
        pass
