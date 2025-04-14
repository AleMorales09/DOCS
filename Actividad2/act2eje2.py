#Ejercicio 2.  
#Dado un numero decimal, determinar y mostrar la cantidad de dígitos enteros y decimales que tiene.

from act2eje1 import contar_digitos

def contar_digitos_decimal(num):
    num=abs(num)
    parte_entera=int(num)
    dig_enteros=contar_digitos(parte_entera)
    parte_decimal=num-parte_entera
    dig_decimales=0

    while parte_decimal>0:
        parte_decimal*=10
        dig=int(parte_decimal)
        parte_decimal-=dig
        dig_decimales+=1

    return dig_enteros,dig_decimales

if __name__ == "__main__":
    num=float(input("Ingrese un número decimal: "))
    enteros,decimales=contar_digitos_decimal(num)
    print(f"El número {num} tiene {enteros} dígitos en la parte entera y {decimales} en la parte decimal")