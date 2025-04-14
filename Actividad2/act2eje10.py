#Ejercicio 10.  
#Dada una matriz NxM, determinar si es una matriz simétrica. 
def simetrica(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    if filas != columnas:
        return 0
    
    for i in range(filas):
        for j in range(i + 1, columnas):
            if matriz[i][j]!=matriz[j][i]:
                return 0
                
    return 1

if __name__=="__main__":
    N=int(input("Ingrese el número de filas (N): "))
    M=int(input("Ingrese el número de columnas (M): "))
    
    matriz=[]
    
    for i in range(N):
        fila=[]
        for j in range(M):
            num=int(input(f"Ingrese el elemento de la posición ({i+1},{j+1}): "))
            fila.append(num)
        matriz.append(fila)
    
    
    if simetrica(matriz):
        print("La matriz es simétrica.")
    else:
        print("La matriz no es simétrica.")