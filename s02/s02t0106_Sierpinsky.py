from array import array as arr
from enum import Enum  # Módulo para la clase de colores ANSI

# Borra la pantalla con caracteres de escape ANSI
def clear_screen():
    print("\033[2J\033[H", end="")

# Encapsulado de los valores ANSI para colores en un enumerado
class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

# Funcion para imprimir matrix
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

#Parametros de mi cuadricula
def generate_triangle(rows = 1):
    Columns = 2 * rows - 1

#Creando la reticula 2D
    matrix = []
#Construyendo el grid
    for _ in range(rows):
        new_row = arr('i', [0] * Columns)
        matrix.append(new_row)

#Validando la construccion del grid
  #print(f"Cantidad de filas: {len(matrix)}")
  #print(f"Cantidad de columnas: {len(matrix[0])}")

#Calculando el centro de la primer fila 
    center = Columns // 2 #Se hace division entera

#estableciendo el cebtro en 1
    matrix[0][center] = 1
  #print_matrix(matrix)

#Se calcula el resto de la matrix
#Siguiendo la logica del siperpinsky Gasket
    for row in range(1,rows):
        for Col in range(0,Columns):
            left_upper_cell = 0
            right_upper_cell = 0
      #print(f"[{row}-{Col}]",end=" ")

#si la columna donde estamos es mayor a cero, despues del borde 0
            if Col > 0:
                left_upper_cell = matrix[row-1][Col-1]  

#Si la columna esta en un elemento antes del borde derecho
            if Col < Columns-1:
                right_upper_cell = matrix[row-1][Col+1]

#Guardo el arreglo 
            if left_upper_cell != right_upper_cell:
                matrix[row][Col] = 1
            else:
                matrix[row][Col] = 0

# Retorna la matriz calculada
    return matrix

# Dibuja la matriz con símbolos coloreados en lugar de listas de números
def draw_matrix(input_matrix, symbol="*"):
    for row in input_matrix:
        for cell in row:
            if cell == 1:
                print(AnsiColor.CYAN.value + symbol + AnsiColor.RESET.value,end="",)
            else:
                print(AnsiColor.RED.value + " ", end="")
        print()

# Método principal para controlar el flujo completo del programa
def main():
    # Generación del triángulo mediante llamado a función (ejemplo con 10 filas)
    matrix = generate_triangle(8)

    # Limpia la terminal
    clear_screen()

    # Dibuja el patrón visualmente en consola
    draw_matrix(matrix, symbol="■")

#Punto de entrada del script
if __name__ == "__main__":
    main()