import os

# apaga uma arquivo : os.remove(aqruivo)
#verficar primeiro se ele existe
try:
    if os.path.exists("demofile3.txt"):
        os.remove("demofile3.txt")
        print("Feito")
    else:
        print("arquivo não existe")
except Exception as e:
    print(e)