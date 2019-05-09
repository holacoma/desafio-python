import os
import math
import random

MAX_LENGTH_ARRAY = 20
MIN_NUMBER = 0
MAX_NUMBER = 100

''' 
 @eramirez
 ezeram94@gmail.com
 Programa para obtener maximo beneficio
'''


def getMaxProfit(inputArray):
	''' __getMaxProfit : funcion para obtener el maximo beneficio del problema de compra y venta. 
		esta funcion trabaja con infinito positivo, debido a que para comparar los resultados con el menor posible inverti la logica de uso
	'''
	lenght = len(inputArray)
	resultArray = []
	result = float('inf')
	index = (0,0)
	# Recorro el arrenglo con un indice \i
	for i in range(0,lenght):
		# Con este indice recorro los posibles resultados
		for x in range(i + 1,lenght):
			# Resto el resultado final por el resultado inicial, para que el valor en caso de ganar de positivo
			current = int(inputArray[i]) - int(inputArray[x]) 
			# Si el resultado es menor guardo el numero y sus indices 
			if current <= result:
				result = current
				index = (i, x)

	# Se retorna el resultado invertido
	return (result * -1)


def getRandomArray():
	''' __getRandomArray : funcion para obtener un arreglo al azar dentro de algunos parametros ya definidos. '''
	randomLength = random.randint(2, MAX_LENGTH_ARRAY)
	output = []
	for x in range(0,randomLength):
		output.append(random.randint(MIN_NUMBER,  MAX_NUMBER))
	print ("__getRandomArray : output", output)
	return output

def main():
	''' __main : funcion principal para probar los metodos existentes '''
	# Hago un ejemplo basico y lo despliego. 
	print ("__main : simple example" )
	inputArray = [6,5,4,3,1]
	print ("__main ; inputArray", inputArray)
	result = getMaxProfit(inputArray)
	print ("__main : result", result)
	# Hago una serie de ejemplos al azar para comprobar el uso. 
	print ("__main : random example" )
	for x in range(1,10):
		inputArray = getRandomArray()
		result = getMaxProfit(inputArray)
		print ("__main : result", result)


if __name__ == "__main__":
	print ("__init ")
	main()