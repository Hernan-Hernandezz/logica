#enumeracion exaustiva
	objetivo = int(input(f'escoge un numero : '))
	epsilon = 0.01
	paso = epsilon**2
	respuesta = 0.0

	while abs(respuesta**2 - objetivo)>=epsilon and respuesta >
        	respuesta += paso
	if abs(respuesta**2 - objetivo) >= epsilon:
        	print(f'no se encontro raiz cuadrada de {objetivo}>
	else :
        	print(f'la raiz cuadrada de {objetivo} es {respues>
#busqueda binaria
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
