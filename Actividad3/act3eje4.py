#Crear un programa que cargue una o más oraciones y luego indique la suma total de vocales y consonantes:  - 
#Crear dos funciones, una para contar las vocales y otra para contar las consonantes que tiene cada palabra.  - - 
#Cada función tomará como parámetro una palabra.  
#En el programa principal mostrar la cantidad total de vocales y la cantidad total de consonantes en el texto de 
#entrada.
def contar_voc(palabra):
    cont=0
    for letra in palabra:
        if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
            cont+=1
    return cont

def contar_cons(palabra):
    cont=0
    for letra in palabra:
        if letra.isalpha() and letra.lower() not in ['a', 'e', 'i', 'o', 'u']:
            cont+=1
    return cont

if __name__ == "__main__":
    cad=input("Ingrese una o más oraciones: ")

    total_voc=0
    total_cons=0

    cadenas=cad.split()

    for cad in cadenas:
        total_voc+=contar_voc(cad)
        total_cons+=contar_cons(cad)

    print(f"\nTotal de vocales: {total_voc}")
    print(f"Total de consonantes: {total_cons}")