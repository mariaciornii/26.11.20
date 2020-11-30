cuvant=str(input('Introduceti cuvantul: '))
l = 0
r = len(cuvant)
print(cuvant)
while l<r:
    nou = ""
    l += 1
    r -= 1
    for i in range(0,l):
        nou += " "
    nou += cuvant[l:r]
    print(nou)