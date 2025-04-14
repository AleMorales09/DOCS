#Ejercicio 9.  
#Para una matriz A de MxN, y dos valores k y h, indicar si el elemento A[k, h] es un punto silla. 
#Nota: un elemento matricial, X[i, j], se llama punto silla si es tanto el valor mayor de la fila i como el valor menor en la 
#columna j.
def punto_silla(matriz, k, h):
    max_fila_k=max(matriz[k])
    min_columna_h=min(matriz[i][h] for i in range(len(matriz)))
    if matriz[k][h]==max_fila_k and matriz[k][h] == min_columna_h:
        return 1
    else:
        return 0

if __name__ == "__main__":
    M = int(input("Ingrese el número de filas (M): "))
    N = int(input("Ingrese el número de columnas (N): "))
    matriz=[]
    
    for i in range(M):
        fila=[]
        for j in range(N):
            num=int(input(f"Ingrese el elemento de la posición ({i+1},{j+1}): "))
            fila.append(num)
        matriz.append(fila)
    k=int(input("Ingrese el valor de k (índice de la fila): "))
    h=int(input("Ingrese el valor de h (índice de la columna): "))
    
    if punto_silla(matriz, k, h):
        print(f"El elemento A[{k}, {h}] es un punto silla")
    else:
        print(f"El elemento A[{k}, {h}] no es un punto silla")
