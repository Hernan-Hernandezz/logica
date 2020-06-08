objetivo =int(input('escoge un entero : '))
epsilon = 0.0001
paso = epsilon ** 2
respuesta = 0

while abs(respuesta**2 -objetivo)>= epsilon and respuesta <= objetivo :
    respuesta += paso
    print(respuesta)
    
if abs(respuesta ** - objetivo) > epsilon:
    print(f'no se encontro raiz cuadrada de {objetivo}')
else :
    print(f'el cuadrado de{objetivo} es {respuesta}' )
