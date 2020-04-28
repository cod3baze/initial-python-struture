"""
As asserções são simplesmente expressões booleanas que verificam se as condições
retornam true ou false. Se for verdade, o programa não faz nada e passa para a próxima
linha de código. No entanto, se for falso, o programa pára e gera um erro.
"""
def avg(marks):
    assert len(marks) != 0, "List is empty."
    return sum(marks) / len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:", avg(mark2))
