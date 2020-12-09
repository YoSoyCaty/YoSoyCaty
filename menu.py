import os
import sys


while True:

    os.system('cls')

    print("========================")
    print("  BIENVENIDO AL EMULADOR  ")
    print("========================")
    print("Aquí se representara el funcionamiento de los módulos del sistema")
    print("Aquello que visualizará/hará el usuario se mostrara en MAYUSCULAS")
    print("y lo que no, se mostrara en minusculas")
    print("Para proseguir en los procedimientos tan solo precione ENTER")
    print("a no ser que se le indique lo contrario")
    print("========================")
    print("1) comprar tarjeta")
    print("2) entrar al metro")
    print("3) salir del metro")
    print("4) guardar historial")
    print("5) consultar datos")
    print("9) salir de la aplicación")
    print("========================")

    option = input("> ")

    os.system('cls')

    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '9':
        print("la opcion ingresada no es valida, intentelo de nuevo")
        print("1) comprar tarjeta")
        print("2) entrar al metro")
        print("3) salir del metro")
        print("4) guardar historial")
        print("5) consultar datos")
        print("9) salir dee la aplicación")
        print("========================")
        option = input("> ")

    os.system('cls')

    if option == '1':
        print("COMPRAR SMART-CARD\n============================")
        
        print("SELECCIONE EL SALDO DE LA TARJETA\n1)2000\n2)5000\n3)10000")
        saldo = input(">")
        os.system('cls')

        while saldo != '1' and saldo != '2' and saldo != '3':
            print("la opcion ingresada no es valida, intentelo de nuevo")
            print("SELECCIONE EL SALDO DE LA TARJETA\n1)2000\n2)5000\n3)10000")
            saldo = input(">")
            os.system('cls')
        
        if saldo == '1':
            print("calculando cobro")
            print("SELECCIONE UN METODO DE PAGO\n1) EFECTIVO\n2) TARJETA")
            cobro = input(">")
            os.system('cls')

            while cobro != '1' and cobro != '2':
                print("la opcion ingresada no es valida, intentelo de nuevo")
                print("SELECCIONE UN METODO DE PAGO\n1) EFECTIVO\n2) TARJETA")
                cobro = input(">")
                os.system('cls')
            
            if cobro == '1':
                print("calculando cobro")
                print("MONTO A PAGAR = 2000\nINGRESE EFECTIVO")
                input("precione ENTER para continuar\n> ")
                os.system('cls')
                print("entregando smart-card")
                print("GRACIAS POR SU COMPRA")
                print("============================\nfin de la operación\n============================")
                input("precione ENTER para continuar\n> ")
                os.system('cls')

            if cobro == '2':
                print("calculando cobro")
                print("MONTO A PAGAR = 2000\nINGRESE TARJETA")
                input("precione ENTER para continuar\n> ")
                os.system('cls')
                print("entregando smart-card")
                print("GRACIAS POR SU COMPRA")
                print("devuelve la tarjeta")
                print("============================\nfin de la operación\n============================")
                input("precione ENTER para continuar\n> ")
                os.system('cls')

        if saldo == '2':
            print("calculando cobro")
            print("SELECCIONE UN METODO DE PAGO\n1) EFECTIVO\n2) TARJETA")
            cobro = input(">")
            os.system('cls')

            while cobro != '1' and cobro != '2':
                print("la opcion ingresada no es valida, intentelo de nuevo")
                print("SELECCIONE UN METODO DE PAGO\n1) EFECTIVO\n2) TARJETA")
                cobro = input(">")
                os.system('cls')
            
            if cobro == '1':
                print("calculando cobro")
                print("MONTO A PAGAR = 5000\nINGRESE EFECTIVO")
                input("precione ENTER para continuar\n> ")
                os.system('cls')
                print("entregando smart-card")
                print("GRACIAS POR SU COMPRA")
                print("============================\nfin de la operación\n============================")
                input("precione ENTER para continuar\n> ")
                os.system('cls')

            if cobro == '2':
                print("calculando cobro")
                print("MONTO A PAGAR = 5000\nINGRESE TARJETA")
                input("precione ENTER para continuar\n> ")
                os.system('cls')
                print("entregando smart-card")
                print("GRACIAS POR SU COMPRA")
                print("devuelve la tarjeta")
                print("============================\nfin de la operación\n============================")
                input("precione ENTER para continuar\n> ")
                os.system('cls')

        if saldo == '3':
            print("calculando cobro")
            print("SELECCIONE UN METODO DE PAGO\n1) EFECTIVO\n2) TARJETA")
            cobro = input(">")
            os.system('cls')

            while cobro != '1' and cobro != '2':
                print("la opcion ingresada no es valida, intentelo de nuevo")
                print("SELECCIONE UN METODO DE PAGO\n1) EFECTIVO\n2) TARJETA")
                cobro = input(">")
                os.system('cls')
            
            if cobro == '1':
                print("calculando cobro")
                print("MONTO A PAGAR = 10000\nINGRESE EFECTIVO")
                input("precione ENTER para continuar\n> ")
                os.system('cls')
                print("entregando smart-card")
                print("GRACIAS POR SU COMPRA")
                print("============================\nfin de la operación\n============================")
                input("precione ENTER para continuar\n> ")
                os.system('cls')

            if cobro == '2':
                print("calculando cobro")
                print("MONTO A PAGAR = 10000\nINGRESE TARJETA")
                input("precione ENTER para continuar\n> ")
                os.system('cls')
                print("entregando smart-card")
                print("GRACIAS POR SU COMPRA")
                print("devuelve la tarjeta")
                print("============================\nfin de la operación\n============================")
                input("precione ENTER para continuar\n> ")
                os.system('cls')

            
        
    if option == '2':
        print("ENTRAR AL METRO\n============================")
        print("PASE LA SMART-CARD POR EL TORNIQUETE DE ENTRADA")
        input("precione ENTER para continuar\n> ")
        os.system('cls')

        print("guardando punto de inicio del trayecto")
        print("PASE A TRAVES DEL TORNIQUETE DE ENTRADA")
        print("============================\nfin de la operación\n============================")
        input("precione ENTER para continuar\n> ")
        os.system('cls')
        
    if option == '3':
        print("SALIR DE METRO\n============================")
        print("PASE LA SMART-CARD POR EL TORNIQUETE DE SALIDA")
        input("precione ENTER para continuar\n> ")
        os.system('cls')
        
        print("guardando punto de termino de trayecto")
        print("calculando monto a descontar de la smart-card")
        print("cobro realizado")
        print("PASE A TRAVEZ DEL TORNIQUETE DE SALIDA")
        print("============================\nfin de la operación\n============================")
        input("precione ENTER para continuar\n> ")
        os.system('cls')
        
    if option == '4':
        print("GUARDAR HISTORIA\n============================")
        print("INGRESA AL PC")
        print("SELECCIONA LA OPCIÓN DE 'GUARDAR HISTORIAL'")
        print("muestra formulario para el guardado del historial")
        input("precione ENTER para continuar\n> ")
        os.system('cls')
        
        print("RELLENA EL HISTORIAL")
        print("SELECCIONA LA OPCIÓN GUADAR")
        print("guarda los datos")
        print("============================\nfin de la operación\n============================")
        input("precione ENTER para continuar\n> ")
        os.system('cls')
        
    if option == '5':
        print("CONSULTAR DATOS")
        print("INGRESA AL PC")
        print("SELECCIONA LA OPCIÓN 'CONSULTAR DATOS'")
        print("muestra las tablas de datos")
        print("============================\nfin de la operación\n============================")
        input("precione ENTER para continuar\n> ")
        os.system('cls')
        
    if option == '9':
        print("gracias por leer")
        break
    








    
