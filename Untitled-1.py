import sys
#Ejercicios
# 1. Escribe un programa que pida un número al usuario 
# si el input no es un numero, que se repita el print
# y luego imprima si ese número es mayor que 10.
while True:
    try:
        print('')
        print("(Escribe 'salir' para terminar el programa o 'siguiente' para pasar al siguiente ejercicio)")
        N1=(input("1. Introduzca un numero: ")).lower()
        print('')
        if N1 == 'salir':
             print('Programa cerrado.')
             sys.exit()
        if N1 == 'siguiente':
            break
        N1 = int(N1)
        if N1 >= 10:
             print(f'Su numero es {N1} y es mayor a 10!')
        else:
            print('Su numero no es mayor a 10. Ingrese otro numero.')
    except ValueError:
        print ("No valido.")
        
#2.Escribe un programa que pida un número al usuario 
# y luego imprima si ese número es positivo o negativo. 
# Si el número es 0, imprime que es neutro.

while True:
    try:
        print('')
        print("(Escribe 'salir' para terminar el programa o 'siguiente' para pasar al siguiente ejercicio)")
        N2 = input('2. Introduce un numero: ').lower()
        print('')

        if N2 == 'salir':
             print('Programa cerrado.')
             sys.exit()
        if N2 == 'siguiente':
            break

        N2 = int(N2)
        if N2 > 0:
            print(f'Su numero {N2} es positivo.')
            print()
        elif N2 < 0:
            print(f'Su numero {N2} es negativo.')
            print('')
        else:
            print('Su numero es neutro') 

    except ValueError:
        print('No valido.')

# 3.Escribe un programa que pida una calificación al usuario (entre 0 y 100) 
# y luego imprima la nota en letras: "A" para 90 o más, "B" para 80-89, "C" para 70-79,
# "D" para 60-69, y "F" para menos de 60.

while True:
    try:
        print()
        print("(Escribe 'salir' para terminar el programa o 'siguiente' para pasar al siguiente ejercicio)")
        N3 = input('3. Introduzca una calificacion (entre 0 y 100): ').lower()
        print('')

        if N3 == 'salir':
            print('Programa cerrado.')
            sys.exit()
        if N3 == 'siguiente':
            break

        N3 = int(N3)
        if N3 < 0 or N3 > 100:
            print('Numero fuera del rango de calificacion') 
        elif N3 >= 90:
            print('Su calificacion es una "A"')
        elif N3 >= 80:
            print('Su calificacion es una "B"')
        elif N3 >= 70:
            print('Su calificacion es una "C"')
        elif N3 >= 60:
            print('Su calificacion es una "D"')
        else:
            print('Su calificacion es una "F"')

    except ValueError:
        print('No valido.')

#4.Escribe un programa que pida la edad y el peso de una persona, 
# y luego imprima si es apta para donar sangre. 
# Para ser apto, la persona debe tener entre 18 y 65 años y pesar al menos 50 kg

while True:
    try:
         print()
         print("(Escribe 'salir' para terminar el programa o 'siguiente' para pasar al siguiente ejercicio)")
         print('4. Le pediremos que introduzca la edad y peso.')

         E4 = input('Edad: ').lower()

         if E4 == 'salir':
            print('Programa cerrado.')
            sys.exit()
         if E4 == 'siguiente':
            break
         
         E4 = int(E4) 
         if E4 < 0 or E4 > 120:
             print('Edad no valida. Intentelo de nuevo.')
             continue
             
         P4 = input('Peso en kg:').lower()
         print()

         if P4 == 'siguiente':
             break 
         elif P4 == 'salir':
             sys.exit()

         P4 = int(P4)
         if P4 < 0 or P4 > 200:
             print('Peso no valido. Intentelo de nuevo.')
             continue
         
         if 18 <= E4 <= 65 and P4 >= 50:
             print('Es apto para donar sangre.')
         else:
             print('No es apto para donar sangre.')

    except ValueError:
        print('No valido.')

# 5.Escribe un programa que pida la temperatura exterior y la velocidad del viento, 
# y luego imprima si es peligroso salir. 
# Es peligroso si la temperatura es menor a 0°C 
# o la velocidad del viento es mayor a 60 km/h.
