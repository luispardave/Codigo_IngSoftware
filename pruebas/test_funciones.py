from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).resolve().parent / "funciones.py"
SPEC = spec_from_file_location("funciones", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
funciones = module_from_spec(SPEC)
SPEC.loader.exec_module(funciones)


def test_operaciones_basicas():
	assert funciones.suma(2, 3) == 5
	assert funciones.resta(7, 4) == 3
	assert funciones.multiplicacion(6, 5) == 30
	assert funciones.potencia(2, 3) == 8


def test_division_y_errores():
	assert funciones.division(10, 2) == 5
	with pytest.raises(ValueError, match="No se puede dividir entre cero"):
		funciones.division(10, 0)


def test_raiz_y_modulos():
	assert funciones.raiz(25) == 5
	assert funciones.modulo(10, 3) == 1
	assert funciones.funcion_piso(10, 3) == 3


def test_incremento_y_decremento():
	assert funciones.incremento(10) == 11.0
	assert funciones.incremento(10, 2.5) == 12.5
	assert funciones.decremento(10) == 9.0
	assert funciones.decremento(10, 2.5) == 7.5


def test_pares_e_impares():
	assert funciones.es_par(4) is True
	assert funciones.es_par(5) is False
	assert funciones.es_impar(4) is False
	assert funciones.es_impar(5) is True


def test_extremos_y_promedios():
	assert funciones.max_de_dos(10, 7) == 10
	assert funciones.min_de_dos(10, 7) == 7
	assert funciones.promedio_de_dos(4, 6) == 5
	assert funciones.promedio_lista([2, 4, 6, 8]) == 5


def test_listas_y_factorial():
	assert funciones.lista_suma([1, 2, 3, 4]) == 10
	assert funciones.lista_producto([1, 2, 3, 4]) == 24
	assert funciones.factorial(5) == 120


def test_porcentaje_y_primos():
	assert funciones.porcentaje(25, 200) == 12.5
	assert funciones.es_primo(2) is True
	assert funciones.es_primo(15) is False
	assert funciones.es_primo(1) is False


def test_fibonacci():
	assert funciones.fibonacci(0) == 0
	assert funciones.fibonacci(1) == 1
	assert funciones.fibonacci(7) == 13


def test_moda():
	assert funciones.moda([1, 2, 2, 3]) == [2]
	assert funciones.moda([4, 4, 1, 1, 3]) == [4, 1]
	assert funciones.moda([1, 2, 3]) == [1, 2, 3]
	assert funciones.moda([7]) == [7]
	with pytest.raises(ValueError, match="La lista no puede estar vacia"):
		funciones.moda([])


def test_volumen_paralelepipedo():
	assert funciones.volumen_paralelepipedo(2, 3, 4) == 24
	assert funciones.volumen_paralelepipedo(1.5, 2, 2) == 6
	assert funciones.volumen_paralelepipedo(0, 5, 5) == 0
	with pytest.raises(ValueError, match="Las dimensiones no pueden ser negativas"):
		funciones.volumen_paralelepipedo(-1, 2, 3)


if __name__ == "__main__":
	raise SystemExit(pytest.main(["-v", __file__]))