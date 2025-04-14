#Ejercicio 5.  
#Dada una lista A de N números reales, crear y mostrar una lista B con aquellos elementos de A que en su parte entera 
#tenga: 
#• Exactamente dos dígitos pares.   
#• Al menos dos dígitos impares. 
from act2eje1 import contar_digitos

def contar_par_impar(num):
    parte_entera=abs(int(num))
    par=0
    impar=0
    while parte_entera>0:
        dig=parte_entera%10
        if dig%2==0:
            par+=1
        else:
            impar+=1
        parte_entera//=10
    
    return par,impar

def cond_num(vec_a):
    vec_b=[]
    
    for num in vec_a:
        par,impar = contar_par_impar(num)
        total_dig=contar_digitos(int(abs(num)))
        if par==2 and impar>=2 and total_dig>=4:
            vec_b.append(num)
    
    return vec_b

if __name__ == "__main__":
    vec_a=[]
    N = int(input("Ingrese la cantidad de números: "))
    for i in range(N):
        num = float(input(f"Ingrese el número {i+1}: "))
        vec_a.append(num)
    vec_b= cond_num(vec_a)
    print("Vector A:", vec_a)
    print("Vector B:", vec_b)