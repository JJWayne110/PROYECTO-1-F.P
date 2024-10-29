def main():
    #Encabezado 
    print("UCAB Elaborado por: XXXXX")

    # Entrada de datos
    print("Indique 4 letras correspondientes a las inciales de sus nombres y apellidos")
    C1=(input()) 
    print("Indique numero entero positivo de 4 digitos(Todos distintos)correspondiente a la clave de su Tarjeta")
    C1c=int(input())
    print("Indique 4 o 5 digitos correspondientes a la deuda de su tarjeta de credito")
    C1d=int(input())
    print("Indique 4 letras correspondientes a las inciales de sus nombres y apellidos")
    C2=(input()) 
    print("Indique numero entero positivo de 4 digitos(Todos distintos)correspondiente a la clave de su Tarjeta")
    C2c=int(input())
    print("Indique 4 o 5 digitos correspondientes a la deuda de su tarjeta de credito")
    C2d=int(input())
    print("Indique 4 letras correspondientes a sus inciales de sus nombres y apellidos")
    C3=(input()) 
    print("Indique numero entero positivo de 4 digitos(Todos distintos)correspondiente a la clave de su Tarjeta")
    C3c=int(input())
    print("Indique 4 o 5 digitos correspondientes a la deuda de su tarjeta de credito")
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
    print("Las letras correspondientes a las iniciales de sus nombres y apellidos (Cliente 1) son:", C1)
    print("El numero de 4 digitos correspondiente a la clave de su tarjeta es:", C1c)
    print("El numero indicado correspondiente a la deuda de su tarjeta es:", C1d )
    print("El monto de interes de deuda del cliente 1 es:", MI1)
    print("La deuda mas el monto de interes del CLIENTE 1 es:", DI1)
    print("El Pago minimo del CLIENTE 1 es:", PM1)

    print("Las letras correspondientes a las iniciales de sus nombres y apellidos (Cliente 2) son:", C2)
    print("El numero de 4 digitos correspondiente a la clave de su tarjeta es:", C2c)
    print("El numero indicado correspondiente a la deuda de su tarjeta es:", C2d )
    print("El monto de interes de deuda del cliente 2 es:", MI2)
    print("La deuda mas el monto de interes del CLIENTE 2 es:", DI2)
    print("El Pago minimo del CLIENTE 2 es:", PM2)

    print("Las letras correspondientes a las iniciales de sus nombres y apellidos (Cliente 3) son:", C3)
    print("El numero de 4 digitos correspondiente a la clave de su tarjeta es:", C3c)
    print("El numero indicado correspondiente a la deuda de su tarjeta es:", C3d )
    print("El monto de interes de deuda del cliente 3 es:", MI3)
    print("La deuda mas el monto de interes del CLIENTE 3 es:", DI3)
    print("El Pago minimo del CLIENTE 3 es:", PM3)

main()