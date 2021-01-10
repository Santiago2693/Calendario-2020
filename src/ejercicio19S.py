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
print("El conjunto de las cadenas validas para la parte 1 es de:",contador)
#para la parte 2 la regla 8 antes era 42 ahora es 42 |42 8
#y la regla 11 era 42 31 ahora es 42 31| 42 11 31, por lo cual nos enfrentamos
#a que se puede entrar en un bucle infinito al genera las cadena 42 42 42, ademas
#la regla 11 ahora tiene 3 posibilidades deferentes en lugar de 2 como las otras
def recursivo2():
    #si analizamos la gramatica si aparece los numeros que se repetiran si se genera
    #un bucle infinito son 42 y 31, por lo cual de las reglas consideradas se va a sacar su
    #transformacion para estas reglas
    regla42=reglasConsideradas[42]
    regla31=reglasConsideradas[31]
    #for r in regla42:
        #print(r)
    #for r in regla31:
        #print(r)
    #afortunadamente ambas reglas generan gramaticas
    #de la misma longitud, por lo cual podemos obtener un
    #punto de quiebre
    puntoQuiebre=len(regla31[0])
    #para este punto hallar todas las reglas posibles no es eficiente
    #por lo cual ahora se va a analizar la cadena y encontraar si se
    #deriva de 0
    for cadena in cadenas:
        quiebre42 = [False for a in range(len(cadena)//puntoQuiebre)]
        quiebre31 = [False for b in range(len(cadena)//puntoQuiebre)]

recursivo2()
