def calcule(nombres):
    somme = 0
    for nombre in nombres:
        if nombre % 2 == 0:
            somme += nombre
    return somme

L = [8, 24,48,2,16]
resultat= calcule(L)

print(resultat)