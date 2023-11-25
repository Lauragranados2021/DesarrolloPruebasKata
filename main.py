#e62c3c89eb4095943dfe28ed5cfad7de mi numero en hash numero a trabaja=6
def challenge_one():
    vectorEntrada=[]
    vectorSalida = []
    #pedimos el tamaño del vector y verificamos que sea menor a 100
    n = int(input("Ingrese la cantidad de digitos dentro de su vector (menor a 100): "))
    if(n<=100):
        #un ciclo para pedir los digitos
        while len(vectorEntrada)<n:

            num = input("Ingrese los digitos:  ")
            vectorEntrada.append(num)

            #empieza en la ultima posicion de mi vector y va de para atras, va restando una posicion desde las mas grande  , acaba hasta que ya no haya posicones osea cuando encuentra la posicione -1 falla
        for i in range(len(vectorEntrada) - 1, -1, -1):
            #Lo vuelvo a String para poder separarlo
            separar=str(vectorEntrada[i])

            #esta linea recorre los elementos dentro de separar que ya son string  los vuelve a enteros y los guarda en div
            div = [int(digito) for digito in separar]
            for e in div:
                #Compruebo mi rango
                if e<6:
                    vectorSalida.append(e)
        print (vectorEntrada)
        print (vectorSalida)
    else:
        print("Usted escribio un numero mayor a 100, la entrada no es valida ")


def challenge_two():
    vectorEntrada = []
    vectorSalida = []
    # pedimos el tamaño del vector y verificamos que no sea vacio
    n = int(input("Ingrese la cantidad de digitos dentro de su vector debe ser mayor a 0 "))
    if (n>0):
        # un ciclo para pedir los digitos
        while len(vectorEntrada) < n:
            num = input("Ingrese los digitos:  ")
            vectorEntrada.append(num)

        print( vectorEntrada)

        for e in vectorEntrada:
                cuadrado=pow(int(e),2)
                if cuadrado<=36:
                    vectorSalida.append(cuadrado)
        print(vectorSalida)
        # el primer for comprueba que los numeros esten en la posicion correcta
        for i in range(len(vectorSalida)-1):
            #el segundo comprueba entre dos numeros, primera con segunda, segunda con tercera ... para poner al mayor en la parte izquierda
            for j in range(0,len(vectorSalida)-i-1):
                if vectorSalida[j]>vectorSalida[j+1]:
                    #cambia los valores de ambas posicones
                    vectorSalida[j],vectorSalida[j+1]=vectorSalida[j+1],vectorSalida[j]

        print(vectorSalida)
    else:
        print("Su vector no debe estar vacio")

def challenge_three():
    vectorEntrada = []
    n = int(input("Ingrese el tamaño de su matriz: "))
    if (n>0):
        # un ciclo para pedir los digitos
        while len(vectorEntrada) < n:
            num = int(input("Ingrese el valor de sus monedas. Recuerde que deben ser positivos:  "))
            if num>0:
                vectorEntrada.append(num)
            else:
                print("usted agrego una moneda negativa, eso no existe")
                #Primero lo ordeno
        vectorEntrada.sort()
        #el minimo cambio que puedo hacer es 1 pero ira sumando a medida que encuentre mas monedas de otros valores
        cambio=1
        for i in vectorEntrada:
            #compruebo que el cambio sea menor a la moneda que tengo, si llega a ser mayor entonces significa que ese es mi mayor
            if(i<=cambio):
                cambio=cambio+i
            else:
                break

        print( vectorEntrada)
        print(cambio)


while True:
    print("\nMenú:")
    print("1. Desafío 1")
    print("2. Desafío 2")
    print("3. Desafío 3")
    print("4. Salir")

    choice = input("Ingrese el número del desafío que desea ejecutar (1-3) presiones 4 para salir: ")

    if choice == '1':
        challenge_one()
    elif choice == '2':
        challenge_two()
    elif choice == '3':
        challenge_three()
    elif choice == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija un número del 1 al 4.")

