#Ejercicio 7.  
#Dada una matriz de MxN elementos, calcular el promedio de cada fila y de cada columna. Mostrar en pantalla la matriz 
#cargada y los promedios correspondientes.
def calcular_prom_filas(matriz):
    prom_filas=[]
    for fila in matriz:
        prom=sum(fila)/len(fila)
        prom_filas.append(prom)
    return prom_filas

def calcular_prom_columnas(matriz):
    num_columnas=len(matriz[0])
    prom_columnas=[]
    
    for j in range(num_columnas):
        suma_columna=0
        for i in range(len(matriz)):
            suma_columna+=matriz[i][j]
        prom=suma_columna/len(matriz)
        prom_columnas.append(prom)
    
    return prom_columnas

if __name__ == "__main__":
    M = int(input("Ingrese el número de filas (M): "))
    N = int(input("Ingrese el número de columnas (N): "))
    matriz=[]
    for i in range(M):
        fila=[]
        for j in range(N):
            num = int(input(f"Ingrese el elemento de la posición ({i+1},{j+1}): "))
            fila.append(num)
        matriz.append(fila)
    prom_filas = calcular_prom_filas(matriz)
    prom_columnas = calcular_prom_columnas(matriz)
    
    for fila in matriz:
        print(fila)
    
    

    print("\nPromedios de las filas:")
    for i in range(len(prom_filas)):
            print(f"Fila {i + 1}: {prom_filas[i]:.2f}")
    
    print("\nPromedios de las columnas:")
    for j in range(len(prom_columnas)):
            print(f"Columna {j + 1}: {prom_columnas[j]:.2f}")