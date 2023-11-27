def demander_prenom():
    prenom = input("Veuillez entrer votre prénom : ")
    return prenom

def afficher_message_hello(prenom):
    print("Hello," , prenom , "!")


prenom_utilisateur = demander_prenom()


afficher_message_hello(prenom_utilisateur)
