file = open("text.txt", "w") #O modo "w" criará um arquivo, se ainda não existir.
file.write("nova linha")
file.close()

file = open("text.txt", "r")
print(file.read())
file.close()