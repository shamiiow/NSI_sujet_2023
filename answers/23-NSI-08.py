def max_dico(dico):
    like = -1
    pseudo = ''
    for i in dico.keys():
        if dico[i] > like:
            like = dico[i]
            pseudo = i
    return pseudo, like

assert max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}) == ('Ada', 201)
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}) == ('Alan', 222)

class Pile:
    """
    Classe definissant une structure de pile.
    """
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booleen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """
        Place l'élément v au sommet de la pile
        """
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return resultat

assert eval_expression([2, 3, '+', 5, '*']) == 25