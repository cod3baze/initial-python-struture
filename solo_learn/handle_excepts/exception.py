n1 = 10
n2 = 0
try:
    print("OK")
    print(n1 / "0")
except ZeroDivisionError:
    print("não pode dividir um número por ZERO!")
except (TypeError, ValueError):
    print("Ocoreu um Erro!")
finally:
    print("feito.")

