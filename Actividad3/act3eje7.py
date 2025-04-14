#Dada una matriz cuadrada de MxM elementos enteros, realizar un programa que permita: 
#a) Calcular la suma de la diagonal principal. 
#b) Almacenar en un vector de k elementos, aquellos números de la matriz cuyo factorial sea mayor o igual a la suma 
#de la diagonal principal obtenida en el punto a).  
#c) Eliminar, del vector resultante, los elementos repetidos  
#d) Ordenar de menor a mayor
from act3eje6 import cargar_matriz
import math

def suma_diag_prin(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def factorial_max(matriz, lim):
    vector = []
    limite=20
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            num = matriz[i][j]
            
            if 0 <= num <= limite:
                fact = math.factorial(num)
                if fact >= limite:
                    vector.append(num)
    
    return vector

def eliminar_repetidos(vector):
    return list(set(vector))

def ordenar_vector(vector):
    return sorted(vector)

def mostrar_vector(vector):
    for elem in vector:
        print(elem, end=" ")
    print()

if __name__ == "__main__":
    m = int(input("Ingrese el tamaño de la matriz M: "))
    
    matriz = cargar_matriz(m)

    for fila in matriz:
        print(fila)

    suma_diag=suma_diag_prin(matriz)
    print(f"\nSuma de la diagonal principal: {suma_diag}")

    vector=factorial_max(matriz, suma_diag)
    print(f"\nElementos cuyo factorial mayor o igual a la suma de diagonal: {vector}")

    vector = eliminar_repetidos(vector)
    vector = ordenar_vector(vector)

    print("\nVector final:")
    mostrar_vector(vector)