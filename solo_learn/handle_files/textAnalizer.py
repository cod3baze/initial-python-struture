def count_char(text, char): #conta quantas vezes um caractere ocorre em uma string.
    count = 0
    for c in text:
        if c == char:
            count +=1
    return count


try:
    file = input("Arquivo: ")
    with open(file) as f:
        text = f.read()
    print(count_char(text, "r"))
    print(f"Com espaços: {len(text)}")
    print(f"sem espaços: {len(text)}")

    for char in "abcdefghijklmnopqrstuvxwyz":
        perc = (100 * count_char(text, char)) / len(text)
        print("{0} - {1}%".format(char, round(perc, 2)))

except FileNotFoundError:
    print("Arquivo não encontrado")
except:
    print("ERRO!")
    raise