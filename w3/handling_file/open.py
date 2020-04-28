
def read_file(file):
    name = str(file)
    try:
     f = open(name)
     print(f.read())
     print(f.readline())
     print(f.read(5))
    except Exception as e:
        print(e.args)
    finally:
        f.close()
        print("\n\n\n\n")

def read_file_mode(file, md):
    name = str(file)
    mode = str(md)
    try:
        p = open(name, mode)
        for x in p:
            print(x)
    except Exception as e:
        print(e)
    finally:
        p.close()
