PATH = 'puzzle_input/ejercicio9M.txt'
def main(ruta, preamble):
    lista = list()
    with open(ruta) as f:
        for line in f:
            lista.append(int(line.strip()))
    #print(lista)
    i = 0

    while(True):
        try:
            for j in range(0,preamble):
                if lista[j+i] < lista[preamble+i]:
                    otroValor = lista[preamble+i] - lista[j+i]
                    print(lista[j+i])
                else:
                    continue
                if otroValor in lista[i:preamble+i]:
                    i+=1
                    break
            if otroValor not in lista[i:preamble+i]:
                print(lista[preamble+i])
                break
        except:
            break

main(PATH, 25)
