#codding utf-8
import time

def coupValide(sommet, coup, taille):
    """
    Permet de vérifier si un coup est valide sur l'échiquier.
    Renvoie un booléen (True si le coup est valide et False sinon).
    """
    x, y = coup
    # On vérifie la validité des coordonnées de la case et de si cette dernière à déjà été parcourue
    if ((0 <= x < taille) and (0 <= y < taille) and (sommet[x][y] == -1)):
        return True
    return False

def coupsValides(sommet, coup, taille):
    """
    Permet de déterminer les coups valides pour le prochain déplacement du cavalier.
    Renvoie une liste contenant les coordonnées de tous les coups valides pour une case.
    """
    x, y = coup
    # On définit les mouvements possibles du cavalier sur l'échiquier
    coupsPossibles = [(x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2), (x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2)]
    listeCoupsValides = []
    # On vérifie la validité de chaque coup possible et on les ajoute à la liste des coups valides
    for coup in coupsPossibles:
        if (coupValide(sommet, coup, taille) == True):
            listeCoupsValides.append(coup)
    return listeCoupsValides

def parcoursCavalierDFS(sommet, coup, position, taille):
    """
    Permet d'effectuer un parcours en profondeur du cavalier sur l'échiquier.
    Renvoie un booléen (True si un chemin hamiltonien est trouvé et False sinon).
    """
    sommet[coup[0]][coup[1]] = position
    # On vérifie si toutes les cases ont été visitées
    if (position == taille * taille):
        return True
    # On parcourt les coups valides à partir de la position actuelle
    for prochainCoup in coupsValides(sommet, coup, taille):
        # On teste chaque coups valide de façon récursive
        if (parcoursCavalierDFS(sommet, prochainCoup, position + 1, taille) == True):
            return True
    # On remet la case dans son état initial si aucun chemin n'est trouvé
    sommet[coup[0]][coup[1]] = -1
    return False

def parcoursCavalier(taille, depart):
    """
    Permet de rechercher un chemin hamiltonien pour le cavalier sur l'échiquier.
    Renvoie une matrice repésentant le chemin hamiltonien sur l'échiquier si il y en a un et rien sinon.
    """
    # On créer une matrice représentant l'échiquier avec des cases vides
    sommet = [[-1] * taille for i in range(taille)]
    if (parcoursCavalierDFS(sommet, depart, 1, taille) == True):
        return sommet
    return None

def programmePrincipal():
    """
    Permet de résoudre le problème du cavalier pour une position de départ et une taille choisies par l'utilisateur.
    Affiche le chemin trouvé ainsi que le temps d'exécution si il existe et un message indiquant qu'aucun chemin n'a été trouvé sinon.
    """
    debut = time.time()
    taille = int(input("Veuillez choisir une taille d'échiquier : "))
    departX = int(input("Veuillez choisir une position de départ sur l'axe X : "))
    departY = int(input("Veuillez choisir une position de départ sur l'axe Y : "))
    depart = (departX, departY)
    solution = parcoursCavalier(taille, depart)
    if (solution is not None):
        print("Chemin trouvé pour un cavalier ayant pour position de départ:", depart)
        for ligne in solution:
            print(ligne)
        fin = time.time()
        tempsExecution = fin - debut
        print("Temps d'exécution : ", tempsExecution)
    else:
        print("Aucun chemin trouvé.")

programmePrincipal()
