PATH='puzzle_input/ejercicio3.txt'
def rutaASeguir(derecha,abajo,camino):
    posicionFila=0
    arbolesCortados=0
    longitud=len(camino[0])
    for i in range(0,len(camino)-abajo,abajo):

        if posicionFila+derecha>=longitud:
            posicionFila=(posicionFila+derecha)-longitud

            if camino[i+abajo][posicionFila]=="#":
                arbolesCortados+=1


        else:
            posicionFila+=derecha

            if camino[i+abajo][posicionFila]=="#":
                arbolesCortados+=1
    return arbolesCortados

def main(ruta):
    #la funcion devuelve una lista con los numeros del archivo
    camino = list()

    with open(ruta) as archivo:
        for line in archivo:
            camino.append(line.strip())



    print("El total de arboles cortados de la parte 1 es de:",rutaASeguir(3,1,camino))
    print("La multiplicacion de los arboles cortados de la parte 2 es de:",rutaASeguir(1,1,camino)*rutaASeguir(3,1,camino)*rutaASeguir(5,1,camino)*rutaASeguir(7,1,camino)*rutaASeguir(1,2,camino))












main(PATH)
