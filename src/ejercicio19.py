import json
PATH='puzzle_input/ejercicio19.txt'
def procesarDatos(ruta):
    """
    Esta funcion toma los datos del archivo y los manda a:
    1. Un diccionario con las reglas de la gramatica
    2. Una lista de las cadenas que luego tendremos que comprobar
    """
    gramatica = dict()
    cadenas = list()
    with open(ruta) as archivo:
        for line in archivo:
            if line == "\n":
                break
            datos = line.strip().split(":")
            gramatica[int(datos[0])]= [x.split() for x in datos[1].strip().split("|")]
        for line in archivo:
            cadenas.append(line.strip())
    print(gramatica)
    return gramatica, cadenas

#ahora deberiamos armar un arbol para luego poder hacer una
#derivacion con la gramatica propuesta

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


tree = Arbol()
tree.insertarNodo(Nodo(contenido = 5))
tree.insertarNodo(Nodo(contenido = 2), clavePadre=5)
tree.insertarNodo(Nodo(contenido = 7), clavePadre=5)
tree.insertarNodo(Nodo(contenido = 8), clavePadre=2)
tree.insertarNodo(Nodo(contenido = 9), clavePadre=2)
tree.insertarNodo(Nodo(contenido = 1), clavePadre=9)
tree.insertarNodo(Nodo(contenido = 10), clavePadre=7)
tree.insertarNodo(Nodo(contenido = 3), clavePadre = 1)
tree.insertarNodo(Nodo(contenido = 4), clavePadre = 1)
print(tree)
