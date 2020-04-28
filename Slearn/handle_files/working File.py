#É uma boa prática evitar o desperdício de recursos, certificando-se de que os arquivos estejam
# sempre fechados depois de serem usados. Uma maneira de fazer isso é usar try e finally.
try:
    file = open("textos", "r")
    print(file.read())
finally:
    file.close()

#Uma maneira alternativa de fazer isso é usando instruções WITH. Isso cria uma variável temporária
#que só é acessível no bloco recuado da instrução with.

with open("textos.txt","r") as f:
    print(f.read())

#O arquivo é fechado automaticamente no final da instrução with, mesmo que ocorram exceções.
