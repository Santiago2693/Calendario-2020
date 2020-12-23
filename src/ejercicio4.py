PATH='puzzle_input/ejercicio4.txt'
"""
path='puzzle_input/ejercicio4.txt'
total=0
camposValidos=0
camposObligatorios = 'byr: iyr: eyr: hgt: hcl: ecl: pid:'

with open(path) as p:
            for line in p:
                if not line=="\n" :
                        for x in camposObligatorios.split():
                            if not line.find(x)==-1:
                                camposValidos=camposValidos+1
                                if camposValidos>=7:
                                    total+=1
                else:
                    camposValidos=0

print (total)



listaDiccionarios=list()
with open(PATH) as f:
    for line in f:

        for x in line.split(':'):





"""
import re
def main():
    pasaportes = list()
    camposObligatorios = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    arch = open(PATH)
    tamano = len(arch.readlines())-1
    arch.close()
    listaDiccionarios = list()
    with open(PATH) as f:
        string = ""
        temp = list()
        for line in f:
            string += " "+line.strip()
            if line == "\n" :
                temp = string.strip().split(" ")
                temp2 = list()
                tabla = dict()
                for valores in temp: #odio esto
                    temp2 = valores.split(":")
                    tabla[temp2[0]]=temp2[1]
                if (set(camposObligatorios).issubset(set(tabla.keys()))) and validarPasaporte(tabla):
                    listaDiccionarios.append(tabla)
                string =""

    #print(listaDiccionarios)
    print("La lista de pasaportes validos es:",len(listaDiccionarios))


def validarPasaporte(pasaporte):
    eyesList=['amb', 'blu', 'brn', 'gry', 'grn','hzl', 'oth']
    value = int(pasaporte["byr"]) in range(1920,2003)
    value = value and int(pasaporte["iyr"]) in range(2010,2021)
    value = value and int(pasaporte["eyr"]) in range(2020, 2031)
    """
    value = value and int(pasaporte["iyr"]) in range(2010,2021)
    value = value and  pasaporte["ecl"] in eyesList
    altura = pasaporte["hgt"]
    if (altura[len(altura)-2:len(altura)]=='cm'):
        value = value and int(pasaporte["hgt"][:-2]) in range(150,194)
    else:
        value =  value and int(pasaporte["hgt"][:-2]) in range(59, 77)
    patronCabello = re.compile("#[0-9a-f]{6}")
    if patronCabello.match(pasaporte["hcl"]) == None:
        value = value and False
    else:
        value = value and True
    patron = re.compile("[0-9]{9}")
    if patron.match(pasaporte["pid"]) == None:
        value = value and False
    else:
        value = value and True
    """
    return value

main()
