def convertir(list):
    dec = 0
    i = 0
    exp = len(list) - 1
    while i < len(list):
        dec += (2**(exp-i))*list[i]
        i += 1
    return dec

assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83
assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130    

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à  déterminer où placer la valeur à  ranger
        j = i
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion
    return tab

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]
assert tri_insertion(liste) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]