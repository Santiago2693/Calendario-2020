import json
import re
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


def derivacionIzq(diccionario, node):
    #casos base
    if (node.getContenido() == "\"a\""):
        return 'a'
    elif (node.getContenido() == "\"b\""):
        return 'b'
    else:
        #caso recursivos
        cadena = ""
        for clave in diccionario[int(node.getContenido())][0]:
            nodo = Nodo(contenido = clave)
            node.setHijo(nodo)
            #return derivacionIzq(diccionario, nodo)
            cadena += derivacionIzq(diccionario, nodo)
        return cadena

def comprobacion(cadena):
    pass

#ahora nos falta en efecto hacer las derivaciones correspondientes
def main(ruta):
    gramatica, cadenas = procesarDatos(ruta)
    #debo construir mi arbol en base a la cadena
    #vamos a hacer derivaciones mas a la izq
    arbolParseo = Arbol()
    #ahora voy a hacer la insercion de los nodos
    raiz = Nodo(contenido ="0")
    arbolParseo.insertarNodo(raiz)
    cadena = derivacionIzq(gramatica, raiz)
    print(arbolParseo)
    print(cadena)

main(PATH)
