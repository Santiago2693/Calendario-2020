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

#una buena alternativa para hacer mas eficiente la busqueda de numeros
#puede ser ordenar primero el preambulo para asi delimitar el espacio
#de busqueda de los numeros dentro del preambulo y asi poder buscar solo
#en un intervalo de esa lista
def main(ruta, preamble):
    lista = list()
    with open(ruta) as f:
        for line in f:
            lista.append(int(line.strip()))
    i = 0
    while True:
        #ordeno mi preambulo
        preambulo = sorted(lista[i:i+preamble])
        #ahora voy a buscar en la mitad inferior o superior,
        #dependiendo de en que sector se encuentre el resto
        encontrado = False
        for j in range(25):
            resto = abs(preambulo[j]-lista[i+preamble])
            if not busquedaBinaria(resto, preambulo) == -1:
                i+=1
                encontrado = True
                break
        if not encontrado:
            return lista[i+preamble]

print(main(PATH, 25))
