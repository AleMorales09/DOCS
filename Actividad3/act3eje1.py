#Ejercicio 1: Crear un programa que determine el valor máximo entre tres números. ¿Cuántas funciones y/o procedimientos son 
#necesarios para resolver este problema? ¿Cuántos parámetros?  
def ingresar_num(cant):
    lista=[]
    for i in range(cant):
        num = float(input(f"Ingrese el {i + 1} número: "))
        lista.append(num)
    return lista

def encontrar_max(lista):
    return max(lista)

if __name__ == "__main__":
    lista=ingresar_num(3)
    mayor=encontrar_max(lista)
    print("El número mayor es:", mayor)
