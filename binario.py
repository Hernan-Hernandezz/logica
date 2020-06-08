operacion = int(input(f'elige \n1. para convertir entero a binario.\n2. para convertir binario a entero. \n'))
entero = 0
constante = 2
binario = 0
dividido = 0
valor_b = '' 
posicion = 0
if operacion ==1 :
    entero = int(input(f'ingresa el numero entero '))
    while 1<=entero :
        binario = entero  % constante 
        dividido = entero / constante
        valor_b = str(binario) + valor_b 
        entero = dividido
        if binario == 1:
            entero = entero - 0.5
        entero =int(entero)
    print (valor_b)
elif operacion == 2 :
    binario = int(input('ingresa el numero binario '))
    potencia=0
    while binario >= 1 :
        
        
        if int(binario)%10 >= 1 :
            entero += (2**potencia)
        
        potencia += 1
        binario /= 10
    print(entero)