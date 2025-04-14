#Crear un programa que: 
#a) cargue dos vectores A y B, con N y M números enteros respectivamente 
#b) calcular la suma de los números cargados en cada vector. 
#c) si N y M son iguales, realice la suma de los vectores. Mostrar el vector resultante 
#¿Cuántas funciones y/o procedimientos son necesarios para resolver este problema?
def carga_vec(n):
    vec=[]
    for i in range(n):
        num=int(input(f"Ingrese el {i + 1} número: "))
        vec.append(num)
    return vec

def sumar_elem(vec):
    return sum(vec)

def sumar_vec(vec1, vec2):
    res=[]
    for i in range(len(vec1)):
        suma=vec1[i]+vec2[i]
        res.append(suma)
    return res

if __name__ == "__main__":
    N = int(input("Ingrese la cantidad del vector A: "))
    M = int(input("Ingrese la cantidad del vector B: "))

    vecA = carga_vec(N)
    vecB = carga_vec(M)
    sum_A = sumar_elem(vecA)
    sum_B = sumar_elem(vecB)

    print(f"\nSuma de elementos del vector A: {sum_A}")
    print(f"Suma de elementos del vector B: {sum_B}")

    if N == M:
        res=sumar_vec(vecA, vecB)
        print(f"\nResultado de la suma de vectores:")
        print(res)
    else:
        print("\nLos vectores no tienen la misma cantidad de elementos")