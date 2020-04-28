#Você pode usar o Python para ler e gravar o conteúdo dos arquivos.
#Arquivos de texto são os mais fáceis de manipular.
#r = leitura; w = mode de escrever; r+ = leitura e gravação!
myFile = open("textos.txt", "r")
print(myFile)
#Uma vez que um arquivo tenha sido aberto e usado, você deve fechá-lo.
myFile.close()

