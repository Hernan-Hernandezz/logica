herramienta = {'pinsas':1, 'destornillador':2,'cortafrio':3}

for objetos in herramienta:
    print(objetos)
for objetos in herramienta.keys():
    print(objetos)
for numero in herramienta.values():
    if numero == 2:
        continue
    print(numero)
for todo in herramienta.items():
    print(todo)
