PATH='puzzle_input/ejercicio14.txt'
PATH2='puzzle_input/ejercicio14M.txt'
#esta funcion convierte un númeo decimal a binario anteponiendo los ceros necesarios
#para que su tamaño sea de 36
def convertirABinario(numero):
    auxiliar=list()
    while numero != 0:
        auxiliar.append(str(numero%2))
        numero=numero//2
    auxiliar.reverse()
    binario=""
    binario=binario.join(auxiliar)
    while len(binario)!=36:
        binario="0"+binario
    #print (binario)
    return binario
#esta funcion convierte un numero binario a decimal
def convertirADecimal(decimal):
    while decimal[0]=="0":
        decimal=decimal[1:]
    numero=0
    for i in range(len(decimal)):
        numero=numero+int(decimal[i])*pow(2, len(decimal)-i-1)

    return numero
#esta funcion obtiene todas las posibles direcciones de memoria
def obtenerDirecciones(direccion):
    #caso base de la funcion rescursiva
    if not "X" in direccion:
        return direccion
    else:
        #se define una varible donde estaran todas las direcciones de memoria
        todasLasDirecciones=""
        #obtiene la primera ocurrencia de X
        i=direccion.index("X")
        #la misma direccion, pero remplazo la X por un 0
        nuevaDireccion0=direccion[:i]+"0"+direccion[i+1:]
        #la misma direccion, pero remplazo la X por un 1
        nuevaDireccion1=direccion[:i]+"1"+direccion[i+1:]
        #Se aplica recursividad, para que todo estese sin "X"
        todasLasDirecciones=todasLasDirecciones+obtenerDirecciones(nuevaDireccion0)+","
        todasLasDirecciones=todasLasDirecciones+obtenerDirecciones(nuevaDireccion1)
        return todasLasDirecciones



#parte 1
def main(ruta):
    diccionarioDatos=dict()
    mascaraActual=""

    with open(ruta) as f:
        #se divide cada elemento del archivo en clave, valor
        for line in f:
            clave,valor=line.split(' = ')
            #si no es una mascara el valor que se deberia guardar en memoria
            #es transformado a binario
            if clave[0:3]=="mem":

                #se extrae la direccion de memoria
                memoria= clave[4:len(clave)-1]
                auxiliar=list(convertirABinario(int(valor)))

                #el valor que deberia ir en la direccion de memoria es transformado
                #para que se ajusten a la regla de la macara actual.
                #print(mascaraActual)
                for i in range(len(mascaraActual)):
                    if not mascaraActual[i]=="X":
                        auxiliar[i]=mascaraActual[i]


                #se guarda el valor en el espacio de memoria correspondiente, por medio
                #de un diccionario
                diccionarioDatos[memoria]= "".join(auxiliar)
                #print(diccionarioDatos[memoria])


            else:
                #si es una mascara se tomara el valor de l mascaraActual para
                #la transformacion necesaria
                mascaraActual=valor.strip()

    total=0
    #se suman todos los espacios de memoria para obtener el valor total, primero convirtiendo el
    #numero binario a decimal
    for clave in diccionarioDatos:
        total=total+int(convertirADecimal(diccionarioDatos[clave]))
    print ("La suma de todos los valores en memoria de la parte 1 es:",total)
#parte 2
def main2(ruta):
    diccionarioDatos=dict()
    mascaraActual=""

    with open(ruta) as f:
        for line in f:
            clave,valor=line.split(' = ')
            #sigue exactamente la misma logia que la parte 1, sin embargo el que se debe transformar
            #son las diecciones de memoria
            if clave[0:3]=="mem":


                memoria= clave[4:len(clave)-1]

                auxiliar=list(convertirABinario(int(memoria)))



                for i in range(len(mascaraActual)):
                    if mascaraActual[i]=="1":
                        auxiliar[i]="1"
                    if mascaraActual[i]=="X":
                        auxiliar[i]="X"
                #se obtiene un string con la direccion
                posiblesDirecciones= "".join(auxiliar)
                todasLasDirecciones=obtenerDirecciones(posiblesDirecciones)
                listaDirecciones=list()
                listaDirecciones=todasLasDirecciones.split(',')
                for direccion in listaDirecciones:
                    diccionarioDatos[direccion]= valor


                #print(diccionarioDatos[memoria])


            else:

                mascaraActual=valor.strip()

    total=0
    for clave in diccionarioDatos:
        total=total+int(diccionarioDatos[clave])
    print ("La suma de todos los valores en memoria de la parte 2 es: ",total)






main(PATH2)
main2(PATH2)
#converirABinario(8)
#convertirADecimal("1000010101010100101011")
