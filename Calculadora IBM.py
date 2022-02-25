#CALCULAR EL INDICE DE MASA CORPORAL Y SU CLASIFICACION
#Aqui es donde obtenemos la cantidad de personas
personas = int(input("personas:"))
#Aqui verificamos que la cantidad sea mayor a 0 si no, no tiene sentido pedir nada
while personas > 0:
    #Le pedimos el nombre y lo guardamos en un input
    nombre = input("Su nombre por favor:")
    #Se pide al edad que siempre es un entero por eso el int()
    edad = int(input("Su edad en años por favor:"))
    #La masa en kilogramos (kg)
    peso = int(input("Su masa en kilogramos por favor:"))
    # como la altura es en metros y no centimetros hay que ponerle punto (ejemplo: 1.70) y por ende es un flotante float()
    altura = float(input("Su altura en metros por favor:"))
    #decimos que float (de estatura) es igual a altura
    float = altura
    #Calculo del IBM, masa(m) (En kg) entre la estatura(h) (en metros) elevada al cuadrado **2
    IBM = peso / altura**2
    #Le imprimos el IBM para que se ponga sad
    print("IBM: " + str(IBM))
    #Hacemos las distintas validaciones
    if IBM < 18.49:
        print ("Bajo peso")
    elif IBM >= 18.50 and IBM <= 25.00:
        print ("Normal")
    elif IBM >= 25.01 and IBM <= 30.00:
        print ("Sobrepeso")
    elif IBM >= 30.01:
        print ("obesidad")

    #Por cada persona a la que le pedimos los datos debemos restarle una (Porque ya la recorrimos)
    #si no el ciclo se vuelve infinito
    personas = personas - 1