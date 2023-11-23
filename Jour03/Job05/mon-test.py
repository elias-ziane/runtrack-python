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
            return
    elif operator == "%":
        result = num1 % num2
    else:
        print("Erreur : Opération non valide")
        return

    message = "Le résultat de {} {} {} est : {}".format(num1, operator, num2, result)
    print(message)


calcule(10, "+", 5)