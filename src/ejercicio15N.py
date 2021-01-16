entrada=[14,8,16,0,1,17]
#funciona, pero no es eficiente cuando se le pasas muchas iteracciones
"""
def numeroHablado(numero,entrada):

        i=len(entrada)-1

        while (i!=numero-1):

            nuevoNumero=0

            for x in range(len(entrada)-2,-1,-1):

                if(entrada[x]==entrada[i]):
                    nuevoNumero=i-x
                    break
            entrada.append(nuevoNumero)
            i+=1
        print("El numero", numero,"hablado:",entrada[numero-1])
    """
#se va a ver cual es el numero habla 2020 o 30000000, por lo cual se realia una funcion que devuelve dicho numero
def numeroHablado(numero,entrada):
        ultimosDosValores=dict()
        #se instancia un diccionario para que almacene las dos ultimas ocurrencias de un numeroActual
        #si solo hay una ocurrencia el segundo valor de la tupla del elemento del diccionario sera 0
        for i in range(len(entrada)):

            ultimosDosValores[entrada[i]]=(i+1,0)
        i=len(entrada)
        numeroActual=entrada[i-1]
        #hasta que halle el numero hablado
        while (i!=numero):
            #si solo hay una ocurrencia del numero actual el siguiente numero es 0
            if ultimosDosValores[numeroActual][1]==0:
                numeroActual=0
            #si no se calcula el numero actual
            else:
                numeroActual=ultimosDosValores[numeroActual][0]-ultimosDosValores[numeroActual][1]
            i+=1
            #finalmente se actualiza la tupla de posiciones del diccionarios con la nueva ocurrencia
            if (numeroActual) in ultimosDosValores:
                ultimosDosValores[numeroActual]=(i,ultimosDosValores[numeroActual][0])
            #si no existe ocurrencia anterior crea un nuevo elemento en el diccionario donde el segundo elemento de la tupla es 0
            else:
                ultimosDosValores[numeroActual]=(i,0)

        print("El numero", numero,"hablado es:",numeroActual)
def main():
    numeroHablado(2020,entrada)
    numeroHablado(30000000,entrada)
main()
