class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print(f"ello, my name is {self.name} !")

p1 = Person("elias", 20)
print(p1.age)

