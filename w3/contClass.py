class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = str(nome)
        self.idade = int(idade)
        self.sexo = str(sexo)

    def getName(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getSexo(self):
        return self.sexo

    def setNome(self, n):
        self.nome = n

    def setIdade(self, i):
        self.idade = i

    def setSexo(self, s):
        self.sexo = s

    def system(self):
        print(f"ola, {self.getName()}")


p1 = Pessoa("elias", 18, "masc")

print(p1.getIdade())
p1.system()
p1.nome = "outr0"
p1.system()


#p2 = Pessoa()
#p2.setNome("alexandre")
#p2.setIdade(20)
#p2.setSexo("masculino!")
#print(p2.getIdade())

