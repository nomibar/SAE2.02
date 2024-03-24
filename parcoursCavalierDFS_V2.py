#coding utf-8
import time

def trouverParcoursHamiltonien(taille, caseDepart):
    """
    Permet de rechercher un parcours hamiltonien pour le cavalier sur l'échiquier.
    Renvoie
    """
    vient_de = {}  # Dictionnaire associant chaque case à sa case parente
    courant = caseDepart
    aVisiter = [courant]  # Liste des cases à explorer
    estVisites = set()  # Ensemble des cases déjà visitées
    while aVisiter:
        courant = aVisiter.pop()
        estVisites.add(courant)
        # On vérifie si toutes les cases ont été visitées
        if (len(estVisites) == taille * taille):
            return [caseDepart] + list(estVisites - {caseDepart})
        # On parcourt les cases voisines non-visitées
        for caseVoisine in obtenirCasesAccessibles(courant, taille):
            if (caseVoisine not in estVisites):
                vient_de[caseVoisine] = courant
                aVisiter.append(caseVoisine)
        # On revient en arrière en suivant la trace des parents si on tombe sur une impasse
        if (not aVisiter):
            while courant != caseDepart:
                courant = vient_de[courant]
                aVisiter.append(courant)
    return None

def obtenirCasesAccessibles(case, taille):
    """
    Permet de déterminer les cases accessibles à partir d'une case donnée pour le cavalier.
    """
    x, y = case
    casesAccessibles = []
    # On définit les mouvements possibles du cavalier sur l'échiquier
    for ligne, colonne in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
        nouvelleLigne = x + ligne
        nouvelleColonne = y + colonne
        if ((0 <= nouvelleLigne < taille) and (0 <= nouvelleColonne < taille)):
            casesAccessibles.append((nouvelleLigne, nouvelleColonne))
    return casesAccessibles

def demanderCoordonnees():
    """
    Permet de demander à l'utilisateur de saisir la taille de l'échiquier et les coordonnées de départ.
    """
    taille = int(input("Veuillez choisir la taille de l'échiquier : "))
    x = int(input("Veuillez choisir la coordonnée X de la case de départ : "))
    y = int(input("Veuillez choisir la coordonnée Y de la case de départ : "))
    return taille, (x, y)

def trouverParcours():
    """
    Permet de rechercher et d'afficher un parcours hamiltonien.
    Affiche le chemin trouvé ainsi que le temps d'exécution si il existe et un message indiquant qu'aucun chemin n'a été trouvé sinon.
    """
    debut = time.time()
    taille, caseDepart = demanderCoordonnees()
    parcours = trouverParcoursHamiltonien(taille, caseDepart)
    if (parcours is not None):
        print(f"Parcours hamiltonien trouvé : \n {parcours}")
        fin = time.time()
        tempsExecution = fin - debut
        print("Temps d'éxecution : ", tempsExecution)
    else:
        print("Aucun parcours hamiltonien trouvé.")

trouverParcours()
