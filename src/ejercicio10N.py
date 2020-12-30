PATH = 'puzzle_input/ejercicio10M.txt'
PATH2 = 'puzzle_input/ejercicio10.txt'
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

#para la parte 2 otra vez flashbacks del ejercicio 19
class Nodo():
    def __init__(self,padre=None, contenido=None):
        self.padre = padre
        self.contenido = contenido
        self.hijos = list()

    def setHijo(self, nuevoHijo):
        """
        El parametro nuevoHijo tiene que ser un tipo nodo
        """
        nuevoHijo.setPadre(self)
        self.hijos.append(nuevoHijo)
        #con la linea anterior me aseguro que los hijos vayan de izq a derecha
    def delHijo(self, hijo):
        hijo.setPadre(None)
        self.hijos.remove(hijo)

    def getPadre(self):
        return self.padre

    def setPadre(self, nodoPadre):
        self.padre = nodoPadre

    def setContenido(self, contenido):
        self.contenido = contenido

    def getContenido(self):
        return self.contenido

    def getHijos(self):
        return self.hijos

class Arbol():
    def __init__(self):
        self.raiz = None

    def insertarNodo(self, elemento, clavePadre= None):
        """
        Elemento es de tipo Nodo
        """
        if self.raiz == None:
            self.raiz = elemento
        elif not clavePadre == None:
            #vendria a ser la insercion bajo algun otro nodo
            referencia = self.buscarNodo(clavePadre)
            if not referencia == None:
                referencia.setHijo(elemento)

    def buscadorHelper(clave, nodoInicial):
        #caso base (?)
        if nodoInicial.getContenido() == clave:
            return nodoInicial
        #primero obtenemos los hijos del nodo nodoInicial
        if len(nodoInicial.getHijos())>=1:
            for node in nodoInicial.getHijos():
                #caso recursivo
                encontrado = Arbol.buscadorHelper(clave, node)
                if not  encontrado == None:
                    return encontrado

        return None

    def buscarNodo(self, clave):
        #bucamos sobre el arbol
        return Arbol.buscadorHelper(clave, self.raiz)

    def eliminarNodo(self, clave):
        pass


    def __str__(self):
        cadenaResultante = ""
        if not self.raiz == None:
            nuevaLista = list()
            for lista in self.recorrerXNivel():
                lis = [t.getContenido() for t in lista]
                nuevaLista.append(lis)
            return str(nuevaLista)
        else:
            return "Arbol vacio"
    def recorrerXNivel(self):
        """
        partimos desde que en un nivel n dado
        los hijos de todos los nodos del nivel n estaran en el nivel n+1
        Este metodo devuelve una lista que contiene sublistas en las cuales
        se recorre al arbol por nivel, asi los mas a la iz son niveles superiores
        """
        masNiveles = True
        masNiveles = masNiveles and not self.raiz==None
        niveles = list()
        nodoBase = self.raiz
        niveles.append([nodoBase]) #que vendria a ser el nivel 0
        while masNiveles:
            #ahora buscariamos los hijos para el siguiente nivel
            nivelAnteior = len(niveles) -1
            comprobacionNivel = False #asumimos que el siguiente nivel ya esta
            #vacio, esto es, que ya no tiene mas hijos
            nuevoNivel = list()
            for nodos in niveles[nivelAnteior]:
                if not nodos.getHijos() == []:
                    comprobacionNivel = comprobacionNivel or True
                    nuevoNivel+= nodos.getHijos()
            if comprobacionNivel:
                niveles.append(nuevoNivel)
            else:
                break

        return niveles

def contarOpciones(nodoInicial, adaptadores, memoria):
    outPutFinal = adaptadores[len(adaptadores)-1]+3
    #caso base (?)
    if nodoInicial.getContenido()+3 > outPutFinal:
        return 0
    elif nodoInicial.getContenido()+3 == outPutFinal:
        return 1
    else:
        formas = 0
        valorBase = nodoInicial.getContenido()
        if valorBase in list(memoria.keys()):
            return memoria[valorBase]
        conjuntoAdmitidos = set(t for t in range(valorBase+1,valorBase+4))
        disponibles = conjuntoAdmitidos.intersection(set(adaptadores))
        for adaptador in list(disponibles):
            hijo = Nodo(contenido = adaptador)
            nodoInicial.setHijo(hijo)
            formas += contarOpciones(hijo,adaptadores, memoria)
        if valorBase not in list(memoria.keys()):
            memoria[valorBase] = formas
        return formas



def main(ruta):
    nodosParseados = dict()
    input = procesarInput(ruta)
    distribucion = calcularDiferencias(input)
    resultadoParte1 = distribucion[1] * distribucion[3]
    print("El resultado de la multiplicacion de los valore de distribucion es: ",resultadoParte1)
    adaptadores = sorted(input)
    formas = contarOpciones(Nodo(contenido =0), adaptadores, nodosParseados)
    print("las formas son: ", formas)
main(PATH2)
