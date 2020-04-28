text = "ola mundo de todos nos!"
char = "o"
count = 0
v = list()
for c in text:
    v.append(c)
    if c == char:
        count += 1
    if " " in v:
        v.remove(" ")
print(count)
print(v)

