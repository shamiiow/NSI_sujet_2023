def verifie(list):
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            return False
    return True

assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([5]) == True



urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat.keys():
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

# la variable 'vainqueur' est inutile ?

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

election = depouille(urne)
assert election == {'B': 4, 'A': 3, 'C': 3} 
assert vainqueur(election) == ['B']

