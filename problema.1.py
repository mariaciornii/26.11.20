cuvant=str(input('Introduceti cuvantul: '))
litera = (input('Introduceti litera cu care trebuie de inlocuit: '))
print('Cuvintele noi sunt:') 
for i in range(0, len(cuvant)):
    cuv_nou = cuvant[0:i] + cuvant[i:len(cuvant)].replace(cuvant[i], litera, 1)
    print(cuv_nou)
