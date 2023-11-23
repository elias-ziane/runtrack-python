def check(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return f"{nombre} est un nombre pair."
        else:
            return f"{nombre} est un nombre impair."
    else:
        return "Veuillez fournir un nombre entier positif."

resultat1 = check(10)
resultat2 = check(7)
resultat3 = check(-3)
resultat4 = check(3.14)

print(resultat1)
print(resultat2)
print(resultat3)
print(resultat4)