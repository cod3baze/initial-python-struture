#expresão regular
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#Encontra todos os caracteres minúsculos alfabeticamente entre "a" e "m" em txt
a = re.findall("[a-m]", txt)
print(a)

# Localize todos os caracteres do dígito:
tx = "that will be 59 dollars"
t = re.findall("\d" , tx)
print(t)

#Procure uma sequência que comece com "he", seguida por dois (alguns) caracteres e um "o":
st = "hello world"
ts = re.findall("he..o", st)
print(ts)

#Verifique se a string começa com 'olá':
vr = re.findall("^hello", st)
if (vr): #vr = ["hello"] == true
    print(f"sim, começa com {vr} ")
else:
    print("Nenhuma combinaçao")

#Verifique se a string termina com 'world':
rv = re.findall("world$", st)
if (rv):
    print(f"sim, termina com {rv}")
else:
    print("Nenhuma combinação")


#Check se a string contiver "ai" seguido por 0 ou mais caracteres "x":
sttr = "the rain in spain falls mainly in the plain!"
ttr = re.findall("aix*", sttr)
print(ttr)
if (ttr):
    print("sim, há pelo menos uma combinação")
else:
    print("henhuma combinação")


#Verifique se a string contém "quedas" ou "estadias":
cont = re.findall("falls|stays", sttr)
if (cont):
    print(f"sim, há pelo menos uma combinação : {cont}")
else:
    print("henhuma combinação")



#Verifique se a string contém "a" seguido por exatamente dois caracteres "l":
oc = re.findall("al{2}", sttr)
print(oc)
if (oc):
    print("sim, há pelo menos uma combinação")
else:
    print("henhuma combinação")


#Verifique se a string começa com "The":
vb = re.findall("\AThe", txt)
print(vb)
if (vb):
    print(f"sim , coemçou com {vb}")
else:
    print("errado!")


#Verifique se "ain" está presente no final de uma PALAVRA:
ain = re.findall(r"ain\b", txt)
print(ain)