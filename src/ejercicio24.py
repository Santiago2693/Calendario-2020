PATH='puzzle_input/ejercicio24.txt'
PATH2 = 'puzzle_input/ejercicio24M.txt'
def procesarDatos(ruta):
    "la funcion devuelve una lista con los movimientos separados por comas"

    movimientos = list()
    with open(ruta) as archivo:
        for line in archivo:
            auxiliar=line.strip()

            i=0
            while i<len(auxiliar):

                if auxiliar[i]=="e" or auxiliar[i]=="w":
                    auxiliar=auxiliar[:i+1]+","+auxiliar[i+1:]
                    i+=2

                else:
                    auxiliara=auxiliar[:i+2]+","+auxiliar[i+2:]
                    i+=1

            movimientos.append(auxiliar[:-1].strip())

    return movimientos
def volterarPorDias(baldosas,dias,adyacentes):
    #ciclo para realizar este proceso de acuerdo al numero de dias
    for contador in range(dias):
        #creamos una copia del diccionario de baldosa para trabajar con este y no
        #modificar el real, por que todas las baldosas se voltean al mismo tiempo
        diccionarioAuxiliar=baldosas.copy()
        #por cada baldosa definida en el diccionario se va a realizar este proceso
        for clave in diccionarioAuxiliar:
            #se define un contador de baldas adyacentes negras
            contadorNegro=0
            #solo comprueba las baldosas definidas en el diccionrio
            for i in adyacentes:
                #se obtiene las coordenadas de todas las baldosas adyacentes a la actual
                adyacenteX=adyacentes[i][0]+clave[0]
                adyacenteY=adyacentes[i][1]+clave[1]
                #si esa baldosa esta definido en el diccionario y es negra se aumenta el contador
                if (adyacenteX,adyacenteY) in diccionarioAuxiliar and diccionarioAuxiliar[adyacenteX,adyacenteY]=="negro":
                    contadorNegro+=1

            #si la baldosa actual es negra y tiene 0 o mas de 2 baldasos adyacentes
            #de color negro se la cambia a blanco
            if diccionarioAuxiliar[clave]=="negro"and  (contadorNegro==0 or contadorNegro>2):
                baldosas[clave]="blanco"
            #si la baldosa actual es blanca y tiene dos baldosas adyacentes de color
            #negro se cambia a negro
            if diccionarioAuxiliar[clave]=="blanco"and contadorNegro==2:
                baldosas[clave]="negro"
            #aca se van a comprobar las baldosas blancas que no estan definidas
            #en el diccionario

            #si la baldosa actual es negra sirve para comprobar las baldosas
            #que no estan definas en el diccionario
            if diccionarioAuxiliar[clave]=="negro":
                #obtengo todas las baldosas adyacentes a esa baldosa negra
                for i in adyacentes:
                    adyacenteX=adyacentes[i][0]+clave[0]
                    adyacenteY=adyacentes[i][1]+clave[1]
                    #si la baldosa adyacente no esta definidas
                    if not(adyacenteX,adyacenteY) in diccionarioAuxiliar :
                        #contador para las baldosas negras adyacentes
                        contadorNegroVacios=0
                        #se comprueban todas las baldas adyacentes a esa baldosa no defnida
                        for j in adyacentes:
                                #si la baldosa existe y es negra
                                if (adyacenteX+adyacentes[j][0],adyacenteY+adyacentes[j][1]) in diccionarioAuxiliar and diccionarioAuxiliar[adyacenteX+adyacentes[j][0],adyacenteY+adyacentes[j][1]]=="negro":
                                    #se aumenta el contador de negros
                                    contadorNegroVacios+=1
                        #si el contador es 2 se define la baldosa y se lo pone en negro
                        if contadorNegroVacios==2:
                            baldosas[adyacentes[i][0]+clave[0],adyacentes[i][1]+clave[1]]="negro"






def main(ruta):
    #en este diccionario se encuentra
    #los valor x,y que debe moverse respecto al centro actual

    valoresMovimiento=dict()
    #representan todas las baldosas y su color actual
    baldosas=dict()
    listaMovimientos=procesarDatos(ruta)
    #los valores que deben aumentarse si se mueve a otro hexagono
    valoresMovimiento["e"]=(692,0)
    valoresMovimiento["w"]=(-692,0)
    valoresMovimiento["se"]=(346,-600)
    valoresMovimiento["sw"]=(-346,-600)
    valoresMovimiento["ne"]=(346,600)
    valoresMovimiento["nw"]=(-346,600)
    #print(listaMovimientos)

    #se coge cada patron de volteo de baldosas
    for movimiento in listaMovimientos:
        #se crea un diccionario que cada elemento respresenta cada movimiento,
        #para llegar a la baldosa a voltear
        listaAuxiliar=list()
        listaAuxiliar=movimiento.split(',')
        #la coordenadas actuales en el mapa de baldosas
        coordenadaX=0
        coordenadaY=0
        #print(movimiento)
        for i in listaAuxiliar:
            #por cada movimiento la coordenada actual aumentara
            #print(valoresMovimiento[i][0],",",valoresMovimiento[i][1])
            coordenadaX+=valoresMovimiento[i][0]
            coordenadaY+=valoresMovimiento[i][1]
            #print(coordenadaX,",",coordenadaY)
        #si la baldosa que se debe voltear esta definida la voltea
        if (coordenadaX,coordenadaY) in baldosas:
            if baldosas[coordenadaX,coordenadaY]=="negro":
                baldosas[coordenadaX,coordenadaY]="blanco"

            else:
                baldosas[coordenadaX,coordenadaY]="negro"
        #si no esta definida, la define y la voltea a negro
        else:
            baldosas[coordenadaX,coordenadaY]="negro"




    contador=0
    for clave in baldosas:
        if baldosas[clave]=="negro":
            contador+=1
    print ("El total de baldosas en color negro es de: ",contador)

    volterarPorDias(baldosas,100,valoresMovimiento)
    contador=0

    for clave in baldosas:
        if baldosas[clave]=="negro":
            contador+=1
    print ("El total de baldosas en color negro despues de 100 dia es de: ",contador)




main(PATH2)
