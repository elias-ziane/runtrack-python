def tri(liste):
    if not liste:
        return liste

    pivot = liste[0]
    inferieurs = [x for x in liste[1:] if x <= pivot]
    superieurs = [x for x in liste[1:] if x > pivot]

    return tri(inferieurs) + [pivot] + tri(superieurs)

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

liste_triee= tri(L)

print(liste_triee)
