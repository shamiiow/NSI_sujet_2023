def multiplication(n1, n2):
    resultat = 0
    if n2 < 0 and n1 < 0:
        for i in range(abs(n2)):
            resultat += abs(n1)
        return resultat
    for i in range(abs(n2)):
        resultat += n1
    return resultat

assert multiplication(3,5) == 15
assert multiplication(-4,-8) == 32
assert multiplication(-2,6) == -12
assert multiplication(-2,0) == 0

def chercher(T,n,i,j):
    if i < 0 or j > len(T) :
        return None    
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] < n :
        return chercher(T, n, m + 1, j)
    elif T[m] > n :
        return chercher(T, n, i, m - 1)
    else :
        return m
    
assert chercher([1,5,6,6,9,12],7,0,10) == None
assert chercher([1,5,6,6,9,12],7,0,5) == None
assert chercher([1,5,6,6,9,12],9,0,5) == 4
assert chercher([1,5,6,6,9,12],6,0,5) == 2