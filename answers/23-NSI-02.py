def indices_maxi(tab):
    max = tab[0]
    i_max = []
    for i in range(len(tab)):
        if tab[i]>max:
            i_max = []
            max = tab[i]
        if tab[i] == max:
            i_max.append(i)
    return (max, i_max)

assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8]) 
assert indices_maxi([7]) == (7, [0])


def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    return T2

assert positif([-1,0,5,-3,4,-6,10,9,-8 ]) == [0, 5, 4, 10, 9]
assert positif([-2]) == []
