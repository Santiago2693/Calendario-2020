path='puzzle_input/ejercicio4.txt'
total=0
camposValidos=0
camposObligatorios = 'byr: iyr: eyr: hgt: hcl: ecl: pid:'

with open(path) as p:
            for line in p:
                if not line=="\n" :
                        print (line)
                        for x in camposObligatorios.split():

                            if not line.find(x)==-1:

                                camposValidos=camposValidos+1
                                print(camposValidos)

                else:

                    if camposValidos>=7:
                        total+=1
                    print(total)
                    camposValidos=0

print (total)
