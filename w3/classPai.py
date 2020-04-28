class Pessoa:
    def __init__(self, fn, ln):
        self.fname = fn
        self.lname = ln

    def printName(self):
        print(self.fname, self.lname)

#                        HERANÇA

# A classe Student herdou as funcoes da classe Pessoa ->(Classe pai)
class Student(Pessoa):
    def __init__(self, fn, ln, year):
        Pessoa.__init__(self, fn, ln)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class", self.graduationyear)



p1 = Student("elias", "alexandre", 2019)
p1.printName()
print(p1.graduationyear)
p1.welcome()