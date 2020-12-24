PATH='puzzle_input/ejercicio14.txt'
def converirABinario(numero):
    auxiliar=list()
    while numero != 0:
        auxiliar.append(str(numero%2))
        numero=numero//2
    auxiliar.reverse()
    binario=""
    binario=binario.join(auxiliar)
    while len(binario)!=36:
        binario="0"+binario
    print (binario)
    return binario

def convertirADecimal(decimal):
    while decimal[0]=="0":
        decimal=decimal[1:]
    numero=0
    for i in range(len(decimal)):
        numero=numero+int(decimal[i])*pow(2, len(decimal)-i-1)
    print (numero)
    return numero

def main(ruta):
    diccionarioDatos=dict()
    mascaraActual=""
    with open(ruta) as f:
        for line in f:
            clave,valor=line.split(' = ')

            if not clave[0:3]=="mem":


                memoria= clave[4:len(clave)-1]
                auxiliar=list(converirABinario(int(valor)))
                print(mascaraActual)


                for i in range(len(mascaraActual)):
                    if not mascaraActual[i]=="x":
                        auxiliar[i]=mascaraActual[i]


                diccionarioDatos[memoria]= "".join(auxiliar)
                print(diccionarioDatos[memoria])


            else:

                mascaraActual=valor





main(PATH)
#converirABinario(8)
#convertirADecimal("1000010101010100101011")
