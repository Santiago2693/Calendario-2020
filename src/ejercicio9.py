import functools
PATH = 'puzzle_input/ejercicio9M.txt'
def busquedaBinaria(numero, lista):
    """
    Esta busqueda no me devuelve la posisicion en el array original
    pero me devuelve un entero positivo si es que el valor se encuentra
    y -1 caso contrario
    """
    listaTemp = lista
    medio = len(lista)
    while medio >0:
        n = len(listaTemp)
        medio = n//2
        if listaTemp[medio] == numero:
            return medio
        elif listaTemp[medio]> numero:
            listaTemp = listaTemp[0:medio]
            continue
        else:
            listaTemp = listaTemp[medio:n]
            continue
    return -1

def encontrarSubset(suma, lista):
    """
    Esta funcion devuelve una lista de numeros contiguos dentro del parametro
    lista que suman el valor del parametro suma
    """
    base = 0
    contador = 2
    while  contador <= len(lista):
        if functools.reduce(lambda a,b: a+b, lista[base:base+contador]) == suma:
            return lista[base:base+contador]
        elif functools.reduce(lambda a,b: a+b, lista[base:base+contador])> suma:
            base += 1
            contador = 2
        else:
            contador +=1
    return []


def main(ruta, preamble):
    lista = list()
    with open(ruta) as f:
        for line in f:
            lista.append(int(line.strip()))
    i = 0
    #una buena alternativa para hacer mas eficiente la busqueda de numeros
    #puede ser ordenar primero el preambulo para asi delimitar el espacio
    #de busqueda de los numeros dentro del preambulo y asi poder buscar solo
    #en un intervalo de esa lista
    while True:
        #ordeno mi preambulo
        preambulo = sorted(lista[i:i+preamble])
        #ahora voy a buscar en la mitad inferior o superior,
        #dependiendo de en que sector se encuentre el resto
        encontrado = False
        for j in range(preamble):
            resto = abs(preambulo[j]-lista[i+preamble])
            if not busquedaBinaria(resto, preambulo) == -1:
                i+=1
                encontrado = True
                break
        if not encontrado:
            valor =lista[i+preamble]
            break
    print("el numero que no sigue la secuencia es: ",valor)
    #ahora buscamos la secuencia
    subset = sorted(encontrarSubset(valor, lista))
    #retornamos la falla de la encriptacion
    return subset[0]+ subset[len(subset)-1]


print("La falla de la encriptacion es:",main(PATH, 25))
