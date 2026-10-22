from typing import List, Tuple
import math


def suma(a: float, b: float) -> float:
	return a + b


def resta(a: float, b: float) -> float:
	return a - b    


def multiplicacion(a: float, b: float) -> float:
	return a * b


def division(a: float, b: float) -> float:
	if b == 0:
		raise ValueError("No se puede dividir entre cero")
	return a / b

def potencia(a: float, b: float) -> float:      
	return a ** b       


def raiz(x: float) -> float:
	return math.sqrt(x)

def modulo(a: int, b: int) -> int:
	return a % b


def funcion_piso(a: int, b: int) -> int:
	return a // b


def incremento(x: float, step: float = 1.0) -> float:
	return x + step


def decremento(x: float, step: float = 1.0) -> float:
	return x - step


def es_par(n: int) -> bool:
	return n % 2 == 0


def es_impar(n: int) -> bool:
	return n % 2 != 0


def max_de_dos(a: float, b: float) -> float:
	return max(a, b)                                


def min_de_dos(a: float, b: float) -> float:
	return min(a, b)


def promedio_de_dos(a: float, b: float) -> float:
	return (a + b) / 2


def promedio_lista(values: List[float]) -> float:
	return sum(values) / len(values) if values else 0       


def lista_suma(values: List[float]) -> float:
	return sum(values)


def lista_producto(values: List[float]) -> float:
	return math.prod(values)


def factorial(n: int) -> int:
	return math.factorial(n)        


def porcentaje(part: float, whole: float) -> float:
	return (part / whole * 100) if whole != 0 else 0


def es_primo(n: int) -> bool:
	if n < 2:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


def fibonacci(n: int) -> int:
	if n <= 1:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)


def moda(values: List[float]) -> List[float]:
	if not values:
		raise ValueError("La lista no puede estar vacia")
	conteo = {}
	for v in values:
		conteo[v] = conteo.get(v, 0) + 1
	max_frecuencia = max(conteo.values())
	return [v for v, c in conteo.items() if c == max_frecuencia]


def volumen_paralelepipedo(largo: float, ancho: float, alto: float) -> float:
	if largo < 0 or ancho < 0 or alto < 0:
		raise ValueError("Las dimensiones no pueden ser negativas")
	return largo * ancho * alto