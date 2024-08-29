# git init (crear repositorio en pc)
# ls (mostrar rutas).
# cd (cambiar ruta)
# pwd (mostrar ruta actual de mi terminal)
# git remote add origin https://github.com/BladSector/Algoritmos-clase-3.git.
# git remote -v (verificar conectividad)
# git push -u origin master (sincronisacion del local y remoto)
# git branch -M main (subir a rama principal main)
# git push -u origin main
# git pull o git pull origin main (descarga de los datos)
# git pull origin main --allow-unrelated-histories
# ctrl shift zz o shift zz.
# git status (verificar lo que vamos a subir)
# git add . (agregar archivo. se puede nombre en especifico)
# git commit -m "comentario"
# git config --global user.email lopezgg98@gmail.com
# git config --global user.name BladSector



#new commit 3 prueba

import sys
#Ejercicios
# 1. Escribe un programa que pida un número al usuario 
# si el input no es un numero, que se repita el print
# y luego imprima si ese número es mayor que 10.
while True:
    try:

        print("\n(Escribe 'salir' para terminar el programa o 'siguiente' para pasar al siguiente ejercicio)\n")
        N1=(input("1. Introduzca un numero: ")).lower()

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
while True:
    try:
         print()
         print("(Escribe 'salir' para terminar el programa o 'siguiente' para pasar al siguiente ejercicio)")
         N6 = input('6. Escribe un numero para saber si es divisible por 5: ').lower()
        
         if N6 =="salir":
             sys.exit()
         if N6 == "siguiente":
             break
         
         N6 = int(N6)
         if N6%5 == 0:
             print(f"Su numero {N6} es divisible por 5.")
         else:
             print(f"Su numero {N6} no es divisible por 5")
    except ValueError:
        print("No valido.")     

# 7.Escribe un programa que pida tres números al usuario y luego imprima si al 
# menos uno de ellos es mayor a 10 y, al mismo tiempo, todos son positivos.

while True:
    try:
        print()
        print("(Escribe 'salir' para terminar el programa o 'siguiente' para pasar al siguiente ejercicio)")
        print("7. Introduzca tres numeros cualquiera a continuacion: ")
        N71 = input("Primer numero: ").lower()
        if N71 == "salir":
                sys.exit()
        elif N71 == "continuar":
            break

        N72 = input("Segundo numero: ").lower()
        if N72 == "salir":
                sys.exit()
        elif N72 == "continuar":
            break

        N73 = input("Tercer numero: ").lower()
        if N73 == "salir":
                sys.exit()
        elif N73 == "continuar":
            break

        N71 = int(N71)
        if N71 > 10:
            print(f"Su numero {N71} es mayor a 10.")
        N72 = int(N72)
        if N72 > 10:
            print(f"Su numero {N72} es mayor a 10.")
        N73 = int(N73)
        if N73 > 10:
           print(f"Su numero {N73} es mayor a 10.")
        else:
            print("Todos sus numeros son positivos!")

        if N71 < 0:
            print(f"El numero {N71} no es positivo")
        if N72 < 0:
            print(f"El numero {N72} no es positivo")
        if N73 < 0:
            print(f"El numero {N73} no es positivo")   

    except ValueError:
        print("No valido.")

# 9.Escribe un programa que pida la cantidad de horas trabajadas y la paga por 
# hora. Si la cantidad de horas trabajadas es más de 40 y la paga por hora es 
# mayor o igual a $20, imprime "Recibe pago extra". Si la paga por hora es menor a 
# $10 y no trabajó más de 40 horas, imprime "Pago insuficiente". En cualquier otro 

