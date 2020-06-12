def raiz(operacion,objetivo):
	if operacion == 1:
#enumeracion exhaustiva
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
	elif operacion != 1 or operacion != 2:
		print('error no existe operacion')
		raiz(int(input('elige operacion con los numeros \n1.enumeracion exhaustiva\n2.busqueda binaria\n')),int(input('elige un numero\n')))
calcular_raiz ='si'
while calcular_raiz == 'si' or calcular_raiz =='SI' or calcular_raiz == 'Si' or calcular_raiz == 'sI' :
	raiz(int(input('elige operacion con los numeros \n1.enumeracion exhaustiva\n2.busqueda binaria\n')),int(input('elige un numero\n')))
	calcular_raiz=input('quieres calcular otra raiz?\nsi\nno\n')
