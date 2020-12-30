PATH ='puzzle_input/ejercicio6M.txt'
PATH2 ='puzzle_input/ejercicio6.txt'
def procesarInput(ruta):
    grupos = list()
    with open(ruta) as arch:
        opciones = list()
        for line in arch:
            if line == '\n':
                grupos.append(opciones)
                opciones = list()
            else:
                opciones.append(set(line.strip()))
        grupos.append(opciones)
    return grupos

def sumatoriaInclusiva(grupos):
    total =0
    for grupo in grupos:
        if len(grupo) ==1:
            total += len(grupo[0])
        elif len(grupo) ==0:
            pass
        else:
            personas = len(grupo)
            union = grupo[0]
            i = 0
            while i< len(grupo):
                union = union.union(grupo[i])
                i+=1
            total += len(union)
    return total

def sumaDirecta(grupos):
    total =0
    for grupo in grupos:
        if len(grupo) ==1:
            total += len(grupo[0])
        elif len(grupo) ==0:
            pass
        else:
            personas = len(grupo)
            interseccion = grupo[0]
            i = 0
            while i< len(grupo):
                interseccion = interseccion.intersection(grupo[i])
                i+=1
            total += len(interseccion)
    return total

print(str(sumatoriaInclusiva(procesarInput(PATH2))))
print(str(sumaDirecta(procesarInput(PATH2))))
