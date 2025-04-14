#Ejercicio 4.  
#Dado un vector con N dígitos, invertir sus elementos considerando lo siguiente: 
#a. Usando un vector auxiliar 
def invertir_aux(vec):
    aux=[]
    for i in range(len(vec) - 1, -1, -1):
        aux.append(vec[i])
    return aux

if __name__ == "__main__":
    vec=[]
    N=int(input("Ingrese la cantidad de dígitos: "))
    for i in range(N):
        num=int(input(f"Ingrese el elemento {i+1}: "))
        vec.append(num)
    inver=invertir_aux(vec)
    print("Vector original:", vec)
    print("Vector invertido:", inver)