PATH='puzzle_input/ejercicio1.txt'
PATH2='puzzle_input/ejercicio1M.txt'
def main(ruta):
    #itero por el archivo y saco los numeros en una lista
    numeros = list()
    multiplicacion=0
    multiplicacionDeTres=0
    with open(ruta) as archivo:
        for line in archivo:
            numeros.append(int(line.strip()))
    #resto el actual numero a 2020 para ver si hallo el complementario para sumar el 2020
    for i in range(len(numeros)):
        #si la resta es negativa ya no se puede sumar 2020, por dicha razon el if
        auxiliar=2020-numeros[i]

        #print (auxiliarDeTres)
        if auxiliar>0:
            #busco el complementario para que sumen 2020 y si existe saco su multiplicacion
            for j in range(i+1,len(numeros)):
                if auxiliar==numeros[j]:
                    multiplicacion=numeros[i]*numeros[j]
                #de manera similar vuelvo a restar los dos numeros a 2020 para encontrar un tercer complementario que de 2020 su suma
                auxiliarDeTres=2020-numeros[i]-numeros[j]
                if auxiliarDeTres>0:
                    for k in range(j+1,len(numeros)):
                        if auxiliarDeTres==numeros[k]:
                            multiplicacionDeTres=numeros[i]*numeros[j]*numeros[k]

    print ("La multiplicación de los dos números que suman 2020 es:",multiplicacion)
    #print("La multiplicación de los tres números que suman 2020 es:",multiplicacionDeTres)


main(PATH2)
