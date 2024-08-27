# git init (crear repositorio en pc)
# git status (verificar lo que vamos a subir)
# git add . (agregar archivo. se puede nombre en especifico)
# git commit -m "comentario"
# git config --global user.email lopezgg98@gmail.com
# git config --global user.name BladSector
# git branch -M main (subir a rama principal)
# git remote add origin https://github.com/BladSector/Algoritmos-clase-3.git
# git pull
# git push -u origin main (sincronisacion del local y remoto)

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
        C3 = input('3. Introduzca una calificacion (entre 0 y 100): ').lower()
        print('')

        if C3 == 'salir':
            print('Programa cerrado.')
            sys.exit()
        if C3 == 'siguiente':
            break

        C3 = int(C3)
        if C3 < 0 or C3 > 100:
            print('Numero fuera del rango de calificacion') 
        elif C3 >= 90:
            print('Su calificacion es una "A"')
        elif C3 >= 80:
            print('Su calificacion es una "B"')
        elif C3 >= 70:
            print('Su calificacion es una "C"')
        elif C3 >= 60:
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
         
         elif 18 <= E4 <= 65 and P4 >= 50:
             print('Es apto para donar sangre.')
         else:
             print('No es apto para donar sangre.')

    except ValueError:
        print('No valido.')

# 6.Escribe un programa que pida un número al usuario y luego imprima si ese 
# número no es divisible por 5.



# 7.Escribe un programa que pida tres números al usuario y luego imprima si al 
# menos uno de ellos es mayor a 10 y, al mismo tiempo, todos son positivos.

# 9.Escribe un programa que pida la cantidad de horas trabajadas y la paga por 
# hora. Si la cantidad de horas trabajadas es más de 40 y la paga por hora es 
# mayor o igual a $20, imprime "Recibe pago extra". Si la paga por hora es menor a 
# $10 y no trabajó más de 40 horas, imprime "Pago insuficiente". En cualquier otro 
# caso, imprime "Pago adecuado".