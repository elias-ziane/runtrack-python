liste_originale = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = []

for element in liste_originale:
    doublon = False

    # Vérifier si l'élément est déjà présent dans la liste sans doublons
    for item in liste_sans_doublons:
        if item == element:
            doublon = True
            break

    # Si l'élément n'est pas un doublon, ajouter à la liste sans doublons en utilisant +=
    if not doublon:
        liste_sans_doublons += [element]

print("Liste originale :", liste_originale)
print("Liste sans doublons :", liste_sans_doublons)
