def fusion(tab1, tab2):
    i1 = 0
    i2 = 0
    tab12 = []
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab12.append(tab1[i1])
            i1 += 1
        else:
            tab12.append(tab2[i2])
            i2 += 1
    while i1 < len(tab1):
        tab12.append(tab1[i1])
        i1 += 1
    while i2 < len(tab2):
        tab12.append(tab2[i2])
        i2 += 1
    return tab12

assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]



romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donné en chiffres romains """
    if len(nombre) == 0:
        return 0
    if len(nombre) == 1:
        return romains[nombre[0]]
        
    elif romains[nombre[0]] >= romains[nombre[1]] :
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return (romains[nombre[1]] - romains[nombre[0]]) + traduire_romain(nombre[2:])

assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIII") == 2023