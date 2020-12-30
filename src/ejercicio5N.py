PATH ='puzzle_input/ejercicio5.txt'
PATH2 ='puzzle_input/ejercicio5M.txt'
def calcularAsiento(asiento,numeroFilas,numeroColumnas):

    inicioFila=0
    finFila=int(numeroFilas)
    inicioColumna=0
    finColumna=int(numeroColumnas)
    for i in range(0,len(asiento[0])):
        if asiento[0][i]=="F":
            finFila=(finFila+inicioFila)/2
        if asiento[0][i]=="B":
            inicioFila=(finFila+inicioFila)/2

    for i in range(0,len(asiento[1])):
        if asiento[1][i]=="L":
            finColumna=(finColumna+inicioColumna)/2
        if asiento[1][i]=="R":
            inicioColumna=(finColumna+inicioColumna)/2
    return(inicioFila*8+inicioColumna)



def main(ruta,numeroFilas,numeroColumnas):
    asientos = list()
    posicionAientos=list()
    posicionMasAlta=0

    with open(ruta) as archivo:
        for line in archivo:
            auxiliar=line.strip()
            asientos.append((auxiliar[0:7], auxiliar[7:len(auxiliar)]))
    for asiento in asientos:
        posicionAientos.append(calcularAsiento(asiento,numeroFilas,numeroColumnas))
    for posicionAiento in posicionAientos:

        if posicionAiento>posicionMasAlta:
            posicionMasAlta=posicionAiento


    print("El asiento para la parte 1 es",posicionMasAlta)
    posicionAientos.sort()
    asientoPropio=posicionAientos[0]
    for posicionAiento in posicionAientos:
        if posicionAiento==asientoPropio:
            asientoPropio+=1
        else:
            break
    print("El asiento para la parte 2 es",asientoPropio)








main(PATH,128,8)
