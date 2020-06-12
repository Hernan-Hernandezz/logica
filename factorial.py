def factorial(n):
	"""calcula el factorial de n
	n int > 0
	returns n
	"""
	if n ==1 :
		return 1
	return n * factorial ( n - 1 )
n = int(input('escoge entero: '))

print(factorial(n))
