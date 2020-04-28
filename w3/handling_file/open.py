try:
 f = open("demofile.txt")
 print(f.read())
 print(f.readline())
 print(f.read(5))
except Exception as e:
    print(e.args)
finally:
    f.close()

print("\n\n\n\n")

try:
    p = open("demofile.txt", "r")
    for x in p:
        print(x)
except Exception as e:
    print(e)
finally:
    p.close()