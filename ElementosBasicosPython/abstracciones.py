""" Escribir un programa donde le de a eligir al usuario de que manera
quiere llegar a la raiz cuadrada, utilizando los programas anteriores """

pregunta = int(input("Que forma elige para llegar a la raiz cuadrada? ingrese 1 si quiere por enumeracion, ingrese 2 si quiere por busqueda binaria, ingrese 3 si quiere por aproximacion: "))
def eleccion(pregunta):
    if pregunta == 1:
        objetivo = int(input("Escoge un entero para encontrar su raiz cuadrada: "))
        respuesta = 0

        while respuesta**2 < objetivo:
            print(respuesta)
            respuesta += 1
            
        if respuesta**2 == objetivo:
            print(f"La raiz cuadrada de {objetivo} es {respuesta}")
        else:
            print(f"{objetivo} no tiene una raiz cuadrada exacta")
            
    elif pregunta == 2:
        objetivo = int(input("Escoge un numero para encontrar su raiz cuadrada: "))
        epsilon = 0.01
        bajo = 0.0
        alto = max(1.0, objetivo)
        respuesta = (alto + bajo) / 2

        while abs(respuesta **2 - objetivo) >= epsilon:
            print(f"bajo={bajo}, alto={alto}, respuesta={respuesta}")
            if respuesta**2 < objetivo:
                bajo = respuesta
            else: 
                alto = respuesta
            
            respuesta = (alto + bajo) /2
            
            print(f"La raiz cuadrada del {objetivo} es {respuesta}")

    else:
        objetivo = int(input("Escoge un numero para encontrar la raiz: "))
        epsilon = 0.01
        paso = epsilon**2
        respuesta = 0.0

        while abs(respuesta**2- objetivo) >= epsilon and respuesta <= objetivo:
            respuesta += paso
        if abs(respuesta**2- objetivo) >= epsilon:
            print(f"No seencontro la raiz cuadraa {objetivo}")
        else:
            print(f"La raiz cuadrada del {objetivo} es {respuesta}")
            
            
eleccion(pregunta)