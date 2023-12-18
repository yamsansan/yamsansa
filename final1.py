#ventana
import tkinter 
ventana = tkinter.Tk()
ventana.geometry("500x500")

etiqueta= tkinter.Label(ventana, text ="Bienvenido al juego! Presiona una opcion:",bg= "green")
etiqueta.pack(fill= tkinter.X)

import numpy as np
import matplotlib.pyplot as plt 
import random
#piedra papel tijera
def pied_pap_tij():
    opciones = ["piedra", "papel", "tijera"]
    opc_computadora = opciones[random.randint(0, 2)]

    bienvenida = """Bienvenido al juego de piedra-papel-tijera
    Elige una opcion:1.Piedra, 2.Papel o 3.Tiejera"""

    print(bienvenida)

    def juego(opc_usuario, opc_computadora, opciones):
            print(opc_usuario)
            print(opc_computadora)
            pierde = "PIERDES"
            gana = "GANASTE"
            empate = "EMPATE"
            piedra = "PIEDRA"
            papel = "PAPEL"
            tijera = "TIEJRA"

            if opc_usuario == 1:
                opc_usuario = piedra
                print(f"Tu: ", opc_usuario, " vs Computador: ", opc_computadora)
                if opc_computadora == opciones[0]:
                    return empate
                if opc_computadora == opciones[1]:
                    return pierde
                if opc_computadora == opciones[2]:
                    return gana
            if opc_usuario == 2:
                opc_usuario = papel
                print(f"Tu: ", opc_usuario, " vs Computador: ", opc_computadora)
                if opc_computadora == opciones[0]:
                    return gana
                if opc_computadora == opciones[1]:
                    return empate
                if opc_computadora == opciones[2]:
                    return pierde
            if opc_usuario == 3:
                opc_usuario = tijera
                print(f"Tu: ", opc_usuario, " vs Computador: ", opc_computadora)
                if opc_computadora == opciones[0]:
                    return pierde
                if opc_computadora == opciones[1]:
                    return gana
                if opc_computadora == opciones[2]:
                    return empate

    try:
        opc_usuario = int(input("Ingrese una opcion: "))

        while (opc_usuario != 1) and (opc_usuario != 2) and (opc_usuario != 3):
            opc_usuario = int(input("Porfavor seleccione una opcion del 1 al 3: "))
        print(juego(opc_usuario=opc_usuario, opc_computadora=opc_computadora,opciones=opciones))

    except ValueError:
        print("Solo puedes ingresar opcion de numero del 1 al 3, reinicia el juego")
#tirar dado
def tirar_dado():
    valor_min= 1
    valor_max= 6

    juega_otravez= "si"

    while juega_otravez == "si":
        print("Tirando los dados...")
        usuario = int(input("Ingrese un numero entre el 1 y el 6: "))
        print("Usuario: ", usuario)
        computadora = random.randint(valor_min, valor_max)
        print("Computadora: ", computadora)
        if usuario > computadora:
           print("No has acertado, el numero del usuario es mayor.")
        elif computadora > usuario:
             print("No has acertado, el numero de la computadora es mayor")
        else:
             print("Los numeros son iguales! Has ganado.")
        juega_otravez= input("¿Tirar otra vez los dados?")
#adivina un numero
def adivina_un_numero():
       numero_compu = random.randint(1,10)
       def adivina():
         print("Adivina el numero contra la computadora, tienes cinco intentos")
       def juego_adivina():
          for i in range (5):
            i+=1
            while True:
             num_usuario=int(input("Ingresa un numero del 1 al 10: "))
             if num_usuario > numero_compu:
                print("El numero es menor al seleccionado. Vuelve a intentarlo: ")
             elif num_usuario < numero_compu:
                   print("El numero es mayor al seleccionado. Vuelve a intentarlo: ")
             elif  num_usuario == numero_compu:
                   print("Has adivina el numero! Por lo cual eres el ganador!")
             break       
             print ("Ya realizaste el total de intentos! ")   
#Graficar funcion
def graficar_fun():
    def sen(x):
	    return np.sin(x)
    u1 = int(input("Ingrese el numero donde quiere comenzar: "))
    u2 = int(input("Ingrese el numero donde quiere terminar: "))
    num = int(input("Ingrese el numero de muestras: "))
    x=np.linspace(-10,10,num=100)
    y=sen(x)
    plt.plot(x,y, color="green")
    plt.title("grafica de funcion")
    plt.xlabel("valores de x")
    plt.ylabel("sen(X)")
    print("ya se esta realizando grafica! aguarda unos segundos.")
    plt.show()


boton1= tkinter.Button(ventana, text= "1. piedra,papel,tijera", command= pied_pap_tij)
boton2= tkinter.Button(ventana, text="2.tirar dado",command= tirar_dado)
boton3= tkinter.Button(ventana, text= "3.adivinar un número", command= adivina_un_numero)
boton4= tkinter.Button(ventana, text= "4.Graficar función", command=graficar_fun)

boton1.pack()
boton2.pack()
boton3.pack()
boton4.pack()




ventana.mainloop()