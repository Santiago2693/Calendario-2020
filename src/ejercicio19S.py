PATH='puzzle_input/ejercicio19S.txt'

"""
Esta parte de codigo sirve para obtener lo siguiente y guardarlo en variables globale
1. Un diccionario con las reglas de la gramatica
2. Una lista de las cadenas que luego tendremos que comprobar
"""
gramatica = dict()
cadenas = list()
with open(PATH) as archivo:
    for line in archivo:
        if line == "\n":
            break
        datos = line.strip().split(":")
        gramatica[int(datos[0])]= [x.split() for x in datos[1].strip().split("|")]
    for line in archivo:
        cadenas.append(line.strip())

reglasConsideradas=dict()
def recursivo(inicioCadena):

    #se coje todas las opciones del resultado de la cadena ejemplo o=[32,42],
    #coje los dos numeros
    transformacion=gramatica[inicioCadena]
    #esto es para eliminar unas comillas debido a que el archivo tiene
    #comillas y cuando lo lee se ponen dobles y si es esto ya es el final de legal
    #cadena o el caso base, por lo cual se devuelve a si mismo
    if ['"a"'] in transformacion:
        return  ['a']
    if ['"b"'] in transformacion:
        return  ['b']
    #se define una lista de todas las cadenas que se formaran con la regla
    if inicioCadena in reglasConsideradas:
        return reglasConsideradas[inicioCadena]
    listaDePosibilidades=list()
    for posibilidades in transformacion:
        listaAuxiliar=list()
        for regla in posibilidades:
            subOpciones=recursivo(int(regla))
            #todo el hijo de la izquierda y lo que se deribe simplemente se debe agregar a legal
            #lista auxiliar, en otras palabras cuando la lista esta vacia se debe agregar algo a ella
            if len(listaAuxiliar)==0:
                listaAuxiliar=subOpciones.copy()
            #se define todas las combinaciones posible que van a generarse en el hijo de la derecha
            #por ello debo iterar y copiar

            else:
                unirReglas=list()
                for a in subOpciones:
                    for b in listaAuxiliar:
                        unirReglas.append(b+a)
                listaAuxiliar=unirReglas.copy()
        listaDePosibilidades+=listaAuxiliar
    reglasConsideradas[inicioCadena]=listaDePosibilidades

    return listaDePosibilidades

gramaticaGenerada=recursivo(0)
contador=0
for a in cadenas:
    if a in gramaticaGenerada:
        contador+=1
print(contador)
