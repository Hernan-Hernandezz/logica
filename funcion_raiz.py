def raiz(operacion,objetivo):
	if operacion == 1:
#enumeracion exaustiva
		objetivo = objetivo
		epsilon = 0.01
		paso = epsilon**2
		respuesta = 0.0

		while abs(respuesta**2 - objetivo)>=epsilon and respuesta <= objetivo:
        		respuesta += paso
		if abs(respuesta**2 - objetivo) >= epsilon:
        		print(f'no se encontro raiz cuadrada de {objetivo}')
		else :
        		print(f'la raiz cuadrada de {objetivo} es {respuesta}')
		print('operacion 1')
	elif operacion == 2:
#busqueda binaria
		objetivo = objetivo
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
		print('operacion 2')
	else:
		print('error')

raiz(int(input('elige operacion \n1.enumeracion exaustiva\n2.busqueda binaria\n')),int(input('elige un numero\n')))
