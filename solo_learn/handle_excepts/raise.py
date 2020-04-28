# pode gerar exceções usando a instrução raise.


print("Oi")
raise ValueError("Lançando um Érro!")
print("foi")

#---

try:
    print("ola, mundo!" + (10 / 0))
except ZeroDivisionError:
    raise ValueError


#Exceções podem ser levantadas com argumentos que fornecem detalhes sobre elas.
name = ("123")
raise NameError("nome inválido!")

# Em exceto blocos, a instrução raise pode ser usada sem argumentos para ressaltar
# qualquer exceção ocorrida
try:
    print(5 / 0)
except:
    print("Ocorreu um erro!")
    raise
