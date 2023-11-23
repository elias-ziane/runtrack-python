def calcule(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Erreur : Division par zéro")
            return "Erreur : Division par zéro"
    elif operator == "%":
        result = num1 % num2
    else:
        print("Erreur : Opération non valide")
        return "Erreur : Opération non valide"

    message = "Résultat de {} {} {} : {}".format(num1, operator, num2, result)
    print(message)
    return message

# Demander à l'utilisateur d'entrer des valeurs
num1 = int(input("Veuillez entrer un nombre : "))
operator = input("Veuillez entrer le signe de l'opération (+, -, *, /, %) : ")
num2 = int(input("Veuillez entrer un nombre : "))

# Appeler la fonction calcule avec les valeurs entrées
resultat_message = calcule(num1, operator, num2)

