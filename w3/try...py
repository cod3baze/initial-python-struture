try:
    x = 0
    print(x)
except Exception as e:
    print(f"ocorreu {e}", end="\n\n\n")

#---------------------------------------------
try:
    print("ello")
except:
    print("ocorreu um erro!")
else:
    print("nao houve erro!", end="\n\n\n")

#---------------------------------------------
try:
    print(ola)
except NameError:
    print("erro de nome", end="\n\n\n")
except:
    print("algo deu errado!", end="\n\n\n")

#---------------------------------------------
try:
    print(olla)
except Exception as e:
    print(e)
finally:
    print("fim da sentença Try..!", end="\n\n\n")