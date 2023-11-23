def compte(nombres):
    count = 0
    for nombre in nombres:
        if nombre % 3 == 0:
            count += 1
    return count

L = [8, 24,48,2,16]
resultat= compte(L)

print(resultat)