entrada=[14,8,16,0,1,17]
#funcuiona, pero no es eficiente cuando se le pasas muchas iteracciones
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
def numeroHablado(numero,entrada):
        ultimosDosValores=dict()
        for i in range(len(entrada)):

            ultimosDosValores[entrada[i]]=(i+1,0)
        i=len(entrada)
        numeroActual=entrada[i-1]

        while (i!=numero):

            if ultimosDosValores[numeroActual][1]==0:
                numeroActual=0
            else:
                numeroActual=ultimosDosValores[numeroActual][0]-ultimosDosValores[numeroActual][1]
            i+=1
            if (numeroActual) in ultimosDosValores:
                ultimosDosValores[numeroActual]=(i,ultimosDosValores[numeroActual][0])
            else:
                ultimosDosValores[numeroActual]=(i,0)

        print("El numero", numero,"hablado es:",numeroActual)
def main():
    numeroHablado(2020,entrada)
    numeroHablado(30000000,entrada)
main()
