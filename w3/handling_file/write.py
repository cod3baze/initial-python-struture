try:
    #cria o arquivo e ecreve nele
    f = open("demofile2.txt", "a")
    f.write(" \n Now the file has more content!")
    f.close()

    #abri o areuivo em mode leitura
    f = open("demofile2.txt", "r")
    print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

try:
    p = open("demofile3.txt", "w")
    p.write("ops. apeguei o conteudo que estava aqui!")
    p.close()

    p = open("demofile3.txt", "r")
    print(p.read())
except Exception as e:
    print(e)
finally:
    p.close()