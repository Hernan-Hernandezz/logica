def nombre_completo(nombre,apellido,inverso=False):
	if inverso:
		return f'{apellido} {nombre}'
	else :
		return f'{nombre} {apellido}'
print(nombre_completo('hernan','hernandez',inverso=True))

