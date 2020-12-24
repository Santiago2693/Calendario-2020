PATH='puzzle_input/ejercicio14.txt'
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

def convertirADecimal(decimal):
    while decimal[0]=="0":
        decimal=decimal[1:]
    numero=0
    for i in range(len(decimal)):
        numero=numero+int(decimal[i])*pow(2, len(decimal)-i-1)

    return numero

def main(ruta):
    diccionarioDatos=dict()
    mascaraActual=""

    with open(ruta) as f:
        for line in f:
            clave,valor=line.split(' = ')

            if clave[0:3]=="mem":


                memoria= clave[4:len(clave)-1]
                auxiliar=list(convertirABinario(int(valor)))


                #print(mascaraActual)
                for i in range(len(mascaraActual)):
                    if mascaraActual[i]=="1":
                        auxiliar[i]="1"
                    if mascaraActual[i]=="0":
                        auxiliar[i]="0"



                diccionarioDatos[memoria]= "".join(auxiliar)
                #print(diccionarioDatos[memoria])


            else:

                mascaraActual=valor.strip()

    total=0
    for clave in diccionarioDatos:
        total=total+int(convertirADecimal(diccionarioDatos[clave]))
    print (total)




main(PATH)
#converirABinario(8)
#convertirADecimal("1000010101010100101011")
