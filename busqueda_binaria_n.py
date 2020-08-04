import random

def busqueda_binaria(lista,comienzo,final,objetivo):
	print(f'encontrar numero {objetivo} entre {comienzo} y {final}')

	if comienzo >final :

		return False
	medio = ( comienzo + final ) //	2

	if lista[medio] == objectivo :
		return True
	elif lista[medio] < objetivo :
		busqueda_binaria( lista, medio + 1, final , objetivo )
	else:
		busqueda_binaria( lista, comienzo, medio -1, objetivo)
if __name__=='__main__':
	tamano_lista = int(input('cual es el tamano de tu lista?'))
	objetivo = int(input('que numero quieres encontrar'))

	lista =[(random.randint( 0, 100)) for i in range(tamano_lista)]
	lista = sorted(lista)
	encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
	print(lista)
	print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
