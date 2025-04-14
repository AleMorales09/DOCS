#Ejercicio 8.  
#Dada una matriz cuadrada de MxM elementos enteros, realizar un programa que permita almacenar en un vector de k 
#elementos, aquellos números de la matriz donde su factorial sea mayor o igual a la suma de la diagonal principal. Luego 
#eliminar del vector resultante los elementos repetidos. 
import math

def calcular_factorial(num):
    return math.factorial(num)

def suma_diagonal_p(matriz):
    suma=0
    for i in range(len(matriz)):
        suma+=matriz[i][i]
    return suma

if __name__ == "__main__":
    M = int(input("Ingrese el tamaño de la matriz cuadrada (M): "))
    
    matriz=[]
    
    for i in range(M):
        fila = []
        for j in range(M):
            num = int(input(f"Ingrese el elemento de la posición ({i+1},{j+1}): "))
            fila.append(num)
        matriz.append(fila)
    suma_diagonal = suma_diagonal_p(matriz)
    vec=[]
    for i in range(M):
        for j in range(M):
            num = matriz[i][j]
            if calcular_factorial(num)>=suma_diagonal:
                vec.append(num)
    vec_sin_rep=list(set(vec))
    
    for fila in matriz:
        print(fila)
    
    print("\nVector sin repetidos:")
    print(vec_sin_rep)
