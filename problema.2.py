persoana = str(input('Introduceti numele si prenumele: '))
if (ord(persoana[0]) in range(65,91)) and (ord(persoana[persoana.find(' ')+1]) in range(65,91)):
    print('Da, numele si pronumele a fost scris corect')    
else:
    print('Nu, numele si pronumele a fost scris gresit') 
