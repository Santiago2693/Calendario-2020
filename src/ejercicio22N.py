PATH='puzzle_input/ejercicio22.txt'
PATH2='puzzle_input/ejercicio22M.txt'
def main1(ruta):
    jugador1=list()
    jugador2=list()
    separador=0
    sumaGanador=0
    #se obtienen las listas de numeros de cada jugador
    with open(ruta) as archivo:
        for line in archivo:
            auxiliar=line.strip()
            if auxiliar=="":
                separador+=1
            if auxiliar.isdigit() and separador==0:
                jugador1.append(int(auxiliar))
            if auxiliar.isdigit() and separador==1:
                jugador2.append(int(auxiliar))
    #mientras un jugador no se quede sin cartas que sigan jugando
    while not (len(jugador1)==0 or len(jugador2)==0):
        #si el jugador 1 lanza la carta mas alta se roba la carta del otro
        if jugador1[0]>=jugador2[0]:
            carta1=jugador1[0]
            carta2=jugador2[0]
            del jugador2[0]
            del jugador1[0]
            jugador1.append(carta1)
            jugador1.append(carta2)
        else:
        #de igual manera con el jugador 1
            carta1=jugador1[0]
            carta2=jugador2[0]
            del jugador2[0]
            del jugador1[0]
            jugador2.append(carta2)
            jugador2.append(carta1)
    #se verifica quien gano y se calcula la suma con las reglas del ejercicio
    if len(jugador1)==0:
        jugador2.reverse()
        for x in range(len(jugador2)):
            sumaGanador+=jugador2[x]*(x+1)
            x+=1
    else:
        jugador1.reverse()
        for x in range(len(jugador1)):
            sumaGanador+=jugador1[x]*(x+1)
            x+=1
    print("El ganador para la parte 1 suma",sumaGanador)

def juegoRecursivo(jugador1,jugador2):
    #se definen dos listas auxiliares para comprobar si el mazo actual de la partida
    #se ha jugado con anterioridad
    barajas1=list()
    barajas2=list()
    #variable para el ganador
    ganador=0
    #se guarda la lista de cartas de cada jugador en las listas auxiliares
    barajas1.append(jugador1.copy())
    barajas2.append(jugador2.copy())
    #las bandera para comprobar si ya existe repeticion de barajas
    bandera1=False
    bandera2=False
    #mientras algun jugador siga teniendo cartas que sigan jugando

    while not (len(jugador1)==0 or len(jugador2)==0):

        #si no tienen u baraja similar a barajas que se se han jugado en el juego
        #actual que sigan jugano

        if bandera1==False and bandera2==False:
            #si la carta que van a jugar es de igual o mayor al numero de cartas sobrantes
            #de su mazo se entra a un juego recursivo
            if (jugador1[0]<=(len(jugador1)-1)) and (jugador2[0]<=(len(jugador2)-1)):
                #se hace una copia de su mazo considerando las reglas del juego
                auxiliar1=list()
                auxiliar2=list()
                auxiliar1=jugador1.copy()
                auxiliar2=jugador2.copy()
                auxiliar1=auxiliar1[1:jugador1[0]+1]
                auxiliar2=auxiliar2[1:jugador2[0]+1]

                ganador=juegoRecursivo(auxiliar1,auxiliar2)
                #dependiendo del ganador del juego recursivo uno de los jugadores
                #robara la carta del otro
                if ganador==1:
                    carta1=jugador1[0]
                    carta2=jugador2[0]
                    del jugador2[0]
                    del jugador1[0]
                    jugador1.append(carta1)
                    jugador1.append(carta2)
                if ganador==2:
                    carta1=jugador1[0]
                    carta2=jugador2[0]
                    del jugador2[0]
                    del jugador1[0]
                    jugador2.append(carta2)
                    jugador2.append(carta1)
            #si no se cumple la condicion anterior el juego sigue como en
            #la parte 1 o el flujo normal;
            else:

                if jugador1[0]>=jugador2[0]:
                    carta1=jugador1[0]
                    carta2=jugador2[0]
                    del jugador2[0]
                    del jugador1[0]
                    jugador1.append(carta1)
                    jugador1.append(carta2)
                else:
                    carta1=jugador1[0]
                    carta2=jugador2[0]
                    del jugador2[0]
                    del jugador1[0]
                    jugador2.append(carta2)
                    jugador2.append(carta1)
            #se comprueba si el mazo resultante de la ronda actual es igual
            #a uno anterior, si es asi, se cambia las banderas para terminar el juego

            for listaAuxiliar in barajas1:
                if listaAuxiliar==jugador1:
                    bandera1=True
            for listaAuxiliar in barajas2:
                if listaAuxiliar==jugador2:
                    bandera2=True
        #caso contrario se para el juego y se determinar al ganador al jugador 1
        if bandera2==True or bandera1==True:
            ganador=1
            break
        #finalmente se añade el mazo actual a la lista de barajas jugadas
        barajas1.append(jugador1.copy())
        barajas2.append(jugador2.copy())
    #si alguien se queda sin cartas se determina el ganador
    if len(jugador1)==0:
        ganador=2
    if len(jugador2)==0:
        ganador=1

    return ganador







def main2(ruta):
    jugador1=list()
    jugador2=list()
    separador=0
    sumaGanador=0
    ganador=0
    #se obtiene la lista de cartas de cada jugador
    with open(ruta) as archivo:
        for line in archivo:
            auxiliar=line.strip()
            if auxiliar=="":
                separador+=1
            if auxiliar.isdigit() and separador==0:
                jugador1.append(int(auxiliar))
            if auxiliar.isdigit() and separador==1:
                jugador2.append(int(auxiliar))
    #empieza el juego recursivo
    ganador=juegoRecursivo(jugador1,jugador2)
    #dependiendo de cual jugador gane se a imprimir la suma de su mazo
    if ganador==2:
        jugador2.reverse()
        for x in range(len(jugador2)):
            sumaGanador+=jugador2[x]*(x+1)
            x+=1
    if ganador==1:
        jugador1.reverse()
        for x in range(len(jugador1)):
            sumaGanador+=jugador1[x]*(x+1)
            x+=1
    print("El ganador para la parte 2 suma",sumaGanador)



main1(PATH)
main2(PATH)
