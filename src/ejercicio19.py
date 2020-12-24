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
            gramatica[int(datos[0])]= datos[1].strip().split("|")
        for line in archivo:
            cadenas.append(line.strip())
    return gramatica, cadenas
