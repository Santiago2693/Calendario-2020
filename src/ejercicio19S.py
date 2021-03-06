PATH='puzzle_input/ejercicio19S.txt'
PATH2='puzzle_input/ejercicio19.txt'
def recursivo(inicioCadena):

    #se coje todas las opciones del resultado de la cadena ejemplo o=[32,42]
    #coje la primera lista en otros caso existiran dos listas de un regla.
    transformacion=gramatica[inicioCadena]
    #esto es para eliminar unas comillas debido a que el archivo tiene
    #comillas y cuando lo lee se ponen dobles y si es esto ya es el final de una
    #cadena o el caso base, por lo cual se devuelve a si mismo ya que la regla
    #no se puede seguir tranformando
    if ['"a"'] in transformacion:
        return  ['a']
    if ['"b"'] in transformacion:
        return  ['b']
    #si la regla ya fue cnsiderada se devulve las cadenas generadas por dicha regla
    if inicioCadena in reglasConsideradas:
        return reglasConsideradas[inicioCadena]
    #se define una lista de posibilidades que guardaran todas las cadenas generadas
    #de la regla actual
    listaDePosibilidades=list()
    for posibilidades in transformacion:
        listaAuxiliar=list()
        for regla in posibilidades:
            subOpciones=recursivo(int(regla))
            #todo el hijo de la izquierda y lo que se derive simplemente se debe agregar a la
            #lista auxiliar, en otras palabras cuando la lista esta vacia se debe agregar todo a ella
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


gramaticaGenerada=recursivo(0)
#se ve cuantas reglas son parte de la regla 0
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
    """
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
    contador = 0
    for cadena in cadenas:
        quiebre42 = [True for a in range(len(cadena)//puntoQuiebre) if a in regla42]
        quiebre31 = [True for b in range(len(cadena)//puntoQuiebre) if b in regla31]
        sumatoria = len(quiebre42) + len(quiebre31)
        if sumatoria == (len(cadena)//puntoQuiebre):
            contador +=1
    return contador
print(recursivo2())
"""
    r42 = reglasConsideradas[42]
    r31 = reglasConsideradas[31]
    chunkSize = len(r42[0])

    count = 0
    for msg in cadenas:
        chunks42 = [False for _ in range(len(msg)//chunkSize)]
        chunks31 = [False for _ in range(len(msg)//chunkSize)]

        # determine which chunks come from which rules
        currChunk = 0
        for i in range(0, len(msg), chunkSize):
            if msg[i:i+chunkSize] in r42:
                chunks42[currChunk] = True
            if msg[i:i+chunkSize] in r31:
                chunks31[currChunk] = True
            currChunk += 1

        # does this message match the rules?
        count42, count31 = 0,0
        currChunk = 0
        if chunks42[currChunk] == True:
            count42 += 1
            currChunk +=1
            while currChunk < len(chunks42) and chunks42[currChunk]:
                count42 += 1
                currChunk += 1
            while currChunk < len(chunks31) and chunks31[currChunk]:
                count31 += 1
                currChunk += 1
            if currChunk == len(chunks31) and 0 < count31 < count42:
                count += 1

    return count

c = recursivo2()
print(c)
