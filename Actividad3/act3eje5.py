#Crear un programa que contenga un menú con las siguientes opciones: - 
#Calcular la potencia K de un número X. - - 
#Obtener la cantidad de dígitos de un número X. 
#Determinar si un número es capicúa. 
#Implementar funciones para cada opción del menú. 
def calcular_pot(x, k):
    return x ** k

def cant_dig(x):
    return len(str(abs(x)))

def es_capicua(x):
    x=abs(x)
    aux=0

    while aux>0:
        dig=x%10
        aux= aux*10+dig
        aux=aux//10

    return aux==x

def menu():
    print("\nMenú:")
    print("1. Calcular la potencia K de un número X.")
    print("2. Obtener la cantidad de dígitos de un número X.")
    print("3. Determinar si un número es capicúa.")
    print("4. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            x=float(input("Ingrese el número X: "))
            k=int(input("Ingrese la potencia K: "))
            res=calcular_pot(x,k)
            print(f"{x} elevado a la {k} es {res}")

        elif opcion == '2':
            x=int(input("Ingrese el número X: "))
            res=cant_dig(x)
            print(f"El número {x} tiene {res} dígitos.")

        elif opcion == '3':
            x = int(input("Ingrese el número X: "))
            if es_capicua(x):
                print(f"El número {x} es capicúa.")
            else:
                print(f"El número {x} no es capicúa.")

        elif opcion == '4':
            print("Fin del programa")
            break

        else:
            print("Opción inválida.")