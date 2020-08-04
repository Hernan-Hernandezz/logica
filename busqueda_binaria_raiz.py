objetivo = int(input(f'escoge un numero'))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0,objetivo)
respuesta = (alto+bajo)/2
while abs(respuesta**2-objetivo) >= epsilon :
	if respuesta**2 < objetivo:
		bajo = respuesta
	else :
		alto = respuesta
	respuesta = (alto+bajo) / 2
print(f'la raiz cuadrada de {objetivo} es {respuesta}')

