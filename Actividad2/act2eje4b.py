#Ejercicio 4.  
#Dado un vector con N dígitos, invertir sus elementos considerando lo siguiente: 
#b. Sin usar un vector auxiliar. 
def inver_sin_aux(vec):
    n=len(vec)
    for i in range(n//2):
        vec[i],vec[n-1-i]=vec[n-1-i],vec[i]

if __name__ == "__main__":
    vec= []
    N = int(input("Ingrese la cantidad de dígitos: "))
    for i in range(N):
        num=int(input(f"Ingrese el elemento {i+1}: "))  
        vec.append(num)  

    print("Vector original:",vec)
    inver_sin_aux(vec)
    print("Vector invertido:",vec)