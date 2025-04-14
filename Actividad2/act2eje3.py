#Ejercicio 3.  
#Dados N números enteros cargados en un vector, todos distintos de cero, mostrar aquellos 
#números que sean compuestos. 
#Nota: Un número compuesto es aquel que posee más de dos divisores.

def det_compuesto(num):
    if num<2:
        return 0

    div=0
    for i in range(1, num+1):
        if num%i==0:
            div+=1
    if div>2:
        return 1
    else:
        return 0
def numeros_compuestos(vec):
    res=[] 
    for num in vec: 
        if det_compuesto(num):
            res.append(num)
    
    return res

if __name__ == "__main__":
    N = int(input("Ingrese la cantidad de números: "))
    vec = []

    print(f"Ingrese {N} números enteros: ")
    for i in range(N):
        num=int(input())
        if num!=0:
            vec.append(num)

    comp=numeros_compuestos(vec)

    if comp:
        print("Los números compuestos en el vector son:", comp)
    else:
        print("No hay números compuestos en el vector.")