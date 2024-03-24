def trouver_parcours_hamiltonien(case_depart):
    vient_de = {}  # Dictionnaire associant chaque case à sa case parente
    a_explorer = [case_depart]  # Liste des cases à explorer
    marquees = set()  # Ensemble des cases déjà visitées

    # Exploration par recherche en profondeur
    while a_explorer:
        courant = a_explorer.pop()
        marquees.add(courant)

        # Vérifier si toutes les cases ont été visitées (parcours hamiltonien trouvé)
        # Création de chemin pour renvoyer le parcours final
        if len(marquees) == 64:
            chemin = [courant]
            while courant in vient_de:
                courant = vient_de[courant]
                chemin.append(courant)
            chemin.reverse()
            return chemin

        # Explorer les cases voisines non visitées
        for case_voisine in obtenir_cases_accessibles(courant):
            if case_voisine not in marquees:
                vient_de[case_voisine] = courant
                a_explorer.append(case_voisine)

    # Aucun parcours hamiltonien trouvé
    return None

# Trouver les cases accesibles et les renvoyer dans un tableau
def obtenir_cases_accessibles(case):

    x, y = case
    cases_accessibles = []

    for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
        nouvelle_x = x + dx
        nouvelle_y = y + dy

        if 0 <= nouvelle_x < 8 and 0 <= nouvelle_y < 8:
            cases_accessibles.append((nouvelle_x, nouvelle_y))

    return cases_accessibles

# Main
def trouver_parcours(x, y):
    case_depart = (x, y)

    parcours = trouver_parcours_hamiltonien(case_depart)

    if parcours:
        print(f"Parcours hamiltonien trouvé : \n {parcours}")
    else:
        print("Aucun parcours hamiltonien trouvé.")

trouver_parcours(0, 0)