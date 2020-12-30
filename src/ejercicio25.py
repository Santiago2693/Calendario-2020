pkCARDM = 1327981
pkDOORM = 2822615
pkCARD=17115212
pkDOOR=3667832
sNumber = 7 # no se si este valor cambia por cada uno
div = 20201227

def loopSize(clave, valorInicial =1):
    n = 0
    while not valorInicial == clave:
        valorInicial *= sNumber
        valorInicial %= div
        n+=1
    return n

def claveEncripcion(subjectNumber, loopSize):
    valorInicial = 1
    for i in range(loopSize):
        valorInicial *= subjectNumber
        valorInicial %= div
    return valorInicial

def main():
    lsCard = loopSize(pkCARD)
    key = claveEncripcion(pkDOOR,lsCard)
    print("La clave de encripcion es: ",key)

main()
