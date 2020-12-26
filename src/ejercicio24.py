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



def main(ruta):
    valoresMovimiento=dict()
    baldosas=dict()
    listaMovimientos=procesarDatos(ruta)
    valoresMovimiento["e"]=(346,0)
    valoresMovimiento["w"]=(-346,0)
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

            if baldosas[coordenadaX,coordenadaY]=="blanco":
                baldosas[coordenadaX,coordenadaY]="negro"

        else:
            baldosas[coordenadaX,coordenadaY]="negro"


    print(baldosas)

    contador=0
    for clave in baldosas:
        if baldosas[clave]=="negro":
            contador+=1
    print ("El total de baldosas en color negro es de: ",contador)











main(PATH)
