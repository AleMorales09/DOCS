#NOTA: Deberá tener en cuenta realizar un menú con estructura modular, en lo posible cada ejercicio en un módulo por 
#separado. 
import act2eje1
import act2eje2
import act2eje3
import act2eje4a
import act2eje4b
import act2eje5
import act2eje6
import act2eje7
import act2eje8
import act2eje9
import act2eje10

def menu():
    print("\nElija el ejercicio que desea ejecutar:")
    print("1. Ejercicio 1 - Contar dígitos")
    print("2. Ejercicio 2 - Contar dígitos enteros y decimales")
    print("3. Ejercicio 3 - Números compuestos")
    print("4. Ejercicio 4 - Invertir un vector")
    print("5. Ejercicio 5 - Filtrar números según dígitos")
    print("6. Ejercicio 6 - Insertar K a la derecha de múltiplos de K")
    print("7. Ejercicio 7 - Promedio de filas y columnas")
    print("8. Ejercicio 8 - Factorial mayor que la suma de la diagonal")
    print("9. Ejercicio 9 - Verificar punto silla")
    print("10. Ejercicio 10 - Verificar simetría de una matriz")
    print("0. Salir")

def main():
    while True:
        menu()
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            act2eje1
        elif opcion == 2:
            act2eje2
        elif opcion == 3:
            act2eje3
        elif opcion == 4:
            act2eje4a
            act2eje4b
        elif opcion == 5:
            act2eje5
        elif opcion == 6:
            act2eje6
        elif opcion == 7:
            act2eje7
        elif opcion == 8:
            act2eje8
        elif opcion == 9:
            act2eje9
        elif opcion == 10:
            act2eje10
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()