PATH='puzzle_input/ejercicio1.txt'
PATH2='puzzle_input/ejercicio1M.txt'
def main(ruta):
    #la funcion devuelve una lista con los numeros del archivo
    numeros = list()
    multiplicacion=0
    multiplicacionDeTres=0
    with open(ruta) as archivo:
        for line in archivo:
            numeros.append(int(line.strip()))

    for i in range(len(numeros)):
        auxiliar=2020-numeros[i]

        #print (auxiliarDeTres)
        if auxiliar>0:
            for j in range(i+1,len(numeros)):
                if auxiliar==numeros[j]:
                    multiplicacion=numeros[i]*numeros[j]

                auxiliarDeTres=2020-numeros[i]-numeros[j]
                if auxiliarDeTres>0:
                    for k in range(j+1,len(numeros)):
                        if auxiliarDeTres==numeros[k]:
                            multiplicacionDeTres=numeros[i]*numeros[j]*numeros[k]

    print ("La multiplicación de los dos números que suman 2020 es:",multiplicacion)
    print("La multiplicación de los tres números que suman 2020 es:",multiplicacionDeTres)


main(PATH2)
