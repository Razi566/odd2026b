"""
Generators
Los generadores son funciones que pueden pausar su ejecucion.
Cuando de invoca una funcion generadora devuelve un objeto (aka Iterador).
El codigo dentro de la funcion no se ejecuta de inmediato, solo se compila
La funcion se ejecuta unicamente cuando iteras sobre el generador.
"""
def My_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6 
    yield 7
    yield 8
    yield 9

# Se invoca  funcion generadora
My_iterador = My_generator()

# Se itera manualmente sobre el generador
# print(next(My_iterador)) # Imprime 1
# print(next(My_iterador)) # Imprime 2
# print(next(My_iterador)) # Imprime 3
# print(next(My_iterador)) # Imprime 4
# print(next(My_iterador)) MARCA ERROR

# Los iteradores se puede iterar con un for
for value in My_iterador:
    print(value)