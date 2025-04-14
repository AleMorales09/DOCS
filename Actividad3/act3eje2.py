#Ejercicio 2: Crear un programa que determine el valor máximo entre 10 números utilizando las funciones/procedimientos del 
#ejercicio anterior.
from act3eje1 import ingresar_num, encontrar_max

if __name__ == "__main__":
    numeros = ingresar_num(10)
    mayor = encontrar_max(numeros)
    print("El número mayor es:", mayor)