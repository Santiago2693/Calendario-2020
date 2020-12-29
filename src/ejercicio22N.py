PATH='puzzle_input/ejercicio22.txt'
def main1(ruta):
    jugador1=list()
    jugador2=list()
    separador=0
    sumaGanador=0
    with open(ruta) as archivo:
        for line in archivo:
            auxiliar=line.strip()
            if auxiliar=="":
                separador+=1
            if auxiliar.isdigit() and separador==0:
                jugador1.append(int(auxiliar))
            if auxiliar.isdigit() and separador==1:
                jugador2.append(int(auxiliar))

    while not (len(jugador1)==0 or len(jugador2)==0):
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
    barajas1=list()
    barajas2=list()
    ganador=0
    barajas1.append(jugador1.copy())
    barajas2.append(jugador2.copy())
    while not (len(jugador1)==0 or len(jugador2)==0):
        bandera1=False
        bandera2=False
        if bandera1==True or bandera2==True:
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
            barajas1.append(jugador1.copy())
            barajas2.append(jugador2.copy())
            for listaAuxiliar in barajas1:
                if listaAuxiliar==jugador1:
                    bandera1=True
            for listaAuxiliar in barajas2:
                if listaAuxiliar==jugador2:
                    bandera2=True







def main2(ruta):
    jugador1=list()
    jugador2=list()
    separador=0
    sumaGanador=0
    with open(ruta) as archivo:
        for line in archivo:
            auxiliar=line.strip()
            if auxiliar=="":
                separador+=1
            if auxiliar.isdigit() and separador==0:
                jugador1.append(int(auxiliar))
            if auxiliar.isdigit() and separador==1:
                jugador2.append(int(auxiliar))
    juegoRecursivo(jugador1,jugador2)

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

main1(PATH)
main2(PATH)
