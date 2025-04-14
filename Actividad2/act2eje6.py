#Ejercicio 6.  
#Dada una lista N de números enteros y un número entero K, insertar K a la derecha de cada múltiplo de K. 
#Ejemplo: [5, 12, 35, 67, 8, 16, 1, 13]   K=4  ➔  [5, 12, 4, 35, 67, 8, 4, 16, 4, 1, 13]
def insertar_k(vec,k,n):
    i=0 
    while i<n:
        if vec[i]%k==0:
            vec.insert(i+1,k)
            i+=1
        i+=1

    return vec

if __name__ == "__main__":
    N = int(input("Ingrese la cantidad de números en la lista: "))
    vec=[]
    for i in range(N):
        num=int(input(f"Ingrese el número {i+1}: "))
        vec.append(num)
    k=int(input("Ingrese el valor de K: "))
    mod_vec= insertar_k(vec,k,N)
    print(f"Lista modificada: {mod_vec}")