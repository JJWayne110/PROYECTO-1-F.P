def main():
    #Encabezado 
    print("UCAB Elaborado por: Eliezer Arias, David Amayo, David Vargas, Gabriel Flores y Jassen Sanchez")

    # Entrada de datos
    #Primer cliente
    print("Indique 4 letras correspondientes a las iniciales de los nombres y apellidos del primer cliente")
    C1=(input()) 
    print("Indique numero entero positivo de 4 digitos (Todos distintos) correspondiente a la clave de la Tarjeta de credito del primer cliente")
    C1c=int(input())
    print("Indique numero entero positivo de 4 o 5 digitos correspondiente a la deuda de la tarjeta de credito del primer cliente")
    C1d=int(input())
    #Segundo cliente
    print("Indique las 4 letras correspondientes a las iniciales de los nombres y apellidos del segundo cliente")
    C2=(input()) 
    print("Indique numero entero positivo de 4 digitos (Todos distintos) correspondiente a la clave de la Tarjeta de credito del segundo cliente")
    C2c=int(input())
    print("Indique numero entero positivo de 4 o 5 digitos correspondiente a la deuda de la tarjeta de credito del segundo cliente")
    C2d=int(input())
    #Tercer Cliente 
    print("Indique 4 letras correspondientes a las iniciales de los nombres y apellidos del tercer cliente")
    C3=(input()) 
    print("Indique numero entero positivo de 4 digitos (Todos distintos) correspondiente a la clave de la tarjeta de credito del tercer cliente")
    C3c=int(input())
    print("Indique numero entero positivo 4 o 5 digitos correspondiente a la deuda de la tarjeta de credito del tercer cliente")
    C3d=int(input())

    #Procesamiento de datos 
    MI1=((C1d*30)//100)
    DI1=(C1d+MI1)
    PM1=(DI1//12)
    MI2=((C2d*30)//100)
    DI2=(C2d+MI2)
    PM2=(DI2//12)
    MI3=((C3d*30)//100)
    DI3=(C3d+MI3)
    PM3=(DI3//12)

    #Salida de datos
    print("")
    print("CLIENTE 1:")
    #CLIENTE 1
    print("Las letras correspondientes a las iniciales de los nombres y apellidos del Cliente 1 son:", C1)
    print("El numero de 4 digitos correspondiente a la clave de la tarjeta del cliente 1 es:", C1c)
    print("El numero indicado correspondiente a la deuda de la tarjeta del cliente 1 es:", C1d )
    print("El Porcentaje de Interés por deuda es fijo y es igual a: 30%")
    print("El monto de interes de deuda del cliente 1 es:", MI1)
    print("La deuda mas el monto de interes del cliente 1 es:", DI1)
    print("El Pago minimo del cliente 1 es:", PM1)
    print("")
    #CLIENTE 2
    print("CLIENTE 2:")
    print("Las letras correspondientes a las iniciales de los nombres y apellidos del Cliente 2 son:", C2)
    print("El numero de 4 digitos correspondiente a la clave de la tarjeta del cliente 2 es:", C2c)
    print("El numero indicado correspondiente a la deuda de la tarjeta del cliente 2 es:", C2d )
    print("El Porcentaje de Interés por deuda es fijo y es igual a: 30%")
    print("El monto de interes de deuda del cliente 2 es:", MI2)
    print("La deuda mas el monto de interes del cliente 2 es:", DI2)
    print("El Pago minimo del cliente 2 es:", PM2)
    print("")

    #CLIENTE 3
    print("CLIENTE 3:")
    print("Las letras correspondientes a las iniciales de los nombres y apellidos del cliente 3 son:", C3)
    print("El numero de 4 digitos correspondiente a la clave de la tarjeta del cliente 3 es:", C3c)
    print("El numero indicado correspondiente a la deuda de la tarjeta del cliente 3 es:", C3d )
    print("El Porcentaje de Interés por deuda es fijo y es igual a: 30%")
    print("El monto de interes de deuda del cliente 3 es:", MI3)
    print("La deuda mas el monto de interes del cliente 3 es:", DI3)
    print("El Pago minimo del cliente 3 es:", PM3)

main()