PATH='puzzle_input/ejercicio3.txt'
PATH2='puzzle_input/ejercicio3M.txt'
#defino una funcion que me devuleve el numero de arboles cortados pasando los pasos para la derecha y para abajo
def rutaASeguir(derecha,abajo,camino):
    posicionFila=0
    arbolesCortados=0
    longitud=len(camino[0])
    for i in range(0,len(camino)-abajo,abajo):
        #si se sale del camino en escencia debe regresar el inicio
        #ejemplo debe ir a la posicion 13, pero la maxima posicion es 10 por lo tanto
        #se va a la 2
        if posicionFila+derecha>=longitud:
            posicionFila=(posicionFila+derecha)-longitud

            if camino[i+abajo][posicionFila]=="#":
                arbolesCortados+=1
        #si no, solo sigue en el camino

        else:
            posicionFila+=derecha

            if camino[i+abajo][posicionFila]=="#":
                arbolesCortados+=1
            #en ambos casos si encuntran un arbol "#" auenta el contador de arbolesCortados
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
