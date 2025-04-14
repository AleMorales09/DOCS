#Escriba un programa que para dos matrices A y B de números enteros de dimensiones MxN, realice la suma o el 
#producto de las matrices (a elección del usuario) y las cargue en otra matriz C. 
#Utilizar funciones y/o procedimientos para: - cargar las matrices - realizar la suma - realizar el producto - mostrar en pantalla una matriz  
#Invóquelas adecuadamente.
def cargar_matriz(m,n):
    matriz=[]
    for i in range(m):
        fila=[]
        for j in range(n):
            num = int(input(f"Ingrese el elemento en la posición [{i+1},{j+1}]: "))
            fila.append(num)
        matriz.append(fila)
    return matriz

def sumar_matrices(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)
    return C

def multiplicar_matrices(A, B):
    m = len(A)
    n = len(B[0])
    p = len(B)
    if len(A[0]) != len(B):
        print("Las matrices no son compatibles")
        return None
    
    C = []
    for i in range(m):
        fila = []
        for j in range(n):
            suma = 0
            for k in range(p):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        C.append(fila)
    return C

def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()


if __name__ == "__main__":
    m = int(input("Ingrese el número de filas M: "))
    n = int(input("Ingrese el número de columnas N: "))
    A = cargar_matriz(m, n)
    B = cargar_matriz(m, n)
    print("\nSeleccione la operación:")
    print("1. Sumar matrices")
    print("2. Multiplicar matrices")
    op=input("Ingrese la operación: ")

    if op=='1':
        C = sumar_matrices(A, B)
        print("\nMatriz resultante de la suma:")
        mostrar_matriz(C)

    elif op=='2':
        C = multiplicar_matrices(A, B)
        if C is not None:
            print("\nMatriz resultante del producto:")
            mostrar_matriz(C)
    
    else:
        print("Opción inválida.")