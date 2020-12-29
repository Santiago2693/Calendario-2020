PATH = 'puzzle_input/ejercicio10M.txt'
def procesarInput(ruta):
    with open(ruta) as f:
        adaptadores = list()
        for linea in f:
            adaptadores.append(int(linea.strip()))
        #en esta lista incluyo el chargin outlet
        adaptadores.append(0)
    return adaptadores

def calcularDiferencias(lista):
    """
    por la descripcion del ejercicio, lo mas logico parece ordenar primero la lista
    """
    adaptadores = sorted(lista)
    adaptadores.append(adaptadores[len(adaptadores)-1]+3)
    contadorDiferencias = dict()
    i=0
    while i < len(adaptadores)-1:
        diferencia = adaptadores[i+1] - adaptadores[i]
        i+=1
        if diferencia not in list(contadorDiferencias.keys()):
            contadorDiferencias[diferencia]= 1
        else:
            contadorDiferencias[diferencia]+= 1

    return contadorDiferencias

def main(ruta):
    input = procesarInput(ruta)
    distribucion = calcularDiferencias(input)
    resultadoParte1 = distribucion[1] * distribucion[3]
    print(distribucion)
    print("El resultado de la multiplicacion de los valore de distribucion es: ",resultadoParte1)
main(PATH)
