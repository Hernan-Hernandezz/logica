class cordenada:
	def __init__(self , x , y ):
		self.x = x
		self.y = y
	def distancia(self , otra_cordenada):
		x_diff = (self.x - otra_cordenada.x)**2
		y_diff = (self.y - otra_cordenada.y)**2
		return (x_diff + y_diff)**0.5

if __name__ == '__main__':

	corden_1 = cordenada(3 , 30)
	corden_2 = cordenada(4 ,8 )
	print(corden_1.distancia(corden_2))
