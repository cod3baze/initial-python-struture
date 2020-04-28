import json

#dados JSON
x = '{"name":"jhon", "age":30}'
#Converter os Dados para dicionario python
y = json.loads(x)
print(y)

#dicionario python
w = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#converter o dicionário para dados JSON
z = json.dumps(w)
print(z)


#Converte objetos Python em strings JSON, e imprima os valores:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#Converte um objeto Python contendo todos os tipos de dados legais:
a = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
#indent para os números de recuos
#separators = padrao("," , ":")
print(json.dumps(a, indent = 5, separators=(". ", " = ")))