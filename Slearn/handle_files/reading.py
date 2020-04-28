file = open("textos.txt", "r")
cont = file.read()
print(len(cont), "Bytes")
file.close()
