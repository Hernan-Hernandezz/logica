import unittest
def suma(num_1 ,num_2):
	return num_1 + num_2
class CajaNegraTest(unittest.TestCase):
	def test_suma_dos_positivos(self):
		num_1 = 10
		num_2 = 5
		resultado = suma( num_1 , num_2 )
		self.assertEqual(resultado , 15 )
<<<<<<< HEAD
	def teste_suma_dos_negativos(logi):
		num_1 = -10
		num_2 = -5
		resultado = suma( num_1 , num_2 )
		logi.assertEqual(resultado , -15 )
=======
	def teste_suma_dos_negativos(self):
		num_1 = -10
		num_2 = -5
		resultado = suma( num_1 , num_2 )
		self.assertEqual(resultado , -15 )
>>>>>>> deeb135672fceec9f24273409adf2e58cce9da8b
if __name__ == '__main__' :
	unittest.main()
