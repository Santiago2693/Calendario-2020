PATH='puzzle_input/ejercicio24.txt'
def procesarDatos(ruta):
    "la funcion devuelve una lista con los movimientos separados por una coma"

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
    totalNegro=0
    diccionarioAuxiliar=baldosas.copy()
    for clave in diccionarioAuxiliar:
        contadorNegro=0
        for i in adyacentes:


            if (adyacentes[i][0]+clave[0],adyacentes[i][1]+clave[1]) in diccionarioAuxiliar and diccionarioAuxiliar[adyacentes[i][0]+clave[0],adyacentes[i][1]+clave[1]]=="negro":

                contadorNegro+=1
        if diccionarioAuxiliar[clave]=="negro"and  (contadorNegro==0 or contadorNegro>2):
            baldosas[clave]="blanco"
        if diccionarioAuxiliar[clave]=="blanco"and contadorNegro==2:
            baldosas[clave]="negro"











def main(ruta):
    valoresMovimiento=dict()
    baldosas=dict()
    listaMovimientos=procesarDatos(ruta)
    valoresMovimiento["e"]=(692,0)
    valoresMovimiento["w"]=(-692,0)
    valoresMovimiento["se"]=(346,-600)
    valoresMovimiento["sw"]=(-346,-600)
    valoresMovimiento["ne"]=(346,600)
    valoresMovimiento["nw"]=(-346,600)
    #print(listaMovimientos)
    for movimiento in listaMovimientos:

        listaAuxiliar=list()
        listaAuxiliar=movimiento.split(',')
        coordenadaX=0
        coordenadaY=0
        #print(movimiento)
        for i in listaAuxiliar:
            #print(valoresMovimiento[i][0],",",valoresMovimiento[i][1])
            coordenadaX+=valoresMovimiento[i][0]
            coordenadaY+=valoresMovimiento[i][1]
            #print(coordenadaX,",",coordenadaY)
        if (coordenadaX,coordenadaY) in baldosas:
            if baldosas[coordenadaX,coordenadaY]=="negro":
                baldosas[coordenadaX,coordenadaY]="blanco"

            else:
                baldosas[coordenadaX,coordenadaY]="negro"

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
    print ("El total de baldosas en color negro es de: ",contador)











main(PATH)
