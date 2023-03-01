def moyenne(list):
    up = 0
    down = 0
    for i in range(len(list)):
        up += list[i][0] * list[i][1]
        down += list[i][1]
    try :
        return up/down
    except ZeroDivisionError:
        return None
    
assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142 
assert moyenne([(3, 0), (5, 0)]) == None





coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], 
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont repreente par 
        des "*" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *",end="")
            else:
                print("  ",end="")
        print()


def zoomListe(liste_depart,k):
    '''renvoie une liste contenant k fois chaque 
       element de liste_depart'''
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille,k):
    '''renvoie une grille ou les lignes sont zoomees k fois 
       ET repetees k fois'''
    grille_zoom=[]
    for elt in grille:
        liste_zoom = zoomListe(elt,k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom

affiche(coeur)
affiche(zoomDessin(coeur, 4))