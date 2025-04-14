#Ejercicio 1.
#Dado un numero entero, determinar y mostrar la cantidad de dígitos que tiene. 

def contar_digitos(n):
    c=0
    aux=abs(n)
    while aux!=0:
        c+=1
        aux=aux//10
    return c

if __name__=="__main__":

    num=int(input("Ingrese un numero entero: "))
    cantidad_digitos=contar_digitos(num)
    print(f"El número {num} tiene {cantidad_digitos} dígitos")