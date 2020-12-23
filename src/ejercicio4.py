import re
import json
PATH='puzzle_input/ejercicio4.txt'
PATH2= 'puzzle_input/ejercicio4M.txt'
VALIDOS= 'puzzle_input/validos.txt'
def main(ruta):
    pasaportes = list()
    camposObligatorios = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    arch = open(ruta)
    tamano = len(arch.readlines())-1
    arch.close()
    bandera = 0
    listaDiccionarios = list()
    with open(ruta) as f:
        string = ""
        temp = list()
        for line in f:
            string += " "+line.strip()
            if line == "\n" or bandera == tamano:
                temp = string.strip().split(" ")
                temp2 = list()
                tabla = dict()
                for valores in temp: #odio esto
                    temp2 = valores.split(":")
                    tabla[temp2[0]]=temp2[1]
                if (set(camposObligatorios).issubset(set(tabla.keys()))) and validarPasaporte(tabla):
                    listaDiccionarios.append(tabla)
                string =""
            bandera+=1

    archive = json.dumps(listaDiccionarios, indent=4)
    nuevo = open("puzzle_input/resultado.json","w")
    nuevo.write(archive)
    nuevo.close()
    print("La lista de pasaportes validos es:",len(listaDiccionarios))
    return listaDiccionarios


def validarPasaporte(pasaporte):
    eyesList=['amb', 'blu', 'brn', 'gry', 'grn','hzl', 'oth']
    value = int(pasaporte["byr"]) in range(1920,2003)
    value = value and (int(pasaporte["iyr"]) in range(2010,2021))
    value = value and (int(pasaporte["eyr"]) in range(2020, 2031))
    value = value and (int(pasaporte["iyr"]) in range(2010,2021))
    value = value and  (pasaporte["ecl"] in eyesList)
    altura = pasaporte["hgt"]
    if (altura[len(altura)-2:len(altura)]=='cm'):
        value = value and (int(altura[:-2]) in range(150,194))
    elif (altura[len(altura)-2:len(altura)]=='in'):
        value =  value and (int(altura[:-2]) in range(59, 77))
    else:
        value = False
    patronCabello = re.compile("^#[0-9a-f]{6}")
    if patronCabello.match(pasaporte["hcl"]) == None:
        value = False
    else:
        value = value and True
    patron = re.compile("^[0-9]{9}")
    if patron.match(pasaporte["pid"]) == None:
        value = False
    else:
        value = value and True

    return value

main(PATH)
