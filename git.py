print ("bienbenidos a Vanidosa")
print ("")
print ("Quienes somos (1) ")
print ("Productos digite (2) ")
print ("Agendar cita (3) ")

u=int(input("digite opcion"))

if (u==1):
    print ("")
    print ("Historia")
    print ("Vanidosa. nació en 1979 en Barranquilla como una pequeña tienda con productos importados de uso general y de perfumería. En 1985, con el incremento de las ventas y la gran acogida entre los clientes locales, se inauguraron 3 tiendas en Barranquilla y una en Cartagena. 5 años después, aprovechando al máximo la apertura económica decretada, Vanidosa reorganizó la empresa a nivel administrativo, profesionalizó su operación e inició la apertura de tiendas en ciudades intermedias, transformándola con mucho esfuerzo y dedicación en una cadena nacional líder en productos importados")
    print ("")
    print ("---------------------------------")
    print ("")
    print ("Vision")
    print ("Ser reconocidos como líderes en belleza, higiene, salud y bienestar en Colombia y en otros países latinoamericanos.")
    print ("")
    print ("---------------------------------")
    print ("")
    print ("Mision")
    print ("Somos Belleza, Higiene, Salud y Bienestar. Trabajamos para mejorar tu estilo y calidad de vida.")
    print ("")
    print ("---------------------------------")
    print ("")
    print ("Valores")
    print ("Innovación, servicio, confianza, pasión, trabajo en equipo y excelencia")


if (u==2):
    print ("catalogo digite (1)")
    print ("servicios digite (2)")
   

    x=int(input("digite opcion"))
    if (x==1):
        print ("Maquillaje")
        

        print ("Stick corrector purificante")
        print ("30.000")
        print ("codigo 101")
        print ("---------------------------------")

        print ("Eternal Cream")
        print ("35.000")
        print ("codigo 102")
        print ("---------------------------------")

        print ("Eternal intensive serum")
        print ("31.000")
        print ("codigo 103")
        print ("---------------------------------")

        print ("Eternal Icy eye cream")
        print ("45.000")
        print ("codigo 104")
        print ("---------------------------------")

        print ("Eternal Repair body serum")
        print ("45.000")
        print ("codigo 105")
        print ("---------------------------------")

        print ("Eternal Sleeping oil")
        print ("35.000")
        print ("codigo 106")
        print ("---------------------------------")

        o=int(input (" si desea Compras (1), si no desea comprar (2) "))

        if o==1:
            print ("esta registrado")
            r=int(input (" si  (1), no  (2) "))
            if r == 1:
                id=int(input("ingresa tu identificacion "))
                if id==1111:
                    print ("gracias por su compra")
                else:
                    print ("usuario invalido")
            else:
                print ("registrarse ")        
                nombre=str(input("digite nombre "))
                g=str(input("digite su correo "))
                n=int(input("digite su numero de celular "))

                print ("bienbenido ",nombre," su identificacion es 1111 ")
        else:
            print ("gracia por ver nuestra pagina")
    if  x== 2:
        print (" sevicio") 

        print ("Manicura (parafina, IBX, gel, acrílico y semipermanente)")
        print ("30.000")
        print ("---------------------------------")
        
        print ("Pedicura")
        print ("30.000")
        print ("---------------------------------")

        print ("Maquillaje (novia, novio, invitados y todo tipo de eventos")
        print ("35.000")
        print ("---------------------------------")

        print ("Extensión, lifting y tinte de pestañas y microblending de cejas")
        print ("35.000")
        print ("---------------------------------")

        print ("Todo tipo de de depilaciones, incluido láser, IPL y Neodimio-YAG")
        print ("20.000")
        print ("---------------------------------")
if (u==3):
    print("usted está a punto de solicitar una cita")
    día=int(input("Ingrese el día para el cual requiere su cita "))
    mes=str(input("Ingrese el mes para el cual requiere su cita (EN LETRAS) "))
    hora=str(input("Ingrese la hora para la cual requiere su cita (ejemplo: 10:20)"))
    punto=int(input("Ingrese el punto fisico para el cual requiere su cita>: Chapinero(1), Fontibon(2), Soacha(3) "))
    if punto==1:
     print("Su cita queda programada para el dia" ,día, "del mes" ,mes, "a las" ,hora, "en Chapinero")
    elif punto==2:
        print("Su cita queda programada para el dia" ,día, "del mes" ,mes, "a las" ,hora, "en Fontibon")
    else:
        print("Su cita queda programada para el dia" ,día, "del mes" ,mes, "a las" ,hora, "en Soacha")


        







