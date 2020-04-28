#Para recuperar cada linha em um arquivo, você pode usar o método
# readlines para retornar uma lista na qual cada elemento é uma linha no arquivo.

file = open("textos.txt", "r")
#print(file.readline())
#file.close()

# ou usando um loop FOR

for line in file:
    print(line)
file.close()