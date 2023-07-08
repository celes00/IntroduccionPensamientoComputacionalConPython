""" num_1 = int(input("Escoge un entero: "))
num_2 = int(input("escoge otro entero: "))

if num_1 > num_2:
    print("El primer numero es mayourque el segundo")
elif num_1 < num_2:
    print("El segundo numero es mayorqueel primero")
else:
    print("Los dos numeros son iguales")
    
    
    Hacer un programa que pregunte las edades de dos usuarios, y sus edades
    que compare las edades e informe cual es el mayor por el nombre """
    
usuario1nombre =(input("Ingresa el nombre del primer usuario: ")) 
usuario1edad =  int(input("Ahora ingresa su edad: "))
usuario2nombre =(input("Ingresa el nombre del segundo usuario: "))
usuario2edad = int(input("Ahora ingresa su edad: "))

if usuario1edad > usuario2edad:
    print(usuario1nombre + " es mayor que " + usuario2nombre)
elif usuario1edad < usuario2edad:
    print(usuario2nombre + " es mayor que " + usuario1nombre)
else:
    print(usuario1nombre + " y " + usuario2nombre + " tienen la misma edad.")