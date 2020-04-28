import os

# apaga uma arquivo : os.remove(aqruivo)
def delete_file(name):
    file = str(name)
    try:
        if os.path.exists(file):
            os.remove(file)
            print("Deletado!")
        else:
            print("Arquivo não existe")
    except Exception as e:
        print(e.args)
