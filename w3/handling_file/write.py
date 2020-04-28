def in_file(fl, bfr=""):
    try:
        # cria o arquivo e ecreve nele
        f = open(str(fl), "a")
        f.write(f" \n {str(bfr)}")
        f.close()

        # abri o arquivo em mode leitura
        f = open(fl, "r")
        print(f.read())
    except Exception as e:
        print(e)
    finally:
        f.close()

def overwrite_in_file(nm, over=""):
    file = str(nm)
    ovr = str(over)
    try:
        p = open(file, "w")
        p.write(ovr)
        p.close()

        p = open(file, "r")
        print(p.read())
    except Exception as e:
        print(e)
    finally:
        p.close()
