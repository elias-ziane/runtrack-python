def myfunc(type,saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("caroote, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Erreur: Aucun produits de ce type ou de cette saison trouvé")
        
        

myfunc("fruits","hiver")
myfunc("fruits","ete")
myfunc("legume","hiver")
myfunc("legume","ete")
